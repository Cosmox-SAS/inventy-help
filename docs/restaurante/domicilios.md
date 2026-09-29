---
title: ¿Cómo manejo los domicilios y cómo le pago a los domiciliarios?
description: "Pasos para configurar domicilios, despacharlos desde el POS y pagarle a los repartidores: al instante o por liquidación."
estado: pendiente-validacion
tipo: rapida
modulo: restaurante
menu: Restaurante › Domicilios
permisos:
  - Ver repartidores
  - Ver liquidaciones de domicilios
  - Crear liquidaciones de domicilios
  - Pagar liquidaciones de domicilios
revisado: 2026-09-29
search:
  boost: 2
tags:
  - Restaurante
  - Domicilios
---

# ¿Cómo manejo los domicilios y cómo le pago a los domiciliarios?

<p class="tambien-se-busca">También se busca como: domicilio, delivery, domiciliario, repartidor, mensajero, pagar domicilios, liquidar domiciliario, costo del domicilio, pedido a domicilio.</p>

<span class="ruta">Restaurante › Domicilios</span>

## Pasos

**1. Configurar (una sola vez)**

1. <span class="ruta">Configuración › Módulos › Restaurante</span>:
    - Activa **Habilitar pedidos a domicilio**.
    - **Ítem de servicio de domicilio**: el servicio que se cobra en la factura (créalo antes en <span class="ruta">Inventario › Servicios</span>).
    - (Opcional) **Valor del domicilio obligatorio**.
    - (Opcional) **Pagar el domicilio al repartidor al instante**.
    - **Cuenta contable de gasto de domicilios** (si usas contabilidad).
2. Crea cada domiciliario como **proveedor** (<span class="ruta">Compras › Proveedores</span>).
3. <span class="ruta">Restaurante › Repartidores</span> › **Nuevo Repartidor** › elige el **Proveedor (tercero)** › marca **Repartidor activo** › **Crear repartidor**.

**2. Tomar un domicilio (POS)**

4. <span class="ruta">Ventas › POS</span> › elige el tipo de pedido **Domicilio**.
5. En **Datos del domicilio**: busca o crea el cliente, **Dirección de entrega**, **Punto de referencia** y el **costo del domicilio**.
6. Agrega los productos › **Realizar pedido**.

**3. Despachar**

7. <span class="ruta">Restaurante › Tablero de pedidos</span> › abre el pedido › **Asignar repartidor**.
8. Cambia el pedido a **En camino** y luego a **Entregado**.
9. Cobra y factura el pedido.

**4. Pagarle al domiciliario** (elige una forma)

- **Al instante (automático):** si activaste **Pagar el domicilio al repartidor al instante**, al facturar (o al asignar el repartidor) Inventy registra solo la **salida de caja** por el valor del domicilio. No haces nada más.
- **Por liquidación (al final del día o de la semana):**
    1. <span class="ruta">Restaurante › Domicilios › Liquidación</span> › **Nueva liquidación**.
    2. Elige **Sede - centro de costo**, **Repartidor**, **Fecha inicio** y **Fecha fin**.
    3. Revisa **Domicilios pendientes por liquidar** y el **Total a liquidar**.
    4. **Fuente del pago**: caja abierta, banco o **Efectivo (sin caja abierta)**.
    5. **Confirmar liquidación**.
    6. (Opcional) **Imprimir tirilla** para que el domiciliario firme.

✅ Listo: al domiciliario se le paga la **suma de los costos de domicilio** de sus pedidos, y queda registrado el egreso y el gasto.

## Si algo falla

| Problema | Solución |
|---|---|
| No aparece el menú **Domicilios** o el tipo de pedido Domicilio | Activa **Habilitar pedidos a domicilio** en Módulos › Restaurante (y el POS debe estar activo). |
| *Primero tienes que asignarle un repartidor antes de entregarlo* | Asigna el repartidor antes de marcar **En camino** o **Entregado**. |
| *El costo del domicilio es obligatorio y debe ser mayor que 0* | Está activo **Valor del domicilio obligatorio**. Escribe el costo. |
| El repartidor no aparece para asignar | Revisa que esté **Repartidor activo** en <span class="ruta">Restaurante › Repartidores</span>. |
| *No hay domicilios pendientes por liquidar para este repartidor en el rango de fechas seleccionado* | Solo se liquidan domicilios **facturados**, con ese repartidor, en esa sede y fechas, que no se hayan pagado antes (ni al instante). Revisa fechas y sede. |
| Un domicilio no aparece en la liquidación | Se facturó con **devolución confirmada**, ya se pagó al instante o ya está en otra liquidación. |
| *El total supera el saldo disponible de la cuenta* | La caja o banco elegido no tiene saldo suficiente. Elige otra fuente. |
| *No se generará asiento contable…* | Falta la **Cuenta contable de gasto de domicilios** en Módulos › Restaurante. |
| Liquidé mal | Abre la liquidación › **Más acciones** › anúlala con un motivo y créala de nuevo. |

## Relacionados

- [Restaurante](index.md)
- [¿Cómo abro la caja?](../pos/abrir-caja.md)
- [¿Cómo registro un pago a un proveedor?](../finanzas/registrar-egreso.md)
