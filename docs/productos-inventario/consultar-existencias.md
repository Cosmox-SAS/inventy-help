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

![Paso 1: pantalla Stock](../assets/capturas/productos-inventario/consultar-existencias/paso-1.png)

**Paso 2.** Mira el **Total empresa**: el valor del inventario de todas las sedes.

![Paso 2: Total empresa](../assets/capturas/productos-inventario/consultar-existencias/paso-2.png)

**Paso 3.** Busca el producto en **Buscar por código o sede...** o filtra por categoría.

![Paso 3: buscador de stock](../assets/capturas/productos-inventario/consultar-existencias/paso-3.png)

**Paso 4.** Revisa la fila: existencias, **Costo sin IVA**, **Costo con IVA** y **Valor Inventario**. Usa **Ver detalle** para más información.

![Paso 4: tabla de existencias](../assets/capturas/productos-inventario/consultar-existencias/paso-4.png)

**Paso 5.** (Opcional) Haz clic en **Exportar Excel**.

![Paso 5: botón Exportar Excel](../assets/capturas/productos-inventario/consultar-existencias/paso-5.png)

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
