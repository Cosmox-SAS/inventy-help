# Centro de Ayuda Inventy

Documentación funcional para **usuarios finales** de Inventy ERP: empresarios, administradores, contadores, vendedores, cajeros y auxiliares.

Portal público: [ayuda.inventy.com.co](https://ayuda.inventy.com.co/).

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
scripts/capturas/      Robot de capturas (capturar.mjs, placeholders.mjs, guias/*.yaml)
scripts/sync_erp.py    Detecta cambios de interfaz en inventy-erp (hook tras cada pull)
scripts/actualizar_guias.sh, claude_actualizar.sh, prompt_actualizacion.md  Actualización automática con Claude Code
```

## Cómo agregar o actualizar un artículo

1. Crea una rama: `git switch -c docs/pos-consignaciones`.
2. Copia la plantilla a la carpeta del módulo. Por defecto usa `plantillas/guia-rapida.md` (pasos directos). Usa `plantillas/tutorial.md` solo si el proceso necesita explicación, y `plantillas/solucion-rapida.md` para problemas.
3. Redacta siguiendo `gestion/guia-de-estilo.md`. Usa los nombres **exactos** de la interfaz.
4. Agrega el artículo al `nav` de `mkdocs.yml`.
5. Valida:

    ```bash
    .venv/bin/python scripts/build_docs.py
    ```

6. Actualiza el tablero: `.venv/bin/python scripts/check_docs.py --estado > gestion/estado-articulos.md`.
7. Abre un Pull Request. GitHub Actions ejecuta las mismas validaciones.

## Estados de revisión

`borrador` → `pendiente-validacion` → `validado` → `publicado` (y `requiere-actualizacion` cuando cambia la interfaz).

- Todo artículo que no esté `publicado` muestra un aviso en el portal.
- Un artículo con `CAPTURA PENDIENTE` o `PENDIENTE DE VALIDACIÓN FUNCIONAL` no puede pasar a `publicado` (lo bloquea `check_docs.py`).
- Para pasar a `validado`, una persona sigue los pasos en Inventy (empresa de demostración) y confirma que funcionan.

## Capturas de pantalla automáticas

Cada paso de cada guía lleva una captura real. Un robot (Playwright + Google Chrome) entra al **ambiente demo** de Inventy, recorre la guía y toma la foto con el botón del paso resaltado.

```bash
npm install                                  # una vez
cp .env.capturas.example .env.capturas       # y completa URL, correo y contraseña del usuario DEMO
npm run capturas                             # todas las guías
npm run capturas -- pos/cierre-de-caja       # solo una guía
npm run capturas -- --ver                    # viendo el navegador
npm run capturas:placeholders                # imágenes "Captura pendiente" para las que falten
```

- Recorridos por guía: `scripts/capturas/guias/*.yaml` (acciones: `menu`, `ir`, `abrir`, `llenar`, `escribir`, `tecla`, `esperar`, `pausa`; `resaltar`, `recortar`, `manual`, `sin_sesion`).
- **Nunca guarda datos en la demo:** bloquea clics en *Guardar, Confirmar, Crear, Validar, Aprobar…* salvo que el paso tenga `guarda_datos: true` y se corra con `CAPTURAS_PERMITIR_GUARDAR=1`. Toma la foto justo antes de confirmar.
- Resultado en `gestion/capturas-reporte.md` (pasos que fallaron y pasos de captura manual).
- `.env.capturas` no se sube a Git. Usa solo un usuario de una **empresa de demostración**.

Para migrar capturas PNG del repositorio a WebP sin pérdida, agrega primero a
Git los PNG nuevos y ejecuta `python3 scripts/optimize_screenshots.py`. El
script solo examina PNG presentes en el índice y convierte aquellos cuyo WebP
es más pequeño y conserva los píxeles decodificados; mantiene los originales
cuando una conversión podría perder metadatos o animación. Revisa las imágenes,
los enlaces actualizados y las eliminaciones, vuelve a preparar los cambios y
ejecuta las validaciones antes de confirmar la migración. **No** uses esta
migración manual como paso habitual de validación.

## Actualización automática con cada pull de inventy-erp

Cada vez que haces `git pull` en tu copia local de **inventy-erp**:

1. Un hook compara los textos que ve el usuario (botones, campos, mensajes, menús, estados, permisos) antes y después del pull.
2. Si alguna guía cita un texto que **ya no existe en ninguna parte** de Inventy, o aparecen/desaparecen opciones de menú, se crea la rama `actualizacion/erp-<commit>` en una carpeta aparte (`../inventy-help-actualizaciones/`). Tu `main` y tus cambios en curso no se tocan.
3. **Claude Code** corre en segundo plano sobre esa rama: lee el código nuevo del ERP (solo lectura), corrige las guías con los nombres exactos, crea guías rápidas para opciones de menú nuevas, valida el sitio y hace commit en la rama.
4. Recibes una notificación de macOS. Revisas y unes:

```bash
git diff main...actualizacion/erp-<commit>          # revisar
git merge actualizacion/erp-<commit>                 # aceptar
git worktree remove ../inventy-help-actualizaciones/erp-<commit> && git branch -d actualizacion/erp-<commit>
```

Nunca bloquea el pull, nunca modifica inventy-erp y nunca hace push. Las guías tocadas quedan en `pendiente-validacion` (o `requiere-actualizacion` si no se pudo verificar): una persona debe validarlas.

| Qué | Cómo |
|---|---|
| Instalar (una vez por máquina) | `sh scripts/instalar_hook.sh ../inventy-erp` |
| Quitar | `sh scripts/instalar_hook.sh --desinstalar ../inventy-erp` |
| Solo marcar guías, sin Claude | crear el archivo `.sin-actualizacion-automatica` o `export INVENTY_HELP_AUTO=0` |
| Tope de gasto por ejecución | `export INVENTY_HELP_PRESUPUESTO=5` (USD, por defecto 5) |
| Ver el progreso | `tail -f .logs/erp-<commit>.log` |
| Revisar un rango a mano | `python3 scripts/sync_erp.py --desde HEAD~20 --simular` |
| Cambiar las instrucciones de Claude | editar `scripts/prompt_actualizacion.md` |

## Mantenimiento con cada versión de Inventy

Cuando `inventy-erp` publique un release que cambie pantallas, menús o mensajes:

1. Revisar la rama `actualizacion/erp-<commit>` y su `gestion/cambios-erp.md` (se generan solos tras el pull).
2. Unirla a `main`, completar capturas y lo que quedó `requiere-actualizacion`.
3. Validar en Inventy y cambiar el estado.

## Publicación

El sitio de producción está disponible en [ayuda.inventy.com.co](https://ayuda.inventy.com.co/). El proyecto `inventy-help` de Cloudflare Pages, conectado a `Cosmox-SAS/inventy-help`, publica automáticamente los cambios de `main`; [inventy-help.pages.dev](https://inventy-help.pages.dev/) sigue disponible como dirección alternativa, sin redirección configurada. Pages tiene habilitadas las vistas previas para las ramas que no son de producción. Comprueba la URL de una vista previa en el despliegue del PR antes de compartirla: la configuración está verificada, pero todavía no se ha comprobado un despliegue de vista previa real.

GitHub Actions ejecuta `.github/workflows/docs-check.yml` en los pull requests y los cambios de `main`. Pages utiliza Python 3.12 (archivo `.python-version`), publica la carpeta `site` y ejecuta este comando de compilación:

```bash
python -m pip install -r requirements.txt && python scripts/build_docs.py --optimize-screenshots
```

El script valida artículos, ejecuta las pruebas y compila MkDocs en modo estricto; un error detiene esa compilación. `--optimize-screenshots` solo funciona en el entorno de GitHub Actions o Cloudflare Pages y convierte capturas dentro de su copia de compilación: no crea commits ni modifica la rama remota. En local, ejecuta `.venv/bin/python scripts/build_docs.py` **sin** esa opción para validar sin convertir archivos fuente. La migración permanente se hace por separado, con el comando manual de la sección de capturas.

### Comprobar un despliegue o resolver un fallo

1. En el PR, consulta **Checks** o la pestaña **Actions** del repositorio para ver el resultado y los registros de `Validate Help Center`. Una ejecución correcta allí no confirma por sí sola que Pages haya publicado el sitio.
2. En Cloudflare, abre **Workers & Pages → inventy-help → Deployments**. Revisa el estado y el registro del despliegue correspondiente a la rama y al commit; para producción, abre también [ayuda.inventy.com.co](https://ayuda.inventy.com.co/) y comprueba la página afectada.
3. Si falla una comprobación, corrige la causa en la rama y repite la validación local. Después de publicar el cambio autorizado, comprueba la nueva ejecución de Actions y el nuevo despliegue de Pages. Si Pages falla aunque Actions pase, revisa primero el registro de compilación de Pages y su configuración de Python, comando y carpeta de salida.

No se presupone una regla de protección de ramas: la revisión y la decisión de unir el PR corresponden a las personas responsables. Para revertir un cambio publicado, prepara y valida una reversión del commit mediante un nuevo PR; no cambies producción, el dominio ni la configuración de Cloudflare sin autorización explícita. Hasta que la reversión se publique, la dirección `pages.dev` puede servir para comparar el despliegue, pero no es un mecanismo de rollback independiente.
