---
title: ¿Cómo hago una factura de venta?
description: Crea, guarda y valida una factura de venta de contado o a crédito desde el menú Ventas.
estado: pendiente-validacion
tipo: tutorial
modulo: ventas
menu: Ventas › Facturas
permisos:
  - Ver facturas de venta
  - Crear facturas de venta
revisado: 2026-09-29
tags:
  - Ventas
  - Facturación
---

# ¿Cómo hago una factura de venta?

<p class="tambien-se-busca">También se busca como: facturar, crear factura, nueva factura, factura a crédito, cuenta de cobro, vender a crédito, factura de contado.</p>

## ¿Para qué sirve?

Para registrar una venta con todos sus detalles: cliente, fecha, forma de pago (contado o crédito), centro de costo, retenciones y observaciones. Al **validarla**, Inventy descuenta el inventario, registra la cuenta por cobrar y genera la contabilidad.

**Úsala cuando:** vendes desde la oficina, a crédito, o necesitas más detalle del que permite el POS.

## Antes de comenzar

- [ ] El **cliente** debe estar [creado](crear-cliente.md).
- [ ] Los **productos o servicios** deben existir y tener precio.
- [ ] Debe existir al menos un **centro de costo**.
- [ ] Permisos: **Ver facturas de venta** y **Crear facturas de venta**.

## Paso a paso

**Paso 1.** Ingresa a <span class="ruta">Ventas › Facturas</span> y haz clic en **Nueva Factura**. Se abre **Nueva Factura de Venta**.

!!! captura "CAPTURA PENDIENTE"
    Formulario **Nueva Factura de Venta**: sección Información General arriba e Ítems de la Factura abajo.

**Paso 2. Información General.**

| Campo | Qué hacer |
|---|---|
| **Cliente** | Búscalo por nombre o documento. |
| **Centro de costo** | Selecciona el que corresponda. |
| **Fecha de emisión** | Por defecto, hoy. **No puede ser una fecha futura.** |
| **Forma de pago** | **Contado** o **Crédito**. |
| **Medio de Pago** | Efectivo, transferencia, etc. (en contado). |
| Voucher o referencia | Número del comprobante, si aplica. |
| Fecha de vencimiento | En crédito: cuándo debe pagar el cliente. |
| Anticipos del cliente | Si el cliente tiene **saldo a favor**, puedes aplicarlo aquí. |
| Calcular retención en la fuente por | Si el cliente practica retención. |
| Vendedor (opcional) | Quién hizo la venta. |
| Observaciones | Notas que quieras dejar en la factura. |

**Paso 3. Ítems de la Factura.** Haz clic en **Agregar ítem**, busca el producto o servicio y escribe cantidad, precio y descuento si aplica. Repite para cada ítem.

**Paso 4.** Revisa el **Total a pagar**.

**Paso 5.** Elige:

- **Guardar borrador**: la guardas sin confirmar. Puedes editarla después.
- **Validar factura**: la confirmas.

**Paso 6.** Si elegiste validar, confirma en **¿Validar factura?** Lee el aviso: *“Al validar ya no podrás editar la factura.”*

## Resultado esperado

- La factura aparece en <span class="ruta">Ventas › Facturas</span> con estado **Validada** (o **Pagada** si fue de contado y quedó cubierta).
- Si tu empresa tiene la **emisión automática** activa, se envía sola a la DIAN. Si no, usa **Emitir electrónica** desde el detalle de la factura. Ver [¿Cómo emito una factura electrónica?](../facturacion-electronica/emitir-factura-electronica.md).
- Desde el detalle puedes **Imprimir tirilla**, **Ver asientos** o **Convertir en recurrente**.

## ¿Me equivoqué en una factura validada?

Una factura validada **no se puede editar**. Según el caso:

- **Devolución** de todo o parte de lo vendido: registra una [devolución de venta](devolucion-venta.md).
- **Anular factura:** desde el detalle, con un **Motivo de anulación**. *Esta acción no se puede revertir.* No es posible anular ventas que ya movieron inventario ni ventas que vienen de remisiones: en esos casos usa la devolución.

## Problemas frecuentes

??? question "“La fecha de emisión no puede ser una fecha futura.”"
    Cambia la fecha a hoy o a una fecha anterior.

??? question "“Este cliente no tiene cupo de crédito disponible.”"
    Aumenta su **Límite de crédito** en la ficha del cliente, o factura de contado.

??? question "“El asiento contable no está balanceado”"
    Algún producto, impuesto o medio de pago no tiene su cuenta contable configurada. Pide a tu contador que revise la configuración contable y el **Catálogo de Impuestos**.

??? question "“El centro de costo es obligatorio.”"
    Selecciona un centro de costo. Si no existe ninguno, créalo en <span class="ruta">Configuración › Centros de Costo</span>.

??? question "“No puedes anular una venta con movimientos de inventario.”"
    Registra una [devolución de venta](devolucion-venta.md) en lugar de anular.

## ¿Necesitas ayuda?

[Contacta a soporte](../soporte.md) si no puedes validar una factura después de revisar lo anterior. Envía el **código de la factura** (o una captura del borrador) y el **mensaje de error**.

## Artículos relacionados

- [¿Cómo creo un cliente?](crear-cliente.md)
- [¿Cómo emito una factura electrónica?](../facturacion-electronica/emitir-factura-electronica.md)
- [¿Cómo registro una devolución de venta?](devolucion-venta.md)
- [¿Cómo registro un pago de un cliente?](../finanzas/registrar-ingreso.md)
