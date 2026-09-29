#!/bin/sh
# Lo llaman los hooks post-merge y post-rewrite de inventy-erp.
# Nunca bloquea el pull: cualquier error se reporta y se ignora.
#
# Modo automático (por defecto, si Claude Code está instalado): las guías se
# actualizan solas en una rama aparte (scripts/actualizar_guias.sh).
# Para desactivarlo: crea el archivo inventy-help/.sin-actualizacion-automatica
# o exporta INVENTY_HELP_AUTO=0. Así solo se marcan las guías afectadas.

HELP_DIR="$(cd "$(dirname "$0")/.." && pwd)"
HOOK="$(basename "$1")"
shift

# post-rewrite también se dispara con `git commit --amend`; solo nos interesa el rebase de un pull.
if [ "$HOOK" = "post-rewrite" ] && [ "${1:-}" != "rebase" ]; then
    exit 0
fi

ERP_DIR="$(git rev-parse --show-toplevel)"
DESDE="$(git rev-parse --short ORIG_HEAD 2>/dev/null)" || exit 0
HASTA="$(git rev-parse --short HEAD)"
[ "$DESDE" = "$HASTA" ] && exit 0

# Git exporta variables del repo del ERP a los hooks; no deben filtrarse a inventy-help.
unset GIT_DIR GIT_WORK_TREE GIT_INDEX_FILE GIT_PREFIX GIT_OBJECT_DIRECTORY GIT_COMMON_DIR

PYTHON="$HELP_DIR/.venv/bin/python"
[ -x "$PYTHON" ] || PYTHON="python3"

if [ "${INVENTY_HELP_AUTO:-1}" != "0" ] && [ ! -f "$HELP_DIR/.sin-actualizacion-automatica" ]; then
    sh "$HELP_DIR/scripts/actualizar_guias.sh" "$ERP_DIR" "$DESDE" "$HASTA" || \
        echo "[centro de ayuda] No se pudo iniciar la actualización automática (el pull sí se completó)."
    exit 0
fi

"$PYTHON" "$HELP_DIR/scripts/sync_erp.py" --erp "$ERP_DIR" --desde "$DESDE" --hasta "$HASTA" || {
    echo "[centro de ayuda] No se pudo revisar los cambios (el pull sí se completó)."
    exit 0
}
if [ -x "$HELP_DIR/.venv/bin/python" ]; then
    "$HELP_DIR/.venv/bin/python" "$HELP_DIR/scripts/check_docs.py" --estado > "$HELP_DIR/gestion/estado-articulos.md" 2>/dev/null || true
fi
exit 0
