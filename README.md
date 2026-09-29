# Centro de Ayuda Inventy

Documentación funcional para **usuarios finales** de Inventy ERP: empresarios, administradores, contadores, vendedores, cajeros y auxiliares.

> Este repositorio **no** contiene documentación técnica. La documentación para desarrolladores y agentes vive en `inventy-erp/documentation/`.

## Ver el sitio en local

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/mkdocs serve        # http://127.0.0.1:8000
```

## Estructura

```
docs/                  Artículos publicados en el portal (Markdown)
  primeros-pasos/  productos-inventario/  compras/  ventas/  pos/
  facturacion-electronica/  finanzas/  contabilidad/  distribucion/
  recursos-humanos/  restaurante/  administracion/
  soluciones-rapidas/  preguntas-frecuentes.md  soporte.md
  assets/capturas/     Capturas reales, por módulo
overrides/             Personalización del tema (aviso de estado de revisión)
plantillas/            Plantillas obligatorias: tutorial y solución rápida
gestion/               Documentos internos (no se publican)
  inventario-funcionalidades.md   Auditoría funcional de Inventy (Fase 1)
  guia-de-estilo.md               Reglas de redacción, capturas y estados
  estado-articulos.md             Tablero generado con el estado de cada artículo
scripts/check_docs.py  Validaciones documentales
```

## Cómo agregar o actualizar un artículo

1. Crea una rama: `git switch -c docs/pos-consignaciones`.
2. Copia la plantilla a la carpeta del módulo. Por defecto usa `plantillas/guia-rapida.md` (pasos directos). Usa `plantillas/tutorial.md` solo si el proceso necesita explicación, y `plantillas/solucion-rapida.md` para problemas.
3. Redacta siguiendo `gestion/guia-de-estilo.md`. Usa los nombres **exactos** de la interfaz.
4. Agrega el artículo al `nav` de `mkdocs.yml`.
5. Valida:

    ```bash
    .venv/bin/python scripts/check_docs.py
    .venv/bin/mkdocs build --strict
    ```

6. Actualiza el tablero: `.venv/bin/python scripts/check_docs.py --estado > gestion/estado-articulos.md`.
7. Abre un Pull Request. El workflow **Validar Centro de Ayuda** corre las mismas validaciones.

## Estados de revisión

`borrador` → `pendiente-validacion` → `validado` → `publicado` (y `requiere-actualizacion` cuando cambia la interfaz).

- Todo artículo que no esté `publicado` muestra un aviso en el portal.
- Un artículo con `CAPTURA PENDIENTE` o `PENDIENTE DE VALIDACIÓN FUNCIONAL` no puede pasar a `publicado` (lo bloquea `check_docs.py`).
- Para pasar a `validado`, una persona sigue los pasos en Inventy (empresa de demostración) y confirma que funcionan.

## Mantenimiento con cada versión de Inventy

Cuando `inventy-erp` publique un release que cambie pantallas, menús o mensajes:

1. Revisar el changelog del release.
2. Marcar como `requiere-actualizacion` los artículos afectados.
3. Actualizar texto y capturas, y volver a validar.

## Publicación

Pendiente de definir el hosting (por ejemplo, GitHub Pages, Cloudflare Pages o un subdominio `ayuda.`). No hay despliegue automático configurado. Antes de publicar, definir `site_url` en `mkdocs.yml`.
