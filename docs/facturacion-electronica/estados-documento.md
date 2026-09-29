---
title: ¿Qué significa cada estado de un documento electrónico?
description: Interpreta los estados Pendiente, Aceptado, Rechazado por DIAN, Falló prevalidación y demás.
estado: pendiente-validacion
tipo: concepto
modulo: facturacion-electronica
menu: Fiscal › Documentos
permisos:
  - Ver documentos electrónicos
revisado: 2026-09-29
tags:
  - Facturación electrónica
  - DIAN
---

# ¿Qué significa cada estado de un documento electrónico?

<p class="tambien-se-busca">También se busca como: estado DIAN, factura aceptada, factura rechazada, pendiente, CUFE, validación DIAN, respuesta DIAN.</p>

Consulta el estado de cualquier documento en <span class="ruta">Fiscal › Documentos</span>. Puedes buscarlo por **número** o por **CUFE**.

!!! captura "CAPTURA PENDIENTE"
    Lista **Documentos electrónicos** con varios estados de ejemplo y el menú de acciones abierto.

## Los estados

| Estado | ¿Qué significa? | ¿Qué debo hacer? |
|---|---|---|
| :material-check-circle:{ style="color:#10b981" } **Aceptado** | La DIAN aprobó el documento. Es válido. | Nada. Puedes enviarlo al cliente con **Enviar email**. |
| :material-check-circle-outline:{ style="color:#10b981" } **Aceptado con observaciones** | La DIAN lo aprobó, pero dejó comentarios. El documento **es válido**. | Revisa **Ver observaciones** y corrige para próximos documentos (por ejemplo, datos del cliente). |
| :material-clock-outline:{ style="color:#f59e0b" } **Pendiente** | Se está enviando o esperando respuesta. | Espera unos minutos y recarga. Si sigue igual por mucho tiempo, usa **Reenviar**. |
| :material-help-circle-outline:{ style="color:#f59e0b" } **Desconocido** | No se recibió una respuesta clara (por ejemplo, por un problema de conexión). | Usa **Reenviar documento electrónico**. |
| :material-alert-circle:{ style="color:#ef4444" } **Falló prevalidación** | Inventy detectó un problema **antes** de enviarlo (faltan datos). **No llegó a la DIAN.** | Usa **Ver error**, corrige el dato y reenvía. |
| :material-close-circle:{ style="color:#ef4444" } **Rechazado por proveedor** | El proveedor tecnológico lo rechazó antes de pasarlo a la DIAN. | Usa **Ver error**. Ver [documento rechazado](documento-rechazado.md). |
| :material-close-circle:{ style="color:#ef4444" } **Rechazado por DIAN** | La DIAN lo rechazó. **No es válido.** | Usa **Ver error**. Ver [documento rechazado](documento-rechazado.md). |

## Acciones disponibles

| Acción | Para qué sirve |
|---|---|
| **Ver observaciones** | Muestra los comentarios de la DIAN en documentos aceptados con observaciones. |
| **Ver error** | Muestra el motivo del rechazo o del fallo. |
| **Ver en DIAN** | Abre el documento en el portal de la DIAN. |
| **Enviar email** | Envía el documento a uno o varios correos (sepáralos con punto y coma `;`). |
| **Reenviar documento electrónico** | Vuelve a enviar el **mismo consecutivo** con los datos actuales. Solo para documentos Pendientes, Desconocidos, Rechazados o que Fallaron la prevalidación. Requiere el permiso **Reenviar documentos electrónicos**. |

## CUFE y CUDE

- **CUFE:** código único de una **factura electrónica**.
- **CUDE:** código único de otros documentos (nota crédito, documento equivalente POS).

Con ellos, tú o tu cliente pueden verificar el documento en la DIAN.

## Artículos relacionados

- [¿Qué hago si un documento es rechazado?](documento-rechazado.md)
- [¿Cómo emito una factura electrónica?](emitir-factura-electronica.md)
