#!/usr/bin/env python3
"""Replace tracked PNG screenshots with smaller, pixel-identical lossless WebP files.

Run from any directory with ``python3 scripts/optimize_screenshots.py``. Source
screenshots are retained whenever conversion is not beneficial or a destination
already exists. Markdown image/link targets are updated only for replacements.
"""
from __future__ import annotations

import io
import os
import re
import subprocess
import tempfile
from pathlib import Path
from typing import Iterable, NamedTuple
from urllib.parse import unquote, urlsplit

from PIL import Image


ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
CAPTURES = DOCS / "assets" / "capturas"
MARKDOWN_LINK = re.compile(r"(!?\[[^\]]*\]\()([^\s)]+)(\))")
FENCED_BLOCK = re.compile(r"^(`{3,}|~{3,}).*?^\1[ \t]*$", re.M | re.S)
INLINE_CODE = re.compile(r"(`+).*?\1", re.S)
PNG_TOKEN = re.compile(r"[^\s<>'\"()\[\]`=]+?\.png\b")


class MigrationReport(NamedTuple):
    converted: int
    retained: int
    before_bytes: int
    after_bytes: int


class UnsupportedScreenshot(ValueError):
    """The PNG has semantics beyond one unprofiled raster frame."""


def _has_non_pixel_chunks(png_bytes: bytes) -> bool:
    """Reject ancillary chunks even when Pillow does not expose their metadata."""
    if not png_bytes.startswith(b"\x89PNG\r\n\x1a\n"):
        return True
    offset = 8
    while offset + 12 <= len(png_bytes):
        length = int.from_bytes(png_bytes[offset:offset + 4], "big")
        chunk_type = png_bytes[offset + 4:offset + 8]
        offset += length + 12
        if offset > len(png_bytes) or chunk_type not in {b"IHDR", b"PLTE", b"IDAT", b"IEND"}:
            return True
        if chunk_type == b"IEND":
            return offset != len(png_bytes)
    return True


def encode_lossless_webp(png_bytes: bytes) -> bytes:
    """Encode and verify the same dimensions and decoded RGBA pixel bytes."""
    if _has_non_pixel_chunks(png_bytes):
        raise UnsupportedScreenshot("PNG has metadata, animation, or unrecognized chunks")
    with Image.open(io.BytesIO(png_bytes)) as source:
        if source.info or getattr(source, "is_animated", False) or getattr(source, "n_frames", 1) != 1:
            raise UnsupportedScreenshot("Animated or metadata-bearing PNG")
        source.load()
        pixels = source.convert("RGBA").tobytes()
        size = source.size
        output = io.BytesIO()
        source.save(output, format="WEBP", lossless=True, exact=True, method=6)
    webp_bytes = output.getvalue()
    with Image.open(io.BytesIO(webp_bytes)) as result:
        result.load()
        if result.size != size or result.convert("RGBA").tobytes() != pixels:
            raise ValueError("WebP conversion changed decoded RGBA pixels")
    return webp_bytes


def _rewrite_links(article: Path, text: str, replacements: dict[Path, Path]) -> str:
    def rewrite_block(block: str) -> str:
        def rewrite_match(match: re.Match[str]) -> str:
            target = match.group(2)
            if not target.endswith(".png"):
                return match.group(0)
            source = (article.parent / target).resolve()
            if source not in replacements:
                return match.group(0)
            return f"{match.group(1)}{target[:-4]}.webp{match.group(3)}"

        return MARKDOWN_LINK.sub(rewrite_match, block)

    pieces = []
    start = 0
    for fenced in FENCED_BLOCK.finditer(text):
        pieces.append(rewrite_block(text[start:fenced.start()]))
        pieces.append(fenced.group(0))
        start = fenced.end()
    pieces.append(rewrite_block(text[start:]))
    return "".join(pieces)


def _unrewritten_pngs(article: Path, text: str, docs_root: Path, candidates: set[Path]) -> set[Path]:
    """Find candidate PNGs still mentioned outside code after safe Markdown rewrites."""
    live_text = INLINE_CODE.sub("", FENCED_BLOCK.sub("", text))
    remaining = set()
    for match in PNG_TOKEN.finditer(live_text):
        token = unquote(match.group(0))
        if urlsplit(token).scheme:
            continue
        target = (docs_root / token.lstrip("/")) if token.startswith("/") else (article.parent / token)
        resolved = target.resolve()
        if resolved in candidates:
            remaining.add(resolved)
    return remaining


