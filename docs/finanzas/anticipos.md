---
title: "¿Qué es un anticipo y cómo se maneja en Inventy?"
description: "Pasos para registrar un anticipo de cliente y usarlo después."
estado: pendiente-validacion
tipo: rapida
modulo: finanzas
menu: "Tesorería › Ingresos"
permisos:
  - Gestionar ingresos
revisado: 2026-09-30
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

**Paso 2.** Elige **Tipo de movimiento**: **Anticipo de cliente**, el **Cliente**, el **Destino**, el **Medio de pago** y el **Ingreso Total**.

![Paso 2: formulario de anticipo](../assets/capturas/finanzas/anticipos/paso-2.png)

**Paso 3.** Haz clic en **Finalizar ingreso**. El cliente queda con **saldo a favor**.

![Paso 3: botón Finalizar ingreso](../assets/capturas/finanzas/anticipos/paso-3.png)

**Paso 4.** Para usarlo en el POS: al cobrar, elige el medio **Anticipo de cliente** (solo aparece si el cliente tiene saldo). Puedes pagar el resto con otro medio.

![Paso 4: medio Anticipo de cliente en el POS](../assets/capturas/finanzas/anticipos/paso-4.png)

**Paso 5.** Para usarlo en una factura: en **Medio de Pago** elige **Anticipo de cliente**. Verás el **Saldo a favor**; aquí debe cubrir el total.

![Paso 5: anticipo en la factura de venta](../assets/capturas/finanzas/anticipos/paso-5.png)

✅ **Listo:** el saldo a favor baja y la venta queda pagada con el anticipo.

!!! info "Anticipo a proveedor"
    <span class="ruta">Tesorería › Egresos</span> › **Nuevo egreso** › Tipo **Anticipo a proveedor** › **Finalizar egreso**. Para usarlo: nuevo egreso **Pago a proveedor** con **Fuente del pago: Anticipo** y aplícalo en **Anticipos aplicados**.

## Si algo falla

| Problema | Solución |
|---|---|
| No aparece **Anticipo de cliente** en el POS | El cliente no tiene saldo, o no existe el medio de pago de ese tipo. |
| *Este cliente no tiene anticipos disponibles* | Regístrale primero el anticipo (pasos 1 a 3). |
| *La suma de los anticipos aplicados debe ser igual al valor total* | Ajusta los valores hasta cuadrar con el total. |
| En la factura no me deja pagar solo una parte | En **Facturas** el anticipo cubre el total. Para pago parcial usa el POS. |

## Relacionados

- [¿Cómo registro un pago de un cliente?](registrar-ingreso.md)
- [¿Cómo vendo en el POS?](../pos/vender-en-pos.md)
