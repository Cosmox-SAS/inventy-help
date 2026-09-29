---
title: ¿Cómo funcionan los roles y permisos?
description: Crea roles como Cajero o Contador y decide qué puede hacer cada uno.
estado: pendiente-validacion
tipo: tutorial
modulo: primeros-pasos
menu: Configuración › Roles y Permisos
permisos:
  - Gestionar permisos
revisado: 2026-09-29
tags:
  - Usuarios
  - Permisos
---

# ¿Cómo funcionan los roles y permisos?

<p class="tambien-se-busca">También se busca como: perfiles, accesos, restringir, bloquear opción, dar permiso, rol de cajero, rol de vendedor.</p>

## ¿Para qué sirve?

Un **rol** es un conjunto de **permisos**. En lugar de dar permisos persona por persona, creas roles como *Cajero*, *Bodega* o *Contador* y se los asignas a los usuarios.

Ejemplo: el rol *Cajero* puede usar el POS y abrir y cerrar caja, pero no ver la contabilidad.

## Antes de comenzar

- [ ] Tener el permiso **Gestionar permisos** (normalmente, rol Administrador).
- [ ] Tener claro qué tareas hace cada cargo en tu empresa.

## Paso a paso

### Crear un rol

**Paso 1.** Ingresa a <span class="ruta">Configuración › Roles y Permisos</span>.

**Paso 2.** Haz clic en **Nuevo rol**. Se abre **Crear Nuevo Rol**.

**Paso 3.** Escribe el nombre del rol (por ejemplo, *Supervisor* u *Operador*).

**Paso 4.** Usa **Buscar permisos...** para encontrar y marcar los permisos que necesita. Están agrupados por módulo.

!!! captura "CAPTURA PENDIENTE"
    Ventana **Crear Nuevo Rol** con permisos agrupados por módulo y algunos marcados.

**Paso 5.** Haz clic en **Crear Rol**.

### Cambiar los permisos de un rol

**Paso 1.** En la lista de roles, abre las acciones del rol.

**Paso 2.** Elige **Gestionar permisos** para marcar o desmarcar permisos, o **Editar nombre** para renombrarlo.

**Paso 3.** Guarda los cambios.

## Resultado esperado

El rol aparece en la lista con la cantidad de **Usuarios con rol** y **Permisos asignados**. Los usuarios con ese rol ven los cambios al recargar la página.

## Recomendaciones

- Da a cada rol **solo lo que necesita**. Es más fácil agregar un permiso después que corregir un error.
- Cuidado con permisos de **eliminar**, **anular** y **reabrir cierre de caja**: dáselos solo a personas de confianza.
- Para vendedores y repartidores que usan la **app móvil**, pide a soporte la lista de permisos recomendados.

## Problemas frecuentes

??? question "“El nombre del rol es obligatorio.” / “Todavía no seleccionaste permisos.”"
    Para crear un rol debes escribir un nombre **y** marcar al menos un permiso.

??? question "Di el permiso pero el usuario sigue sin ver el menú"
    1. Revisa que el **módulo** esté activo en <span class="ruta">Configuración › Módulos</span>.
    2. Pide al usuario que **recargue la página** o cierre sesión y vuelva a entrar.
    3. Revisa que el usuario tenga asignado **ese** rol en <span class="ruta">Configuración › Usuarios</span>.

## ¿Necesitas ayuda?

[Contacta a soporte](../soporte.md) si no encuentras un permiso para una tarea. Indica el **nombre del rol** y **qué debe poder hacer** el usuario.

## Artículos relacionados

- [¿Cómo agrego usuarios a mi empresa?](crear-usuarios.md)
- [Soluciones rápidas: usuarios y permisos](../soluciones-rapidas/usuarios.md)
