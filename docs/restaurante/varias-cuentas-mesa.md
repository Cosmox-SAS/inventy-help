---
title: ¿Cómo activo varias cuentas en una misma mesa?
description: Pasos para permitir que cada cliente de una mesa tenga su propia cuenta y pague por separado.
estado: pendiente-validacion
tipo: rapida
modulo: restaurante
menu: Configuración › Módulos › Restaurante
permisos:
  - Editar configuración de restaurante
revisado: 2026-09-29
search:
  boost: 2
tags:
  - Restaurante
  - Mesas
---

# ¿Cómo activo varias cuentas en una misma mesa?

<p class="tambien-se-busca">También se busca como: varias cuentas por mesa, cuentas separadas, dividir la cuenta, separar cuenta, cada uno paga lo suyo, cuenta aparte, dos pedidos en la misma mesa, mesa ocupada, split.</p>

<span class="ruta">Configuración › Módulos › Restaurante</span>

## Pasos

**Activar (una sola vez)**

1. <span class="ruta">Configuración › Módulos</span> › **Restaurante**.
2. Activa **Habilitar pedidos a la mesa**.
3. Ahora aparece debajo **Permitir varias cuentas por mesa** › actívalo.

**Usarlo en el POS**

4. <span class="ruta">Ventas › POS</span> › tipo de pedido **A la mesa** › **Seleccionar mesa** › elige la mesa › agrega lo del primer cliente › **Realizar pedido**.
5. **Nuevo pedido** (pestaña **+**) › **A la mesa** › elige **la misma mesa** › agrega lo del segundo cliente › **Realizar pedido**.
6. Repite por cada cliente. Tip: usa **Renombrar pedido** para identificar cada cuenta (ej. *Mesa 4 — María*).
7. Cada cuenta se cobra por separado.

✅ Listo: la mesa queda con varias cuentas abiertas y cada cliente paga la suya.

!!! captura "CAPTURA PENDIENTE"
    Configuración de módulos › Restaurante con **Habilitar pedidos a la mesa** y **Permitir varias cuentas por mesa** activos.

## Si algo falla

| Problema | Solución |
|---|---|
| No me sale **Permitir varias cuentas por mesa** | Primero activa **Habilitar pedidos a la mesa**: la opción está oculta hasta entonces. |
| No me sale el módulo **Restaurante** en Módulos | No está en tu plan (aparece *Este módulo está bloqueado por tu suscripción*) o tu rol no tiene permiso de configuración de restaurante. |
| *La mesa seleccionada ya está ocupada por otro pedido…* | La opción **Permitir varias cuentas por mesa** está apagada. Actívala (pasos 1–3) y recarga el POS. |
| Activé la opción pero el POS sigue diciendo que la mesa está ocupada | Recarga la página del POS. |
| No aparece el tipo **A la mesa** | Falta activar **Habilitar pedidos a la mesa**. |
| *Sin mesas disponibles* | Crea las mesas en <span class="ruta">Restaurante › Mesas</span>. |
| Quiero dividir una cuenta que ya está abierta | [PENDIENTE DE VALIDACIÓN FUNCIONAL: si se pueden mover productos de un pedido a otro.] Por ahora, crea las cuentas separadas desde el inicio. |

## Relacionados

- [Restaurante](index.md)
- [¿Cómo manejo los domicilios?](domicilios.md)
- [¿Cómo activo o desactivo módulos?](../primeros-pasos/activar-modulos.md)
