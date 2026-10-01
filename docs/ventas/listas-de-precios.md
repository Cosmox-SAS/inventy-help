---
title: "¿Cómo manejo las listas de precios?"
description: "Dónde se activan las listas de precios, cómo crearlas, darles precio por producto o presentación, asignarlas a un cliente o caja, cambiarla en la venta POS y qué precio cobra Inventy."
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

**Qué es:** un grupo de precios especiales (ej. *Mayorista*) que se asigna a un **cliente** o a una **caja**. Cada precio de la lista es para un producto (o una presentación) **en una sede**.

## Pasos

**Paso 1.** Activa la opción (una sola vez): ingresa a <span class="ruta">Configuración › Módulos</span>, elige **Ventas** y enciende **Habilitar listas de precios**. Se guarda solo.

![Paso 1: opción listas de precios en Módulos › Ventas](../assets/capturas/ventas/listas-de-precios/paso-1.png)

**Paso 2.** Ingresa a <span class="ruta">Ventas › Ajustes › Listas de precios</span> y haz clic en **Nueva lista**.

![Paso 2: botón Nueva lista](../assets/capturas/ventas/listas-de-precios/paso-2.png)

**Paso 3.** Escribe el **Nombre** (ej. *Mayorista*), deja **Activa** marcada y haz clic en **Crear**.

![Paso 3: ventana Nueva lista de precios](../assets/capturas/ventas/listas-de-precios/paso-3.png)

**Paso 4.** Dale precio a cada producto: en <span class="ruta">Inventario › Productos</span> abre el producto, haz clic en **Editar producto** y abre la pestaña **Precios**. Por cada precio haz clic en **Añadir precio**, elige la **Lista**, la **Presentación** (*Ítem base* es la unidad; o una caja, ej. *CAJA X 12*), la **Sede** y escribe el **Precio (con impuestos)**. Haz clic en **Guardar precios**. Si vendes en varias sedes, agrega una fila por sede.

![Paso 4: pestaña Precios del producto](../assets/capturas/ventas/listas-de-precios/paso-4.png)

**Paso 5.** Asigna la lista al cliente: en <span class="ruta">Ventas › Clientes</span> abre el cliente, haz clic en **Editar**, elige la **Lista de precios** en **Datos del rol de cliente** y haz clic en **Actualizar cliente**.

![Paso 5: lista de precios en la ficha del cliente](../assets/capturas/ventas/listas-de-precios/paso-5.png)

**Paso 6.** Vende normal. Al elegir ese cliente en el POS o en la factura, los productos salen con el precio de su lista (ej. café a *$16.000* en vez de *$18.500*).

![Paso 6: precio de la lista en el POS](../assets/capturas/ventas/listas-de-precios/paso-6.png)

**Paso 7.** (Opcional) Configura la caja: en <span class="ruta">Tesorería › Caja › Cajas</span> › **Acciones › Editar**:

- **Lista de precios**: la usa el POS de esa caja cuando el cliente no tiene lista con precio para el producto.
- **Permitir cambiar la lista de precios desde la venta POS**: deja que el cajero elija la lista en cada venta.

Haz clic en **Guardar cambios**.

![Paso 7: lista de precios en la caja](../assets/capturas/ventas/listas-de-precios/paso-7.png)

**Paso 8.** (Opcional) Si la caja lo permite, en el POS aparece **Lista de precios** debajo del cliente. Por defecto dice **Automática (cliente / caja)**; ábrela y elige otra lista (ej. *Mayorista*) solo para esa venta.

![Paso 8: selector Lista de precios en el POS](../assets/capturas/ventas/listas-de-precios/paso-8.png)

✅ **Listo:** cada vez que le vendas a ese cliente, Inventy usa los precios de su lista.

## ¿Qué precio cobra Inventy?

Para cada producto de la venta, en este orden (usa el primero que encuentre):

| Orden | POS | Factura de venta |
|---|---|---|
| — | Si el cajero **eligió una lista** en la venta (paso 8): se usa **solo esa**; lo que no tenga precio en ella sale a precio base | — (no aplica) |
| 1 | Precio de la **lista del cliente** para ese producto y tu sede | Igual |
| 2 | Precio de la **lista de la caja** abierta | — (no aplica) |
| 3 | **Precio base** del producto (o de la presentación) | Precio base |

- La caja tiene su **propio precio** en la lista. Si no le pones precio a *CAJA X 12*, la caja sale a su precio base aunque la unidad tenga precio en la lista.
- Si el cliente tiene un **tipo de cliente con descuento**, el descuento se aplica **encima** del precio de la lista.
- Una lista **desactivada** se ignora: se cobra el precio base (el cliente la conserva asignada).
- Si apagas **Habilitar listas de precios**, todo vuelve al precio base.

## Si algo falla

| Problema | Solución |
|---|---|
| No aparece **Listas de precios** en el menú | Activa **Habilitar listas de precios** en <span class="ruta">Configuración › Módulos › Ventas</span> (paso 1). |
| No aparece la pestaña **Precios** en el producto | La misma opción del paso 1 está apagada. |
| *La sede es requerida.* | Elige la **Sede** en cada fila del precio. |
| *La lista de precios es requerida.* | Elige la **Lista** en la fila o bórrala con el ícono de la papelera. |
| *Ya existe un precio para esta lista/presentación/sede.* | Ese precio ya está creado: cámbialo en su fila en vez de agregar otro. |
| El cliente sigue saliendo con el precio normal | Revisa que el cliente tenga la lista en su ficha, que la lista esté **Activa** y que el producto (o esa presentación) tenga precio en esa lista **para tu sede**. |
| No aparece **Lista de precios** en el POS | La caja no tiene marcada **Permitir cambiar la lista de precios desde la venta POS** (paso 7). |
| En la factura no toma la lista de la caja | Es normal: la lista de la caja solo aplica en el POS. Asigna la lista al cliente. |
| ¿Lista de precios o tipo de cliente? | **Lista**: precios fijos por producto. **Tipo de cliente**: un % de descuento para todo. Se pueden usar juntos. |
| Son muchos productos | Usa <span class="ruta">Inventario › Importar precios</span>. |

## Relacionados

- [¿Cómo manejo las presentaciones de compra y de venta?](../productos-inventario/presentaciones.md)
- [¿Cómo creo un cliente?](crear-cliente.md)
- [¿Cómo creo un tipo de cliente?](tipos-de-cliente.md)
- [¿Cómo vendo en el POS?](../pos/vender-en-pos.md)
