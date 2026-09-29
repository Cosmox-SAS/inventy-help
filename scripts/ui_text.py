"""Extrae los textos visibles para el usuario desde el código de Inventy ERP.

Funciona sobre archivos .tsx/.ts (pantallas) y .php (estados, permisos y mensajes).
Solo se usa para detectar cambios de interfaz; nunca se publica.
"""
from __future__ import annotations

import re

JSX_TEXT = re.compile(r">\s*([^<>{}\n][^<>{}]{1,160}?)\s*<")
PROP = re.compile(
    r"\b(?:label|title|placeholder|description|helperText|hint|emptyMessage|emptyTitle|emptyDescription"
    r"|confirmText|cancelText|confirmLabel|message|tooltip|aria-label|triggerLabel)\s*[=:]\s*[{]?\s*(['\"`])((?:(?!\1).){2,200})\1"
)
TOAST = re.compile(r"(?:toast|notify)(?:\.\w+)?\(\s*(['\"`])((?:(?!\1).){3,200})\1")
QUOTED = re.compile(r"(['\"])([¿¡A-ZÁÉÍÓÚÑ][^'\"\n]{3,200})\1")
ES_HINT = re.compile(
    r"[áéíóúñ¿¡]|\b(el|la|los|las|de|del|para|con|sin|una|un|no|se|por|debe|puede|guardar|crear|nuevo|nueva)\b",
    re.I,
)
CODEY = re.compile(r"^[\w.\-/@:]+$|=>|&&|\|\||className|\bconst\b|\$\{|^\s*\)|;\s*$|::|->")


def _clean(src: str) -> str:
    src = re.sub(r"^\s*(import|use|namespace) .*$", "", src, flags=re.M)
    src = re.sub(r"/\*.*?\*/", "", src, flags=re.S)
    return re.sub(r"^\s*(//|#|\*).*$", "", src, flags=re.M)


def extract(src: str, path: str = "") -> set[str]:
    """Devuelve el conjunto de textos visibles de un archivo."""
    src = _clean(src)
    found: list[str] = []
    if path.endswith(".php"):
        found += [m.group(2) for m in QUOTED.finditer(src) if ES_HINT.search(m.group(2)) or " " in m.group(2)]
    else:
        found += [m.group(1) for m in JSX_TEXT.finditer(src)]
        found += [m.group(2) for m in PROP.finditer(src)]
        found += [m.group(2) for m in TOAST.finditer(src)]
        found += [m.group(2) for m in QUOTED.finditer(src) if ES_HINT.search(m.group(2))]

    textos: set[str] = set()
    for texto in found:
        texto = re.sub(r"\s+", " ", texto).strip()
        if len(texto) >= 3 and not CODEY.search(texto) and re.search(r"[A-Za-zÁÉÍÓÚáéíóúñÑ]", texto):
            textos.add(texto)
    return textos
