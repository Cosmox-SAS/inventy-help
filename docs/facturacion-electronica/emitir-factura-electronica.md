---
title: ¿Cómo emito una factura electrónica?
description: Envía una factura de venta a la DIAN de forma automática, desde el POS o manualmente.
estado: pendiente-validacion
tipo: tutorial
modulo: facturacion-electronica
menu: Ventas › Facturas  ·  Ventas › POS
permisos:
  - Ver facturas de venta
  - Crear facturas de venta
revisado: 2026-09-29
tags:
  - Facturación electrónica
  - DIAN
---

# ¿Cómo emito una factura electrónica?

<p class="tambien-se-busca">También se busca como: facturar electrónicamente, enviar a la DIAN, emitir factura, factura DIAN, generar CUFE.</p>

## ¿Para qué sirve?

Para enviar tu factura de venta a la DIAN y que tenga validez como factura electrónica. El cliente la recibe en su correo.

## Antes de comenzar

- [ ] Tu empresa debe estar **habilitada** para facturación electrónica. Ver [Facturación electrónica](index.md).
- [ ] Debe existir una **resolución activa** para factura electrónica en tu sede. Ver [resoluciones](resoluciones.md).
- [ ] El cliente debe tener **datos completos** (tipo y número de documento, nombre o razón social, correo) y **no** tener marcado *No genera documentos electrónicos*.

## Paso a paso

Hay tres formas de emitir. Usa la que corresponda a tu forma de trabajo.

### 1. Automáticamente (recomendado)

Si el administrador activó **Emitir documento electrónico automáticamente** en <span class="ruta">Configuración › Módulos › Fiscal</span>, cada factura se envía a la DIAN **en el momento en que la validas**. No tienes que hacer nada más.

### 2. Desde el POS

En la ventana **Cobrar venta**, deja marcada la casilla **Generar factura electrónica** antes de **Confirmar cobro**. Si el cliente no genera documentos electrónicos, verás *“Este cliente no genera documentos electrónicos”*.

### 3. Manualmente desde la factura

**Paso 1.** Ingresa a <span class="ruta">Ventas › Facturas</span> y abre la factura **validada**.

**Paso 2.** Haz clic en **Emitir electrónica**.

**Paso 3.** En **¿Emitir factura electrónica?**, selecciona el **Tipo de documento electrónico**.

!!! warning "Esta acción consume un consecutivo"
    *“Se enviará la factura a la DIAN. Esta acción consume un consecutivo de la resolución.”* Revisa la factura antes de emitir.

!!! captura "CAPTURA PENDIENTE"
    Ventana **¿Emitir factura electrónica?** con el selector de tipo de documento.

**Paso 4.** Confirma.

## Resultado esperado

- En el detalle de la factura, el campo **Documento electrónico** muestra el número y el estado.
- En <span class="ruta">Fiscal › Documentos</span> el documento aparece como **Aceptado** (o en otro estado; ver [qué significa cada estado](estados-documento.md)).
- El cliente recibe la factura en su correo. Si necesitas enviarla de nuevo o a otro correo, usa **Enviar email**.

## Problemas frecuentes

??? question "“No hay una resolución activa disponible para este tipo de documento.”"
    No hay una resolución **activa** y **vigente** para ese tipo de documento en tu sede. Revisa <span class="ruta">Fiscal › Resoluciones</span>.

??? question "“La resolución no tiene consecutivos disponibles.”"
    Se agotó el rango de numeración (estado **Agotada**). Solicita una nueva resolución a la DIAN y [regístrala](resoluciones.md).

??? question "“La resolución de facturación no tiene configurada la clave técnica asignada por la DIAN.”"
    Edita la resolución y escribe la **Clave técnica**. Si no la tienes, [contacta a soporte](../soporte.md).

??? question "No aparece el botón Emitir electrónica"
    La factura debe estar **validada**, y puede que ya se haya emitido automáticamente. Revisa el campo **Documento electrónico** del detalle.

## ¿Necesitas ayuda?

[Contacta a soporte](../soporte.md) con el **número de la factura** y una **captura** del estado o del error.

## Artículos relacionados

- [¿Qué significa cada estado?](estados-documento.md)
- [¿Qué hago si un documento es rechazado?](documento-rechazado.md)
- [¿Cómo hago una factura de venta?](../ventas/crear-factura-venta.md)
