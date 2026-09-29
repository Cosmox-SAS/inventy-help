#!/bin/sh
# Trabajo en segundo plano: Claude Code actualiza las guías en la carpeta de la
# rama de actualización, se valida el sitio y se hace commit en esa rama.
# Lo lanza scripts/actualizar_guias.sh; no se llama a mano.
#
# Variables opcionales:
#   INVENTY_HELP_PRESUPUESTO  tope de gasto en USD por ejecución (por defecto 5)
#   INVENTY_HELP_MODELO       modelo de Claude a usar (por defecto el configurado)
set -u

WT="$1"
ERP_DIR="$2"
DESDE="$3"
HASTA="$4"
JSON="$5"

HELP_DIR="$(cd "$(dirname "$0")/.." && pwd)"
PYTHON="$HELP_DIR/.venv/bin/python"
MKDOCS="$HELP_DIR/.venv/bin/mkdocs"
RAMA="actualizacion/erp-$HASTA"
HOY="$(date +%Y-%m-%d)"
PRESUPUESTO="${INVENTY_HELP_PRESUPUESTO:-5}"

avisar() {
    echo "$1"
    osascript -e "display notification \"$1\" with title \"Centro de Ayuda Inventy\"" >/dev/null 2>&1 || true
}

echo "== $(date '+%Y-%m-%d %H:%M:%S') Inicio: inventy-erp $DESDE..$HASTA en $WT"

ERP_ESTADO_ANTES="$(git -C "$ERP_DIR" status --porcelain)"

PROMPT="$(sed \
    -e "s|{ERP}|$ERP_DIR|g" \
    -e "s|{DESDE}|$DESDE|g" \
    -e "s|{HASTA}|$HASTA|g" \
    -e "s|{JSON}|$JSON|g" \
    -e "s|{HOY}|$HOY|g" \
    -e "s|{PYTHON}|$PYTHON|g" \
    -e "s|{MKDOCS}|$MKDOCS|g" \
    "$HELP_DIR/scripts/prompt_actualizacion.md")"

set -- \
    --permission-mode dontAsk \
    --add-dir "$ERP_DIR" \
    --add-dir "$(dirname "$JSON")" \
    --allowedTools \
        "Read" "Glob" "Grep" "Edit" "Write" \
        "Bash(git -C $ERP_DIR grep:*)" \
        "Bash(git -C $ERP_DIR diff:*)" \
        "Bash(git -C $ERP_DIR show:*)" \
        "Bash(git -C $ERP_DIR log:*)" \
        "Bash($PYTHON scripts/check_docs.py:*)" \
        "Bash($MKDOCS build:*)" \
    --disallowedTools \
        "Edit(/$ERP_DIR/**)" "Write(/$ERP_DIR/**)" \
        "Edit(scripts/**)" "Write(scripts/**)" \
        "Edit(.github/**)" "Write(.github/**)" \
    --max-budget-usd "$PRESUPUESTO"

if [ -n "${INVENTY_HELP_MODELO:-}" ]; then
    set -- "$@" --model "$INVENTY_HELP_MODELO"
fi

cd "$WT" || exit 1
claude -p "$PROMPT" "$@"
RESULTADO_CLAUDE=$?
echo "== Claude Code terminó con código $RESULTADO_CLAUDE"

# Seguridad: el ERP no debe haber cambiado.
if [ "$(git -C "$ERP_DIR" status --porcelain)" != "$ERP_ESTADO_ANTES" ]; then
    avisar "⚠️ Se detectaron cambios en inventy-erp durante la actualización. Revísalos con git status."
fi

VALIDACION="ok"
"$PYTHON" scripts/check_docs.py || VALIDACION="falló check_docs"
"$MKDOCS" build --strict -q || VALIDACION="falló mkdocs build"
"$PYTHON" scripts/check_docs.py --estado > gestion/estado-articulos.md 2>/dev/null || true

git add -A
if git diff --cached --quiet; then
    avisar "Claude Code no hizo cambios para inventy-erp $HASTA. Revisa el log."
    exit 0
fi

git commit -q -F - <<EOF
docs: actualizar guías por cambios de inventy-erp $DESDE..$HASTA

Generado automáticamente tras el pull de inventy-erp.
Validación: $VALIDACION.
Revisar antes de unir a main: gestion/cambios-erp.md.

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
EOF

echo "== Commit en $RAMA: $(git log --oneline -1)"
if [ "$VALIDACION" = "ok" ]; then
    avisar "Guías actualizadas en la rama $RAMA. Revisa y une a main cuando quieras."
else
    avisar "Guías actualizadas en $RAMA, pero la validación $VALIDACION. Revisa el log."
fi
