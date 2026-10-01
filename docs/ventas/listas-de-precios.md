---
title: "¿Cómo manejo las listas de precios?"
description: "Dónde se activan las listas de precios, cómo crearlas, darles precio por producto o presentación y asignarlas a un cliente."
estado: pendiente-validacion
tipo: rapida
modulo: ventas
menu: "Ventas › Ajustes › Listas de precios"
permisos:
  - Ver listas de precios
  - Editar productos
revisado: 2026-10-01
search:
  boost: 2
tags:
  - Ventas
  - Precios
  - Clientes
---

# ¿Cómo manejo las listas de precios?

<p class="tambien-se-busca">También se busca como: lista de precios, precio mayorista, precio especial, precio por cliente, precio diferente, tarifa, precio por sede, precio por caja.</p>

**Qué es:** un grupo de precios especiales (ej. *Mayorista*) que se asigna a clientes. Inventy cobra el precio de la **lista del cliente**; si no tiene, el de la **lista de la sede o la caja**; si tampoco, el **precio base** del producto.

## Pasos

**Paso 1.** Activa la opción (una sola vez): ingresa a <span class="ruta">Configuración › Módulos</span>, elige **Ventas** y enciende **Habilitar listas de precios**. Se guarda solo.

![Paso 1: opción listas de precios en Módulos › Ventas](../assets/capturas/ventas/listas-de-precios/paso-1.png)

**Paso 2.** Ingresa a <span class="ruta">Ventas › Ajustes › Listas de precios</span> y haz clic en **Nueva lista**.

![Paso 2: botón Nueva lista](../assets/capturas/ventas/listas-de-precios/paso-2.png)

**Paso 3.** Escribe el **Nombre** (ej. *Mayorista*), deja **Activa** marcada y haz clic en **Crear**.

![Paso 3: ventana Nueva lista de precios](../assets/capturas/ventas/listas-de-precios/paso-3.png)

**Paso 4.** Dale precio a cada producto: en <span class="ruta">Inventario › Productos</span> abre el producto, haz clic en **Editar producto** y abre la pestaña **Precios**. Por cada precio haz clic en **Añadir precio**, elige la **Lista**, la **Presentación** (*Ítem base* es la unidad; o una caja, ej. *CAJA X 12*), la **Sede** y escribe el **Precio (con impuestos)**. Haz clic en **Guardar precios**.

![Paso 4: pestaña Precios del producto](../assets/capturas/ventas/listas-de-precios/paso-4.png)

**Paso 5.** Asigna la lista al cliente: en <span class="ruta">Ventas › Clientes</span> abre el cliente, haz clic en **Editar**, elige la **Lista de precios** en **Datos del rol de cliente** y haz clic en **Actualizar cliente**.

![Paso 5: lista de precios en la ficha del cliente](../assets/capturas/ventas/listas-de-precios/paso-5.png)

**Paso 6.** Vende normal. Al elegir ese cliente en el POS o en la factura, los productos salen con el precio de su lista (ej. café a *$16.000* en vez de *$18.500*).

![Paso 6: precio de la lista en el POS](../assets/capturas/ventas/listas-de-precios/paso-6.png)

✅ **Listo:** cada vez que le vendas a ese cliente, Inventy usa los precios de su lista.

!!! tip "Lista por sede o por caja"
    Para que todo un punto de venta use una lista, asígnala en la caja: <span class="ruta">Tesorería › Caja › Cajas</span> › **Acciones › Editar** › **Lista de precios**. La lista del cliente siempre gana.

## Si algo falla

| Problema | Solución |
|---|---|
| No aparece **Listas de precios** en el menú | Activa **Habilitar listas de precios** en <span class="ruta">Configuración › Módulos › Ventas</span> (paso 1). |
| No aparece la pestaña **Precios** en el producto | La misma opción del paso 1 está apagada. |
| *La sede es requerida.* | Elige la **Sede** en cada fila del precio. |
| *La lista de precios es requerida.* | Elige la **Lista** en la fila o bórrala con el ícono de la papelera. |
| *Ya existe un precio para esta lista/presentación/sede.* | Ese precio ya está creado: cámbialo en su fila en vez de agregar otro. |
| El cliente sigue saliendo con el precio normal | Revisa que el cliente tenga la lista en su ficha y que el producto tenga precio en esa lista **para tu sede**. |
| Son muchos productos | Usa <span class="ruta">Inventario › Importar precios</span>. |

## Relacionados

- [¿Cómo manejo las presentaciones de compra y de venta?](../productos-inventario/presentaciones.md)
- [¿Cómo creo un cliente?](crear-cliente.md)
- [¿Cómo creo un tipo de cliente?](tipos-de-cliente.md)
- [¿Cómo vendo en el POS?](../pos/vender-en-pos.md)
