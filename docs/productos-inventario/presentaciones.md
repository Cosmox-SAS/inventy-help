---
title: "¿Cómo manejo las presentaciones de compra y de venta?"
description: "Pasos para crear presentaciones (caja, paquete) y usarlas al comprar, vender, con proveedores y con listas de precios de clientes."
estado: pendiente-validacion
tipo: rapida
modulo: productos-inventario
menu: "Inventario › Productos"
permisos:
  - Editar productos
revisado: 2026-09-30
search:
  boost: 2
tags:
  - Productos
  - Presentaciones
  - Compras
  - Ventas
---

# ¿Cómo manejo las presentaciones de compra y de venta?

<p class="tambien-se-busca">También se busca como: presentación, empaque, caja, paquete, blíster, unidad de compra, unidad de venta, factor de conversión, vender por caja, comprar por caja, código del proveedor, referencia del proveedor, precio por caja.</p>

**Qué es:** un empaque del producto (caja, paquete, blíster) con su propio código de barras y precio. **No hay presentaciones separadas de compra y de venta**: las mismas sirven para las dos.

**Antes de empezar:** activa **Presentaciones** en <span class="ruta">Configuración › Módulos › Inventario</span>.

## Pasos

**Paso 1.** Ingresa a <span class="ruta">Inventario › Productos</span>, abre el producto y edítalo.

![Paso 1: producto en edición](../assets/capturas/productos-inventario/presentaciones/paso-1.png)

**Paso 2.** En **Comportamiento del producto**, haz clic en **Activar presentaciones** y guarda.

![Paso 2: opción Activar presentaciones](../assets/capturas/productos-inventario/presentaciones/paso-2.png)

**Paso 3.** Abre la pestaña **Presentaciones** y haz clic en **Agregar presentación**.

![Paso 3: pestaña Presentaciones](../assets/capturas/productos-inventario/presentaciones/paso-3.png)

**Paso 4.** Completa **Unidad** (ej. *Caja*), **Factor** (cuántas unidades trae, ej. *12*), **Código de barras** del empaque y, si quieres, su **Precio de venta**. Guarda.

![Paso 4: formulario de la presentación](../assets/capturas/productos-inventario/presentaciones/paso-4.png)

**Paso 5.** **Para comprar:** en la factura de compra, en la línea del producto elige la presentación y escribe cuántos empaques compras.

![Paso 5: presentación en la línea de la factura de compra](../assets/capturas/productos-inventario/presentaciones/paso-5.png)

**Paso 6.** **Para vender:** en el POS escanea el código del empaque o elige la presentación. También se elige en la factura de venta y en las preventas.

![Paso 6: presentación al vender](../assets/capturas/productos-inventario/presentaciones/paso-6.png)

**Paso 7.** **Proveedores:** en la pestaña **Referencias de Proveedores**, haz clic en **Agregar Referencia**, elige el **Proveedor** y escribe su **Código de referencia** (el código con que él llama a tu producto).

![Paso 7: pestaña Referencias de Proveedores](../assets/capturas/productos-inventario/presentaciones/paso-7.png)

**Paso 8.** **Clientes:** en la pestaña **Precios**, haz clic en **Añadir precio**, elige la **lista de precios**, la **presentación** y la **sede**, y escribe el precio. Asigna esa lista al cliente en su ficha.

![Paso 8: pestaña Precios del producto](../assets/capturas/productos-inventario/presentaciones/paso-8.png)

✅ **Listo:** el producto se compra y se vende por empaque, y el inventario siempre se lleva en unidades.

!!! info "Cómo se relaciona todo"
    | | Qué se usa | Ejemplo |
    |---|---|---|
    | **Presentación** | Es del **producto** y sirve igual para comprar y vender. | *Caja x 12*, factor 12 |
    | **Inventario** | Siempre en la unidad base. | Comprar 5 cajas = entran **60 unidades** |
    | **Costo** | El precio del empaque se divide por el factor. | Caja a $24.000 → **$2.000** por unidad |
    | **Proveedor** | **Referencia** (su código para tu producto). Sirve para reconocer el producto al subir su XML. | Código *1023* |
    | **Cliente** | **Lista de precios** con precio por presentación y sede. | Caja más barata para mayoristas |

    **Precio que se cobra:** 1) la lista del cliente → 2) en el POS, la lista de la caja → 3) el precio de la presentación (o precio unitario × factor si no tiene).

## Si algo falla

| Problema | Solución |
|---|---|
| No aparece la pestaña **Presentaciones** | Actívala en <span class="ruta">Configuración › Módulos › Inventario</span> y en el producto (**Activar presentaciones**). |
| *Selecciona una unidad diferente a la unidad base del producto.* | La presentación debe tener otra unidad (Caja, Paquete…). |
| No aparece **Referencias de Proveedores** | Solo existe si el módulo **Compras** está activo. |
| No aparece la pestaña **Precios** | Activa **Habilitar listas de precios** en <span class="ruta">Configuración › Módulos › Ventas</span>. |
| *Ya existe un precio para esta lista/presentación/sede.* | Ese precio ya está creado: edítalo en vez de agregar otro. |
| Al subir el XML del proveedor no elige la caja | La referencia del proveedor identifica el **producto**, no el empaque. Elige tú la presentación en esa línea. |
| El costo promedio quedó muy alto | Revisa que en la compra elegiste la presentación: el costo se divide por el **Factor** solo si la línea tiene la presentación. |
| Muchos productos con empaques | Usa <span class="ruta">Inventario › Importar presentaciones</span>. |

## Relacionados

- [¿Cómo creo un producto?](crear-producto.md)
- [¿Cómo registro una factura de compra?](../compras/registrar-factura-compra.md)
- [¿Cómo vendo en el POS?](../pos/vender-en-pos.md)
