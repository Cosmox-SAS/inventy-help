---
title: "Soluciones rápidas: usuarios y permisos"
description: No veo un menú, no tengo permiso, límite de usuarios del plan.
estado: pendiente-validacion
tipo: solucion
modulo: administracion
revisado: 2026-09-29
tags:
  - Usuarios
  - Permisos
  - Soluciones rápidas
---

# Soluciones rápidas: usuarios y permisos

## "No veo un menú o una opción" { #no-veo-un-menu-o-una-opcion }

**PROBLEMA:** un compañero ve una opción que yo no veo, o una guía menciona un menú que no aparece.

**CAUSA:** en Inventy una opción aparece solo si se cumplen **las tres** condiciones:

1. El **módulo está incluido en el plan** de tu empresa.
2. El **módulo u opción está activado** en <span class="ruta">Configuración › Módulos</span> (por ejemplo, Promociones, Listas de precios, Lotes, Seriales, Remisiones, Domicilios).
3. Tu **rol tiene el permiso** para verla.

**SOLUCIÓN:**

1. Usa la búsqueda del menú (<kbd>Ctrl</kbd> + <kbd>K</kbd>) por si la opción está en otro lugar.
2. Pide al administrador que revise las tres condiciones.
3. Después del cambio, **recarga la página**.

**ESCALAR A SOPORTE:** si el administrador revisó las tres condiciones y la opción sigue sin aparecer.

**INFORMACIÓN PARA SOPORTE:** correo del usuario, nombre del rol, opción que busca.

## "Me dice que no tengo permiso"

**PROBLEMA:** aparecen mensajes como *“No tienes permiso para…”* o una página de acceso denegado.

**CAUSA:** tu rol no incluye ese permiso.

**SOLUCIÓN:** pide al administrador que agregue el permiso a tu rol en <span class="ruta">Configuración › Roles y Permisos › Gestionar permisos</span>. Ver [roles y permisos](../primeros-pasos/roles-y-permisos.md).

**ESCALAR A SOPORTE:** si el administrador no encuentra el permiso adecuado.

**INFORMACIÓN PARA SOPORTE:** acción que intentabas hacer, pantalla, captura del mensaje.

## "No puedo crear más usuarios"

**PROBLEMA:** aparece *“Límite del plan alcanzado”*.

**CAUSA:** tu plan tiene un número máximo de usuarios.

**SOLUCIÓN:** revisa <span class="ruta">Configuración › Suscripción › Límites y consumo</span>. Puedes cambiar a un plan con más usuarios. [PENDIENTE DE VALIDACIÓN FUNCIONAL: si se pueden desactivar usuarios para liberar cupo.]

**ESCALAR A SOPORTE:** si el consumo mostrado no coincide con tus usuarios reales.

**INFORMACIÓN PARA SOPORTE:** plan actual, cantidad de usuarios activos.

## "El módulo aparece bloqueado"

**PROBLEMA:** en Módulos aparece *“Este módulo está bloqueado por tu suscripción”*.

**CAUSA:** tu plan no incluye ese módulo.

**SOLUCIÓN:** usa **Mejorar plan** o revisa <span class="ruta">Configuración › Suscripción</span>.

**ESCALAR A SOPORTE:** si crees que tu plan sí debería incluirlo.

**INFORMACIÓN PARA SOPORTE:** plan contratado, módulo que necesitas.
