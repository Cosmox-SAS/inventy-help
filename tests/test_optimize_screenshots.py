import importlib.util
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from PIL import Image
from PIL.PngImagePlugin import PngInfo


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "optimize_screenshots.py"


def load_converter():
    spec = importlib.util.spec_from_file_location("optimize_screenshots", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class ScreenshotMigrationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.docs = Path(self.temp.name) / "docs"
        self.capture = self.docs / "assets/capturas/sales/step-1.png"
        self.capture.parent.mkdir(parents=True)
        self.article = self.docs / "sales/article.md"
        self.article.parent.mkdir(parents=True)

    def test_converts_only_smaller_exact_pixels_and_updates_image_target(self):
        image = Image.new("RGBA", (80, 80), (0, 0, 0, 0))
        image.putpixel((12, 14), (255, 0, 0, 0))
        image.putpixel((20, 21), (0, 255, 0, 128))
        image.save(self.capture)
        original = Image.open(self.capture).convert("RGBA").tobytes()
        self.article.write_text(
            "![Screen](../assets/capturas/sales/step-1.png)\n"
            "```md\n![Example](../assets/capturas/sales/step-1.png)\n```\n",
            encoding="utf-8",
        )

        report = load_converter().migrate_screenshots(self.docs, [self.capture])

        webp = self.capture.with_suffix(".webp")
        self.assertEqual(report.converted, 1)
        self.assertLess(report.after_bytes, report.before_bytes)
        self.assertFalse(self.capture.exists())
        self.assertEqual(Image.open(webp).convert("RGBA").tobytes(), original)
        self.assertEqual(
            self.article.read_text(encoding="utf-8"),
            "![Screen](../assets/capturas/sales/step-1.webp)\n"
            "```md\n![Example](../assets/capturas/sales/step-1.png)\n```\n",
        )

    def test_retains_png_if_webp_is_not_smaller(self):
        import random

        rng = random.Random(7)
        image = Image.new("RGB", (16, 16))
        image.putdata([(rng.randrange(256), rng.randrange(256), rng.randrange(256)) for _ in range(256)])
        image.save(self.capture, optimize=True)
        self.article.write_text("![Screen](../assets/capturas/sales/step-1.png)\n", encoding="utf-8")

        report = load_converter().migrate_screenshots(self.docs, [self.capture])

        self.assertEqual((report.converted, report.retained), (0, 1))
        self.assertTrue(self.capture.exists())
        self.assertFalse(self.capture.with_suffix(".webp").exists())
        self.assertIn("step-1.png", self.article.read_text(encoding="utf-8"))

    def test_collision_and_encode_failure_keep_original_and_reference(self):
        Image.new("RGBA", (80, 80), (0, 0, 0, 0)).save(self.capture)
        original = self.capture.read_bytes()
        self.article.write_text("![Screen](../assets/capturas/sales/step-1.png)\n", encoding="utf-8")
        converter = load_converter()
        destination = self.capture.with_suffix(".webp")
        destination.write_bytes(b"existing")

        collision = converter.migrate_screenshots(self.docs, [self.capture])
        self.assertEqual((collision.converted, collision.retained), (0, 1))
        self.assertEqual(destination.read_bytes(), b"existing")
        destination.unlink()

        with patch.object(converter, "encode_lossless_webp", side_effect=OSError("encode failed")):
            with self.assertRaises(OSError):
                converter.migrate_screenshots(self.docs, [self.capture])
        self.assertEqual(self.capture.read_bytes(), original)
        self.assertFalse(destination.exists())
        self.assertIn("step-1.png", self.article.read_text(encoding="utf-8"))

    def test_reference_write_failure_does_not_delete_original(self):
        Image.new("RGBA", (80, 80), (0, 0, 0, 0)).save(self.capture)
        original = self.capture.read_bytes()
        article_text = "![Screen](../assets/capturas/sales/step-1.png)\n"
        self.article.write_text(article_text, encoding="utf-8")
        second_article = self.article.with_name("other.md")
        second_article.write_text(article_text, encoding="utf-8")
        converter = load_converter()
        write = converter._atomic_write
        calls = 0

        def fail_second_write(path, data):
            nonlocal calls
            calls += 1
            if calls == 2:
                raise OSError("write failed")
            write(path, data)

        with patch.object(converter, "_atomic_write", side_effect=fail_second_write):
            with self.assertRaises(OSError):
                converter.migrate_screenshots(self.docs, [self.capture])

        self.assertEqual(self.capture.read_bytes(), original)
        self.assertFalse(self.capture.with_suffix(".webp").exists())
        self.assertEqual(self.article.read_text(encoding="utf-8"), article_text)
        self.assertEqual(second_article.read_text(encoding="utf-8"), article_text)

    def test_retains_metadata_bearing_and_animated_pngs(self):
        cases = ["metadata", "animated"]
        for case in cases:
            with self.subTest(case=case):
                self.capture.with_suffix(".webp").unlink(missing_ok=True)
                image = Image.new("RGBA", (80, 80), (0, 0, 0, 0))
                if case == "metadata":
                    metadata = PngInfo()
                    metadata.add_text("author", "Inventy")
                    image.save(self.capture, pnginfo=metadata)
                else:
                    second = Image.new("RGBA", (80, 80), (255, 0, 0, 255))
                    image.save(self.capture, save_all=True, append_images=[second], duration=100)
                original = self.capture.read_bytes()
                article_text = "![Screen](../assets/capturas/sales/step-1.png)\n"
                self.article.write_text(article_text, encoding="utf-8")

                report = load_converter().migrate_screenshots(self.docs, [self.capture])

                self.assertEqual((report.converted, report.retained), (0, 1))
                self.assertEqual(self.capture.read_bytes(), original)
                self.assertFalse(self.capture.with_suffix(".webp").exists())
                self.assertEqual(self.article.read_text(encoding="utf-8"), article_text)

    def test_retains_png_if_any_live_reference_cannot_be_rewritten(self):
        unsupported = [
            '![Titled](../assets/capturas/sales/step-1.png "Title")',
            '[screen]: ../assets/capturas/sales/step-1.png',
            '<img src="../assets/capturas/sales/step-1.png">',
        ]
        for reference in unsupported:
            with self.subTest(reference=reference):
                self.capture.with_suffix(".webp").unlink(missing_ok=True)
                Image.new("RGBA", (80, 80), (0, 0, 0, 0)).save(self.capture)
                original = self.capture.read_bytes()
                article_text = f"![Screen](../assets/capturas/sales/step-1.png)\n{reference}\n"
                self.article.write_text(article_text, encoding="utf-8")

                report = load_converter().migrate_screenshots(self.docs, [self.capture])

                self.assertEqual((report.converted, report.retained), (0, 1))
                self.assertEqual(self.capture.read_bytes(), original)
                self.assertFalse(self.capture.with_suffix(".webp").exists())
                self.assertEqual(self.article.read_text(encoding="utf-8"), article_text)

    def test_retains_png_with_unrecognized_ancillary_metadata(self):
        import zlib

        Image.new("RGBA", (80, 80), (0, 0, 0, 0)).save(self.capture)
        original = self.capture.read_bytes()
        chunk_type = b"vpAg"
        payload = b"semantic metadata"
        chunk = (
            len(payload).to_bytes(4, "big")
            + chunk_type
            + payload
            + zlib.crc32(chunk_type + payload).to_bytes(4, "big")
        )
        iend = original.rfind(b"\x00\x00\x00\x00IEND")
        self.capture.write_bytes(original[:iend] + chunk + original[iend:])
        original = self.capture.read_bytes()
        self.article.write_text("![Screen](../assets/capturas/sales/step-1.png)\n", encoding="utf-8")

        report = load_converter().migrate_screenshots(self.docs, [self.capture])

        self.assertEqual((report.converted, report.retained), (0, 1))
        self.assertEqual(self.capture.read_bytes(), original)
        self.assertFalse(self.capture.with_suffix(".webp").exists())


if __name__ == "__main__":
    unittest.main()
