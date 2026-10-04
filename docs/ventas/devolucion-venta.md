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

![Paso 1: lista de devoluciones](../assets/capturas/ventas/devolucion-venta/paso-1.webp)

**Paso 2.** Elige **Cliente**, **Sucursal**, **Factura de Venta** y **Motivo**.

![Paso 2: información general de la devolución](../assets/capturas/ventas/devolucion-venta/paso-2.webp)

**Paso 3.** En **Ítems a Devolver**, elige **Devolución Parcial** o **Devolución Total**. En parcial, escribe la **Cant. a devolver** de cada producto.

![Paso 3: ítems a devolver](../assets/capturas/ventas/devolucion-venta/paso-3.webp)

**Paso 4.** En **Reintegro**, elige cómo le devuelves el dinero al cliente: **Efectivo** (sale de tu caja) o **Nota crédito** (queda como saldo a favor para su próxima compra). Revisa **Reduce cartera**, **Efectivo** y **Nota crédito**.

![Paso 4: forma de reintegro](../assets/capturas/ventas/devolucion-venta/paso-4.webp)

**Paso 5.** Revisa el **Total a devolver**, haz clic en **Confirmar devolución** y confirma.

![Paso 5: botón Confirmar devolución](../assets/capturas/ventas/devolucion-venta/paso-5.webp)

✅ **Listo:** la devolución queda **Confirmada**, el inventario vuelve y la factura muestra *Devolución total* o *parcial*. Si elegiste **Nota crédito**, el cliente queda con saldo a favor (<span class="ruta">Ventas › Notas crédito</span>). Si emites automático, se envía la nota crédito electrónica a la DIAN.

## Si algo falla

| Problema | Solución |
|---|---|
| No aparece la factura | Elige primero el **Cliente**. Solo salen facturas validadas. |
| *No hay una resolución activa de nota crédito disponible para esta sucursal.* | Registra una [resolución](../facturacion-electronica/resoluciones.md) para nota crédito. |
| La nota crédito fue rechazada | Ver [documento rechazado](../facturacion-electronica/documento-rechazado.md). |

## Relacionados

- [¿Cómo hago una factura de venta?](crear-factura-venta.md)
