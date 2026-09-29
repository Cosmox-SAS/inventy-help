---
title: ¿Cómo creo un cliente?
description: Registra un cliente con sus datos de identificación, contacto y condiciones de crédito.
estado: pendiente-validacion
tipo: tutorial
modulo: ventas
menu: Ventas › Clientes
permisos:
  - Ver clientes
  - Crear clientes
revisado: 2026-09-29
tags:
  - Ventas
  - Clientes
---

# ¿Cómo creo un cliente?

<p class="tambien-se-busca">También se busca como: registrar cliente, nuevo cliente, agregar comprador, datos del cliente, NIT del cliente, cupo de crédito, RUT.</p>

## ¿Para qué sirve?

Para guardar los datos de las personas o empresas a las que vendes. Un cliente bien registrado permite emitir **facturas electrónicas sin rechazos**, venderle a **crédito** y consultar su **cartera**.

## Antes de comenzar

- [ ] Ten a mano el **RUT** del cliente (PDF) o sus datos: tipo y número de documento, nombre o razón social, correo, teléfono y dirección.
- [ ] Permisos: **Ver clientes** y **Crear clientes**.

## Paso a paso

**Paso 1.** Ingresa a <span class="ruta">Ventas › Clientes</span> y crea un **Nuevo cliente**.

**Paso 2. (Recomendado) Sube el RUT.** Adjunta el RUT del cliente en **PDF**. Inventy lo lee y **completa los datos automáticamente**. Verás *“Datos cargados. Revisa la información antes de guardar.”*

!!! warning "Revisa siempre lo que se completó"
    La lectura automática puede equivocarse. Compara los datos con el RUT antes de guardar. Si aparece *“No pudimos leer el RUT…”*, escribe los datos a mano.

!!! captura "CAPTURA PENDIENTE"
    Formulario **Nuevo cliente** con la zona para adjuntar el RUT resaltada.

**Paso 3. Identificación.** Completa:

| Campo | Qué escribir |
|---|---|
| **Tipo de documento** | Cédula, NIT, etc. |
| **Número de documento** | Sin puntos ni espacios. Máximo 20 caracteres. |
| Nombres y apellidos | Si es una persona. |
| **Razón social** | Si es una empresa (ej. *Distribuidora Norte S.A.S*). |
| Nombre comercial | Nombre con el que opera, si es distinto. |

**Paso 4. Información de contacto.** Correo electrónico, **¿Recibir documentos electrónicos al correo?**, teléfonos, **Sede**, dirección y **Responsabilidad tributaria**.

!!! tip "Correo para facturas electrónicas"
    La factura electrónica le llega al cliente al correo que registres aquí. Verifícalo con él.

**Paso 5. Datos del rol de cliente** (condiciones comerciales):

| Campo | Qué significa |
|---|---|
| **Límite de crédito** | Cupo máximo que te puede deber. **0 = sin crédito.** |
| **Plazo de pago (días)** | Días para pagar sus facturas a crédito. Vacío = configuración por defecto. |
| Habilitar descuentos por pronto pago | Si aplica a tu negocio. |
| Lista de precios | Precios especiales para este cliente (si usas listas de precios). |
| Vendedor responsable | Vendedor que atiende al cliente. |
| Tipo de cliente | Clasificación (mayorista, minorista…). Puede tener descuento propio. |
| Calcular retención en la fuente por | Si el cliente te practica retención: por línea o por **Total de factura**. |

**Paso 6.** Si este cliente **no debe recibir factura electrónica**, marca **No genera documentos electrónicos**: *“Las ventas a este cliente no se emiten ante la DIAN.”*

**Paso 7.** Haz clic en **Guardar cliente**.

## Resultado esperado

El cliente aparece en <span class="ruta">Ventas › Clientes</span> y ya puedes seleccionarlo en el POS y en las facturas.

!!! tip "Crear clientes desde el POS"
    En el POS también puedes crear un cliente desde **Seleccionar cliente › Crear cliente**, sin salir de la venta.

## Problemas frecuentes

??? question "“Este número de documento ya está registrado para este tipo de identificación.”"
    El cliente ya existe. Búscalo en la lista de clientes por su número de documento.

??? question "“El número de identificación contiene caracteres no válidos.”"
    Escribe solo números (y letras si el tipo de documento lo permite), sin puntos, comas ni espacios.

??? question "“El correo electrónico no es válido.”"
    Revisa que tenga el formato `nombre@dominio.com` y no tenga espacios.

??? question "“Este cliente no tiene cupo de crédito disponible.”"
    Su **Límite de crédito** es 0 o ya está usado. Edita el cliente para aumentar el cupo o cobra de contado.

## ¿Necesitas ayuda?

[Contacta a soporte](../soporte.md) si las facturas electrónicas de un cliente son rechazadas por sus datos. Envía el **número de documento del cliente** y el **número de la factura** rechazada.

## Artículos relacionados

- [¿Cómo hago una factura de venta?](crear-factura-venta.md)
- [¿Cómo vendo en el POS?](../pos/vender-en-pos.md)
- [¿Qué hago si un documento es rechazado?](../facturacion-electronica/documento-rechazado.md)
