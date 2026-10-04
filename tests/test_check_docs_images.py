import importlib.util
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "check_docs.py"
spec = importlib.util.spec_from_file_location("check_docs", SCRIPT)
check_docs = importlib.util.module_from_spec(spec)
spec.loader.exec_module(check_docs)


class WebPValidationTests(unittest.TestCase):
    def test_quick_guide_accepts_webp_and_detects_pending_webp(self):
        with tempfile.TemporaryDirectory() as directory:
            docs = Path(directory)
            article = docs / "sales/article.md"
            article.parent.mkdir()
            pending = docs / "assets/capturas/pending.txt"
            pending.parent.mkdir(parents=True)
            pending.write_text("assets/capturas/sales/step-1.png\n", encoding="utf-8")
            article.write_text(
                "---\ntitle: Example\ndescription: Example\nestado: publicado\n"
                "tipo: rapida\nmodulo: sales\nrevisado: 2026-10-04\n---\n"
                "## Pasos\n**Paso 1.** Do something.\n"
                "![Screen](../assets/capturas/sales/step-1.webp)\n"
                "## Si algo falla\nHelp.\n## Relacionados\nNone.\n",
                encoding="utf-8",
            )
            with patch.object(check_docs, "DOCS", docs), patch.object(check_docs, "PENDIENTES_CAPTURAS", pending):
                self.assertEqual(
                    check_docs.validar(article),
                    ["estado 'publicado' con capturas provisionales (Captura pendiente)"],
                )


if __name__ == "__main__":
    unittest.main()
