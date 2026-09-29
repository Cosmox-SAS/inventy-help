---
title: ¿Cómo registro una resolución de la DIAN?
description: Registra la resolución de numeración autorizada por la DIAN para tus documentos electrónicos.
estado: pendiente-validacion
tipo: tutorial
modulo: facturacion-electronica
menu: Fiscal › Doc Electrónicos › Resoluciones
permisos:
  - Ver resoluciones de documentos electrónicos
  - Crear resoluciones de documentos electrónicos
revisado: 2026-09-29
tags:
  - Facturación electrónica
  - Resolución
---

# ¿Cómo registro una resolución de la DIAN?

<p class="tambien-se-busca">También se busca como: resolución de facturación, numeración, prefijo, rango de facturas, consecutivo, clave técnica, renovar resolución.</p>

## ¿Para qué sirve?

La **resolución** es la autorización de la DIAN que define el **prefijo** y el **rango de números** que puedes usar en tus documentos electrónicos. Sin una resolución activa y vigente, Inventy no puede emitir.

**Úsala cuando:** empiezas a facturar electrónicamente, se agota el rango o se vence la resolución.

## Antes de comenzar

- [ ] Ten a mano la resolución de la DIAN: **número**, **prefijo**, **rango desde / hasta**, **fechas de vigencia** y **clave técnica**.
- [ ] Permiso: **Crear resoluciones de documentos electrónicos**.

## Paso a paso

**Paso 1.** Ingresa a <span class="ruta">Fiscal › Resoluciones</span> y crea una **Nueva resolución**.

**Paso 2. Datos de la resolución.**

| Campo | Qué escribir |
|---|---|
| **Tipo de documento** | Factura electrónica de venta, nota crédito, documento soporte, etc. |
| **Prefijo** | El prefijo autorizado (ej. `FV`). |
| **Número de resolución** | Solo dígitos (ej. `18760000001`). |

**Paso 3. Rango de numeración.**

| Campo | Qué escribir |
|---|---|
| **Rango desde** / **Rango hasta** | El rango autorizado (ej. 1 a 5000000). |
| Próximo consecutivo (opcional) | Si ya usaste números de este rango en otro sistema, escribe el siguiente disponible. Si lo dejas vacío, empieza en el *Rango desde*. |
| **Fecha de inicio** / **Fecha de vencimiento** | Vigencia de la resolución. |

**Paso 4. Alcance y estado.** Elige las **sedes** donde aplica (o **Todas las sedes**), el **Estado** y escribe la **Clave técnica**.

!!! captura "CAPTURA PENDIENTE"
    Formulario **Nueva resolución** completo.

**Paso 5.** Haz clic en **Crear resolución**.

!!! danger "Revisa todo antes de crear"
    Después de crear la resolución **no se pueden modificar** el tipo de documento, el prefijo, el número, el rango, el próximo consecutivo, las fechas ni la clave técnica. Si te equivocas, deberás registrar una nueva.

## Resultado esperado

La resolución aparece en la lista con su estado:

| Estado | Significa |
|---|---|
| **Activa** | Se está usando para emitir. |
| **Inactiva** | Registrada, pero no se usa. |
| **Agotada** | Ya se usaron todos los números del rango. |
| **Vencida** | Pasó la fecha de vencimiento. |

## Problemas frecuentes

??? question "“El número de resolución solo puede contener dígitos.”"
    Escribe el número sin letras, guiones ni espacios.

??? question "“… no puede modificarse después de crear la resolución.”"
    Esos datos son fijos. Registra una nueva resolución con los datos correctos y deja la anterior **Inactiva**.

??? question "“No hay una resolución activa de nota crédito disponible para esta sucursal.”"
    Cada tipo de documento necesita su propia resolución (o configuración). Registra una para **Nota crédito electrónica** en esa sede.

## ¿Necesitas ayuda?

[Contacta a soporte](../soporte.md) si no sabes qué número o prefijo registrar. Envía una **copia de la resolución** de la DIAN (sin contraseñas ni certificados).

## Artículos relacionados

- [¿Cómo emito una factura electrónica?](emitir-factura-electronica.md)
- [Facturación electrónica](index.md)
