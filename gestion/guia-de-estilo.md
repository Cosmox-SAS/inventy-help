# Guía de estilo del Centro de Ayuda

> Documento interno. Aplica a todo artículo dentro de `docs/`.

## Para quién escribimos

Empresarios, administradores, contadores, vendedores, cajeros, auxiliares de inventario y empleados. **No** escribimos para desarrolladores.

## Formato por defecto: guía rápida

Para el equipo comercial de Inventy (y para cualquier usuario con prisa), las guías van **al grano**: plantilla `plantillas/guia-rapida.md` (`tipo: rapida`).

- Solo **Pasos**, **Si algo falla** y **Relacionados**.
- Un paso = una línea, con la ruta del menú y el botón exacto: `Inventario › Traslados › **Nuevo traslado**`.
- Sin explicar conceptos, sin “¿para qué sirve?”, sin párrafos introductorios.
- Si el proceso lo hacen varias personas, agrupa los pasos por rol en una línea en negrita (**Aprobar** (sede de origen)).
- Cierra con `✅ Listo:` y el resultado en una línea.
- Problemas en tabla de dos columnas: *Problema | Solución*, una línea cada una.

La plantilla larga (`plantillas/tutorial.md`, `tipo: tutorial`) queda solo para procesos que de verdad necesiten contexto (por ejemplo, facturación electrónica ante la DIAN).

## Voz y tono

- Español de Colombia, claro y profesional. Tuteo (“ingresa”, “selecciona”).
- Frases cortas. Un paso = una acción.
- Verbos de interfaz: **haz clic en**, **selecciona**, **escribe**, **ingresa al menú**.
- Sin tecnicismos: nada de controladores, endpoints, base de datos, tenant, API (salvo “app móvil”).

| ❌ Evitar | ✅ Preferir |
|---|---|
| El sistema persiste la entidad. | Inventy guarda el producto. |
| Tenant | Empresa |
| Sesión de caja en estado OPEN | Caja abierta |
| Error 403 | “No tienes permiso para…” |
| Endpoint / API móvil | App móvil de Inventy |

## Nombres de la interfaz

- Se escriben **exactamente** como aparecen en pantalla, en **negrita** para botones y campos.
- Rutas de menú con la clase `ruta`: `<span class="ruta">Ventas › Facturas</span>`.
- Nunca inventar botones, campos ni pantallas. Si no se pudo verificar: `[PENDIENTE DE VALIDACIÓN FUNCIONAL: …]` y estado `pendiente-validacion`.

## Títulos

- Formulados como la pregunta del usuario: “¿Cómo cierro la caja?”, “¿Por qué no me deja guardar un producto?”.
- Debajo del título, la línea `También se busca como:` con sinónimos y formas coloquiales (ayuda al buscador).

## Capturas de pantalla

- Solo capturas **reales** de Inventy, tomadas en una empresa de demostración (sin datos de clientes reales).
- Guardar en `docs/assets/capturas/<modulo>/<guia>-<n>.png`, ancho 1440 px (escritorio) o 390 px (móvil).
- Resaltar con recuadros o flechas en el color de acento; nunca tapar texto relevante.
- Mientras no exista la captura:

```markdown
!!! captura "CAPTURA PENDIENTE"
    Formulario de creación de producto, resaltando el botón **Crear Producto**.
```

## Estados de revisión (campo `estado`)

| Estado | Significado | ¿Quién lo cambia? |
|---|---|---|
| `borrador` | En redacción. | Redactor |
| `pendiente-validacion` | Redactado a partir del código; falta confirmar en la interfaz real. | Redactor |
| `validado` | Alguien siguió los pasos en Inventy y funcionan. | Validador (soporte / producto) |
| `publicado` | Validado, con capturas reales y revisión editorial. | Responsable del Centro de Ayuda |
| `requiere-actualizacion` | Cambió la interfaz o el proceso. | Cualquiera |

Todo artículo que no esté `publicado` muestra automáticamente un aviso en la parte superior. **Un artículo con `CAPTURA PENDIENTE` o `PENDIENTE DE VALIDACIÓN` no puede estar `publicado`** (lo valida `scripts/check_docs.py`).

## Soporte y datos sensibles

- Nunca pedir contraseñas, PIN, códigos de verificación ni datos completos de tarjetas.
- Sí pedir: nombre de la empresa, correo del usuario afectado, número del documento, fecha y hora, captura del mensaje de error.
