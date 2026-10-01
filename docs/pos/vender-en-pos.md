---
title: ¿Cómo vendo en el POS?
description: Pasos para hacer una venta en el punto de venta, de agregar productos a cobrar.
estado: pendiente-validacion
tipo: rapida
modulo: pos
menu: Ventas › POS
permisos:
  - Acceder al POS
revisado: 2026-09-30
search:
  boost: 2
tags:
  - POS
  - Ventas
---

# ¿Cómo vendo en el POS?

<p class="tambien-se-busca">También se busca como: hacer una venta, facturar en caja, cobrar, vender en mostrador, registrar venta, venta rápida, tirilla.</p>

**Antes de empezar:** la [caja debe estar abierta](abrir-caja.md).

## Pasos

**Paso 1.** Ingresa a <span class="ruta">Ventas › POS</span>.

![Paso 1: pantalla del POS](../assets/capturas/pos/vender-en-pos/paso-1.png)

**Paso 2.** Busca el producto en **Buscar producto…** (nombre o código) o escanea el código de barras.

![Paso 2: buscador de productos](../assets/capturas/pos/vender-en-pos/paso-2.png)

**Paso 3.** Haz clic en el producto para agregarlo al carrito. Repite con cada producto.

![Paso 3: producto agregado al carrito](../assets/capturas/pos/vender-en-pos/paso-3.png)

**Paso 4.** Para cambiar la cantidad, haz clic en la cantidad de la línea del carrito.

![Paso 4: cantidad de la línea](../assets/capturas/pos/vender-en-pos/paso-4.png)

**Paso 5.** Por defecto se vende a **Consumidor Final**. Para otro cliente, abre **Seleccionar cliente**, búscalo o usa **Crear cliente**.

![Paso 5: selección de cliente](../assets/capturas/pos/vender-en-pos/paso-5.png)

**Paso 6.** Haz clic en **Realizar venta** (o <kbd>Ctrl</kbd> + <kbd>Enter</kbd>).

![Paso 6: botón Realizar venta](../assets/capturas/pos/vender-en-pos/paso-6.png)

**Paso 7.** En **Cobrar venta**, elige el medio de pago y escribe el valor recibido. Si paga con varios medios, agrega cada uno. En tarjeta o transferencia, escribe la **Referencia**.

![Paso 7: ventana Cobrar venta](../assets/capturas/pos/vender-en-pos/paso-7.png)

**Paso 8.** Deja marcada **Generar factura electrónica** si corresponde y haz clic en **Confirmar cobro**. El botón muestra el **Cambio** a devolver.

![Paso 8: botón Confirmar cobro](../assets/capturas/pos/vender-en-pos/paso-8.png)

✅ **Listo:** aparece *“Venta registrada con éxito.”*, se imprime la tirilla (o se abre el PDF) y el carrito queda vacío.

## Si algo falla

| Problema | Solución |
|---|---|
| *Debes abrir una caja antes de registrar una venta.* | [Abre la caja](abrir-caja.md). |
| *La caja de la sesión abierta no tiene una cuenta contable configurada…* | En <span class="ruta">Tesorería › Caja › Cajas</span>, **Acciones › Editar** la caja y elige su **Cuenta contable**. |
| *Ya llegaste al monto máximo de la caja…* | Usa **Registrar consignación** en el POS. |
| *Necesitas asignar un cliente antes de facturar.* | Usa **Asignar cliente** (ventas a crédito requieren cliente). |
| *Selecciona un vendedor antes de facturar.* | Tu empresa exige vendedor: selecciónalo al cobrar. |
| *Stock insuficiente para …* | No hay existencias en tu sede. Revisa el [stock](../productos-inventario/consultar-existencias.md). |
| *El saldo a crédito supera el cupo disponible del cliente…* | Cobra una parte con otro medio, o un supervisor autoriza con su **PIN**. |
| *No hay medios de pago configurados…* | El administrador los crea en <span class="ruta">Ventas › Ajustes › Medios de Pago</span>. |
| *No se pudo abrir el PDF de la factura…* | Permite las ventanas emergentes para Inventy en el navegador. |
| No aparece **Editar descuento** | Se activa en <span class="ruta">Configuración › Módulos › Ventas › Descuento manual por producto en el POS</span>. |

## Relacionados

- [¿Cómo abro la caja?](abrir-caja.md)
- [¿Cómo cierro la caja?](cierre-de-caja.md)
- [¿Cómo emito una factura electrónica?](../facturacion-electronica/emitir-factura-electronica.md)
- [¿Qué es un anticipo y cómo se maneja?](../finanzas/anticipos.md)
