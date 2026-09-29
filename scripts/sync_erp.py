#!/usr/bin/env python3
"""Detecta cambios de interfaz en Inventy ERP y marca las guías afectadas.

Se ejecuta automáticamente después de cada `git pull` en inventy-erp (hook
post-merge / post-rewrite instalado con scripts/instalar_hook.sh), o a mano:

    python3 scripts/sync_erp.py --erp ../inventy-erp --desde ORIG_HEAD --hasta HEAD
    python3 scripts/sync_erp.py --erp ../inventy-erp --desde HEAD~30 --simular

Qué hace:
1. Compara los textos visibles (botones, campos, mensajes, menús, estados,
   permisos) de los archivos que cambiaron entre dos versiones.
2. Si una guía cita un texto que desapareció o cambió, la marca como
   `requiere-actualizacion`.
3. Escribe el reporte gestion/cambios-erp.md con lo que cambió, las guías
   afectadas y las pantallas nuevas que aún no tienen guía.

No hace commit ni push: los cambios quedan en inventy-help para revisarlos.
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from ui_text import extract  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
REPORTE = ROOT / "gestion" / "cambios-erp.md"

# Rutas de inventy-erp que definen lo que el usuario ve.
RUTAS_UI = [
    "resources/js/pages",
    "resources/js/components",
    "modules/*/App/Enums",
    "modules/*/App/Http/Requests",
    "modules/*/App/Actions",
    "modules/*/App/Http/Controllers",
    "lang/es",
]
EXTENSIONES = (".tsx", ".ts", ".php")
IGNORAR = re.compile(r"(\.test\.|__tests__|/Tests/|\.d\.ts$)")
NAVEGACION = "resources/js/components/navigation/navigation-registry.ts"
ESTADO_FM = re.compile(r"^(estado:\s*)([\w-]+)\s*$", re.M)
FRONT_MATTER = re.compile(r"\A---\n(.*?)\n---\n", re.S)


def git(erp: Path, *args: str) -> str:
    resultado = subprocess.run(["git", "-C", str(erp), *args], capture_output=True, text=True)
    if resultado.returncode != 0:
        raise RuntimeError(resultado.stderr.strip() or f"git {' '.join(args)} falló")
    return resultado.stdout


def contenido(erp: Path, rev: str, ruta: str) -> str:
    try:
        return git(erp, "show", f"{rev}:{ruta}")
    except RuntimeError:
        return ""


def archivos_cambiados(erp: Path, desde: str, hasta: str) -> list[tuple[str, str]]:
    salida = git(erp, "diff", "--name-status", "--no-renames", desde, hasta, "--", *RUTAS_UI)
    cambios = []
    for linea in salida.splitlines():
        estado, _, ruta = linea.partition("\t")
        if ruta.endswith(EXTENSIONES) and not IGNORAR.search(ruta):
            cambios.append((estado[0], ruta))
    return cambios


def titulos_menu(fuente: str) -> set[str]:
    return set(re.findall(r"(?:title|label):\s*'([^']+)'", fuente))


def sigue_existiendo(erp: Path, rev: str, texto: str, cache: dict[str, bool]) -> bool:
    """True si el texto sigue apareciendo en algún archivo de interfaz de la versión nueva."""
    if texto not in cache:
        resultado = subprocess.run(
            ["git", "-C", str(erp), "grep", "-q", "-F", texto, rev, "--", *RUTAS_UI],
            capture_output=True,
        )
        cache[texto] = resultado.returncode == 0
    return cache[texto]


def cargar_guias() -> dict[Path, str]:
    return {p: p.read_text(encoding="utf-8") for p in sorted(DOCS.rglob("*.md"))}


def citado_en(texto: str, cuerpo: str) -> bool:
    """Una guía cita un texto si aparece literal (en negrita, cursiva o entre comillas)."""
    if len(texto) < 4:
        return False
    return texto in cuerpo


def marcar_requiere_actualizacion(path: Path, cuerpo: str) -> bool:
    match = FRONT_MATTER.match(cuerpo)
    if not match:
        return False
    front = match.group(1)
    estado = ESTADO_FM.search(front)
    if not estado or estado.group(2) == "requiere-actualizacion":
        return False
    nuevo_front = ESTADO_FM.sub(r"\1requiere-actualizacion", front, count=1)
    path.write_text(cuerpo.replace(front, nuevo_front, 1), encoding="utf-8")
    return True


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--erp", default=str(ROOT.parent / "inventy-erp"), help="ruta del repo inventy-erp")
    parser.add_argument("--desde", default="ORIG_HEAD", help="versión anterior (por defecto ORIG_HEAD)")
    parser.add_argument("--hasta", default="HEAD", help="versión nueva (por defecto HEAD)")
    parser.add_argument("--simular", action="store_true", help="muestra el resultado sin modificar archivos")
    parser.add_argument("--json", help="además, guarda el resultado en este archivo JSON")
    args = parser.parse_args()

    erp = Path(args.erp).resolve()
    try:
        desde = git(erp, "rev-parse", "--short", args.desde).strip()
        hasta = git(erp, "rev-parse", "--short", args.hasta).strip()
    except RuntimeError as error:
        print(f"[centro de ayuda] No se pudo leer el rango de versiones: {error}")
        return 0

    if desde == hasta:
        return 0

    cambios = archivos_cambiados(erp, desde, hasta)
    if not cambios:
        print(f"[centro de ayuda] {desde}..{hasta}: sin cambios de interfaz.")
        return 0

    guias = cargar_guias()
    # guía -> texto desaparecido -> textos nuevos en los mismos archivos (posibles reemplazos)
    afectadas: dict[Path, dict[str, set[str]]] = {}
    textos_eliminados_total = 0
    pantallas_nuevas: list[str] = []
    detalle_archivos: list[str] = []
    cache_existencia: dict[str, bool] = {}

    for estado, ruta in cambios:
        antes = extract(contenido(erp, desde, ruta), ruta) if estado != "A" else set()
        despues = extract(contenido(erp, hasta, ruta), ruta) if estado != "D" else set()
        eliminados = sorted(antes - despues)
        agregados = sorted(despues - antes)

        if estado == "A" and ruta.startswith("resources/js/pages/") and ruta.endswith(".tsx"):
            pantallas_nuevas.append(ruta)

        if not eliminados and not agregados:
            continue

        textos_eliminados_total += len(eliminados)
        detalle_archivos.append(
            f"- `{ruta}` ({ {'A': 'nuevo', 'D': 'eliminado', 'M': 'modificado'}.get(estado, estado)}):"
            f" {len(eliminados)} texto(s) quitados, {len(agregados)} agregados"
        )
        for texto in eliminados:
            citantes = [p for p, cuerpo in guias.items() if citado_en(texto, cuerpo)]
            if not citantes or sigue_existiendo(erp, hasta, texto, cache_existencia):
                continue
            for path in citantes:
                afectadas.setdefault(path, {}).setdefault(texto, set()).update(agregados[:3])

    menu_antes = titulos_menu(contenido(erp, desde, NAVEGACION))
    menu_despues = titulos_menu(contenido(erp, hasta, NAVEGACION))
    menu_nuevo = sorted(menu_despues - menu_antes)
    menu_quitado = sorted(menu_antes - menu_despues)
    for texto in menu_quitado:
        if sigue_existiendo(erp, hasta, texto, cache_existencia):
            continue
        for path, cuerpo in guias.items():
            if citado_en(texto, cuerpo):
                afectadas.setdefault(path, {}).setdefault(texto, set())

    marcadas = []
    if not args.simular:
        for path in afectadas:
            if marcar_requiere_actualizacion(path, guias[path]):
                marcadas.append(path)

    # ── Reporte ──────────────────────────────────────────────────────────────
    ahora = dt.datetime.now().strftime("%Y-%m-%d %H:%M")
    asunto = git(erp, "log", "-1", "--format=%s", hasta).strip()
    lineas = [
        f"## {ahora} · inventy-erp `{desde}..{hasta}`",
        "",
        f"Último commit: {asunto}",
        "",
        f"**{len(cambios)}** archivos de interfaz cambiaron · **{textos_eliminados_total}** textos quitados · "
        f"**{len(afectadas)}** guías afectadas.",
        "",
    ]
    if afectadas:
        lineas += ["### Guías que requieren actualización", ""]
        for path, textos in sorted(afectadas.items()):
            lineas.append(f"- [ ] [{path.relative_to(DOCS)}](../docs/{path.relative_to(DOCS).as_posix()})")
            for texto, reemplazos in sorted(textos.items()):
                pista = f" → posible reemplazo: {', '.join(f'«{r}»' for r in sorted(reemplazos))}" if reemplazos else ""
                lineas.append(f"    - «{texto}» ya no existe en Inventy{pista}")
        lineas.append("")
    if menu_nuevo or menu_quitado:
        lineas += ["### Cambios en el menú", ""]
        lineas += [f"- ➕ {t}" for t in menu_nuevo] + [f"- ➖ {t}" for t in menu_quitado]
        lineas.append("")
    if pantallas_nuevas:
        lineas += ["### Pantallas nuevas (revisar si necesitan guía)", ""]
        lineas += [f"- `{p}`" for p in pantallas_nuevas]
        lineas.append("")
    if detalle_archivos:
        lineas += ["<details><summary>Archivos con cambios de texto</summary>", "", *detalle_archivos, "", "</details>", ""]

    bloque = "\n".join(lineas)
    if args.json:
        Path(args.json).write_text(
            json.dumps(
                {
                    "desde": desde,
                    "hasta": hasta,
                    "commit": asunto,
                    "guias_afectadas": {
                        p.relative_to(DOCS).as_posix(): {t: sorted(r) for t, r in textos.items()}
                        for p, textos in sorted(afectadas.items())
                    },
                    "menu_nuevo": menu_nuevo,
                    "menu_quitado": menu_quitado,
                    "pantallas_nuevas": pantallas_nuevas,
                },
                ensure_ascii=False,
                indent=2,
            ),
            encoding="utf-8",
        )
    if args.simular:
        print(bloque)
        return 0

    encabezado = "# Cambios de Inventy ERP que afectan el Centro de Ayuda\n\n> Generado por `scripts/sync_erp.py` después de cada `git pull` en inventy-erp. Lo más reciente, arriba.\n\n"
    previo = REPORTE.read_text(encoding="utf-8").split("\n", 4)[-1] if REPORTE.exists() else ""
    previo = previo[previo.find("## "):] if "## " in previo else ""
    REPORTE.write_text(encabezado + bloque + "\n" + previo, encoding="utf-8")

    print(
        f"[centro de ayuda] {len(cambios)} archivos de interfaz cambiaron; "
        f"{len(afectadas)} guía(s) afectada(s), {len(marcadas)} marcada(s) como 'requiere-actualizacion'."
    )
    print(f"[centro de ayuda] Reporte: {REPORTE}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
