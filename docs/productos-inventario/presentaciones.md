---
title: "¿Cómo manejo las presentaciones de compra y de venta?"
description: "Dónde se activan las presentaciones y cómo crearlas (caja, paquete) y usarlas al comprar, vender y con proveedores."
estado: pendiente-validacion
tipo: rapida
modulo: productos-inventario
menu: "Inventario › Productos"
permisos:
  - Editar productos
revisado: 2026-10-01
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

## Pasos

**Paso 1.** Activa la opción (una sola vez para la empresa): ingresa a <span class="ruta">Configuración › Módulos</span>, elige **Inventario** y enciende **Presentaciones**. Se guarda solo.

![Paso 1: opción Presentaciones en Módulos › Inventario](../assets/capturas/productos-inventario/presentaciones/paso-1.png)

**Paso 2.** Activa el producto: en <span class="ruta">Inventario › Productos</span> abre el producto, haz clic en **Editar producto** y, en **Comportamiento del producto**, haz clic en **Activar presentaciones**. Haz clic en **Actualizar Producto**.

![Paso 2: Activar presentaciones en el producto](../assets/capturas/productos-inventario/presentaciones/paso-2.png)

**Paso 3.** Vuelve a **Editar producto**, abre la pestaña **Presentaciones** y haz clic en **Agregar presentación**.

![Paso 3: pestaña Presentaciones](../assets/capturas/productos-inventario/presentaciones/paso-3.png)

**Paso 4.** Escribe el **Nombre** (ej. *CAJA X 12*), elige la **Unidad** (ej. *Caja*), el **Factor** (cuántas unidades trae, ej. *12*), el **Código de barras** del empaque si tiene y su **Precio de venta (con impuestos)**. Haz clic en **Guardar**.

![Paso 4: formulario de la presentación](../assets/capturas/productos-inventario/presentaciones/paso-4.png)

**Paso 5.** **Para comprar:** en la factura de compra, en la línea del producto elige la **Presentación** (ej. *CAJA X 12*), escribe cuántas cajas compras y **el precio de una caja** (ej. 12 × $11.000 = *132.000*). Inventy no multiplica el precio solo.

![Paso 5: presentación en la línea de la factura de compra](../assets/capturas/productos-inventario/presentaciones/paso-5.png)

**Paso 6.** **Para vender:** en el POS la caja aparece como otra tarjeta (ej. *CAFÉ MOLIDO 500 G · CAJA X 12*) con su precio y su stock en paquetes. Haz clic en ella o escanea su código. En la factura de venta se elige igual que en la compra.

![Paso 6: presentación en el POS](../assets/capturas/productos-inventario/presentaciones/paso-6.png)

**Paso 7.** **Proveedores:** en **Editar producto › Referencias de Proveedores**, haz clic en **Agregar Referencia**, elige el **Proveedor** y escribe su código (el código con que él llama a tu producto).

![Paso 7: pestaña Referencias de Proveedores](../assets/capturas/productos-inventario/presentaciones/paso-7.png)

✅ **Listo:** compras y vendes por caja; el inventario se mueve en unidades (1 caja = 12 unidades).

!!! tip "Precio especial por cliente"
    Para dar a un cliente otro precio de la unidad o de la caja usa [listas de precios](../ventas/listas-de-precios.md).

## Si algo falla

| Problema | Solución |
|---|---|
| No aparece la pestaña **Presentaciones** | Actívala en <span class="ruta">Configuración › Módulos › Inventario</span> y en el producto (**Activar presentaciones**). |
| *Selecciona una unidad diferente a la unidad base del producto.* | La presentación debe tener otra unidad (Caja, Paquete…). |
| No aparece **Referencias de Proveedores** | Solo existe si el módulo **Compras** está activo. |
| No aparece la pestaña **Precios** | Activa **Habilitar listas de precios** en <span class="ruta">Configuración › Módulos › Ventas</span>. |
| *Ya existe un precio para esta lista/presentación/sede.* | Ese precio ya está creado: edítalo en vez de agregar otro. |
| Al subir el XML del proveedor no elige la caja | La referencia del proveedor identifica el **producto**, no el empaque. Elige tú la presentación en esa línea. |
| El costo promedio quedó muy alto o muy bajo | Revisa la línea de la compra: con la presentación elegida, el **Precio** debe ser el de **una caja**, no el de una unidad. |
| Muchos productos con empaques | Usa <span class="ruta">Inventario › Importar presentaciones</span>. |

## Relacionados

- [¿Cómo creo un producto?](crear-producto.md)
- [¿Cómo registro una factura de compra?](../compras/registrar-factura-compra.md)
- [¿Cómo vendo en el POS?](../pos/vender-en-pos.md)
- [¿Cómo manejo las listas de precios?](../ventas/listas-de-precios.md)
