#!/usr/bin/env python3
"""Validaciones documentales del Centro de Ayuda Inventy.

Revisa cada artículo de docs/ y falla (código 1) si encuentra errores:

- Metadatos obligatorios (title, description, estado, tipo, modulo, revisado).
- Estado de revisión válido.
- Tutoriales y guías rápidas con todas las secciones de su plantilla, en orden.
- Soluciones rápidas con PROBLEMA / CAUSA / SOLUCIÓN / ESCALAR / INFORMACIÓN.
- Artículos "publicado" sin capturas ni validaciones pendientes.
- Sin lenguaje técnico de desarrollo.
- Sin pedir contraseñas ni datos sensibles en la información para soporte.

Uso:
    python scripts/check_docs.py            # valida
    python scripts/check_docs.py --estado   # imprime el tablero de estado en Markdown
"""
from __future__ import annotations

import argparse
import datetime as dt
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"

ESTADOS = {
    "borrador": "Borrador",
    "pendiente-validacion": "Pendiente de validación",
    "validado": "Validado funcionalmente",
    "publicado": "Publicado",
    "requiere-actualizacion": "Requiere actualización",
}
TIPOS = {"tutorial", "rapida", "solucion", "concepto", "indice", "faq", "referencia"}
CAMPOS_OBLIGATORIOS = ("title", "description", "estado", "tipo", "modulo", "revisado")

SECCIONES_TUTORIAL = [
    "¿Para qué sirve?",
    "Antes de comenzar",
    "Paso a paso",
    "Resultado esperado",
    "Problemas frecuentes",
    "¿Necesitas ayuda?",
    "Artículos relacionados",
]
SECCIONES_RAPIDA = ["Pasos", "Si algo falla", "Relacionados"]
CAMPOS_SOLUCION = ["PROBLEMA", "CAUSA", "SOLUCIÓN", "ESCALAR A SOPORTE", "INFORMACIÓN PARA SOPORTE"]

PENDIENTES = re.compile(r"CAPTURA PENDIENTE|PENDIENTE DE VALIDACIÓN FUNCIONAL", re.I)
TERMINOS_TECNICOS = re.compile(
    r"\b(controlador|controller|endpoint|tenant|backend|frontend|base de datos|payload|migraci[oó]n|API)\b"
)
DATOS_SENSIBLES = re.compile(r"contraseña|clave|PIN|c[oó]digo de verificaci[oó]n|tarjeta", re.I)
FRONT_MATTER = re.compile(r"\A---\n(.*?)\n---\n", re.S)
H2 = re.compile(r"^## +(.+?)\s*(\{.*\})?\s*$", re.M)
FENCE = re.compile(r"^```.*?^```", re.S | re.M)
PASO = re.compile(r"^\*\*Paso (\d+)\.\*\*", re.M)
IMAGEN = re.compile(r"!\[[^\]]*\]\(([^)\s]+assets/capturas/[^)\s]+\.(?:png|webp))\)")
PENDIENTES_CAPTURAS = DOCS / "assets" / "capturas" / "pendientes.txt"


def capturas_pendientes() -> set[str]:
    if not PENDIENTES_CAPTURAS.exists():
        return set()
    listed = {l.strip() for l in PENDIENTES_CAPTURAS.read_text(encoding="utf-8").splitlines() if l.strip()}
    # The pending manifest predates WebP migration; both suffixes identify the same screenshot.
    variants = set(listed)
    for name in listed:
        if name.endswith((".png", ".webp")):
            variants.update({str(Path(name).with_suffix(ext)) for ext in (".png", ".webp")})
    return variants


def leer(path: Path) -> tuple[dict, str]:
    texto = path.read_text(encoding="utf-8")
    match = FRONT_MATTER.match(texto)
    if not match:
        return {}, texto
    try:
        return yaml.safe_load(match.group(1)) or {}, texto[match.end():]
    except yaml.YAMLError as error:
        return {"_error_yaml": str(error).splitlines()[0]}, texto[match.end():]


