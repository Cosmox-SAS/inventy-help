---
title: "¿Cómo parametrizo la contabilidad de una empresa nueva?"
description: "Lista de verificación, en orden, para dejar la contabilidad de una empresa nueva lista antes de la primera venta o compra."
estado: pendiente-validacion
tipo: concepto
modulo: contabilidad
revisado: 2026-11-12
tags:
  - Contabilidad
  - Configuración
---

# ¿Cómo parametrizo la contabilidad de una empresa nueva?

<p class="tambien-se-busca">También se busca como: parametrización contable, puesta en marcha contable, implementación contable, configurar contabilidad desde cero, checklist contable, PUC inicial.</p>

Sigue esta lista **en orden**: cada paso usa las cuentas que dejó listas el anterior. Si saltas uno, Inventy no va a tener dónde contabilizar y el documento mostrará *"El asiento contable no está balanceado"* al intentar validarlo (ver [¿Cómo funciona la contabilidad en Inventy?](como-funciona.md)).

**Antes de empezar:** necesitas el módulo **Contabilidad** incluido en tu plan y el permiso de administrador. Si tienes contador, hazla con él: varias decisiones (qué cuentas usar, si vas a manejar centros de costo) son contables, no técnicas.

## 1. Activa el módulo

- [ ] [Activa el módulo **Contabilidad**](../primeros-pasos/activar-modulos.md) en <span class="ruta">Configuración › Módulos</span>. Sin esto, los documentos funcionan igual pero no generan asientos.

## 2. Plan de cuentas (PUC)

- [ ] [Carga las cuentas auxiliares por defecto](cuentas-auxiliares.md) en <span class="ruta">Contabilidad › Plan de Cuentas</span>. Es el paso que más tiempo ahorra: deja casi todas las cuentas de los pasos siguientes ya asignadas.
- [ ] Si tu contador ya maneja un plan de cuentas propio, crea las cuentas auxiliares que falten en vez de (o además de) las de por defecto.

## 3. Impuestos

- [ ] [Crea los impuestos](../impuestos/crear-impuesto.md) que vas a usar: IVA, retenciones (Retefuente, ReteIVA, ReteICA), INC, etc.
- [ ] [Crea un catálogo de impuestos](../impuestos/catalogo-impuestos.md) por cada combinación que uses (ej. *IVA 19%*, *Excluido*) y asígnale sus cuentas (base, impuesto, costo e inventario).
- [ ] Asigna el catálogo correspondiente a cada producto en <span class="ruta">Inventario › Productos</span>. Sin esto, las ventas y compras de ese producto no contabilizan impuestos ni costo.

## 4. Configuración contable inicial

- [ ] [Revisa y completa las cuentas](configuracion-contable.md) en <span class="ruta">Contabilidad › Configuración</span>: Cuentas a Pagar (compras), Anticipos de Clientes, Notas Crédito de Clientes, Saldos a favor de aliados de recaudo (Addi, Sistecrédito), Recargos por pago con datáfono y Anticipo a Proveedores.

## 5. Centros de costo (opcional)

- [ ] Si quieres ver la utilidad por área del negocio (ej. *Mostrador*, *Domicilios*), [crea tus centros de costo](../primeros-pasos/centros-de-costo.md). Si no, no hay que tocar nada: cada sede ya trae uno llamado **Principal**.

## 6. Cuentas que viven en otros módulos

Estas también contabilizan, pero se configuran donde se crea cada cosa, no en Contabilidad:

- [ ] **Cajas:** cuenta contable de cada caja en <span class="ruta">Tesorería › Caja › Cajas</span> › **Editar**.
- [ ] **Cuentas bancarias:** cuenta contable de cada cuenta en <span class="ruta">Tesorería › Bancos</span>, y si cobras 4x1000, la **Tarifa GMF** y su cuenta ([ver opción](../primeros-pasos/opciones-modulos.md#bancos)).
- [ ] **Medios de pago:** cuenta bancaria por sede para tarjeta y transferencia, en <span class="ruta">Ventas › Ajustes › Medios de Pago</span>.
- [ ] **Tipos de cliente:** si vendes a crédito, la **Cuenta por cobrar** de cada tipo en <span class="ruta">Ventas › Ajustes › Tipos de clientes</span> (ver [solución si falta](../soluciones-rapidas/ventas.md#al-validar-la-factura-a-credito-me-pide-configurar-la-cuenta-contable)).
- [ ] **Terceros:** retenciones (Retefuente, ReteIVA, ReteICA) que aplican a cada cliente o proveedor, en su ficha, sección **Retenciones**.

## 7. Prueba antes de abrir

- [ ] Crea una factura de venta de prueba y haz clic en **Ver asientos** antes de validarla: debe mostrar el asiento completo, sin avisos de cuenta faltante.
- [ ] Valídala y revisa <span class="ruta">Contabilidad › Balance de Prueba</span>: los débitos y créditos deben cuadrar.
- [ ] Repite la prueba con una compra si también vas a contabilizar proveedores.

## 8. Para cuando ya tengas historial

- [ ] Si vienes de otro sistema, carga los **saldos iniciales** de cartera en <span class="ruta">Tesorería › Cartera</span> (lo que te deben los clientes y lo que debes a proveedores).
- [ ] Cuando cierres un mes o un año, usa <span class="ruta">Contabilidad › Cierres contables</span> para que nadie modifique asientos de fechas ya cerradas.

## Si algo falla

| Problema | Solución |
|---|---|
| *El asiento contable no está balanceado* | Te falta un paso de esta lista. Usa **Ver asientos** en el documento: te dice qué línea no tiene cuenta. |
| No veo el módulo **Contabilidad** en el menú | No está incluido en tu plan, o no lo activaste en <span class="ruta">Configuración › Módulos</span>. |
| No encuentro una cuenta al configurar un catálogo o una caja | Revisa que ya cargaste las [cuentas auxiliares](cuentas-auxiliares.md) o crea la que falte. |
| Mi contador quiere revisar todo antes de abrir | Dale acceso con un rol que tenga los permisos de Contabilidad y Plan de Cuentas (ver [roles y permisos](../primeros-pasos/roles-y-permisos.md)). |

## Relacionados

- [¿Cómo funciona la contabilidad en Inventy?](como-funciona.md)
- [¿Cómo cargo y creo cuentas auxiliares?](cuentas-auxiliares.md)
- [¿Cómo hago la configuración contable inicial?](configuracion-contable.md)
- [¿Qué es y cómo creo un catálogo de impuestos?](../impuestos/catalogo-impuestos.md)
- [Recomendaciones para comenzar](../primeros-pasos/recomendaciones.md)
