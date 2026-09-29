---
title: ¿Cómo registro un pago de un cliente?
description: Registra el recaudo de facturas a crédito o un anticipo de un cliente.
estado: pendiente-validacion
tipo: tutorial
modulo: finanzas
menu: Tesorería › Operación › Ingresos
permisos:
  - Gestionar ingresos
revisado: 2026-09-29
tags:
  - Tesorería
  - Cartera
---

# ¿Cómo registro un pago de un cliente?

<p class="tambien-se-busca">También se busca como: recaudo, abono, cliente pagó, recibo de caja, cobrar cartera, pago de factura a crédito, anticipo de cliente.</p>

## ¿Para qué sirve?

Cuando un cliente te paga una factura a crédito (total o parcial), registras un **ingreso**. Así su saldo baja, el dinero entra a tu caja o banco y se genera la contabilidad.

También sirve para registrar un **anticipo**: dinero que el cliente te paga antes de comprar. Después lo podrás aplicar a sus facturas.

## Antes de comenzar

- [ ] Que el cliente tenga **facturas a crédito pendientes** (para recaudo).
- [ ] Una **caja abierta** o una **cuenta bancaria** donde entra el dinero.
- [ ] Permiso: **Gestionar ingresos**.

## Paso a paso

**Paso 1.** Ingresa a <span class="ruta">Tesorería › Ingresos</span> y haz clic en **Nuevo ingreso**.

**Paso 2. Información del ingreso.**

| Campo | Qué hacer |
|---|---|
| **Fecha de ingreso** | Fecha del registro. |
| **Tipo de movimiento** | **Recaudo de cartera** (paga facturas) o **Anticipo de cliente**. |
| **Cliente** | Quién paga. |
| **Centro de costo** | El que corresponda. |
| **Fecha del pago** | Cuándo pagó el cliente. |
| **Destino** | **Caja** o **Cuenta bancaria** donde entra el dinero. |
| **Medio de pago** | Efectivo, transferencia electrónica, etc. |
| **Ingreso Total** | Valor recibido. |
| Comprobante (opcional) | Número del comprobante o voucher. |

!!! captura "CAPTURA PENDIENTE"
    Formulario de ingreso con la sección Distribución del ingreso y dos facturas asignadas.

**Paso 3. Distribución del ingreso** (en recaudo). Asigna el valor recibido a las facturas que el cliente está pagando. El contador **Por distribuir** debe llegar a cero: verás **Distribución completa**.

**Paso 4.** Elige **Guardar borrador** o **Finalizar ingreso** y confirma.

## Resultado esperado

- El ingreso queda finalizado en <span class="ruta">Tesorería › Ingresos</span>.
- El saldo de las facturas baja (o quedan **Pagadas**).
- El dinero aparece en la caja o cuenta bancaria elegida.

## Problemas frecuentes

??? question "“No hay destinos disponibles: habilita el módulo bancario o abre una caja.”"
    Necesitas una caja **abierta** o una **cuenta bancaria**. [Abre una caja](../pos/abrir-caja.md) o pide al administrador que cree la cuenta.

??? question "“La suma de las asignaciones debe ser igual al valor total”"
    Lo que asignaste a las facturas no suma el **Ingreso Total**. Ajusta los valores hasta que **Por distribuir** quede en cero.

??? question "“Ingresa el valor de abono para la factura con retención antes de finalizar”"
    Una de las facturas tiene retención. Escribe cuánto se abona a esa factura.

## ¿Necesitas ayuda?

[Contacta a soporte](../soporte.md) con el **cliente**, los **números de factura** y el **valor** del pago.

## Artículos relacionados

- [¿Cómo hago una factura de venta?](../ventas/crear-factura-venta.md)
- [¿Cómo registro un pago a un proveedor?](registrar-egreso.md)
