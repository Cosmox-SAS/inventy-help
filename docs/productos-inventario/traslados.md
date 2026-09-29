---
title: ¿Cómo hago un traslado entre sedes?
description: Pasos para trasladar mercancía de una sede a otra.
estado: pendiente-validacion
tipo: rapida
modulo: productos-inventario
menu: Inventario › Traslados
permisos:
  - Crear traslados de inventario
  - Aprobar traslados de inventario
  - Confirmar recepción de traslados
revisado: 2026-09-29
search:
  boost: 2
tags:
  - Inventario
  - Traslados
---

# ¿Cómo hago un traslado entre sedes?

<p class="tambien-se-busca">También se busca como: traslado de inventario, mover mercancía, transferencia entre sedes, pasar inventario a otra tienda, recibir traslado.</p>

<span class="ruta">Inventario › Traslados</span>

## Pasos

**Solicitar**

1. <span class="ruta">Inventario › Traslados</span> › **Nuevo traslado**.
2. Elige **Sede de origen** y **Sede de destino**.
3. **Agregar producto** › busca el producto › escribe la cantidad. Repite por cada producto.
4. **Solicitar traslado** › confirma.

**Aprobar** (otro usuario, de la sede de origen)

5. Abre el traslado (estado **Solicitado**).
6. Ajusta la cantidad aprobada si envías menos (0 = no se envía).
7. **Aprobar** › confirma.

**Recibir** (sede de destino, o quien lo solicitó)

8. Abre el traslado (estado **Aprobado**).
9. **Recibir** › **Confirmar recepcion**.

✅ Listo: la mercancía sale del origen y entra al destino.

!!! captura "CAPTURA PENDIENTE"
    Detalle de un traslado Solicitado con el botón **Aprobar** resaltado.

## Si algo falla

| Problema | Solución |
|---|---|
| No aparece **Aprobar** | Debe aprobarlo **otro usuario** (no quien lo solicitó), asignado a la **sede de origen** y con el permiso **Aprobar traslados de inventario**. |
| No aparece **Recibir** | Debe hacerlo un usuario de la **sede de destino** con el permiso **Confirmar recepción de traslados**, o quien lo solicitó. |
| *Stock insuficiente en la sede de origen…* | Aprueba menos cantidad o deja ese producto en 0. |
| *La sede de origen y destino no pueden ser la misma* | Cambia una de las dos sedes. |
| Me equivoqué y ya lo solicité | Que la sede de origen lo **Rechace** › **Clonar** › corrige › solicita de nuevo. |
| El stock del producto aparece reservado | Hay un traslado **Aprobado** sin recibir. Que el destino lo reciba. |

## Relacionados

- [¿Cuánto inventario tengo?](consultar-existencias.md)
- [¿Cómo hago un ajuste de inventario?](ajuste-inventario.md)
