---
title: "¿Cómo emito una factura electrónica?"
description: "Pasos para enviar una factura de venta a la DIAN."
estado: pendiente-validacion
tipo: rapida
modulo: facturacion-electronica
menu: "Ventas › Facturas"
permisos:
  - Ver facturas de venta
  - Crear facturas de venta
revisado: 2026-09-30
search:
  boost: 2
tags:
  - Facturación electrónica
  - DIAN
---

# ¿Cómo emito una factura electrónica?

<p class="tambien-se-busca">También se busca como: facturar electrónicamente, enviar a la DIAN, emitir factura, factura DIAN, generar CUFE.</p>

**Antes de empezar:** tu empresa debe estar habilitada y tener una [resolución activa](resoluciones.md).

## Pasos

**Paso 1.** Ingresa a <span class="ruta">Ventas › Facturas</span> y abre la factura **Validada**.

![Paso 1: lista de facturas](../assets/capturas/facturacion-electronica/emitir-factura-electronica/paso-1.png)

**Paso 2.** Haz clic en **Emitir electrónica**.

![Paso 2: botón Emitir electrónica](../assets/capturas/facturacion-electronica/emitir-factura-electronica/paso-2.png)

**Paso 3.** En **¿Emitir factura electrónica?**, elige el **Tipo de documento electrónico** y confirma.

![Paso 3: ventana Emitir factura electrónica](../assets/capturas/facturacion-electronica/emitir-factura-electronica/paso-3.png)

**Paso 4.** Revisa el estado en <span class="ruta">Fiscal › Documentos</span>.

![Paso 4: lista de documentos electrónicos](../assets/capturas/facturacion-electronica/emitir-factura-electronica/paso-4.png)

✅ **Listo:** el documento queda **Aceptado** y el cliente lo recibe en su correo.

!!! info "Otras formas de emitir"
    - **Automática:** activa **Emitir documento electrónico automáticamente** en <span class="ruta">Configuración › Módulos › Fiscal</span> y cada factura se envía al validarla.
    - **Desde el POS:** deja marcada **Generar factura electrónica** al cobrar.

## Si algo falla

| Problema | Solución |
|---|---|
| *No hay una resolución activa disponible para este tipo de documento.* | Revisa <span class="ruta">Fiscal › Resoluciones</span>. |
| *La resolución no tiene consecutivos disponibles.* | Registra una resolución nueva. |
| No aparece **Emitir electrónica** | Quizá ya se emitió sola (emisión automática). Mira el campo **Documento electrónico**. |
| Quedó rechazado | Ver [documento rechazado](documento-rechazado.md). |

## Relacionados

- [¿Qué significa cada estado?](estados-documento.md)
- [¿Qué hago si un documento es rechazado?](documento-rechazado.md)
