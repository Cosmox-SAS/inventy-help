---
title: ¿Cómo cierro la caja?
description: Cuenta el efectivo, registra el arqueo y decide qué hacer con el dinero al terminar el turno.
estado: pendiente-validacion
tipo: tutorial
modulo: pos
menu: Ventas › POS  ·  Tesorería › Caja › Cajas
permisos:
  - Acceder al POS
  - Ver cajas
revisado: 2026-09-29
tags:
  - POS
  - Caja
---

# ¿Cómo cierro la caja?

<p class="tambien-se-busca">También se busca como: cierre de caja, cuadre de caja, arqueo, cerrar turno, cuadrar caja, entregar caja, faltante, sobrante, descuadre.</p>

## ¿Para qué sirve?

Al cerrar la caja **cuentas el efectivo** que hay en el cajón y lo registras en Inventy. El sistema lo compara con lo que *debería* haber según las ventas y movimientos del turno, y te dice si la caja **cuadra**, tiene **sobrante** o **faltante**.

**Úsala cuando:** terminas tu turno o al final del día.

## Antes de comenzar

- [ ] Tener una **caja abierta** a tu nombre.
- [ ] **Contar el efectivo** del cajón (billetes y monedas).
- [ ] Decidir con tu supervisor qué se hará con el dinero: dejarlo en caja, consignarlo al banco o retirarlo.

## Paso a paso

**Paso 1.** Desde el POS, haz clic en **Cerrar caja** en la barra superior. También puedes hacerlo desde <span class="ruta">Tesorería › Caja › Cajas</span> con la acción **Cerrar caja**.

**Paso 2.** Revisa el **Resumen del arqueo**: fecha y hora de **Apertura** y **Monto base**.

!!! captura "CAPTURA PENDIENTE"
    Ventana **Cerrar caja** con el resumen del arqueo, el campo Efectivo contado y los destinos del dinero.

**Paso 3.** En **Efectivo contado**, escribe el total del efectivo que contaste.

**Paso 4.** Decide qué pasa con el dinero:

| Parte del dinero | Opciones | Qué significa |
|---|---|---|
| **Destino del monto base** | **Dejar en caja** · **Egresar** | La base puede quedarse para el siguiente turno o retirarse de la caja. |
| **Destino del excedente** (lo que supera la base) | **Dejar en caja** · **Consignar** | El excedente puede quedarse o consignarse a una **Cuenta bancaria**. |

- Si eliges **Consignar**, selecciona la **Cuenta bancaria**. *(Solo aparece si tu empresa usa el módulo de bancos y tiene cuentas activas.)*
- Si eliges **Egresar**, escribe el **Motivo del egreso** (ej. *pago a proveedor*).

**Paso 5.** Si quieres, escribe **Observaciones** del arqueo.

**Paso 6.** Haz clic en **Cerrar caja**. Inventy verifica el conteo (verás *Verificando...*).

**Paso 7.** En la ventana **Confirmar cierre de caja**, revisa el mensaje:

- Si la caja **cuadra**, verás *“¿Confirmas el cierre de caja?…”*.
- Si **no cuadra**, verás *“Con el valor ingresado, la caja queda descuadrada. Verifica el conteo antes de confirmar.”* Vuelve a contar antes de continuar.
- Si el monto es **muy distinto** a lo esperado, verás *“El monto contado es muy distinto al esperado. Verifica que no falte o sobre un cero o la coma decimal.”* Para continuar, debes **volver a escribir el monto contado** y explicar el **Motivo**.

**Paso 8.** Haz clic en **Confirmar cierre**.

## Resultado esperado

- La caja queda **Cerrada** y aparece en <span class="ruta">Tesorería › Caja › Sesiones</span>.
- Desde **Sesiones** puedes usar **Imprimir cierre** para obtener el comprobante.
- Si elegiste consignar, el dinero queda registrado en la cuenta bancaria.

## Si te equivocaste en el cierre

Desde <span class="ruta">Tesorería › Caja › Sesiones</span>, un usuario autorizado puede:

- **Corregir arqueo:** cambia el valor contado. Debes explicar por qué se corrige. La sesión queda marcada como *“Este arqueo fue corregido”*.
- **Reabrir cierre:** vuelve a abrir el último cierre. *Esto revertirá la consignación y los ajustes del cierre.* Requiere el permiso **Reabrir cierre de caja**.

## Problemas frecuentes

??? question "La caja queda descuadrada"
    1. Vuelve a contar el efectivo con calma.
    2. Revisa si hubo pagos con tarjeta o transferencia registrados como efectivo (o al revés).
    3. Revisa si alguien sacó dinero sin registrarlo.
    4. Si la diferencia es real, cierra de todas formas y explica la situación en **Observaciones**. Tu supervisor podrá revisarla.

??? question "No aparece la opción Consignar"
    Tu empresa no tiene el módulo de bancos activo o no hay **cuentas bancarias activas**. El administrador debe crearlas en <span class="ruta">Tesorería › Bancos › Cuentas bancarias</span>.

??? question "“El monto no coincide con el valor contado.”"
    En la confirmación de un monto anómalo, el valor que volviste a escribir es diferente del primero. Escríbelo exactamente igual.

??? question "“No tienes permiso para imprimir este cierre.” / “La sesión no está cerrada.”"
    Solo se pueden imprimir sesiones **cerradas**, y tu rol debe tener permiso. Pídeselo al administrador.

## ¿Necesitas ayuda?

[Contacta a soporte](../soporte.md) si no puedes cerrar la caja o si un cierre muestra valores que no corresponden a las ventas del día. Envía el **nombre de la caja**, la **fecha de la sesión** y una **captura del resumen**.

## Artículos relacionados

- [¿Cómo abro la caja?](abrir-caja.md)
- [¿Cómo vendo en el POS?](vender-en-pos.md)
- [Soluciones rápidas: POS y caja](../soluciones-rapidas/pos-caja.md)
