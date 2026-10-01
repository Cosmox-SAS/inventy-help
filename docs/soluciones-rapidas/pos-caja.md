---
title: "Soluciones rápidas: POS y caja"
description: No me deja vender, caja descuadrada, monto máximo de caja, no abre el PDF.
estado: pendiente-validacion
tipo: solucion
modulo: pos
revisado: 2026-09-29
tags:
  - POS
  - Caja
  - Soluciones rápidas
---

# Soluciones rápidas: POS y caja

## "No me deja vender, dice que abra una caja"

**PROBLEMA:** al vender aparece *“Debes abrir una caja antes de registrar una venta.”*

**CAUSA:** no tienes una sesión de caja abierta.

**SOLUCIÓN:** [abre la caja](../pos/abrir-caja.md). Si tu negocio vende sin caja, el administrador puede activar **Permitir ventas de contado sin sesión de caja** en <span class="ruta">Configuración › Módulos › Ventas</span>.

**ESCALAR A SOPORTE:** si la caja aparece abierta pero el POS sigue pidiendo abrirla.

**INFORMACIÓN PARA SOPORTE:** nombre de la caja, sede, usuario, captura.

## "Al cobrar dice que la caja no tiene cuenta contable"

**PROBLEMA:** al confirmar el cobro aparece *“La caja de la sesión abierta no tiene una cuenta contable configurada. Configure la cuenta en la caja registradora.”*

**CAUSA:** la empresa usa Contabilidad y la caja se creó sin **Cuenta contable**.

**SOLUCIÓN:** en <span class="ruta">Tesorería › Caja › Cajas</span>, abre **Acciones › Editar** de la caja, elige la **Cuenta contable** (ej. *Caja general*) y haz clic en **Guardar cambios**. No hace falta cerrar la caja. Vuelve a cobrar.

**ESCALAR A SOPORTE:** si no aparece ninguna cuenta para elegir (carga antes las [cuentas auxiliares por defecto](../contabilidad/cuentas-auxiliares.md)).

**INFORMACIÓN PARA SOPORTE:** nombre de la caja, sede, captura del mensaje.

## "No hay cajas para abrir"

**PROBLEMA:** aparece *“No hay cajas disponibles para abrir en este momento.”*

**CAUSA:** no hay cajas creadas, o todas están abiertas por otros usuarios.

**SOLUCIÓN:**

1. Revisa en <span class="ruta">Tesorería › Caja › Sesiones</span> si hay una sesión **Abierta** que alguien olvidó cerrar, y pide que la [cierren](../pos/cierre-de-caja.md).
2. Si necesitas otra caja, créala con **Crear caja** o en <span class="ruta">Tesorería › Caja › Cajas › Nueva caja</span>.

**ESCALAR A SOPORTE:** si una sesión quedó abierta y nadie puede cerrarla.

**INFORMACIÓN PARA SOPORTE:** nombre de la caja, sede, usuario que la abrió.

## "Dice que llegué al monto máximo de la caja"

**PROBLEMA:** aparece *“Ya llegaste al monto máximo de la caja. Debes consignar para continuar vendiendo.”*

**CAUSA:** la caja tiene configurado un **Monto máximo en caja** y el efectivo lo alcanzó. Es una medida de seguridad.

**SOLUCIÓN:**

1. En el POS, usa **Registrar consignación**: elige la **Cuenta bancaria**, el **Monto (COP)** y la referencia, y haz clic en **Confirmar consignación**.
2. Si no tienes permiso para consignar, pide a tu supervisor que lo haga.

**ESCALAR A SOPORTE:** si después de consignar sigue apareciendo el mensaje.

**INFORMACIÓN PARA SOPORTE:** nombre de la caja, valor consignado, hora.

## "La caja no cuadra"

**PROBLEMA:** al cerrar aparece *“Con el valor ingresado, la caja queda descuadrada.”*

**CAUSA:** el efectivo contado es diferente del esperado. Causas comunes: pagos con tarjeta registrados como efectivo (o al revés), cambio mal entregado, retiros no registrados, error al contar.

**SOLUCIÓN:**

1. Vuelve a contar el efectivo.
2. Revisa las ventas del turno y sus medios de pago en <span class="ruta">Tesorería › Caja › Movimientos de caja</span>.
3. Si la diferencia es real, cierra y explica en **Observaciones**.
4. Si te equivocaste al digitar, un supervisor puede usar **Corregir arqueo** en <span class="ruta">Tesorería › Caja › Sesiones</span>.

**ESCALAR A SOPORTE:** si el valor esperado no corresponde a las ventas del día.

**INFORMACIÓN PARA SOPORTE:** caja, fecha de la sesión, valor contado, captura del resumen.

## "Dice que el monto contado es muy distinto al esperado"

**PROBLEMA:** al cerrar aparece *“El monto contado es muy distinto al esperado. Verifica que no falte o sobre un cero o la coma decimal.”*

**CAUSA:** probablemente sobra o falta un cero al escribir el valor.

**SOLUCIÓN:** revisa el valor. Si es correcto, vuelve a escribirlo en **Vuelve a escribir el monto contado** y explica el **Motivo**.

**ESCALAR A SOPORTE:** no suele ser necesario.

**INFORMACIÓN PARA SOPORTE:** —

## "No abre el PDF de la factura"

**PROBLEMA:** aparece *“No se pudo abrir el PDF de la factura. Permite las ventanas emergentes para este sitio.”*

**CAUSA:** el navegador bloquea las ventanas emergentes.

**SOLUCIÓN:** en la barra de direcciones del navegador, haz clic en el ícono de ventana bloqueada y elige **Permitir siempre** para Inventy. Luego vuelve a intentarlo.

**ESCALAR A SOPORTE:** si después de permitir las ventanas emergentes sigue sin abrir.

**INFORMACIÓN PARA SOPORTE:** navegador que usas, número de la factura.

## "No aparecen los medios de pago"

**PROBLEMA:** al cobrar aparece *“No hay medios de pago configurados…”*

**CAUSA:** tu empresa no ha creado medios de pago.

**SOLUCIÓN:** el administrador debe crearlos en <span class="ruta">Ventas › Ajustes › Medios de Pago</span>.

**ESCALAR A SOPORTE:** si ya existen y no aparecen.

**INFORMACIÓN PARA SOPORTE:** nombres de los medios de pago, captura del POS.
