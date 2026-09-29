---
title: ¿Qué es y cómo creo un catálogo de impuestos?
description: Qué es el catálogo de impuestos y pasos para crearlo y asignarlo a los productos.
estado: pendiente-validacion
tipo: rapida
modulo: impuestos
menu: Fiscal › Impuestos › Catálogo de Impuestos
permisos:
  - Ver catálogo de impuestos
  - Crear catálogo de impuestos
revisado: 2026-09-29
search:
  boost: 2
tags:
  - Impuestos
  - Catálogo de impuestos
---

# ¿Qué es y cómo creo un catálogo de impuestos?

<p class="tambien-se-busca">También se busca como: catálogo de impuestos, grupo de impuestos, impuestos del producto, configurar IVA del producto, régimen, cuentas de impuestos.</p>

**Qué es:** un **paquete de impuestos** que se le asigna a un producto. Dice qué impuestos (y retenciones) se cobran **al venderlo** y cuáles se pagan **al comprarlo**, y en qué cuentas contables se registran.

Ejemplo: catálogo *“Gravado 19 %”* → Venta: IVA 19 % · Compra: IVA 19 %. Todos los productos con IVA 19 % usan ese mismo catálogo.

## Pasos

**Antes:** crea los impuestos y retenciones que vas a usar. Ver [¿Cómo creo un impuesto?](crear-impuesto.md).

1. <span class="ruta">Fiscal › Catálogo de Impuestos</span> › **Nuevo Catálogo**.
2. **Nombre del Catálogo**: ej. *Gravado 19 %*, *Excluido*, *INC 8 %*.
3. **Impuestos de Ventas** › **Agregar Impuesto** › busca y agrega cada impuesto que cobras al vender.
4. **Impuestos de Compras** › **Agregar Impuesto** › agrega cada impuesto que pagas al comprar.
5. Si usas contabilidad, elige las cuentas: **Cuenta del impuesto**, **Cuenta de devolución**, **Cuenta Base (Base Gravable)**, **Cuenta Costo de Inventario**, **Cuenta Valor de Inventario** (pídelas a tu contador).
6. **Crear Catálogo**.
7. Asígnalo a los productos: <span class="ruta">Inventario › Productos</span> › producto › **Catálogo de impuestos**.

✅ Listo: al vender o comprar ese producto, Inventy calcula sus impuestos solo.

!!! captura "CAPTURA PENDIENTE"
    Formulario **Nuevo Catálogo de Impuestos** con IVA 19 % en ventas y compras.

## Si algo falla

| Problema | Solución |
|---|---|
| Aparece **Configuración contable incompleta** / **Cuentas por configurar** | Falta una cuenta contable en el catálogo. Complétala (con tu contador). |
| *El asiento contable no está balanceado* al facturar | El catálogo del producto tiene cuentas vacías. Revisa el catálogo. |
| No me deja crear el producto sin catálogo | Si usas contabilidad, el catálogo es obligatorio en el producto. |
| El producto no cobra IVA | Revisa que su catálogo tenga el IVA en **Impuestos de Ventas**. |
| ¿Cuántos catálogos creo? | Uno por cada combinación distinta de impuestos (ej. gravado 19 %, gravado 5 %, excluido, exento). |

## Relacionados

- [¿Cómo creo un impuesto o una retención?](crear-impuesto.md)
- [¿Cómo creo un producto?](../productos-inventario/crear-producto.md)
- [¿Cómo se aplican las retenciones?](retenciones.md)
