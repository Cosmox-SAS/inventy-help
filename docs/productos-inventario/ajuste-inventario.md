---
title: ¿Cómo hago un ajuste de inventario?
description: Registra entradas o salidas manuales de inventario por pérdidas, daños, sobrantes o saldo inicial.
estado: pendiente-validacion
tipo: tutorial
modulo: productos-inventario
menu: Inventario › Existencias › Ajuste de inventario
permisos:
  - Ver ajustes de inventario
  - Crear ajustes de inventario
revisado: 2026-09-29
tags:
  - Inventario
  - Ajustes
---

# ¿Cómo hago un ajuste de inventario?

<p class="tambien-se-busca">También se busca como: corregir inventario, entrada de inventario, salida de inventario, dar de baja, producto dañado, pérdida, faltante, sobrante, inventario inicial, cargar existencias.</p>

## ¿Para qué sirve?

Para corregir las existencias cuando no corresponden a una compra ni a una venta. Ejemplos:

- Cargar el **inventario inicial** cuando empiezas a usar Inventy.
- Registrar productos **dañados, vencidos o perdidos** (salida).
- Registrar un **sobrante** encontrado en la bodega (entrada).

## Antes de comenzar

- [ ] Los productos deben estar [creados](crear-producto.md).
- [ ] Permisos: **Ver ajustes de inventario** y **Crear ajustes de inventario**.

## Paso a paso

**Paso 1.** Ingresa a <span class="ruta">Inventario › Ajuste de inventario</span> y haz clic en **Nuevo ajuste**.

**Paso 2. Datos del ajuste.** Selecciona la **Sede** y describe el motivo general (ej. *“Inventario inicial”* o *“Productos vencidos de marzo”*).

!!! captura "CAPTURA PENDIENTE"
    Formulario de ajuste con Datos del ajuste y dos líneas (una de entrada y una de salida).

**Paso 3. Líneas del ajuste.** Haz clic en **Agregar linea** y, para cada producto:

1. Elige el **Tipo de ajuste**: entrada (aumenta) o salida (disminuye).
2. Busca el producto.
3. Escribe la cantidad.
4. Si quieres, agrega una nota a la línea.

**Paso 4.** Elige:

- **Guardar borrador**: lo guardas sin aplicarlo. Puedes seguir editándolo.
- **Confirmar ajuste**: aplica los cambios al inventario.

!!! warning "Revisa antes de confirmar"
    *“Al confirmar se aplicaran las entradas y salidas al inventario. Luego no podras editarlo ni eliminarlo.”*

!!! tip "¿Muchos productos? Importa el ajuste"
    Usa **Importar ajuste** para cargar las líneas desde un archivo. Es la forma más rápida de cargar el inventario inicial.

## Resultado esperado

El ajuste queda **Completado** y las existencias cambian en <span class="ruta">Inventario › Stock</span>. En **Movimientos** y **Kardex** verás el ajuste como origen del cambio.

## Problemas frecuentes

??? question "“Stock insuficiente…” al confirmar una salida"
    Estás sacando más unidades de las que hay en esa sede. Revisa la cantidad o la sede seleccionada. (Si tu empresa activó **Permitir stock negativo**, este mensaje no aparece.)

??? question "“El ajuste deja stock por debajo del reservado.”"
    Parte de ese stock está **reservado** (por ejemplo, para un pedido o traslado). Reduce la cantidad de salida o libera primero la reserva.

??? question "Me equivoqué en un ajuste ya confirmado"
    No se puede editar. Haz un **nuevo ajuste** en sentido contrario para corregirlo, o pide a un usuario con el permiso **Anular ajustes de inventario** que lo anule.

## ¿Necesitas ayuda?

[Contacta a soporte](../soporte.md) con el **código del ajuste**, la **sede** y el mensaje de error.

## Artículos relacionados

- [¿Cuánto inventario tengo?](consultar-existencias.md)
- [¿Cómo creo un producto?](crear-producto.md)
