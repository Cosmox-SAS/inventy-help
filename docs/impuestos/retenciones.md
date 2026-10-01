---
title: "¿Cómo se aplican las retenciones?"
description: "Pasos para configurar Retefuente, ReteIVA y ReteICA en clientes y proveedores."
estado: pendiente-validacion
tipo: rapida
modulo: impuestos
menu: "Ventas › Clientes · Compras › Proveedores"
permisos:
  - Editar clientes
  - Editar proveedores
revisado: 2026-10-01
search:
  boost: 2
tags:
  - Impuestos
  - Retenciones
---

# ¿Cómo se aplican las retenciones?

<p class="tambien-se-busca">También se busca como: retención en la fuente, retefuente, reteiva, reteica, me retienen, retener a proveedor, autorretenedor, base mínima retención, retención por línea.</p>

**Qué es:** parte del pago que no se entrega al tercero, sino que se retiene para pagarla a la DIAN o al municipio. En compras tú retienes al proveedor; en ventas el cliente te retiene a ti.

**Antes de empezar:** crea las retenciones como impuestos de tipo **Retención** ([guía](crear-impuesto.md)).

## Pasos

**Paso 1.** Abre el proveedor (<span class="ruta">Compras › Proveedores</span>) o el cliente (<span class="ruta">Ventas › Clientes</span>) y haz clic en **Editar**.

![Paso 1: botón Editar del tercero](../assets/capturas/impuestos/retenciones/paso-1.png)

**Paso 2.** En **Retenciones**, elige el impuesto de **Retefuente**, **Reteiva** y/o **Reteica**, cada uno con su **Cuenta contable** (ej. *236540001 Retención en la fuente por compras*). Haz clic en **Actualizar proveedor** (o **Actualizar cliente**).

![Paso 2: sección Retenciones](../assets/capturas/impuestos/retenciones/paso-2.png)

**Paso 3.** Al hacer una factura de ese tercero, las retenciones aparecen debajo de su nombre. En **Calcular retención en la fuente por**, deja **Total de factura** (usa la Retefuente del tercero) o elige **Línea** (usa la del catálogo de cada producto).

![Paso 3: retenciones del tercero en la factura](../assets/capturas/impuestos/retenciones/paso-3.png)

**Paso 4.** Agrega los productos. El resumen muestra cada retención restada y el **Total** ya neto.

![Paso 4: retenciones en el resumen de la factura](../assets/capturas/impuestos/retenciones/paso-4.png)

✅ **Listo:** Inventy calcula las retenciones solo en cada factura de ese tercero.

## Si algo falla

| Problema | Solución |
|---|---|
| No se aplicó la retención | ¿El tercero la tiene configurada? ¿La base supera la **Base Mínima**? ¿Está bien elegido **Línea / Total de factura**? |
| Al cobrar una factura con retención pide un valor | Escribe cuánto abona el cliente a esa factura. |
| No sé qué porcentaje usar | Lo define tu contador según la norma vigente. |

## Relacionados

- [¿Cómo creo un impuesto o una retención?](crear-impuesto.md)
- [¿Qué es y cómo creo un catálogo de impuestos?](catalogo-impuestos.md)
