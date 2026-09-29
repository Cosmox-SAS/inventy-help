---
title: ¿Cómo vendo en el POS?
description: Registra una venta en el punto de venta, cobra con uno o varios medios de pago y entrega el comprobante.
estado: pendiente-validacion
tipo: tutorial
modulo: pos
menu: Ventas › POS
permisos:
  - Acceder al POS
revisado: 2026-09-29
tags:
  - POS
  - Ventas
---

# ¿Cómo vendo en el POS?

<p class="tambien-se-busca">También se busca como: hacer una venta, facturar en caja, cobrar, vender en mostrador, registrar venta, venta rápida, tirilla.</p>

## ¿Para qué sirve?

Para registrar ventas de mostrador de forma rápida: agregas los productos, eliges el cliente, cobras y Inventy genera la factura, descuenta el inventario y registra el dinero en tu caja.

## Antes de comenzar

- [ ] Tener la [caja abierta](abrir-caja.md) (salvo que tu empresa permita vender sin caja).
- [ ] Que los productos estén [creados](../productos-inventario/crear-producto.md) y tengan precio.
- [ ] Que existan **Medios de Pago** configurados.
- [ ] Permiso: **Acceder al POS**.

## Paso a paso

**Paso 1.** Ingresa a <span class="ruta">Ventas › POS</span>. Se abre la pantalla **Punto de venta**.

!!! captura "CAPTURA PENDIENTE"
    Pantalla completa del POS: buscador de productos, categorías, tarjetas de productos y el carrito a la derecha.

**Paso 2. Agrega productos.** Tienes tres formas:

- Escribe en **Buscar producto…** el nombre o el código y selecciona el producto.
- **Escanea el código de barras** con el lector.
- Filtra por **categoría** y haz clic en la tarjeta del producto.

Cada clic agrega una unidad al carrito.

**Paso 3. Ajusta el carrito** (si hace falta):

- **Cantidad:** haz clic en la cantidad del producto para cambiarla.
- **Nota:** agrega indicaciones para el producto (ej. *sin cebolla*).
- **Descuento:** usa **Editar descuento** para aplicar un porcentaje. Esta opción solo aparece si el administrador activó **Descuento manual por producto en el POS**.
- **Quitar:** elimina un producto del carrito, o usa **Limpiar venta** para empezar de nuevo.

**Paso 4. Elige el cliente.** Por defecto la venta se hace a **Consumidor Final** (o al cliente por defecto de la caja). Para cambiarlo, abre **Seleccionar cliente**, búscalo por nombre o identificación, o usa **Crear cliente**.

!!! tip "¿Varias ventas al tiempo?"
    Con el botón **Nuevo pedido** abres otra venta en una pestaña aparte, sin perder la que tienes en curso.

**Paso 5.** Haz clic en **Realizar venta** (o presiona <kbd>Ctrl</kbd> + <kbd>Enter</kbd>). Se abre la ventana **Cobrar venta**.

**Paso 6. Registra el pago.**

1. Revisa el **Total a pagar**.
2. Selecciona el **medio de pago** (efectivo, tarjeta, transferencia…) y escribe el monto recibido.
3. Si el cliente paga con **varios medios**, agrega cada uno con su monto hasta cubrir el total.
4. Para pagos con tarjeta o transferencia, escribe la **Referencia** (número de voucher o autorización).
5. Si tu empresa lo exige, selecciona el **vendedor**.
6. Marca o desmarca **Generar factura electrónica** según corresponda.

!!! captura "CAPTURA PENDIENTE"
    Ventana **Cobrar venta** con dos medios de pago y el botón **Confirmar cobro** mostrando el cambio.

**Paso 7.** Haz clic en **Confirmar cobro**. Si el cliente pagó de más en efectivo, el botón te muestra el **Cambio** que debes devolver.

## Resultado esperado

- Aparece el mensaje **“Venta registrada con éxito.”**
- Se imprime la **tirilla**, o se abre el **PDF de la factura** si tu empresa lo configuró así.
- El carrito queda vacío y listo para la siguiente venta.
- Si marcaste factura electrónica, puedes ver su estado en <span class="ruta">Fiscal › Documentos</span>.

## Ventas a crédito

Si el cliente pagará después, elige el medio de pago de tipo **Crédito** (cada empresa le pone su nombre en <span class="ruta">Ventas › Ajustes › Medios de Pago</span>) e indica el **Plazo (días)** o la **Fecha de vencimiento**.

- Si la venta supera el **cupo de crédito** del cliente, verás: *“El saldo a crédito supera el cupo disponible del cliente…”*. Cobra una parte con otro medio o reduce el valor a crédito.
- Si tu empresa exige autorización, un supervisor puede aprobar el cupo extra escribiendo su **PIN** en **Autorización de supervisor**.

## Problemas frecuentes

??? question "“Debes abrir una caja antes de registrar una venta.”"
    [Abre la caja](abrir-caja.md) y vuelve a intentarlo.

??? question "“Ya llegaste al monto máximo de la caja. Debes consignar para continuar vendiendo.”"
    Tu caja tiene más efectivo del máximo permitido. Registra una **consignación** desde el POS (**Registrar consignación**) o pide a tu supervisor que lo haga.

??? question "“Necesitas asignar un cliente antes de facturar.”"
    Esta venta requiere un cliente identificado (por ejemplo, venta a crédito). Usa **Asignar cliente**.

??? question "“Selecciona un vendedor antes de facturar.”"
    Tu empresa exige vendedor en el POS. Selecciónalo en la ventana de cobro.

??? question "“Stock insuficiente para …: disponible X, requerido Y.”"
    No hay existencias suficientes del producto en tu sede. Revisa el [stock](../productos-inventario/consultar-existencias.md) o pide a bodega un ajuste o traslado.

??? question "“No hay medios de pago configurados…”"
    El administrador debe crearlos en <span class="ruta">Ventas › Ajustes › Medios de Pago</span>.

??? question "“No se pudo abrir el PDF de la factura. Permite las ventanas emergentes para este sitio.”"
    Tu navegador bloqueó la ventana del PDF. Permite las ventanas emergentes para Inventy en la configuración del navegador.

??? question "“Una venta de solo obsequios no está permitida.”"
    Agrega al menos un producto que no sea obsequio.

## ¿Necesitas ayuda?

[Contacta a soporte](../soporte.md) si una venta se cobró pero no aparece en <span class="ruta">Ventas › Facturas</span>. Envía la **hora** de la venta, el **nombre de la caja**, el **total** y una foto de la tirilla si la tienes.

## Artículos relacionados

- [¿Cómo abro la caja?](abrir-caja.md)
- [¿Cómo cierro la caja?](cierre-de-caja.md)
- [¿Cómo registro una devolución de venta?](../ventas/devolucion-venta.md)
- [¿Cómo emito una factura electrónica?](../facturacion-electronica/emitir-factura-electronica.md)