def _atomic_write(path: Path, data: bytes) -> None:
    with tempfile.NamedTemporaryFile(dir=path.parent, prefix=f".{path.name}.", delete=False) as stream:
        temporary = Path(stream.name)
        stream.write(data)
    try:
        os.chmod(temporary, path.stat().st_mode & 0o777)
        os.replace(temporary, path)
    finally:
        temporary.unlink(missing_ok=True)


def migrate_screenshots(docs_root: Path, png_paths: Iterable[Path]) -> MigrationReport:
    """Migrate selected PNGs and their Markdown references; preserve originals on errors."""
    docs_root = docs_root.resolve()
    capture_root = (docs_root / "assets" / "capturas").resolve()
    candidates: dict[Path, tuple[Path, bytes, bytes]] = {}
    retained = before_bytes = after_bytes = 0

    for path in png_paths:
        source = path.resolve()
        if not source.is_relative_to(capture_root) or source.suffix.lower() != ".png":
            raise ValueError(f"Not a screenshot PNG: {path}")
        if not source.exists():
            continue  # A previous run already replaced this tracked PNG.
        original = source.read_bytes()
        before_bytes += len(original)
        destination = source.with_suffix(".webp")
        if destination.exists():
            retained += 1
            after_bytes += len(original)
            continue
        try:
            converted = encode_lossless_webp(original)
        except UnsupportedScreenshot:
            retained += 1
            after_bytes += len(original)
            continue
        if len(converted) >= len(original):
            retained += 1
            after_bytes += len(original)
            continue
        candidates[source] = (destination, original, converted)
        after_bytes += len(converted)

    original_articles = {article: article.read_bytes() for article in docs_root.rglob("*.md")}
    replacements = {source: data[0] for source, data in candidates.items()}
    unsafe = set()
    for article, original in original_articles.items():
        rewritten = _rewrite_links(article, original.decode("utf-8"), replacements)
        unsafe.update(_unrewritten_pngs(article, rewritten, docs_root, set(candidates)))
    for source in unsafe:
        _, original, converted = candidates.pop(source)
        retained += 1
        after_bytes += len(original) - len(converted)

    replacements = {source: data[0] for source, data in candidates.items()}
    articles: dict[Path, tuple[bytes, bytes]] = {}
    for article, original in original_articles.items():
        text = original.decode("utf-8")
        updated = _rewrite_links(article, text, replacements).encode("utf-8")
        if updated != original:
            articles[article] = (original, updated)

    created: list[Path] = []
    updated_articles: list[Path] = []
    removed: list[Path] = []
    try:
        for destination, _, webp_bytes in candidates.values():
            with tempfile.NamedTemporaryFile(dir=destination.parent, prefix=f".{destination.name}.", delete=False) as stream:
                temporary = Path(stream.name)
                stream.write(webp_bytes)
            try:
                os.link(temporary, destination)  # Atomic creation; never overwrite a collision.
                created.append(destination)
            finally:
                temporary.unlink(missing_ok=True)
        for article, (_, updated) in articles.items():
            _atomic_write(article, updated)
            updated_articles.append(article)
        for source in candidates:
            source.unlink()
            removed.append(source)
    except Exception:
        for source in removed:
            source.write_bytes(candidates[source][1])
        for article in updated_articles:
            _atomic_write(article, articles[article][0])
        for destination in created:
            destination.unlink(missing_ok=True)
        raise

    return MigrationReport(len(candidates), retained, before_bytes, after_bytes)


def tracked_pngs() -> list[Path]:
    result = subprocess.run(
        ["git", "ls-files", "-z", "--", "docs/assets/capturas"],
        cwd=ROOT,
        check=True,
        capture_output=True,
    )
    return [ROOT / name.decode("utf-8") for name in result.stdout.split(b"\0") if name.endswith(b".png")]


def main() -> None:
    report = migrate_screenshots(DOCS, tracked_pngs())
    saved = report.before_bytes - report.after_bytes
    print(
        f"Converted {report.converted} PNGs; retained {report.retained}; "
        f"{report.before_bytes:,} -> {report.after_bytes:,} bytes ({saved:,} saved)."
    )


if __name__ == "__main__":
    main()
