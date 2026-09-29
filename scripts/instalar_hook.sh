#!/bin/sh
# Instala en tu copia local de inventy-erp los hooks que avisan al Centro de Ayuda
# después de cada `git pull` (merge o rebase). No modifica archivos versionados
# de inventy-erp: solo escribe en .git/hooks de tu máquina.
#
# Uso:  sh scripts/instalar_hook.sh [ruta-a-inventy-erp]
#       sh scripts/instalar_hook.sh --desinstalar [ruta-a-inventy-erp]
set -eu

HELP_DIR="$(cd "$(dirname "$0")/.." && pwd)"
MARCA="# centro-de-ayuda-inventy"

DESINSTALAR=0
if [ "${1:-}" = "--desinstalar" ]; then
    DESINSTALAR=1
    shift
fi
ERP_DIR="$(cd "${1:-$HELP_DIR/../inventy-erp}" && pwd)"
HOOKS_DIR="$(git -C "$ERP_DIR" rev-parse --git-path hooks)"
case "$HOOKS_DIR" in /*) ;; *) HOOKS_DIR="$ERP_DIR/$HOOKS_DIR" ;; esac

for HOOK in post-merge post-rewrite; do
    DESTINO="$HOOKS_DIR/$HOOK"

    if [ "$DESINSTALAR" -eq 1 ]; then
        if [ -f "$DESTINO" ] && grep -q "$MARCA" "$DESTINO"; then
            rm "$DESTINO"
            echo "✓ Eliminado $DESTINO"
        fi
        continue
    fi

    if [ -f "$DESTINO" ] && ! grep -q "$MARCA" "$DESTINO"; then
        echo "✗ Ya existe un hook $HOOK que no es del Centro de Ayuda: $DESTINO"
        echo "  No lo sobrescribo. Agrega a mano esta línea al final de ese archivo:"
        echo "  sh \"$HELP_DIR/scripts/hook_erp.sh\" \"\$0\" \"\$@\""
        continue
    fi

    cat > "$DESTINO" <<EOF
#!/bin/sh
$MARCA
# Instalado por $HELP_DIR/scripts/instalar_hook.sh
sh "$HELP_DIR/scripts/hook_erp.sh" "\$0" "\$@"
EOF
    chmod +x "$DESTINO"
    echo "✓ Instalado $DESTINO"
done
