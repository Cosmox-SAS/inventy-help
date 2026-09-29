---
title: ¿Cómo agrego usuarios a mi empresa?
description: Crea usuarios directamente o invítalos por correo, y asígnales rol y sede.
estado: pendiente-validacion
tipo: tutorial
modulo: primeros-pasos
menu: Configuración › Usuarios
permisos:
  - Ver usuarios
  - Crear usuarios
revisado: 2026-09-29
tags:
  - Usuarios
  - Configuración
---

# ¿Cómo agrego usuarios a mi empresa?

<p class="tambien-se-busca">También se busca como: crear usuario, nuevo empleado en el sistema, dar acceso, invitar, agregar cajero, agregar vendedor.</p>

## ¿Para qué sirve?

Para que cada persona de tu equipo tenga su propio acceso a Inventy, con los permisos que le correspondan y en la sede donde trabaja.

**Hay dos formas:**

| Forma | Cuándo usarla |
|---|---|
| **Invitar usuario** (recomendada) | La persona recibe un correo y **ella misma** define su contraseña. Tú nunca conoces su clave. |
| **Nuevo usuario** | Creas el usuario y le asignas una contraseña tú mismo. Útil si la persona no tiene acceso a su correo en ese momento. |

## Antes de comenzar

- [ ] Que exista el **rol** que le vas a asignar. Ver [Roles y permisos](roles-y-permisos.md).
- [ ] Que exista la **sede** donde trabajará (<span class="ruta">Configuración › Sedes</span>).
- [ ] Revisa que tu plan tenga cupo de usuarios. Si no, verás *“Límite del plan alcanzado”*.

## Paso a paso

### Opción A: invitar por correo

**Paso 1.** Ingresa a <span class="ruta">Configuración › Usuarios</span> y haz clic en **Invitaciones**.

**Paso 2.** Haz clic en **Invitar usuario**.

**Paso 3.** Completa **Nombre**, **Correo electrónico**, **Rol** y **Sede**. Haz clic en **Enviar invitación**.

!!! captura "CAPTURA PENDIENTE"
    Ventana **Invitar usuario** con los cuatro campos obligatorios.

**Paso 4.** La persona recibe un correo, abre el enlace, completa su **Nombre completo** y su **contraseña**, y hace clic en **Unirme a la empresa**.

!!! tip "Si la persona ya usa Inventy en otra empresa"
    Conserva su contraseña actual. Al aceptar la invitación, solo debe escribirla para confirmar que la cuenta es suya.

### Opción B: crear el usuario directamente

**Paso 1.** Ingresa a <span class="ruta">Configuración › Usuarios</span> y haz clic en **Nuevo usuario**.

**Paso 2.** Completa los **Datos del usuario**:

| Campo | Qué escribir |
|---|---|
| **Nombre completo** | Nombre y apellido de la persona. |
| **Correo electrónico** | Correo con el que ingresará. |
| **Rol** | Qué podrá hacer en Inventy. |
| **Sede** | Dónde trabaja. |
| **Contraseña** y **Confirmar contraseña** | Mínimo 8 caracteres. |

**Paso 3.** Guarda el usuario y entrega la contraseña a la persona de forma privada. Pídele que la [cambie](pantalla-principal.md#tu-perfil) en su primer ingreso.

## Resultado esperado

El usuario aparece en la lista de **Usuarios** con su **Sede** y **Rol**. En la opción A, la invitación queda **pendiente** hasta que la persona la acepte.

## Problemas frecuentes

??? question "“Ya existe una invitación pendiente o un usuario con este correo.”"
    Esa persona ya fue invitada o ya es usuario de tu empresa. Búscala en la lista de Usuarios o en Invitaciones.

??? question "La persona dice que el enlace no funciona"
    Al abrir el enlace puede ver uno de estos mensajes:

    - *“Esta invitación venció”*: envíale una nueva.
    - *“Esta invitación fue revocada”*: alguien la canceló; envía otra si corresponde.
    - *“Esta invitación ya fue aceptada”*: ya tiene acceso; solo debe [iniciar sesión](ingresar.md).
    - *“No encontramos esta invitación”*: el enlace está incompleto; pídele que lo copie completo.

??? question "“Límite del plan alcanzado”"
    Tu plan no permite más usuarios. Revisa <span class="ruta">Configuración › Suscripción › Límites y consumo</span>.

## ¿Necesitas ayuda?

[Contacta a soporte](../soporte.md) si la invitación no llega después de revisar Spam. Indica el **correo invitado** y la **hora** en que la enviaste.

## Artículos relacionados

- [¿Cómo funcionan los roles y permisos?](roles-y-permisos.md)
- [Soluciones rápidas: usuarios y permisos](../soluciones-rapidas/usuarios.md)
