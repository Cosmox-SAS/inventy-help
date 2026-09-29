---
title: ¿Qué hago si un documento electrónico es rechazado?
description: Revisa el error, corrige la causa y reenvía una factura o nota rechazada o sin respuesta.
estado: pendiente-validacion
tipo: tutorial
modulo: facturacion-electronica
menu: Fiscal › Documentos
permisos:
  - Ver documentos electrónicos
  - Reenviar documentos electrónicos
revisado: 2026-09-29
tags:
  - Facturación electrónica
  - DIAN
  - Errores
---

# ¿Qué hago si un documento electrónico es rechazado?

<p class="tambien-se-busca">También se busca como: factura rechazada, rechazo DIAN, no fue aceptada, error DIAN, reenviar factura, falló prevalidación, sin conexión con la DIAN, estado desconocido.</p>

## ¿Para qué sirve?

Un documento **rechazado** o que **falló la prevalidación** no tiene validez ante la DIAN. Esta guía te ayuda a encontrar la causa, corregirla y volver a enviarlo.

## Antes de comenzar

- [ ] Permisos: **Ver documentos electrónicos** y **Reenviar documentos electrónicos**.

## Paso a paso

**Paso 1.** Ingresa a <span class="ruta">Fiscal › Documentos</span> y busca el documento por número o CUFE.

**Paso 2.** Revisa su estado. Ver [qué significa cada estado](estados-documento.md).

**Paso 3.** Abre las acciones del documento y haz clic en **Ver error**. Lee el mensaje con calma: normalmente dice qué dato está mal.

!!! captura "CAPTURA PENDIENTE"
    Ventana **Ver error** de un documento Rechazado por DIAN.

**Paso 4.** Corrige la causa. Las más comunes:

| Si el error habla de… | Corrige en… |
|---|---|
| Identificación, nombre, correo o dirección del **cliente** | La ficha del cliente en <span class="ruta">Ventas › Clientes</span>. |
| **Resolución**, prefijo, rango o clave técnica | <span class="ruta">Fiscal › Resoluciones</span>. |
| **Impuestos** o tarifas | <span class="ruta">Fiscal › Impuestos › Catálogo de Impuestos</span> (con tu contador). |
| Datos de **tu empresa** (NIT, razón social) | <span class="ruta">Configuración › Empresa</span> (consulta antes con soporte). |
| Conexión, tiempo de espera, servicio no disponible | Nada que corregir: solo reenvía más tarde. |

**Paso 5.** Vuelve a <span class="ruta">Fiscal › Documentos</span> y usa **Reenviar documento electrónico**. Lee el aviso: *“Se reenviará el mismo consecutivo a la DIAN con los datos actuales de la factura.”* Confirma.

## Resultado esperado

Verás *“Documento … reenviado exitosamente. Estado: …”*. Si el estado es **Aceptado**, terminaste.

## Qué hacer cuando hay un problema de conexión

Si el documento quedó **Pendiente** o **Desconocido** por un problema de conexión con la DIAN o con el proveedor:

1. **No vuelvas a crear la factura.** El documento ya tiene su consecutivo.
2. Espera unos minutos y usa **Reenviar documento electrónico**.
3. Si después de varios intentos sigue igual, [contacta a soporte](../soporte.md).

## Problemas frecuentes

??? question "“Solo se pueden reenviar documentos con estado pendiente, desconocido, rechazado o fallido.”"
    El documento ya fue **Aceptado** (o aceptado con observaciones). No necesita reenviarse.

??? question "Corregí el cliente pero sigue saliendo el mismo error"
    Verifica que corregiste el dato exacto que indica el error y que guardaste los cambios. Si persiste, [contacta a soporte](../soporte.md): puede que ese dato se tome de la factura original y no de la ficha del cliente. [PENDIENTE DE VALIDACIÓN FUNCIONAL: qué datos se actualizan al reenviar.]

??? question "“Aceptado con observaciones”: ¿debo hacer algo?"
    El documento **es válido**. Revisa **Ver observaciones** para evitar el mismo comentario en futuros documentos.

## ¿Necesitas ayuda?

[Contacta a soporte](../soporte.md) si el error no es claro o persiste después de corregir. Envía:

- **Número del documento** y **CUFE** (si lo tiene).
- **Captura completa** de **Ver error**.
- Qué corregiste antes de reenviar.

## Artículos relacionados

- [¿Qué significa cada estado?](estados-documento.md)
- [¿Cómo registro una resolución de la DIAN?](resoluciones.md)
- [Soluciones rápidas: facturación electrónica](../soluciones-rapidas/facturacion-electronica.md)
