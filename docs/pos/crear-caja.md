---
title: "¿Cómo creo una caja?"
description: "Pasos para crear una caja registradora antes de abrirla en el POS."
estado: pendiente-validacion
tipo: rapida
modulo: pos
menu: "Tesorería › Caja › Cajas"
permisos:
  - Ver cajas
  - Crear caja
revisado: 2026-09-30
tags:
  - POS
  - Caja
  - Tesorería
---

# ¿Cómo creo una caja?

<p class="tambien-se-busca">También se busca como: crear caja, nueva caja, caja registradora, agregar caja, caja menor, caja principal, configurar caja.</p>

**Antes de empezar:** debe existir un **centro de costo** (Inventy trae *Principal* por defecto).

## Pasos

**Paso 1.** Ingresa a <span class="ruta">Tesorería › Caja › Cajas</span> y haz clic en **Nueva caja**.

![Paso 1: botón Nueva caja](../assets/capturas/pos/crear-caja/paso-1.png)

**Paso 2.** Escribe el **Nombre** de la caja (ej. *Caja Mostrador*).

![Paso 2: campo Nombre](../assets/capturas/pos/crear-caja/paso-2.png)

**Paso 3.** Elige el **Centro de costo**.

![Paso 3: campo Centro de costo](../assets/capturas/pos/crear-caja/paso-3.png)

**Paso 4.** Elige la **Cuenta contable** del efectivo (ej. *Caja general*). **Es obligatoria si tu empresa usa Contabilidad**: sin ella, el POS no deja cobrar. Si quieres, elige también el **Cliente por defecto** (vacío = Consumidor Final) y el **Monto máximo en caja**.

![Paso 4: campos opcionales de la caja](../assets/capturas/pos/crear-caja/paso-4.png)

**Paso 5.** Haz clic en **Crear caja**.

![Paso 5: botón Crear caja](../assets/capturas/pos/crear-caja/paso-5.png)

**Paso 6.** La caja aparece en la lista como **Cerrada**, lista para [abrirla en el POS](abrir-caja.md).

![Paso 6: caja creada en la lista](../assets/capturas/pos/crear-caja/paso-6.png)

✅ **Listo:** ya puedes [abrir la caja](abrir-caja.md) y empezar a vender.

## Si algo falla

| Problema | Solución |
|---|---|
| *No tienes permiso para crear una caja.* | Pide el permiso **Crear caja** al administrador. |
| No hay centros de costo | Créalo en <span class="ruta">Configuración › Centros de Costo</span>. |
| El POS me pide consignar a cada rato | El **Monto máximo en caja** es muy bajo. Súbelo o déjalo en 0 (sin límite). |
| *La caja de la sesión abierta no tiene una cuenta contable configurada…* | Edita la caja (**Acciones › Editar**) y elige su **Cuenta contable**. Se puede hacer con la caja abierta. |

## Relacionados

- [¿Cómo abro la caja?](abrir-caja.md)
- [¿Cómo vendo en el POS?](vender-en-pos.md)
- [¿Cómo manejo las listas de precios?](../ventas/listas-de-precios.md)
