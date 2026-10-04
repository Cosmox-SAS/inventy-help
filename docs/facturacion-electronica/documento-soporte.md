---
title: "¿Cómo emito un documento soporte electrónico?"
description: "Pasos para generar el documento soporte de una compra a un proveedor no obligado a facturar."
estado: pendiente-validacion
tipo: rapida
modulo: facturacion-electronica
menu: "Compras › Facturas"
permisos:
  - Crear facturas de compra
revisado: 2026-10-01
search:
  boost: 3
tags:
  - Facturación electrónica
  - Documento soporte
  - Compras
---

# ¿Cómo emito un documento soporte electrónico?

<p class="tambien-se-busca">También se busca como: documento soporte, generar documento soporte, emitir documento soporte, DS, compra a persona natural, proveedor no obligado a facturar.</p>

**Antes de empezar:** debe existir una resolución activa de **Documento soporte electrónico**.

## Pasos

**Paso 1.** En <span class="ruta">Compras › Proveedores</span>, crea (o edita) el proveedor y marca **No obligado a facturar**. Guarda con **Crear proveedor** (o **Guardar**). Solo se hace una vez.

![Paso 1: casilla No obligado a facturar](../assets/capturas/facturacion-electronica/documento-soporte/paso-1.webp)

**Paso 2.** Ve a <span class="ruta">Compras › Facturas</span> › **Nueva Factura** y elige el proveedor. La casilla **Requiere documento soporte electrónico** se marca sola. En **N° Factura Proveedor** escribe el número de su cuenta de cobro.

![Paso 2: casilla Requiere documento soporte electrónico](../assets/capturas/facturacion-electronica/documento-soporte/paso-2.webp)

**Paso 3.** Agrega los productos o servicios, haz clic en **Registrar Factura** y confirma con **Validar factura**.

![Paso 3: botón Registrar Factura](../assets/capturas/facturacion-electronica/documento-soporte/paso-3.webp)

**Paso 4.** Si no se envió solo, abre la factura y haz clic en **Emitir documento soporte**. Confirma.

![Paso 4: botón Emitir documento soporte](../assets/capturas/facturacion-electronica/documento-soporte/paso-4.webp)

✅ **Listo:** el documento aparece en <span class="ruta">Fiscal › Documentos</span>. Si está **Aceptado**, terminaste.

## Si algo falla

| Problema | Solución |
|---|---|
| No aparece **Emitir documento soporte** | Tu empresa debe tener la facturación electrónica habilitada. Además, la factura debe estar validada, marcada como *Requiere documento soporte*, sin documento previo y sin devoluciones. |
| *La factura no requiere documento soporte electrónico: el proveedor está obligado a facturar.* | Marca al proveedor como **No obligado a facturar** si corresponde. |
| *La factura ya tiene un documento soporte electrónico activo.* | Ya se emitió: búscalo en **Fiscal › Documentos**. |
| *No hay una resolución activa disponible para este tipo de documento.* | [Registra la resolución](resoluciones.md) de documento soporte. |

## Relacionados

- [¿Cómo registro una factura de compra?](../compras/registrar-factura-compra.md)
