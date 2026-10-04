---
title: "¿Cómo hago una factura de venta?"
description: "Pasos para crear y validar una factura de venta de contado o a crédito."
estado: pendiente-validacion
tipo: rapida
modulo: ventas
menu: "Ventas › Facturas"
permisos:
  - Ver facturas de venta
  - Crear facturas de venta
revisado: 2026-10-01
search:
  boost: 2
tags:
  - Ventas
  - Facturación
---

# ¿Cómo hago una factura de venta?

<p class="tambien-se-busca">También se busca como: facturar, crear factura, nueva factura, factura a crédito, cuenta de cobro, vender a crédito, factura de contado.</p>

**Antes de empezar:** el cliente y los productos deben existir.

!!! warning "Si vas a vender a crédito"
    Si tu empresa usa Contabilidad, el cliente debe tener un **Tipo de cliente** con **Cuenta por cobrar** (en su ficha: **Editar › Datos del rol de cliente › Tipo de cliente**). Si no, al validar sale *“Configura una cuenta de cuentas por cobrar en el tipo de cliente para facturar a crédito con contabilidad activa.”* Ver [cómo solucionarlo](../soluciones-rapidas/ventas.md#al-validar-la-factura-a-credito-me-pide-configurar-la-cuenta-contable).

## Pasos

**Paso 1.** Ingresa a <span class="ruta">Ventas › Facturas</span> y haz clic en **Nueva Factura**.

![Paso 1: botón Nueva Factura](../assets/capturas/ventas/crear-factura-venta/paso-1.webp)

**Paso 2.** En **Información General**, elige **Cliente**, **Centro de costo** y **Fecha de emisión**.

![Paso 2: cliente, centro de costo y fecha](../assets/capturas/ventas/crear-factura-venta/paso-2.webp)

**Paso 3.** En **Ítems de la Factura**, elige el producto en **Buscar producto...** y escribe la cantidad. El precio, el impuesto y el descuento se llenan solos. Usa **Agregar nueva línea** para más productos.

![Paso 3: ítems de la factura](../assets/capturas/ventas/crear-factura-venta/paso-3.webp)

**Paso 4.** Elige **Forma de pago**: **Contado** (con su **Medio de Pago**) o **Crédito** (verás el **Cupo disponible** y la **Fecha de vencimiento**). Hazlo **después** de agregar los productos.

![Paso 4: forma y medio de pago](../assets/capturas/ventas/crear-factura-venta/paso-4.webp)

**Paso 5.** Revisa el **Total a pagar** y haz clic en **Validar factura**. Confirma en **¿Validar factura?**

![Paso 5: botón Validar factura](../assets/capturas/ventas/crear-factura-venta/paso-5.webp)

**Paso 6.** En el detalle, **Más acciones** tiene **PDF**, **Ver asientos**, **Imprimir tirilla**, **Clonar** y **Convertir en recurrente**. Si tu empresa factura electrónicamente y no se envió sola, ahí también verás **Emitir electrónica** ([guía](../facturacion-electronica/emitir-factura-electronica.md)).

![Paso 6: menú Más acciones de la factura](../assets/capturas/ventas/crear-factura-venta/paso-6.webp)

✅ **Listo:** la factura queda **Validada** (o **Pagada**) y afecta inventario, cartera y contabilidad. Ya no se puede editar.

!!! tip "¿Aún no estás seguro?"
    Usa **Guardar borrador**: queda guardada sin afectar nada y la puedes terminar después.

## Si algo falla

| Problema | Solución |
|---|---|
| *La fecha de emisión no puede ser una fecha futura.* | Usa hoy o una fecha anterior. |
| *El monto a crédito debe ser igual al total de la factura.* | Elegiste **Crédito** antes de agregar o cambiar productos. Haz clic en **Contado** y otra vez en **Crédito** para recalcular. |
| *Este cliente no tiene cupo de crédito disponible.* | Sube su cupo o factura de contado. |
| A crédito: *Configura una cuenta de cuentas por cobrar en el tipo de cliente…* | El cliente no tiene tipo de cliente o el tipo no tiene **Cuenta por cobrar**. Ver [solución](../soluciones-rapidas/ventas.md#al-validar-la-factura-a-credito-me-pide-configurar-la-cuenta-contable). |
| *El asiento contable no está balanceado* | Usa **Ver asientos**: la línea sin cuenta dice qué falta. Si dice *Configura la cuenta por cobrar en el tipo de cliente*, asígnale al cliente un [tipo de cliente](tipos-de-cliente.md) con cuenta por cobrar. |
| *El centro de costo es obligatorio.* | Crea uno en <span class="ruta">Configuración › Centros de Costo</span>. |
| Me equivoqué en una factura validada | Haz una [devolución](devolucion-venta.md). Anular solo es posible si no movió inventario. |

## Relacionados

- [¿Cómo emito una factura electrónica?](../facturacion-electronica/emitir-factura-electronica.md)
- [¿Cómo registro un pago de un cliente?](../finanzas/registrar-ingreso.md)
