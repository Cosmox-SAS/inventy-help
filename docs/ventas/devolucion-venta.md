---
title: ¿Cómo registro una devolución de venta?
description: Registra la devolución total o parcial de una factura de venta validada.
estado: pendiente-validacion
tipo: tutorial
modulo: ventas
menu: Ventas › Devoluciones
permisos:
  - Ver devoluciones de venta
  - Crear devoluciones de venta
revisado: 2026-09-29
tags:
  - Ventas
  - Devoluciones
  - Nota crédito
---

# ¿Cómo registro una devolución de venta?

<p class="tambien-se-busca">También se busca como: devolución, cliente devuelve, cambio de producto, nota crédito, reversar venta, producto defectuoso.</p>

## ¿Para qué sirve?

Para registrar que un cliente te devolvió todo o parte de lo que compró. La devolución **reingresa el inventario**, ajusta lo que el cliente te debe y genera la contabilidad. Si la factura original fue electrónica, la devolución corresponde a una **nota crédito**.

## Antes de comenzar

- [ ] La factura original debe estar **Validada**.
- [ ] Permisos: **Ver devoluciones de venta** y **Crear devoluciones de venta**.

## Paso a paso

**Paso 1.** Ingresa a <span class="ruta">Ventas › Devoluciones</span> y crea una **Nueva devolución**. Se abre **Nueva Devolución de Venta**.

**Paso 2. Información General.**

| Campo | Qué hacer |
|---|---|
| **Cliente** | Selecciónalo primero. |
| **Sucursal** | Sede donde se recibe la devolución. |
| **Factura de Venta** | La factura que se devuelve (usa **Ver factura** para revisarla). |
| **Motivo** | Defectuoso, Artículo incorrecto, Exceso, No entregado en despacho u Otro. |
| Fecha de emisión y observaciones | Opcionales. |

!!! captura "CAPTURA PENDIENTE"
    Formulario **Nueva Devolución de Venta** con Cliente, Factura de Venta y Motivo.

**Paso 3. Ítems a Devolver.** Elige:

- **Devolución Total**: se devuelven todos los ítems de la factura.
- **Devolución Parcial**: indica qué ítems y cuántas unidades se devuelven.

**Paso 4.** Revisa el **Total a devolver**. Puedes usar **Ver asientos** para ver cómo queda la contabilidad.

**Paso 5.** **Guardar borrador** si aún no estás seguro, o confirma la devolución. Aparece **Confirmar devolución**: *“Una vez confirmada no podrá editarse.”*

## Resultado esperado

- La devolución queda **Confirmada** en <span class="ruta">Ventas › Devoluciones</span>.
- En la lista de facturas, la factura original muestra **Devolución total** o **Devolución parcial**.
- El inventario de los productos devueltos aumenta.
- Si tu empresa emite documentos automáticamente, se envía la **nota crédito electrónica**. Revisa su estado en <span class="ruta">Fiscal › Documentos</span>. [PENDIENTE DE VALIDACIÓN FUNCIONAL: flujo de emisión manual de la nota crédito.]

## Problemas frecuentes

??? question "No aparece la factura en el buscador"
    Primero selecciona el **Cliente**: el campo muestra *“Selecciona un cliente primero”*. Además, solo aparecen facturas **validadas** de ese cliente.

??? question "La nota crédito electrónica fue rechazada"
    Ver [¿Qué hago si un documento es rechazado?](../facturacion-electronica/documento-rechazado.md). Si el mensaje es *“No hay una resolución activa de nota crédito disponible para esta sucursal.”*, tu empresa debe registrar una [resolución](../facturacion-electronica/resoluciones.md) para notas crédito.

## ¿Necesitas ayuda?

[Contacta a soporte](../soporte.md) con el **código de la devolución**, el **número de la factura** original y el mensaje de error.

## Artículos relacionados

- [¿Cómo hago una factura de venta?](crear-factura-venta.md)
- [¿Qué significa cada estado de un documento electrónico?](../facturacion-electronica/estados-documento.md)
