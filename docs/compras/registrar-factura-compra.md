---
title: ¿Cómo registro una factura de compra?
description: Registra la factura de un proveedor para ingresar la mercancía al inventario y la cuenta por pagar.
estado: pendiente-validacion
tipo: tutorial
modulo: compras
menu: Compras › Operación › Facturas
permisos:
  - Crear facturas de compra
revisado: 2026-09-29
tags:
  - Compras
  - Proveedores
---

# ¿Cómo registro una factura de compra?

<p class="tambien-se-busca">También se busca como: registrar compra, ingresar mercancía, entrada de mercancía, factura de proveedor, cargar compra, registrar gasto con factura.</p>

## ¿Para qué sirve?

Para registrar lo que te facturó un proveedor. Al validarla, Inventy **suma la mercancía a tu inventario**, registra lo que le **debes al proveedor** y genera la contabilidad.

## Antes de comenzar

- [ ] Ten la factura del proveedor (idealmente el **XML o ZIP** de su factura electrónica).
- [ ] Los productos deben existir en tu catálogo (o créalos durante el registro).
- [ ] Tu empresa debe tener activo el módulo **Compras**.
- [ ] Permiso: **Crear facturas de compra**.

## Paso a paso

**Paso 1.** Ingresa a <span class="ruta">Compras › Facturas</span> y haz clic en **Nueva Factura**. Se abre **Nueva Factura de Compra**.

**Paso 2. (Recomendado) Completa la factura con el documento del proveedor.** Sube el **XML o ZIP** de la factura electrónica (también acepta PDF o imagen). Inventy lee el documento y busca el proveedor y los productos en tu catálogo.

!!! warning "Verifica los datos leídos"
    Los valores que la IA leyó del documento aparecen marcados: *“Este valor lo leyó la IA del documento. Verifícalo.”* Compáralos siempre con la factura.

!!! captura "CAPTURA PENDIENTE"
    Zona **Completa la factura con el documento del proveedor** y un campo marcado como leído por la IA.

**Paso 3. Elige el modo de registro:**

| Modo | Úsalo cuando |
|---|---|
| **Compra Directa** | Compraste sin orden de compra. Agregas los ítems a mano. |
| **Con Orden de Compra** | La compra viene de una orden de compra. Los ítems se cargan desde la orden. |
| **Asiento Manual** | [PENDIENTE DE VALIDACIÓN FUNCIONAL: casos de uso.] |

**Paso 4. Información General.**

| Campo | Qué escribir |
|---|---|
| **Proveedor** | Búscalo. Si no existe, puedes crearlo. |
| **Centro de costo** | El que corresponda. |
| **Orden de Compra** | Solo en modo *Con Orden de Compra*. |
| **N° Factura Proveedor** | El número de la factura del proveedor (ej. `FE-001234`). |
| **Fecha de emisión** | La fecha de la factura. |
| Plazo de pago (días) / Fecha de vencimiento | Cuándo debes pagarla. |
| Calcular retención en la fuente por | Si le practicas retención al proveedor. |
| **Cuenta a Pagar (Neto)** | Cuenta contable de la deuda con el proveedor. |
| Requiere documento soporte electrónico | Se marca solo si el proveedor **no está obligado a facturar**. |

**Paso 5. Ítems de la Factura.** Haz clic en **Agregar ítem** y registra cada producto con cantidad, precio y descuento. En modo *Con Orden de Compra*, los ítems se cargan de la orden.

**Paso 6.** Revisa el **Total a pagar** y elige **Guardar borrador** o **Registrar Factura**. Confirma en **¿Validar factura?**

## Resultado esperado

- La factura aparece en <span class="ruta">Compras › Facturas</span> con su **Total COP** y **Saldo COP**.
- El inventario de los productos aumenta en la sede.
- Si el proveedor no está obligado a facturar y tu empresa emite automáticamente, se genera el **documento soporte electrónico**.

## Problemas frecuentes

??? question "“El número de factura ya existe para este proveedor.” / “Esta factura ya está registrada”"
    Esa factura ya se registró. Búscala en la lista por número o proveedor.

??? question "“No encontramos este proveedor”"
    El proveedor del documento no está en tu lista. Revisa los datos y usa **Crear proveedor**, o selecciona uno existente.

??? question "“No se pudo leer el documento.”"
    Prueba con el **XML** o el **ZIP** original de la factura electrónica. Si no lo tienes, registra la factura a mano.

??? question "“El precio debe ser mayor a 0.”"
    Todos los ítems deben tener precio.

??? question "“El asiento contable no está balanceado”"
    Falta una cuenta contable en algún producto, impuesto o en la **Cuenta a Pagar**. Pide a tu contador que la revise.

??? question "Cambié de modo y se borraron los ítems"
    Al cambiar entre *Compra Directa* y *Con Orden de Compra*, Inventy limpia los ítems cargados (te lo advierte antes de hacerlo).

## ¿Necesitas ayuda?

[Contacta a soporte](../soporte.md) con el **número de la factura del proveedor**, el **nombre del proveedor** y el archivo XML si el problema es con la lectura del documento.

## Artículos relacionados

- [¿Cómo registro un pago a un proveedor?](../finanzas/registrar-egreso.md)
- [¿Cuánto inventario tengo?](../productos-inventario/consultar-existencias.md)
