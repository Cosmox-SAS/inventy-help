---
title: "¿Cómo activo varias cuentas en una misma mesa?"
description: "Pasos para que cada cliente de una mesa tenga su propia cuenta."
estado: pendiente-validacion
tipo: rapida
modulo: restaurante
menu: "Configuración › Módulos › Restaurante"
permisos:
  - Editar configuración de restaurante
revisado: 2026-09-30
search:
  boost: 2
tags:
  - Restaurante
  - Mesas
---

# ¿Cómo activo varias cuentas en una misma mesa?

<p class="tambien-se-busca">También se busca como: varias cuentas por mesa, cuentas separadas, dividir la cuenta, separar cuenta, cada uno paga lo suyo, cuenta aparte, dos pedidos en la misma mesa, mesa ocupada, split.</p>

## Pasos

**Paso 1.** Ingresa a <span class="ruta">Configuración › Módulos</span> y selecciona **Restaurante**.

![Paso 1: módulo Restaurante en Configuración](../assets/capturas/restaurante/varias-cuentas-mesa/paso-1.webp)

**Paso 2.** Activa **Habilitar pedidos a la mesa**.

![Paso 2: opción Habilitar pedidos a la mesa](../assets/capturas/restaurante/varias-cuentas-mesa/paso-2.webp)

**Paso 3.** Debajo aparece **Permitir varias cuentas por mesa**: actívala.

![Paso 3: opción Permitir varias cuentas por mesa](../assets/capturas/restaurante/varias-cuentas-mesa/paso-3.webp)

**Paso 4.** En el POS, elige **A la mesa**, **Seleccionar mesa**, agrega lo del primer cliente y haz clic en **Realizar pedido**.

![Paso 4: pedido a la mesa en el POS](../assets/capturas/restaurante/varias-cuentas-mesa/paso-4.webp)

**Paso 5.** Haz clic en **Nuevo pedido** (**+**), elige **A la mesa** y **la misma mesa**, agrega lo del segundo cliente y **Realizar pedido**. Repite por cada cliente.

![Paso 5: botón Nuevo pedido](../assets/capturas/restaurante/varias-cuentas-mesa/paso-5.webp)

✅ **Listo:** la mesa queda con varias cuentas y cada cliente paga la suya. Usa **Renombrar pedido** para identificarlas (ej. *Mesa 4 — María*).

## Si algo falla

| Problema | Solución |
|---|---|
| No sale **Permitir varias cuentas por mesa** | Primero activa **Habilitar pedidos a la mesa**. |
| *La mesa seleccionada ya está ocupada por otro pedido…* | La opción está apagada. Actívala y recarga el POS. |
| No aparece el módulo Restaurante | No está en tu plan o tu rol no tiene permiso. |
| *Sin mesas disponibles* | Crea las mesas en <span class="ruta">Restaurante › Mesas</span>. |
| Dividir una cuenta ya abierta | [PENDIENTE DE VALIDACIÓN FUNCIONAL: si se pueden mover productos entre pedidos.] Crea las cuentas separadas desde el inicio. |

## Relacionados

- [¿Cómo manejo los domicilios?](domicilios.md)
- [Todas las opciones de Módulos](../primeros-pasos/opciones-modulos.md)
