---
title: ¿Cómo abro la caja?
description: Abre una sesión de caja con el monto base para empezar a vender en el POS.
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

# ¿Cómo abro la caja?

<p class="tambien-se-busca">También se busca como: apertura de caja, iniciar turno, abrir turno, base de caja, sencillo, abrir sesión de caja.</p>

## ¿Para qué sirve?

Abrir la caja registra **con cuánto efectivo empiezas el turno** (la *base*). Desde ese momento, todas las ventas en efectivo quedan asociadas a tu caja, y al final del día podrás [cerrarla](cierre-de-caja.md) y comparar lo que hay con lo que debería haber.

**Úsala cuando:** empiezas tu turno de trabajo en el POS.

## Antes de comenzar

- [ ] Que exista al menos una **caja** creada en <span class="ruta">Tesorería › Caja › Cajas</span>.
- [ ] Contar el **efectivo inicial** (la base) que dejas en el cajón.
- [ ] Permisos: **Acceder al POS** y **Ver cajas**.

## Paso a paso

**Paso 1.** Ingresa a <span class="ruta">Ventas › POS</span>. Si no tienes una caja abierta, Inventy te mostrará la ventana **Abrir caja**. También puedes abrirla con el botón **Abrir caja** de la barra superior del POS.

!!! captura "CAPTURA PENDIENTE"
    Ventana **Abrir caja** dentro del POS, con el selector de caja y el campo Monto base.

**Paso 2.** En el selector, elige tu caja (**Selecciona una caja**).

**Paso 3.** Escribe el **Monto base**: el efectivo con el que empiezas. Si empiezas sin efectivo, déjalo en **0**.

!!! info "Si el cierre anterior dejó dinero en la caja"
    Inventy propone automáticamente el **monto base del cierre anterior**. Verifica que coincida con el efectivo que realmente encuentras en el cajón.

**Paso 4.** Confirma la apertura.

### Otra forma: desde Tesorería

Un administrador también puede abrir una caja desde <span class="ruta">Tesorería › Caja › Cajas</span>, usando la acción **Abrir caja** de la caja correspondiente.

## Resultado esperado

- Aparece el mensaje **“Caja abierta exitosamente.”**
- Ya puedes [vender en el POS](vender-en-pos.md).
- En <span class="ruta">Tesorería › Caja › Sesiones</span> tu sesión aparece como **Abierta**.

## Problemas frecuentes

??? question "“No hay cajas disponibles para abrir en este momento.”"
    **Por qué pasa:** no hay cajas creadas, o todas ya están abiertas por otros usuarios.

    **Qué hacer:** si tienes permiso, usa el botón **Crear caja**. Si no, pide al administrador que cree una caja o que cierre una sesión que haya quedado abierta.

??? question "“No tienes permiso para abrir una caja.”"
    Tu rol no tiene permiso para abrir cajas. Pídeselo al administrador.

??? question "“Debes abrir una caja antes de registrar una venta.”"
    Intentaste vender sin caja abierta. Abre la caja siguiendo esta guía. Si tu empresa vende sin caja, el administrador puede activar **Permitir ventas de contado sin sesión de caja** en <span class="ruta">Configuración › Módulos › Ventas</span>.

## ¿Necesitas ayuda?

[Contacta a soporte](../soporte.md) si la caja aparece abierta por otra persona y nadie puede cerrarla. Indica el **nombre de la caja**, la **sede** y el **usuario** que la abrió.

## Artículos relacionados

- [¿Cómo vendo en el POS?](vender-en-pos.md)
- [¿Cómo cierro la caja?](cierre-de-caja.md)
- [Soluciones rápidas: POS y caja](../soluciones-rapidas/pos-caja.md)