def validar(path: Path) -> list[str]:
    rel = path.relative_to(DOCS)
    meta, cuerpo = leer(path)
    errores: list[str] = []

    if rel.as_posix() == "index.md":
        return errores  # la portada no lleva estado de revisión

    if "_error_yaml" in meta:
        return [f"metadatos mal escritos (usa comillas si el texto tiene ':'): {meta['_error_yaml']}"]

    for campo in CAMPOS_OBLIGATORIOS:
        if not meta.get(campo):
            errores.append(f"falta el metadato '{campo}'")

    estado = meta.get("estado")
    if estado and estado not in ESTADOS:
        errores.append(f"estado '{estado}' no válido (usa: {', '.join(ESTADOS)})")

    tipo = meta.get("tipo")
    if tipo and tipo not in TIPOS:
        errores.append(f"tipo '{tipo}' no válido (usa: {', '.join(sorted(TIPOS))})")

    revisado = meta.get("revisado")
    if revisado and not isinstance(revisado, dt.date):
        errores.append("'revisado' debe ser una fecha AAAA-MM-DD")

    sin_codigo = FENCE.sub("", cuerpo)

    secciones = {"tutorial": SECCIONES_TUTORIAL, "rapida": SECCIONES_RAPIDA}.get(tipo)
    if secciones:
        encontrados = [h.group(1).strip() for h in H2.finditer(sin_codigo)]
        faltan = [s for s in secciones if s not in encontrados]
        if faltan:
            errores.append(f"{tipo} sin secciones: {', '.join(faltan)}")
        else:
            orden = [encontrados.index(s) for s in secciones]
            if orden != sorted(orden):
                errores.append(f"las secciones de la guía {tipo} no siguen el orden de la plantilla")

    if tipo == "solucion":
        bloques = re.split(r"^## ", sin_codigo, flags=re.M)[1:]
        if not bloques:
            errores.append("solución rápida sin problemas (## ...)")
        for bloque in bloques:
            titulo = bloque.splitlines()[0].strip()
            faltan = [c for c in CAMPOS_SOLUCION if f"**{c}" not in bloque and f" {c}" not in bloque]
            if faltan:
                errores.append(f"'{titulo}': faltan {', '.join(faltan)}")
            for linea in bloque.splitlines():
                if "INFORMACIÓN PARA SOPORTE" in linea and DATOS_SENSIBLES.search(linea.split(":**", 1)[-1]):
                    errores.append(f"'{titulo}': la información para soporte pide datos sensibles")

    if tipo == "rapida":
        seccion = re.split(r"^## ", sin_codigo, flags=re.M)
        pasos_txt = next((b for b in seccion if b.startswith("Pasos")), "")
        bloques = PASO.split(pasos_txt)[1:]
        numeros = bloques[0::2]
        if not numeros:
            errores.append("la sección Pasos no tiene pasos con el formato **Paso N.**")
        for numero, texto in zip(numeros, bloques[1::2]):
            if not IMAGEN.search(texto):
                errores.append(f"el Paso {numero} no tiene captura de pantalla")
        esperados = [str(n) for n in range(1, len(numeros) + 1)]
        if numeros and numeros != esperados:
            errores.append(f"los pasos no son consecutivos: {', '.join(numeros)}")

    if estado == "publicado":
        usadas = {(path.parent / src).resolve().relative_to(DOCS.resolve()).as_posix() for src in IMAGEN.findall(sin_codigo)}
        if usadas & capturas_pendientes():
            errores.append("estado 'publicado' con capturas provisionales (Captura pendiente)")

    if estado in ("publicado", "validado") and PENDIENTES.search(sin_codigo):
        if estado == "publicado" or "VALIDACIÓN" in PENDIENTES.search(sin_codigo).group(0).upper():
            errores.append(f"estado '{estado}' con contenido pendiente (captura o validación)")

    for n, linea in enumerate(sin_codigo.splitlines(), 1):
        if TERMINOS_TECNICOS.search(linea):
            errores.append(f"lenguaje técnico en línea {n}: {TERMINOS_TECNICOS.search(linea).group(0)!r}")

    return errores


def tablero(articulos: list[Path]) -> str:
    filas = []
    conteo: dict[str, int] = {}
    for path in articulos:
        meta, cuerpo = leer(path)
        estado = meta.get("estado", "—")
        conteo[estado] = conteo.get(estado, 0) + 1
        pendientes_img = capturas_pendientes()
        imagenes = [(path.parent / s).resolve().relative_to(DOCS.resolve()).as_posix() for s in IMAGEN.findall(cuerpo)]
        capturas = len(re.findall(r"CAPTURA PENDIENTE", cuerpo)) + sum(1 for i in imagenes if i in pendientes_img)
        validaciones = len(re.findall(r"PENDIENTE DE VALIDACIÓN FUNCIONAL", cuerpo))
        filas.append(
            f"| {meta.get('modulo', '—')} | [{meta.get('title', path.stem)}](../docs/{path.relative_to(DOCS).as_posix()}) "
            f"| {meta.get('tipo', '—')} | {ESTADOS.get(estado, estado)} | {capturas} | {validaciones} | {meta.get('revisado', '—')} |"
        )
    resumen = " · ".join(f"**{ESTADOS.get(k, k)}:** {v}" for k, v in sorted(conteo.items()))
    return "\n".join(
        [
            "# Tablero de estado de artículos",
            "",
            "> Generado con `python scripts/check_docs.py --estado > gestion/estado-articulos.md`. No editar a mano.",
            "",
            resumen,
            "",
            "| Módulo | Artículo | Tipo | Estado | Capturas pendientes | Validaciones pendientes | Revisado |",
            "|---|---|---|---|---|---|---|",
            *sorted(filas),
            "",
        ]
    )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--estado", action="store_true", help="imprime el tablero de estado en Markdown")
    args = parser.parse_args()

    articulos = sorted(p for p in DOCS.rglob("*.md") if p.relative_to(DOCS).as_posix() != "index.md")

    if args.estado:
        print(tablero(articulos))
        return 0

    total = 0
    for path in [DOCS / "index.md", *articulos]:
        for error in validar(path):
            total += 1
            print(f"{path.relative_to(ROOT)}: {error}")

    if total:
        print(f"\n✗ {total} problema(s) en {len(articulos) + 1} archivos.")
        return 1
    print(f"✓ {len(articulos) + 1} archivos revisados sin problemas.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
