---
title: "¿Qué hago si un documento electrónico es rechazado?"
description: "Pasos para ver el error, corregirlo y reenviar el documento."
estado: pendiente-validacion
tipo: rapida
modulo: facturacion-electronica
menu: "Fiscal › Documentos"
permisos:
  - Ver documentos electrónicos
  - Reenviar documentos electrónicos
revisado: 2026-09-30
tags:
  - Facturación electrónica
  - DIAN
  - Errores
---

# ¿Qué hago si un documento electrónico es rechazado?

<p class="tambien-se-busca">También se busca como: factura rechazada, rechazo DIAN, no fue aceptada, error DIAN, reenviar factura, falló prevalidación, sin conexión con la DIAN, estado desconocido.</p>

## Pasos

**Paso 1.** Ingresa a <span class="ruta">Fiscal › Documentos</span> y busca el documento por número o CUFE.

![Paso 1: lista de documentos](../assets/capturas/facturacion-electronica/documento-rechazado/paso-1.png)

**Paso 2.** Abre las acciones del documento y haz clic en **Ver error**.

![Paso 2: acción Ver error](../assets/capturas/facturacion-electronica/documento-rechazado/paso-2.png)

**Paso 3.** Corrige la causa: datos del cliente (<span class="ruta">Ventas › Clientes</span>), resolución (<span class="ruta">Fiscal › Resoluciones</span>) o impuestos (<span class="ruta">Fiscal › Catálogo de Impuestos</span>).

![Paso 3: ventana con el error](../assets/capturas/facturacion-electronica/documento-rechazado/paso-3.png)

**Paso 4.** Vuelve al documento y haz clic en **Reenviar documento electrónico**. Confirma.

![Paso 4: acción Reenviar documento electrónico](../assets/capturas/facturacion-electronica/documento-rechazado/paso-4.png)

✅ **Listo:** aparece *“Documento … reenviado exitosamente. Estado: …”*. Si dice **Aceptado**, terminaste.

## Si algo falla

| Problema | Solución |
|---|---|
| Quedó **Pendiente** o **Desconocido** (sin conexión) | **No crees la factura de nuevo.** Espera unos minutos y reenvía. |
| *Solo se pueden reenviar documentos con estado pendiente, desconocido, rechazado o fallido.* | Ya fue aceptado: no necesita reenvío. |
| **Aceptado con observaciones** | Es válido. Revisa **Ver observaciones** para próximas facturas. |
| El error persiste | [Contacta a soporte](../soporte.md) con número, CUFE y captura de **Ver error**. |

## Relacionados

- [¿Qué significa cada estado?](estados-documento.md)
- [¿Cómo registro una resolución de la DIAN?](resoluciones.md)
