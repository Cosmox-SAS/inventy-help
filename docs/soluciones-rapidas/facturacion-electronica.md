---
title: "Soluciones rápidas: facturación electrónica"
description: Factura rechazada, sin resolución, sin consecutivos, sin respuesta de la DIAN.
estado: pendiente-validacion
tipo: solucion
modulo: facturacion-electronica
revisado: 2026-09-29
tags:
  - Facturación electrónica
  - Soluciones rápidas
---

# Soluciones rápidas: facturación electrónica

## "Mi factura fue rechazada"

**PROBLEMA:** el documento aparece como **Rechazado por DIAN**, **Rechazado por proveedor** o **Falló prevalidación**.

**CAUSA:** algún dato del documento no cumple las validaciones (cliente, impuestos, resolución o datos de la empresa).

**SOLUCIÓN:** sigue la guía [¿Qué hago si un documento es rechazado?](../facturacion-electronica/documento-rechazado.md): **Ver error** → corregir → **Reenviar documento electrónico**.

**ESCALAR A SOPORTE:** si el error no es claro o persiste después de corregir.

**INFORMACIÓN PARA SOPORTE:** número del documento, CUFE si lo tiene, captura de **Ver error**.

## "Dice que no hay resolución activa"

**PROBLEMA:** aparece *“No hay una resolución activa disponible para este tipo de documento.”* (o su versión para nota crédito o documento soporte).

**CAUSA:** no hay una resolución **Activa** y vigente para ese tipo de documento en tu sede.

**SOLUCIÓN:**

1. Ve a <span class="ruta">Fiscal › Resoluciones</span>.
2. Revisa que exista una resolución de ese tipo, en estado **Activa**, que incluya tu sede y que no esté vencida.
3. Si no existe, [regístrala](../facturacion-electronica/resoluciones.md).

**ESCALAR A SOPORTE:** si la resolución existe y está activa, pero el mensaje sigue apareciendo.

**INFORMACIÓN PARA SOPORTE:** tipo de documento, sede, captura de la lista de resoluciones.

## "Se acabaron los consecutivos"

**PROBLEMA:** aparece *“La resolución no tiene consecutivos disponibles.”*

**CAUSA:** se usaron todos los números del rango (resolución **Agotada**).

**SOLUCIÓN:** solicita una nueva numeración a la DIAN y [regístrala](../facturacion-electronica/resoluciones.md) en Inventy.

**ESCALAR A SOPORTE:** si ya registraste la nueva resolución y sigue el mensaje.

**INFORMACIÓN PARA SOPORTE:** prefijo y número de la resolución nueva.

## "Falta la clave técnica"

**PROBLEMA:** aparece *“La resolución de facturación no tiene configurada la clave técnica asignada por la DIAN.”*

**CAUSA:** la resolución se registró sin **Clave técnica**.

**SOLUCIÓN:** registra la clave técnica. Como los datos principales de una resolución no se pueden cambiar después de creada, si no puedes editarla [contacta a soporte](../soporte.md).

**ESCALAR A SOPORTE:** siempre que no tengas la clave técnica.

**INFORMACIÓN PARA SOPORTE:** prefijo y número de la resolución.

## "La factura se quedó pendiente / no hay conexión con la DIAN"

**PROBLEMA:** el documento está **Pendiente** o **Desconocido** desde hace rato.

**CAUSA:** problema temporal de conexión con la DIAN o con el proveedor tecnológico.

**SOLUCIÓN:**

1. **No crees la factura de nuevo.**
2. Espera unos minutos y usa **Reenviar documento electrónico** en <span class="ruta">Fiscal › Documentos</span>.

**ESCALAR A SOPORTE:** si sigue igual después de varios intentos durante más de una hora.

**INFORMACIÓN PARA SOPORTE:** número del documento, hora de emisión, estado actual.

## "El cliente no recibió la factura"

**PROBLEMA:** el documento fue **Aceptado** pero el cliente no lo tiene.

**CAUSA:** correo del cliente incorrecto, correo en Spam, o el cliente no tiene activado **¿Recibir documentos electrónicos al correo?**

**SOLUCIÓN:** en <span class="ruta">Fiscal › Documentos</span>, usa **Enviar email** y escribe el correo correcto (varios, separados por `;`). Corrige también la ficha del cliente.

**ESCALAR A SOPORTE:** si el envío falla.

**INFORMACIÓN PARA SOPORTE:** número del documento, correo destino.
