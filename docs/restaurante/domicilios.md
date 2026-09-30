---
title: "¿Cómo manejo los domicilios y le pago a los domiciliarios?"
description: "Pasos para configurar domicilios, despacharlos y pagarle al repartidor."
estado: pendiente-validacion
tipo: rapida
modulo: restaurante
menu: "Restaurante › Domicilios"
permisos:
  - Ver repartidores
  - Ver liquidaciones de domicilios
  - Crear liquidaciones de domicilios
  - Pagar liquidaciones de domicilios
revisado: 2026-09-30
search:
  boost: 2
tags:
  - Restaurante
  - Domicilios
---

# ¿Cómo manejo los domicilios y le pago a los domiciliarios?

<p class="tambien-se-busca">También se busca como: domicilio, delivery, domiciliario, repartidor, mensajero, pagar domicilios, liquidar domiciliario, costo del domicilio, pedido a domicilio.</p>

**Antes de empezar:** activa **Habilitar pedidos a domicilio** y el **Ítem de servicio de domicilio** en <span class="ruta">Configuración › Módulos › Restaurante</span>, y crea al domiciliario como **proveedor**.

## Pasos

**Paso 1.** Ingresa a <span class="ruta">Restaurante › Repartidores</span> › **Nuevo Repartidor**, elige el **Proveedor (tercero)**, marca **Repartidor activo** y haz clic en **Crear repartidor**.

![Paso 1: formulario Nuevo repartidor](../assets/capturas/restaurante/domicilios/paso-1.png)

**Paso 2.** En <span class="ruta">Ventas › POS</span>, elige el tipo de pedido **Domicilio**.

![Paso 2: tipo de pedido Domicilio](../assets/capturas/restaurante/domicilios/paso-2.png)

**Paso 3.** En **Datos del domicilio**, busca o crea el cliente, la **Dirección de entrega**, el **Punto de referencia** y el costo del domicilio.

![Paso 3: ventana Datos del domicilio](../assets/capturas/restaurante/domicilios/paso-3.png)

**Paso 4.** Agrega los productos y haz clic en **Realizar pedido**.

![Paso 4: botón Realizar pedido](../assets/capturas/restaurante/domicilios/paso-4.png)

**Paso 5.** En <span class="ruta">Restaurante › Tablero de pedidos</span>, abre el pedido y haz clic en **Asignar repartidor**. Luego márcalo **En camino** y **Entregado**, y factúralo.

![Paso 5: tablero de pedidos y Asignar repartidor](../assets/capturas/restaurante/domicilios/paso-5.png)

**Paso 6.** Para pagarle: <span class="ruta">Restaurante › Domicilios › Liquidación</span> › **Nueva liquidación**. Elige **Sede - centro de costo**, **Repartidor**, **Fecha inicio** y **Fecha fin**.

![Paso 6: formulario Nueva liquidación](../assets/capturas/restaurante/domicilios/paso-6.png)

**Paso 7.** Revisa los **Domicilios pendientes por liquidar** y el **Total a liquidar**, elige la **Fuente del pago** y haz clic en **Confirmar liquidación**.

![Paso 7: total y Confirmar liquidación](../assets/capturas/restaurante/domicilios/paso-7.png)

✅ **Listo:** al domiciliario se le paga la suma de los costos de domicilio de sus pedidos. Puedes **Imprimir tirilla** para que firme.

## Si algo falla

| Problema | Solución |
|---|---|
| Quiero pagarle en cada pedido, sin liquidar | Activa **Pagar el domicilio al repartidor al instante** en Módulos › Restaurante: la salida de caja se registra sola. |
| *Primero tienes que asignarle un repartidor antes de entregarlo.* | Asigna el repartidor antes de marcar En camino o Entregado. |
| *El costo del domicilio es obligatorio y debe ser mayor que 0.* | Escribe el costo del domicilio. |
| *No hay domicilios pendientes por liquidar…* | Solo entran pedidos **facturados**, de esa sede y fechas, no pagados antes. |
| *El total supera el saldo disponible de la cuenta.* | Elige otra fuente del pago. |
| *No se generará asiento contable…* | Configura la **Cuenta contable de gasto de domicilios**. |
| Liquidé mal | En el detalle: **Más acciones › Anular** y créala de nuevo. |

## Relacionados

- [¿Cómo activo varias cuentas en una misma mesa?](varias-cuentas-mesa.md)
- [Todas las opciones de Módulos](../primeros-pasos/opciones-modulos.md)
