---
title: "¿Cómo registro una devolución de venta?"
description: "Pasos para registrar la devolución total o parcial de una factura."
estado: pendiente-validacion
tipo: rapida
modulo: ventas
menu: "Ventas › Devoluciones"
permisos:
  - Ver devoluciones de venta
  - Crear devoluciones de venta
revisado: 2026-09-30
tags:
  - Ventas
  - Devoluciones
  - Nota crédito
---

# ¿Cómo registro una devolución de venta?

<p class="tambien-se-busca">También se busca como: devolución, cliente devuelve, cambio de producto, nota crédito, reversar venta, producto defectuoso.</p>

**Antes de empezar:** la factura debe estar **Validada**.

## Pasos

**Paso 1.** Ingresa a <span class="ruta">Ventas › Devoluciones</span> y crea una **Nueva devolución**.

![Paso 1: lista de devoluciones](../assets/capturas/ventas/devolucion-venta/paso-1.png)

**Paso 2.** Elige **Cliente**, **Sucursal**, **Factura de Venta** y **Motivo**.

![Paso 2: información general de la devolución](../assets/capturas/ventas/devolucion-venta/paso-2.png)

**Paso 3.** En **Ítems a Devolver**, elige **Devolución Total** o **Devolución Parcial** e indica las cantidades.

![Paso 3: ítems a devolver](../assets/capturas/ventas/devolucion-venta/paso-3.png)

**Paso 4.** Revisa el **Total a devolver** y confirma la devolución.

![Paso 4: total y confirmación](../assets/capturas/ventas/devolucion-venta/paso-4.png)

✅ **Listo:** la devolución queda **Confirmada**, el inventario vuelve y la factura muestra *Devolución total* o *parcial*. Si emites automático, se envía la **nota crédito** a la DIAN.

## Si algo falla

| Problema | Solución |
|---|---|
| No aparece la factura | Elige primero el **Cliente**. Solo salen facturas validadas. |
| *No hay una resolución activa de nota crédito disponible para esta sucursal.* | Registra una [resolución](../facturacion-electronica/resoluciones.md) para nota crédito. |
| La nota crédito fue rechazada | Ver [documento rechazado](../facturacion-electronica/documento-rechazado.md). |

## Relacionados

- [¿Cómo hago una factura de venta?](crear-factura-venta.md)
