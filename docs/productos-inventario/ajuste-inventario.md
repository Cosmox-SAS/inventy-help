---
title: "¿Cómo hago un ajuste de inventario?"
description: "Pasos para registrar entradas o salidas manuales de inventario."
estado: pendiente-validacion
tipo: rapida
modulo: productos-inventario
menu: "Inventario › Ajuste de inventario"
permisos:
  - Ver ajustes de inventario
  - Crear ajustes de inventario
revisado: 2026-09-30
tags:
  - Inventario
  - Ajustes
---

# ¿Cómo hago un ajuste de inventario?

<p class="tambien-se-busca">También se busca como: corregir inventario, entrada de inventario, salida de inventario, dar de baja, producto dañado, pérdida, sobrante, inventario inicial, cargar existencias.</p>

## Pasos

**Paso 1.** Ingresa a <span class="ruta">Inventario › Ajuste de inventario</span> y haz clic en **Nuevo ajuste**.

![Paso 1: botón Nuevo ajuste](../assets/capturas/productos-inventario/ajuste-inventario/paso-1.png)

**Paso 2.** Elige la **Sede** y escribe el motivo (ej. *Inventario inicial*).

![Paso 2: datos del ajuste](../assets/capturas/productos-inventario/ajuste-inventario/paso-2.png)

**Paso 3.** Haz clic en **Agregar linea**, elige el **Tipo de ajuste** (entrada o salida), el producto y la cantidad. Repite por cada producto.

![Paso 3: líneas del ajuste](../assets/capturas/productos-inventario/ajuste-inventario/paso-3.png)

**Paso 4.** Haz clic en **Confirmar ajuste** y confirma.

![Paso 4: botón Confirmar ajuste](../assets/capturas/productos-inventario/ajuste-inventario/paso-4.png)

✅ **Listo:** el ajuste queda **Completado** y el stock cambia. Ya no se puede editar.

## Si algo falla

| Problema | Solución |
|---|---|
| *Stock insuficiente…* | Estás sacando más de lo que hay en esa sede. Revisa cantidad y sede. |
| *El ajuste deja stock por debajo del reservado.* | Parte del stock está reservado (pedido o traslado). Saca menos. |
| Me equivoqué en un ajuste confirmado | Haz otro ajuste en sentido contrario, o pide que lo anulen (permiso **Anular ajustes de inventario**). |
| ¿Muchos productos? | Usa **Importar ajuste**. |

## Relacionados

- [¿Cuánto inventario tengo?](consultar-existencias.md)
