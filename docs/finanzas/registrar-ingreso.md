---
title: "¿Cómo registro un pago de un cliente?"
description: "Pasos para registrar el recaudo de facturas a crédito."
estado: pendiente-validacion
tipo: rapida
modulo: finanzas
menu: "Tesorería › Ingresos"
permisos:
  - Gestionar ingresos
revisado: 2026-10-19
tags:
  - Tesorería
  - Cartera
---

# ¿Cómo registro un pago de un cliente?

<p class="tambien-se-busca">También se busca como: recaudo, abono, cliente pagó, recibo de caja, cobrar cartera, pago de factura a crédito.</p>

**Antes de empezar:** necesitas una caja abierta o una cuenta bancaria donde entra el dinero.

## Pasos

**Paso 1.** Ingresa a <span class="ruta">Tesorería › Ingresos</span> y haz clic en **Nuevo ingreso**.

![Paso 1: botón Nuevo ingreso](../assets/capturas/finanzas/registrar-ingreso/paso-1.webp)

**Paso 2.** Elige **Tipo de movimiento**: **Recaudo de cartera**, y el **Cliente**.

![Paso 2: tipo de movimiento y cliente](../assets/capturas/finanzas/registrar-ingreso/paso-2.webp)

**Paso 3.** Completa **Centro de costo**, **Fecha del pago**, **Destino** (**Banco**, **Caja**, **Anticipo** o **Nota crédito**; con *Caja* se usa tu caja abierta), **Medio de pago** e **Ingreso Total**.

![Paso 3: información del ingreso](../assets/capturas/finanzas/registrar-ingreso/paso-3.webp)

**Paso 4.** En **Distribución del ingreso**, haz clic en el **Saldo pendiente** de cada factura que paga: se llena su **Valor abono**. Sigue hasta que **Por distribuir** diga **Distribución completa**. Si una factura pide **Cuenta de cartera (factura importada)**, elige la cuenta por cobrar del cliente (ej. *130505001 — Clientes nacionales*), nunca una cuenta de caja o de banco.

![Paso 4: distribución del ingreso](../assets/capturas/finanzas/registrar-ingreso/paso-4.webp)

**Paso 5.** Haz clic en **Finalizar ingreso** y confirma.

![Paso 5: botón Finalizar ingreso](../assets/capturas/finanzas/registrar-ingreso/paso-5.webp)

✅ **Listo:** las facturas bajan su saldo (o quedan **Pagadas**) y el dinero entra a la caja o banco.

## Si algo falla

| Problema | Solución |
|---|---|
| *No hay destinos disponibles: habilita el módulo bancario o abre una caja.* | [Abre una caja](../pos/abrir-caja.md) o crea una cuenta bancaria. |
| *La suma de las asignaciones debe ser igual al valor total* | Ajusta hasta que **Por distribuir** quede en cero. |
| *Ingresa el valor de abono para la factura con retención antes de finalizar* | Escribe cuánto abona a esa factura. |
| *La factura … no tiene una cuenta contable de cartera configurada. Selecciona una cuenta para continuar.* | Es una factura importada (saldo inicial). En **Cuenta de cartera (factura importada)** elige la cuenta por cobrar (ej. *130505001 — Clientes nacionales*). Si eliges una cuenta de caja o banco, la contabilidad queda mal. Solo se pide la primera vez. |
| *No hay una cuenta contable configurada para el destino o la cartera de una de las facturas.* | Al destino le falta cuenta contable. Con **Banco**: en <span class="ruta">Tesorería › Cuentas bancarias</span> edita la cuenta, elige su **Cuenta contable** y haz clic en **Guardar cambios**. Con **Caja**: en <span class="ruta">Tesorería › Caja › Cajas</span> edita la caja y elige su **Cuenta contable**. Con **Anticipo** o **Nota crédito**: pide a tu contador que configure esas cuentas en <span class="ruta">Contabilidad › Configuración</span>. |

## Relacionados

- [¿Qué es un anticipo y cómo se maneja?](anticipos.md)
- [¿Cómo hago una factura de venta?](../ventas/crear-factura-venta.md)
