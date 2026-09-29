---
title: ¿Cómo registro un pago a un proveedor?
description: Registra el pago de facturas de compra o un anticipo a un proveedor.
estado: pendiente-validacion
tipo: tutorial
modulo: finanzas
menu: Tesorería › Operación › Egresos
permisos:
  - Gestionar egresos
revisado: 2026-09-29
tags:
  - Tesorería
  - Proveedores
  - Gastos
---

# ¿Cómo registro un pago a un proveedor?

<p class="tambien-se-busca">También se busca como: egreso, pagar proveedor, comprobante de egreso, abono a proveedor, pagar factura de compra, registrar gasto, anticipo a proveedor.</p>

## ¿Para qué sirve?

Cuando pagas una o varias facturas de un proveedor, registras un **egreso**. Así baja lo que le debes, el dinero sale de tu caja o banco y se genera la contabilidad.

!!! info "¿Quieres registrar un gasto?"
    Primero registra la **factura del gasto** como [factura de compra](../compras/registrar-factura-compra.md). Después, registra su **pago** aquí.

## Antes de comenzar

- [ ] Que el proveedor tenga **facturas de compra pendientes** (para pagos).
- [ ] Una **caja abierta** o una **cuenta bancaria** de donde sale el dinero.
- [ ] Permiso: **Gestionar egresos**.

## Paso a paso

**Paso 1.** Ingresa a <span class="ruta">Tesorería › Egresos</span> y haz clic en **Nuevo egreso**.

**Paso 2. Información del egreso.**

| Campo | Qué hacer |
|---|---|
| **Fecha de egreso** | Fecha del registro. |
| **Tipo de movimiento** | **Pago a proveedor** o **Anticipo a proveedor**. |
| **Proveedor** | A quién le pagas. |
| **Centro de costo** | El que corresponda. |
| **Fecha del pago** | Cuándo se hizo el pago. |
| **Fuente del pago** | **Caja** o **Cuenta bancaria** de donde sale el dinero. |
| **Egreso Total** | Valor pagado. |
| Comprobante (opcional) | Número del comprobante o voucher. |

**Paso 3. Distribución del egreso.** Asigna el valor a las facturas que estás pagando hasta que **Por distribuir** quede en cero.

!!! captura "CAPTURA PENDIENTE"
    Formulario **Nuevo egreso** con la Distribución del egreso completa.

**Paso 4.** Elige **Guardar borrador** o **Finalizar egreso** y confirma.

## Resultado esperado

- El egreso queda finalizado en <span class="ruta">Tesorería › Egresos</span>.
- El saldo de las facturas de compra baja.
- El dinero sale de la caja o cuenta bancaria elegida.

## Problemas frecuentes

??? question "“No hay destinos disponibles: habilita el módulo bancario o abre una caja.”"
    Necesitas una caja **abierta** o una **cuenta bancaria** activa.

??? question "“La suma de las asignaciones debe ser igual al valor total”"
    Ajusta los valores asignados a las facturas hasta que **Por distribuir** quede en cero.

??? question "Quiero borrar un egreso"
    Solo se pueden eliminar egresos en **borrador**: *“Se eliminará este egreso en borrador y su distribución.”*

## ¿Necesitas ayuda?

[Contacta a soporte](../soporte.md) con el **proveedor**, los **números de factura** y el **valor** pagado.

## Artículos relacionados

- [¿Cómo registro una factura de compra?](../compras/registrar-factura-compra.md)
- [¿Cómo registro un pago de un cliente?](registrar-ingreso.md)
