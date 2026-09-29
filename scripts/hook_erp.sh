#!/bin/sh
# Lo llaman los hooks post-merge y post-rewrite de inventy-erp.
# Nunca bloquea el pull: cualquier error se reporta y se ignora.

HELP_DIR="$(cd "$(dirname "$0")/.." && pwd)"
HOOK="$(basename "$1")"
shift

# post-rewrite también se dispara con `git commit --amend`; solo nos interesa el rebase de un pull.
if [ "$HOOK" = "post-rewrite" ] && [ "${1:-}" != "rebase" ]; then
    exit 0
fi

PYTHON="$HELP_DIR/.venv/bin/python"
[ -x "$PYTHON" ] || PYTHON="python3"

ERP_DIR="$(git rev-parse --show-toplevel)"

"$PYTHON" "$HELP_DIR/scripts/sync_erp.py" --erp "$ERP_DIR" --desde ORIG_HEAD --hasta HEAD || {
    echo "[centro de ayuda] No se pudo revisar los cambios (el pull sí se completó)."
    exit 0
}

# Actualiza el tablero de estado si hay entorno con dependencias.
if [ -x "$HELP_DIR/.venv/bin/python" ]; then
    "$HELP_DIR/.venv/bin/python" "$HELP_DIR/scripts/check_docs.py" --estado > "$HELP_DIR/gestion/estado-articulos.md" 2>/dev/null || true
fi
exit 0
