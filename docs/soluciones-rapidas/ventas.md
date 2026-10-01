---
title: "Soluciones rápidas: ventas"
description: Pide cuenta por cobrar, sin cupo de crédito, fecha futura, no puedo anular, asiento no balanceado.
estado: pendiente-validacion
tipo: solucion
modulo: ventas
revisado: 2026-10-01
tags:
  - Ventas
  - Soluciones rápidas
---

# Soluciones rápidas: ventas

## "Al validar la factura a crédito me pide configurar la cuenta contable"

**PROBLEMA:** al validar una factura **a crédito** aparece *“Configura una cuenta de cuentas por cobrar en el tipo de cliente para facturar a crédito con contabilidad activa.”*

**CAUSA:** la empresa usa Contabilidad y el cliente **no tiene tipo de cliente**, o su tipo de cliente **no tiene Cuenta por cobrar**.

**SOLUCIÓN:**

1. Abre el cliente en <span class="ruta">Ventas › Clientes</span> › **Editar** y mira **Tipo de cliente** (en **Datos del rol de cliente**).
2. Si está vacío, elige uno (ej. *General*) y haz clic en **Actualizar cliente**.
3. Si ya tiene tipo, ve a <span class="ruta">Ventas › Ajustes › Tipos de clientes</span> (barra izquierda **Ventas** → sección **AJUSTES**), edita ese tipo y elige la **Cuenta por cobrar** (ej. *130505001 — Clientes nacionales*). Guarda.
4. Vuelve a la factura, ábrela con **Editar** y valídala desde ahí: al guardarla, toma la cuenta nueva. Si la validas sin editarla, puede seguir saliendo el mismo mensaje.

**ESCALAR A SOPORTE:** si el tipo de cliente ya tiene cuenta, editaste la factura y el mensaje sigue.

**INFORMACIÓN PARA SOPORTE:** número de la factura, nombre del cliente, tipo de cliente, captura del mensaje.

## "No me deja vender a crédito"

**PROBLEMA:** aparece *“Este cliente no tiene cupo de crédito disponible.”* o *“El saldo a crédito supera el cupo disponible del cliente…”*

**CAUSA:** el **Límite de crédito** del cliente es 0 o ya está usado con otras facturas.

**SOLUCIÓN:**

1. Cobra una parte de contado y deja el resto a crédito.
2. O aumenta el **Límite de crédito** en la ficha del cliente (<span class="ruta">Ventas › Clientes</span>).
3. En el POS, si tu empresa lo permite, un supervisor puede autorizar el cupo extra con su **PIN**.

**ESCALAR A SOPORTE:** si el cliente no tiene deudas y aun así no hay cupo.

**INFORMACIÓN PARA SOPORTE:** documento del cliente, cupo configurado, valor de la venta.

## "No puedo poner esa fecha en la factura"

**PROBLEMA:** aparece *“La fecha de emisión no puede ser una fecha futura.”*

**CAUSA:** las facturas no pueden tener fecha posterior a hoy.

**SOLUCIÓN:** usa la fecha de hoy o una anterior.

**ESCALAR A SOPORTE:** no aplica.

**INFORMACIÓN PARA SOPORTE:** —

## "No puedo anular una factura"

**PROBLEMA:** aparece *“No puedes anular una venta con movimientos de inventario.”* o *“…que incluye líneas convertidas desde una remisión.”*

**CAUSA:** esas facturas no se pueden anular porque ya afectaron el inventario o vienen de una remisión.

**SOLUCIÓN:** registra una [devolución de venta](../ventas/devolucion-venta.md) total.

**ESCALAR A SOPORTE:** si la devolución tampoco es posible.

**INFORMACIÓN PARA SOPORTE:** número de la factura, motivo.

## "Me equivoqué en una factura ya validada"

**PROBLEMA:** necesito cambiar una factura validada.

**CAUSA:** las facturas validadas no se pueden editar.

**SOLUCIÓN:** registra una [devolución](../ventas/devolucion-venta.md) (total o parcial) y crea una factura nueva con los datos correctos.

**ESCALAR A SOPORTE:** si la factura ya fue aceptada por la DIAN y tienes dudas sobre cómo corregirla.

**INFORMACIÓN PARA SOPORTE:** número de la factura, qué dato está mal.

## "Dice que el asiento contable no está balanceado"

**PROBLEMA:** al validar aparece *“El asiento contable no está balanceado”*.

**CAUSA:** falta la cuenta contable de un producto, impuesto, medio de pago o de la configuración contable.

**SOLUCIÓN:** usa **Ver asientos** para ver qué línea queda sin cuenta y pide a tu contador que la configure en <span class="ruta">Contabilidad › Configuración</span> o en el **Catálogo de Impuestos**.

**ESCALAR A SOPORTE:** si toda la configuración parece correcta.

**INFORMACIÓN PARA SOPORTE:** captura de **Ver asientos**, productos de la factura.
