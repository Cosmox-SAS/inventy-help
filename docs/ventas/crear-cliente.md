---
title: "¿Cómo creo un cliente?"
description: "Pasos para registrar un cliente con sus datos y condiciones de crédito."
estado: pendiente-validacion
tipo: rapida
modulo: ventas
menu: "Ventas › Clientes"
permisos:
  - Ver clientes
  - Crear clientes
revisado: 2026-09-30
tags:
  - Ventas
  - Clientes
---

# ¿Cómo creo un cliente?

<p class="tambien-se-busca">También se busca como: registrar cliente, nuevo cliente, agregar comprador, datos del cliente, NIT del cliente, cupo de crédito, RUT.</p>

**Antes de empezar:** ten el RUT del cliente en PDF o sus datos.

## Pasos

**Paso 1.** Ingresa a <span class="ruta">Ventas › Clientes</span> y haz clic en **Nuevo cliente**.

![Paso 1: botón Nuevo cliente](../assets/capturas/ventas/crear-cliente/paso-1.png)

**Paso 2.** (Recomendado) Adjunta el **RUT en PDF**: Inventy completa los datos solo. Revísalos.

![Paso 2: carga del RUT](../assets/capturas/ventas/crear-cliente/paso-2.png)

**Paso 3.** Completa **Tipo de documento**, **Número de documento** y el nombre o **Razón social**.

![Paso 3: identificación del cliente](../assets/capturas/ventas/crear-cliente/paso-3.png)

**Paso 4.** En **Información de contacto**, escribe el correo (para facturas electrónicas), teléfonos, **Sede** y dirección.

![Paso 4: información de contacto](../assets/capturas/ventas/crear-cliente/paso-4.png)

**Paso 5.** En **Datos del rol de cliente**, define **Límite de crédito** (0 = sin crédito), **Plazo de pago (días)**, vendedor, tipo de cliente y retención.

![Paso 5: condiciones comerciales](../assets/capturas/ventas/crear-cliente/paso-5.png)

**Paso 6.** Haz clic en **Guardar cliente**.

![Paso 6: botón Guardar cliente](../assets/capturas/ventas/crear-cliente/paso-6.png)

✅ **Listo:** el cliente ya se puede elegir en el POS y en las facturas.

## Si algo falla

| Problema | Solución |
|---|---|
| *Este número de documento ya está registrado para este tipo de identificación.* | El cliente ya existe: búscalo por documento. |
| *El número de identificación contiene caracteres no válidos.* | Escribe sin puntos, comas ni espacios. |
| *No pudimos leer el RUT…* | Escribe los datos a mano. |
| *Este cliente no tiene cupo de crédito disponible.* | Sube el **Límite de crédito** o vende de contado. |
| El cliente no debe recibir factura electrónica | Marca **No genera documentos electrónicos**. |

## Relacionados

- [¿Cómo hago una factura de venta?](crear-factura-venta.md)
- [¿Cómo se aplican las retenciones?](../impuestos/retenciones.md)
