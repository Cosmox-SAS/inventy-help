---
title: "¿Cómo registro un pago a un proveedor?"
description: "Pasos para registrar el pago de facturas de compra."
estado: pendiente-validacion
tipo: rapida
modulo: finanzas
menu: "Tesorería › Egresos"
permisos:
  - Gestionar egresos
revisado: 2026-10-01
tags:
  - Tesorería
  - Proveedores
  - Gastos
---

# ¿Cómo registro un pago a un proveedor?

<p class="tambien-se-busca">También se busca como: egreso, pagar proveedor, comprobante de egreso, abono a proveedor, pagar factura de compra, registrar gasto.</p>

**Antes de empezar:** la factura del proveedor debe estar registrada ([factura de compra](../compras/registrar-factura-compra.md)).

## Pasos

**Paso 1.** Ingresa a <span class="ruta">Tesorería › Egresos</span> y haz clic en **Nuevo egreso**.

![Paso 1: botón Nuevo egreso](../assets/capturas/finanzas/registrar-egreso/paso-1.png)

**Paso 2.** Elige **Tipo de movimiento**: **Pago a proveedor**, y el **Proveedor**.

![Paso 2: tipo de movimiento y proveedor](../assets/capturas/finanzas/registrar-egreso/paso-2.png)

**Paso 3.** Revisa **Centro de costo** y **Fecha del pago**. En **Fuente del pago** elige **Banco**, **Caja** (sale de tu caja abierta) o **Anticipo**. Escribe el **Egreso Total** y, si quieres, el **Comprobante**.

![Paso 3: información del egreso](../assets/capturas/finanzas/registrar-egreso/paso-3.png)

**Paso 4.** En **Distribución del egreso**, escribe el **Valor abono** de cada factura (o haz clic en el **Saldo pendiente** para pagarla completa) hasta que abajo diga **Distribución completa**.

![Paso 4: distribución del egreso](../assets/capturas/finanzas/registrar-egreso/paso-4.png)

**Paso 5.** Haz clic en **Finalizar** y confirma con **Finalizar**.

![Paso 5: botón Finalizar](../assets/capturas/finanzas/registrar-egreso/paso-5.png)

✅ **Listo:** el egreso queda **Finalizado** con número **PGE-**, baja el saldo de la factura del proveedor y el dinero sale de la caja o banco. Si aún no quieres confirmarlo, usa **Guardar borrador**.

## Si algo falla

| Problema | Solución |
|---|---|
| *No hay destinos disponibles…* | Necesitas una caja abierta o una cuenta bancaria. |
| *La suma de las asignaciones debe ser igual al valor total* | Ajusta hasta que **Por distribuir** quede en cero. |
| Quiero borrar un egreso | Solo se eliminan los que están en **borrador**. |

## Relacionados

- [¿Qué es un anticipo y cómo se maneja?](anticipos.md)
- [¿Cómo registro una factura de compra?](../compras/registrar-factura-compra.md)
