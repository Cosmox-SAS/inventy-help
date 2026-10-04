---
title: "¿Cuánto inventario tengo?"
description: "Pasos para consultar existencias y valor del inventario por sede."
estado: pendiente-validacion
tipo: rapida
modulo: productos-inventario
menu: "Inventario › Stock"
permisos:
  - Ver stock
revisado: 2026-09-30
tags:
  - Inventario
  - Stock
---

# ¿Cuánto inventario tengo?

<p class="tambien-se-busca">También se busca como: existencias, stock, saldo de inventario, cuánto me queda, unidades disponibles, valor del inventario, inventario por bodega.</p>

## Pasos

**Paso 1.** Ingresa a <span class="ruta">Inventario › Stock</span>.

![Paso 1: pantalla Stock](../assets/capturas/productos-inventario/consultar-existencias/paso-1.webp)

**Paso 2.** Mira arriba el valor del inventario: el total de la sede elegida y el **Total empresa** (todas las sedes).

![Paso 2: Total empresa](../assets/capturas/productos-inventario/consultar-existencias/paso-2.webp)

**Paso 3.** Busca el producto en **Buscar por código o sede...**, o filtra por sede y categoría. Usa **Actualizar** para recargar.

![Paso 3: buscador de stock](../assets/capturas/productos-inventario/consultar-existencias/paso-3.webp)

**Paso 4.** Revisa la fila: **Cantidad**, **Reservado** (apartado para pedidos o traslados), **Disponible** (lo que puedes vender), **Costo sin IVA**, **Costo con IVA**, **Rentabilidad** y **Valor Inventario**. En **Acciones** verás más detalle.

![Paso 4: tabla de existencias](../assets/capturas/productos-inventario/consultar-existencias/paso-4.webp)

**Paso 5.** (Opcional) Haz clic en **Exportar Excel**.

![Paso 5: botón Exportar Excel](../assets/capturas/productos-inventario/consultar-existencias/paso-5.webp)

✅ **Listo:** conoces las unidades y el valor de cada producto por sede.

## Si algo falla

| Problema | Solución |
|---|---|
| *No hay stock registrado* | Aún no hay movimientos: registra una compra o un ajuste de entrada. |
| Un producto no aparece | Puede estar marcado **No maneja inventario** o no tener movimientos. |
| No cuadra con la bodega | Revisa el **Kardex** del producto y haz un **Conteo físico** o un [ajuste](ajuste-inventario.md). |
| Productos por agotarse | <span class="ruta">Inventario › Alertas de stock</span>. |

## Relacionados

- [¿Cómo hago un ajuste de inventario?](ajuste-inventario.md)
- [¿Cómo hago un traslado entre sedes?](traslados.md)
