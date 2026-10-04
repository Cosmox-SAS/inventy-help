"""Check SEO metadata in actual MkDocs output, not template source."""

from __future__ import annotations

import subprocess
import sys
import tempfile
import unittest
from html.parser import HTMLParser
from pathlib import Path
from xml.etree import ElementTree

from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
BASE_URL = "https://ayuda.inventy.com.co/"
IMAGE_URL = BASE_URL + "assets/brand/social-preview.png"


class HeadParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.tags: list[tuple[str, dict[str, str]]] = []
        self.title = ""
        self.in_title = False

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag == "title":
            self.in_title = True
        if tag in {"meta", "link"}:
            self.tags.append((tag, {key: value or "" for key, value in attrs}))

    def handle_endtag(self, tag: str) -> None:
        if tag == "title":
            self.in_title = False

    def handle_data(self, data: str) -> None:
        if self.in_title:
            self.title += data

    def values(self, tag: str, attribute: str, expected: str) -> list[str]:
        return [
            attrs.get("content" if tag == "meta" else "href", "")
            for kind, attrs in self.tags
            if kind == tag and attrs.get(attribute) == expected
        ]


class SEOMetadataTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.directory = tempfile.TemporaryDirectory()
        cls.site = Path(cls.directory.name) / "site"
        result = subprocess.run(
            [sys.executable, "-m", "mkdocs", "build", "--site-dir", str(cls.site), "--quiet"],
            cwd=ROOT,
            capture_output=True,
            text=True,
        )
        if result.returncode:
            cls.directory.cleanup()
            raise AssertionError(f"MkDocs build failed:\n{result.stdout}\n{result.stderr}")

    @classmethod
    def tearDownClass(cls) -> None:
        cls.directory.cleanup()

    def page_head(self, path: str) -> HeadParser:
        parser = HeadParser()
        html = (self.site / path).read_text(encoding="utf-8")
        parser.feed(html.split("</head>", 1)[0])
        return parser

    def test_home_and_nested_page_metadata(self) -> None:
        pages = (
            (
                "index.html",
                BASE_URL,
                "Centro de Ayuda Inventy",
                "Guías paso a paso, soluciones rápidas y preguntas frecuentes para usar Inventy ERP.",
                "website",
            ),
            (
                "productos-inventario/crear-producto/index.html",
                BASE_URL + "productos-inventario/crear-producto/",
                "¿Cómo creo un producto? - Centro de Ayuda Inventy",
                "Pasos para crear un producto con precio, impuestos y unidad.",
                "article",
            ),
        )
        for path, canonical, title, description, kind in pages:
            with self.subTest(path=path):
                head = self.page_head(path)
                self.assertEqual(head.title, title)
                self.assertEqual(head.values("meta", "name", "description"), [description])
                self.assertEqual(head.values("link", "rel", "canonical"), [canonical])
                self.assertEqual(head.values("meta", "property", "og:type"), [kind])
                self.assertEqual(head.values("meta", "property", "og:locale"), ["es_CO"])
                self.assertEqual(head.values("meta", "property", "og:title"), [title])
                self.assertEqual(head.values("meta", "property", "og:description"), [description])
                self.assertEqual(head.values("meta", "property", "og:url"), [canonical])
                self.assertEqual(head.values("meta", "property", "og:image"), [IMAGE_URL])
                self.assertEqual(head.values("meta", "property", "og:image:width"), ["1200"])
                self.assertEqual(head.values("meta", "property", "og:image:height"), ["630"])
                self.assertEqual(
                    head.values("meta", "property", "og:image:alt"),
                    ["Inventy · Centro de Ayuda. Guías claras para tu negocio."],
                )
                self.assertEqual(head.values("meta", "name", "twitter:card"), ["summary_large_image"])
                self.assertEqual(head.values("meta", "name", "twitter:title"), [title])
                self.assertEqual(head.values("meta", "name", "twitter:description"), [description])
                self.assertEqual(head.values("meta", "name", "twitter:url"), [canonical])
                self.assertEqual(head.values("meta", "name", "twitter:image"), [IMAGE_URL])
                self.assertEqual(head.values("meta", "name", "twitter:image:alt"), ["Inventy · Centro de Ayuda. Guías claras para tu negocio."])

    def test_static_discovery_files_and_image(self) -> None:
        home = self.page_head("index.html")
        self.assertEqual(home.values("link", "rel", "icon"), ["assets/brand/favicon.svg"])
        favicon = self.site / "assets/brand/favicon.svg"
        self.assertEqual(ElementTree.parse(favicon).getroot().tag, "{http://www.w3.org/2000/svg}svg")
        image = self.site / "assets/brand/social-preview.png"
        with Image.open(image) as social:
            self.assertEqual((social.format, social.size), ("PNG", (1200, 630)))
        self.assertEqual(
            (self.site / "robots.txt").read_text(),
            "User-agent: *\nAllow: /\nSitemap: https://ayuda.inventy.com.co/sitemap.xml\n",
        )
        sitemap = (self.site / "sitemap.xml").read_text()
        self.assertIn("https://ayuda.inventy.com.co/", sitemap)
        self.assertIn("https://ayuda.inventy.com.co/productos-inventario/crear-producto/", sitemap)
        self.assertNotIn("pages.dev", sitemap)

    def test_error_page_does_not_advertise_an_empty_url(self) -> None:
        head = self.page_head("404.html")
        self.assertEqual(head.values("link", "rel", "canonical"), [])
        self.assertEqual(head.values("meta", "property", "og:url"), [])
        self.assertEqual(head.values("meta", "name", "twitter:url"), [])
        self.assertEqual(head.values("meta", "property", "og:type"), ["website"])

    def test_metadata_escapes_attribute_characters(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            docs = root / "docs"
            docs.mkdir()
            (docs / "index.md").write_text("# Home\n", encoding="utf-8")
            (docs / "escape.md").write_text(
                '---\ntitle: \'Guía "A & B" <C>\'\n'
                'description: \'Texto "A & B" <C>.\'\n---\n# Escaping\n',
                encoding="utf-8",
            )
            (root / "mkdocs.yml").write_text(
                "site_name: Centro de Ayuda Inventy\n"
                f"site_url: {BASE_URL}\n"
                "theme:\n  name: material\n"
                f"  custom_dir: {ROOT / 'overrides'}\n",
                encoding="utf-8",
            )
            result = subprocess.run(
                [sys.executable, "-m", "mkdocs", "build", "--quiet"],
                cwd=root,
                capture_output=True,
                text=True,
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            html = (root / "site/escape/index.html").read_text(encoding="utf-8")
            head = HeadParser()
            head.feed(html.split("</head>", 1)[0])
            title = 'Guía "A & B" <C> - Centro de Ayuda Inventy'
            description = 'Texto "A & B" <C>.'
            self.assertEqual(head.title, title)
            self.assertEqual(head.values("meta", "property", "og:title"), [title])
            self.assertEqual(head.values("meta", "name", "twitter:description"), [description])
            self.assertIn("Guía &#34;A &amp; B&#34; &lt;C&gt;", html)


if __name__ == "__main__":
    unittest.main()
