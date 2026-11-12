#!/usr/bin/env python3
"""Make the built search index accent-insensitive.

MkDocs' search plugin (and the Material theme's lunr-based worker that reads
its output) does not fold accents: a lunr index built from "¿Cómo creo un
producto?" never matches a user who types "como creo un producto" or
"nomina" instead of "nómina". There is no supported mkdocs.yml option for
this (the search plugin's `pipeline` only accepts built-in stemmer/stopword
filters) and the lunr worker itself runs in a separate, versioned bundle we
do not control from `theme.custom_dir`.

Instead of touching the client runtime, this rewrites `site/search/search_index.json`
after the build: for every document, it appends an accent-folded copy of its
own title+text to its `text` field. Both the accented and unaccented spelling
of every word now live in the same lunr document, so either one matches,
without changing what is displayed (titles are untouched; only the hidden
indexed text grows).

Run after `mkdocs build` (scripts/build_docs.py already does this).
"""
from __future__ import annotations

import json
import sys
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
INDEX = ROOT / "site" / "search" / "search_index.json"


def sin_tildes(texto: str) -> str:
    """Strips diacritics (á→a, ñ→n, ü→u...) via Unicode decomposition."""
    descompuesto = unicodedata.normalize("NFKD", texto)
    return "".join(c for c in descompuesto if not unicodedata.combining(c))


def main() -> int:
    if not INDEX.exists():
        print(f"[buscador] No existe {INDEX}; corre `mkdocs build` primero.")
        return 1

    indice = json.loads(INDEX.read_text(encoding="utf-8"))
    tocados = 0

    for doc in indice.get("docs", []):
        original = f"{doc.get('title', '')} {doc.get('text', '')}"
        plano = sin_tildes(original)
        if plano != original:
            doc["text"] = f"{doc.get('text', '')} {plano}"
            tocados += 1

    INDEX.write_text(json.dumps(indice, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
    print(f"[buscador] {tocados} documento(s) del índice ahora son buscables sin tildes.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
