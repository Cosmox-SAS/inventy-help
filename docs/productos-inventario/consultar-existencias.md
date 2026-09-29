---
title: ¿Cuánto inventario tengo?
description: Consulta las existencias y el valor de tu inventario por producto y por sede.
estado: pendiente-validacion
tipo: tutorial
modulo: productos-inventario
menu: Inventario › Existencias › Stock
permisos:
  - Ver stock
revisado: 2026-09-29
tags:
  - Inventario
  - Stock
---

# ¿Cuánto inventario tengo?

<p class="tambien-se-busca">También se busca como: existencias, stock, saldo de inventario, cuánto me queda, unidades disponibles, valor del inventario, inventario por bodega.</p>

## ¿Para qué sirve?

Para saber **cuántas unidades** tienes de cada producto en cada sede y **cuánto vale** tu inventario.

## Antes de comenzar

- [ ] Tu empresa debe tener activo el módulo **Inventario**.
- [ ] Permiso: **Ver stock**. Para descargar a Excel: **Exportar stock a Excel**.

## Paso a paso

**Paso 1.** Ingresa a <span class="ruta">Inventario › Stock</span>.

**Paso 2.** Arriba verás el **Total empresa**: el valor del inventario sumando todas las sedes.

!!! captura "CAPTURA PENDIENTE"
    Pantalla **Stock** con el Total empresa, filtros y la tabla de existencias.

**Paso 3.** Busca el producto en **Buscar por código o sede...** o filtra por categoría.

**Paso 4.** Lee la tabla: para cada producto y sede verás las existencias, el **Costo sin IVA**, el **Costo con IVA** y el **Valor Inventario**.

**Paso 5.** Usa **Ver detalle** para ver más información de un producto en una sede. Si hay unidades **reservadas** (por ejemplo, en pedidos o traslados pendientes), puedes ver el origen de la reserva.

**Paso 6. (Opcional)** Haz clic en **Exportar Excel** para descargar el listado.

## Resultado esperado

Conoces las existencias y el valor de cada producto por sede.

## Otras consultas útiles

| Quiero saber… | Ve a… |
|---|---|
| Qué productos están por agotarse | <span class="ruta">Inventario › Alertas de stock</span> |
| Por qué cambió la cantidad de un producto | <span class="ruta">Inventario › Movimientos</span> o **Kardex** |
| Qué lotes están por vencer | <span class="ruta">Inventario › Lotes por vencer</span> (si usas lotes) |

## Problemas frecuentes

??? question "“No hay stock registrado”"
    Todavía no hay movimientos de inventario. Registra una [compra](../compras/registrar-factura-compra.md) o un [ajuste de entrada](ajuste-inventario.md).

??? question "Un producto no aparece en el stock"
    - Puede estar marcado como **No maneja inventario**.
    - Puede que nunca haya tenido movimientos.
    - Revisa el filtro de categoría y la búsqueda.

??? question "El stock en Inventy no coincide con lo que hay en la bodega"
    Revisa el **Kardex** del producto para ver cada entrada y salida. Si hay diferencias reales, haz un **Conteo físico** o un [ajuste de inventario](ajuste-inventario.md).

## ¿Necesitas ayuda?

[Contacta a soporte](../soporte.md) si una cantidad no se explica con los movimientos. Envía el **código del producto**, la **sede** y la cantidad que esperabas ver.

## Artículos relacionados

- [¿Cómo hago un ajuste de inventario?](ajuste-inventario.md)
- [¿Cómo creo un producto?](crear-producto.md)
