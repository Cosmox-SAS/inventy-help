---
title: ¿Cómo se aplican las retenciones?
description: Configura Retefuente, ReteIVA y ReteICA en clientes y proveedores, y cómo Inventy las calcula en las facturas.
estado: pendiente-validacion
tipo: rapida
modulo: impuestos
menu: Ventas › Clientes  ·  Compras › Proveedores
permisos:
  - Editar clientes
  - Editar proveedores
revisado: 2026-09-29
search:
  boost: 2
tags:
  - Impuestos
  - Retenciones
---

# ¿Cómo se aplican las retenciones?

<p class="tambien-se-busca">También se busca como: retención en la fuente, retefuente, reteiva, reteica, me retienen, retener a proveedor, autorretenedor, base mínima retención, retención por línea.</p>

**Qué es:** una retención es una parte del pago que **no se entrega** al tercero, sino que se retiene para pagarla a la DIAN o al municipio.

- **En compras:** tú le retienes al **proveedor** (pagas menos).
- **En ventas:** el **cliente** te retiene a ti (te paga menos).

## Pasos

**1. Crea las retenciones**: <span class="ruta">Fiscal › Catálogo de Impuestos › Impuestos y retenciones</span> › **Nuevo Impuesto** › Tipo **Retención**. Ver [guía](crear-impuesto.md).

**2. Configúralas en el tercero** (cliente o proveedor):

1. Abre el cliente (<span class="ruta">Ventas › Clientes</span>) o proveedor (<span class="ruta">Compras › Proveedores</span>) › edítalo.
2. Sección **Retenciones**: elige el impuesto en **Retefuente**, **Reteiva** y/o **Reteica** (y su cuenta contable si usas contabilidad).
3. **Calcular retención en la fuente por**:
    - **Total de factura** → aplica la Retefuente del tercero sobre el total.
    - **Línea** → aplica la retención que trae el **catálogo de impuestos de cada producto**.
4. Guarda.

**3. Factura normal.** Inventy calcula las retenciones solo. En la factura puedes cambiar **Calcular retención en la fuente por** para ese documento.

✅ Listo: las retenciones aparecen en el resumen de la factura y restan del **Total a pagar**.

## Cómo calcula Inventy

| Retención | Base | Cuándo se aplica |
|---|---|---|
| **Retefuente** (Total de factura) | Subtotal de la factura | Si el tercero tiene Retefuente y la base supera la **Base Mínima**. |
| **Retefuente** (Línea) | Subtotal de cada producto, agrupado por retención | Según el catálogo de cada producto, si la suma supera la **Base Mínima**. En compras, solo si el proveedor tiene Retefuente configurada. |
| **ReteIVA** | El **IVA** de la factura (no el subtotal) | Si el tercero tiene Reteiva. |
| **ReteICA** | [PENDIENTE DE VALIDACIÓN FUNCIONAL: base usada] | Si el tercero tiene Reteica. |

## Si algo falla

| Problema | Solución |
|---|---|
| No se aplicó la retención | 1) ¿El tercero la tiene configurada? 2) ¿La base supera la **Base Mínima**? 3) ¿Está bien elegido **Línea / Total de factura**? |
| Al cobrar una factura con retención pide un valor | En el ingreso aparece *Ingresa el valor de abono para la factura con retención antes de finalizar*: escribe cuánto abona el cliente a esa factura. |
| No sé qué porcentaje usar | Eso lo define tu contador según la norma vigente. |

## Relacionados

- [¿Cómo creo un impuesto o una retención?](crear-impuesto.md)
- [¿Qué es y cómo creo un catálogo de impuestos?](catalogo-impuestos.md)
- [¿Cómo registro una factura de compra?](../compras/registrar-factura-compra.md)
