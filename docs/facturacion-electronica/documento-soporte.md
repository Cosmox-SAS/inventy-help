---
title: ¿Cómo emito un documento soporte electrónico?
description: Genera el documento soporte electrónico de una compra a un proveedor no obligado a facturar.
estado: pendiente-validacion
tipo: tutorial
modulo: facturacion-electronica
menu: Compras › Operación › Facturas
permisos:
  - Crear facturas de compra
revisado: 2026-09-29
search:
  boost: 3
tags:
  - Facturación electrónica
  - Documento soporte
  - Compras
---

# ¿Cómo emito un documento soporte electrónico?

<p class="tambien-se-busca">También se busca como: documento soporte, generar documento soporte, emitir documento soporte, DS, documento soporte DIAN, compra a persona natural, proveedor no obligado a facturar, proveedor sin factura electrónica.</p>

## ¿Para qué sirve?

Cuando le compras a un proveedor que **no está obligado a expedir factura** (por ejemplo, algunas personas naturales), tu empresa genera el **documento soporte electrónico** y lo envía a la DIAN para soportar esa compra.

En Inventy **no se crea por separado**: se genera **a partir de la factura de compra** de ese proveedor.

## Antes de comenzar

- [ ] Tu empresa debe estar **habilitada** para documentos electrónicos. Ver [Facturación electrónica](index.md).
- [ ] Debe existir una **resolución activa** de tipo **Documento soporte electrónico** para tu sede. Ver [¿Cómo registro una resolución?](resoluciones.md).
- [ ] El proveedor debe tener marcada la casilla **No obligado a facturar** (*“Sus facturas de compra generan documento soporte electrónico.”*) en <span class="ruta">Compras › Proveedores</span>.
- [ ] Permiso: **Crear facturas de compra** (y gestionar facturas de compra para emitir manualmente).

## Paso a paso

**Paso 1. Marca al proveedor.** En <span class="ruta">Compras › Proveedores</span>, edita el proveedor y activa **No obligado a facturar**. Solo tienes que hacerlo una vez.

**Paso 2. Registra la compra.** Crea la [factura de compra](../compras/registrar-factura-compra.md) de ese proveedor. La casilla **Requiere documento soporte electrónico** se marca **automáticamente** (*“Se marca automáticamente si el proveedor no está obligado a facturar.”*).

!!! captura "CAPTURA PENDIENTE"
    Formulario de factura de compra con la casilla **Requiere documento soporte electrónico** marcada.

**Paso 3. Valida la factura** con **Registrar Factura** y confirma.

**Paso 4. Emite el documento soporte.**

- **Si tu empresa tiene la emisión automática activa** (<span class="ruta">Configuración › Módulos › Fiscal › Emitir documento electrónico automáticamente</span>), el documento soporte se envía solo al validar. No tienes que hacer nada más.
- **Si no**, abre la factura de compra y haz clic en **Emitir documento soporte**. En **¿Emitir documento soporte?** lee el aviso *“Se enviará el documento soporte a la DIAN. Esta acción consume un consecutivo de la resolución.”* y confirma.

!!! captura "CAPTURA PENDIENTE"
    Detalle de la factura de compra con el botón **Emitir documento soporte** resaltado.

## Resultado esperado

- En el detalle de la factura de compra, el campo **Documento soporte electrónico** muestra el número y el estado.
- El documento aparece en <span class="ruta">Fiscal › Documentos</span>. Si está **Aceptado**, terminaste. Ver [qué significa cada estado](estados-documento.md).

## ¿Y si le devuelvo mercancía al proveedor?

La devolución de compra sobre una factura con documento soporte genera una **Nota de ajuste al documento soporte**. Para eso necesitas:

- Que el documento soporte original esté **aceptado por la DIAN**.
- Una resolución activa de **nota de ajuste al documento soporte** en la sede.

[PENDIENTE DE VALIDACIÓN FUNCIONAL: pasos para emitir la nota de ajuste desde la devolución de compra.]

## Problemas frecuentes

??? question "No aparece el botón Emitir documento soporte"
    El botón solo aparece si se cumplen **todas** estas condiciones:

    - La factura está **validada** o **pagada** (no en borrador).
    - La factura tiene marcada **Requiere documento soporte** (el proveedor es *No obligado a facturar*).
    - La factura **no tiene ya** un documento soporte (quizá se emitió automáticamente: revisa el campo **Documento soporte electrónico**).
    - La factura no tiene **devoluciones confirmadas** y no fue importada.
    - Tu rol tiene permiso para gestionar facturas de compra.

??? question "“La factura no requiere documento soporte electrónico: el proveedor está obligado a facturar.”"
    El proveedor no está marcado como **No obligado a facturar**. Si realmente no está obligado, corrige la ficha del proveedor. Si está obligado, él debe enviarte su factura electrónica: no se genera documento soporte.

??? question "“La factura debe estar validada o pagada para emitir el documento soporte electrónico.”"
    Valida primero la factura de compra.

??? question "“La factura ya tiene un documento soporte electrónico activo.”"
    Ya se emitió. Búscalo en <span class="ruta">Fiscal › Documentos</span>. Si fue rechazado, usa **Reenviar documento electrónico** (ver [documento rechazado](documento-rechazado.md)).

??? question "“No hay una resolución activa disponible para este tipo de documento.”"
    Registra la [resolución](resoluciones.md) de **Documento soporte electrónico** para tu sede.

??? question "Marqué el proveedor después de registrar la factura"
    La casilla de la factura se toma del proveedor **al crearla**. Si la factura aún está en **borrador**, edítala y marca **Requiere documento soporte electrónico**. [PENDIENTE DE VALIDACIÓN FUNCIONAL: si puede corregirse en una factura ya validada.]

## ¿Necesitas ayuda?

[Contacta a soporte](../soporte.md) si el documento soporte es rechazado y no entiendes el error. Envía el **código de la factura de compra**, el **nombre del proveedor** y una captura de **Ver error**.

## Artículos relacionados

- [¿Cómo registro una factura de compra?](../compras/registrar-factura-compra.md)
- [¿Qué significa cada estado?](estados-documento.md)
- [¿Qué hago si un documento es rechazado?](documento-rechazado.md)
- [¿Cómo registro una resolución de la DIAN?](resoluciones.md)
