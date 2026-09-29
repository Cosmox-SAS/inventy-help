#!/bin/sh
# Actualización automática del Centro de Ayuda tras un pull de inventy-erp.
#
# 1. Crea una rama `actualizacion/erp-<hasta>` en una carpeta de trabajo aparte
#    (git worktree), sin tocar tu copia principal de inventy-help.
# 2. Corre el detector de cambios allí.
# 3. Si hay guías afectadas u opciones de menú nuevas, lanza Claude Code en
#    segundo plano para actualizarlas (scripts/claude_actualizar.sh).
#
# Uso: sh scripts/actualizar_guias.sh <ruta-inventy-erp> <desde> <hasta>
set -eu

HELP_DIR="$(cd "$(dirname "$0")/.." && pwd)"
ERP_DIR="$1"
DESDE="$2"
HASTA="$3"

RAMA="actualizacion/erp-$HASTA"
WT_BASE="$(cd "$HELP_DIR/.." && pwd)/inventy-help-actualizaciones"
WT="$WT_BASE/erp-$HASTA"
LOGS="$HELP_DIR/.logs"
JSON="$LOGS/erp-$HASTA.json"
LOG="$LOGS/erp-$HASTA.log"
PYTHON="$HELP_DIR/.venv/bin/python"
[ -x "$PYTHON" ] || PYTHON="python3"

mkdir -p "$LOGS" "$WT_BASE"

if git -C "$HELP_DIR" rev-parse --verify -q "refs/heads/$RAMA" >/dev/null; then
    echo "[centro de ayuda] La rama $RAMA ya existe; no se vuelve a generar."
    exit 0
fi

BASE="$(git -C "$HELP_DIR" rev-parse --verify -q refs/heads/main || git -C "$HELP_DIR" rev-parse HEAD)"
git -C "$HELP_DIR" worktree add -q -b "$RAMA" "$WT" "$BASE"

"$PYTHON" "$WT/scripts/sync_erp.py" --erp "$ERP_DIR" --desde "$DESDE" --hasta "$HASTA" --json "$JSON" | sed 's/^/  /'

PENDIENTES="$("$PYTHON" -c "import json,sys; d=json.load(open(sys.argv[1])); print(len(d['guias_afectadas']) + len(d['menu_nuevo']) + len(d['menu_quitado']))" "$JSON" 2>/dev/null || echo 0)"

if [ "$PENDIENTES" = "0" ]; then
    git -C "$HELP_DIR" worktree remove --force "$WT"
    git -C "$HELP_DIR" branch -q -D "$RAMA"
    echo "[centro de ayuda] Ninguna guía necesita cambios."
    exit 0
fi

if ! command -v claude >/dev/null 2>&1; then
    git -C "$WT" add -A
    git -C "$WT" commit -q -m "docs: marcar guías afectadas por inventy-erp $DESDE..$HASTA"
    echo "[centro de ayuda] Claude Code no está instalado: dejé las guías marcadas en la rama $RAMA."
    exit 0
fi

nohup sh "$HELP_DIR/scripts/claude_actualizar.sh" "$WT" "$ERP_DIR" "$DESDE" "$HASTA" "$JSON" > "$LOG" 2>&1 &

echo "[centro de ayuda] $PENDIENTES cambio(s) para el Centro de Ayuda. Claude Code los está aplicando en segundo plano."
echo "[centro de ayuda]   Rama: $RAMA"
echo "[centro de ayuda]   Carpeta: $WT"
echo "[centro de ayuda]   Progreso: tail -f $LOG"
echo "[centro de ayuda] Te aviso con una notificación cuando termine."
