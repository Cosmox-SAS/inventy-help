---
title: "¿Qué es un anticipo y cómo se maneja en Inventy?"
description: "Pasos para registrar un anticipo de cliente y usarlo después."
estado: pendiente-validacion
tipo: rapida
modulo: finanzas
menu: "Tesorería › Ingresos"
permisos:
  - Gestionar ingresos
revisado: 2026-10-01
search:
  boost: 2
tags:
  - Anticipos
  - Tesorería
---

# ¿Qué es un anticipo y cómo se maneja en Inventy?

<p class="tambien-se-busca">También se busca como: anticipo, abono previo, saldo a favor, pago por adelantado, depósito del cliente, separado, adelanto a proveedor.</p>

**Qué es:** dinero que el cliente paga **antes** de la factura. Queda como **saldo a favor** y luego se aplica a sus compras.

**Antes de empezar:** debe existir un medio de pago de tipo **Anticipo de cliente** en <span class="ruta">Ventas › Ajustes › Medios de Pago</span>.

## Pasos

**Paso 1.** Ingresa a <span class="ruta">Tesorería › Ingresos</span> y haz clic en **Nuevo ingreso**.

![Paso 1: botón Nuevo ingreso](../assets/capturas/finanzas/anticipos/paso-1.png)

**Paso 2.** En **Tipo de movimiento** elige **Anticipo de cliente**. Elige el **Cliente**, el **Destino** (**Banco** o **Caja**), el **Medio de pago** y escribe el **Ingreso Total**.

![Paso 2: formulario de anticipo](../assets/capturas/finanzas/anticipos/paso-2.png)

**Paso 3.** Haz clic en **Finalizar** y confirma con **Finalizar**. El cliente queda con **saldo a favor** (número **ING-**).

![Paso 3: botón Finalizar](../assets/capturas/finanzas/anticipos/paso-3.png)

**Paso 4.** Para usarlo en el POS: agrega los productos, elige el cliente y haz clic en **Realizar venta**. En **Cobrar venta** elige **Anticipo de cliente** (solo aparece si el cliente tiene saldo). Verás el **Saldo anticipo**.

![Paso 4: medio Anticipo de cliente en el POS](../assets/capturas/finanzas/anticipos/paso-4.png)

**Paso 5.** Haz clic en **Agregar Anticipo de cliente**. En **Distribuir anticipo**, haz clic en el **Saldo disponible** (o escribe el valor en **Aplicar**) y haz clic en **Confirmar distribución**.

![Paso 5: ventana Distribuir anticipo](../assets/capturas/finanzas/anticipos/paso-5.png)

**Paso 6.** Si falta, cobra el resto con otro medio. Haz clic en **Confirmar cobro**.

![Paso 6: botón Confirmar cobro](../assets/capturas/finanzas/anticipos/paso-6.png)

**Paso 7.** Para usarlo en una factura de venta: elige el **Cliente**, **Forma de pago: Contado** y en **Medio de Pago** elige **Anticipo de cliente**. Verás el **Saldo a favor**; aquí el anticipo debe cubrir el total.

![Paso 7: anticipo en la factura de venta](../assets/capturas/finanzas/anticipos/paso-7.png)

✅ **Listo:** el saldo a favor del cliente baja en lo que usaste y la venta queda pagada.

!!! info "Anticipo a proveedor"
    <span class="ruta">Tesorería › Egresos</span> › **Nuevo egreso** › Tipo **Anticipo a proveedor** › **Finalizar**. Para usarlo: nuevo egreso **Pago a proveedor** con **Fuente del pago: Anticipo** y aplícalo en **Anticipos aplicados**.

## Si algo falla

| Problema | Solución |
|---|---|
| No aparece **Anticipo de cliente** en el POS | El cliente no tiene saldo, o no existe el medio de pago de ese tipo. |
| *Selecciona a qué anticipos aplicar el pago.* | Haz clic en **Agregar Anticipo de cliente** y completa **Distribuir anticipo** (paso 5). |
| *Este cliente no tiene anticipos disponibles* | Regístrale primero el anticipo (pasos 1 a 3). |
| *La suma de los anticipos aplicados debe ser igual al valor total* | Ajusta los valores hasta cuadrar con el total. |
| En la factura no me deja pagar solo una parte | En **Facturas** el anticipo cubre el total. Para pago parcial usa el POS. |

## Relacionados

- [¿Cómo registro un pago de un cliente?](registrar-ingreso.md)
- [¿Cómo vendo en el POS?](../pos/vender-en-pos.md)
