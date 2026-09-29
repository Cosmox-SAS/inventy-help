---
title: ¿Qué es un anticipo y cómo se maneja en Inventy?
description: Registra anticipos de clientes y a proveedores, y aplícalos en facturas, POS y pagos.
estado: pendiente-validacion
tipo: rapida
modulo: finanzas
menu: Tesorería › Ingresos  ·  Tesorería › Egresos
permisos:
  - Gestionar ingresos
  - Gestionar egresos
revisado: 2026-09-29
search:
  boost: 2
tags:
  - Anticipos
  - Tesorería
---

# ¿Qué es un anticipo y cómo se maneja en Inventy?

<p class="tambien-se-busca">También se busca como: anticipo, abono previo, saldo a favor, pago por adelantado, depósito del cliente, separado, adelanto a proveedor.</p>

**Qué es:** dinero que se paga **antes** de que exista la factura.

- **Anticipo de cliente:** el cliente te paga por adelantado → queda como **saldo a favor** del cliente.
- **Anticipo a proveedor:** tú le pagas por adelantado al proveedor → queda como saldo a tu favor con él.

Después, ese saldo se **aplica** a una o varias facturas.

## Pasos

**Registrar un anticipo de cliente**

1. <span class="ruta">Tesorería › Ingresos</span> › **Nuevo ingreso**.
2. **Tipo de movimiento**: **Anticipo de cliente**.
3. **Cliente**, **Destino** (caja o banco), **Medio de pago**, **Ingreso Total**.
4. **Finalizar ingreso**.

**Usar el anticipo del cliente**

- **En una factura** (<span class="ruta">Ventas › Facturas › Nueva Factura</span>): **Medio de Pago** › elige el medio tipo **Anticipo de cliente**. Verás el **Saldo a favor**. Aquí el anticipo debe cubrir el total.
- **En el POS**: al cobrar, elige el medio **Anticipo de cliente** (solo aparece si el cliente tiene saldo). Puedes pagar una parte con anticipo y el resto con otro medio.
- **En un recaudo** (<span class="ruta">Tesorería › Ingresos</span>): usa **Anticipos aplicados** para cruzar el saldo con facturas pendientes.

**Registrar un anticipo a proveedor**

1. <span class="ruta">Tesorería › Egresos</span> › **Nuevo egreso**.
2. **Tipo de movimiento**: **Anticipo a proveedor**.
3. **Proveedor**, **Fuente del pago**, **Egreso Total**.
4. **Finalizar egreso**.

**Usar el anticipo al proveedor**

1. <span class="ruta">Tesorería › Egresos</span> › **Nuevo egreso** › **Pago a proveedor**.
2. **Fuente del pago**: **Anticipo**.
3. En **Anticipos aplicados**, elige el anticipo y asígnalo a las facturas.
4. **Finalizar egreso**.

✅ Listo: el saldo del anticipo baja y las facturas quedan pagadas o abonadas.

!!! note "Requisito"
    Para usar anticipos de clientes debe existir un **medio de pago** de tipo **Anticipo de cliente** en <span class="ruta">Ventas › Ajustes › Medios de Pago</span>.

## Si algo falla

| Problema | Solución |
|---|---|
| No aparece el medio **Anticipo de cliente** en el POS | El cliente no tiene saldo a favor, o no existe el medio de pago tipo *Anticipo de cliente*. |
| *Este cliente no tiene anticipos disponibles* | El cliente no tiene saldo. Regístrale primero el anticipo. |
| *La suma de los anticipos aplicados debe ser igual al valor total* | Ajusta los valores hasta que cuadren con el total del pago. |
| En la factura no me deja pagar solo una parte con anticipo | En **Facturas** el anticipo debe cubrir el total. Para pago parcial, usa el POS o aplica el anticipo después con un ingreso. |
| ¿Dónde veo cuánto saldo a favor tiene un cliente? | Al elegir el medio **Anticipo de cliente** en una factura se muestra el **Saldo a favor**. |

## Relacionados

- [¿Cómo registro un pago de un cliente?](registrar-ingreso.md)
- [¿Cómo registro un pago a un proveedor?](registrar-egreso.md)
- [¿Cómo vendo en el POS?](../pos/vender-en-pos.md)
