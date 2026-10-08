---
title: "Todas las opciones de Configuración › Módulos (y por qué no me aparece una)"
description: Lista de cada opción de configuración de Inventy, qué hace y qué debe estar activo para que aparezca.
estado: pendiente-validacion
tipo: referencia
modulo: primeros-pasos
menu: Configuración › Módulos
permisos: []
revisado: 2026-09-29
search:
  boost: 2
tags:
  - Configuración
  - Módulos
---

# Todas las opciones de Configuración › Módulos

<p class="tambien-se-busca">También se busca como: no me aparece la opción, dónde se activa, configuración, ajustes, activar opción, habilitar función, no sale, opción oculta.</p>

<span class="ruta">Configuración › Módulos</span> › elige el módulo a la izquierda › activa la opción.

!!! tip "¿No te aparece una opción?"
    1. Mira la columna **Solo aparece si…**: algunas opciones se muestran solo después de activar otra.
    2. Si el módulo dice *Este módulo está bloqueado por tu suscripción*, no está en tu plan.
    3. Tu rol necesita el permiso de configuración de ese módulo.

## Ventas

| Opción | Qué hace | Solo aparece si… |
|---|---|---|
| **Permitir ventas de contado sin sesión de caja** | Vender en efectivo sin abrir caja. | — |
| **Permitir obsequios** | Marcar productos como obsequio en la venta. | — |
| **Habilitar promociones** | Muestra el menú Promociones. | — |
| **Habilitar listas de precios** | Precios especiales por cliente o caja. Ver [listas de precios](../ventas/listas-de-precios.md). | — |
| **Crédito ilimitado para clientes** | Todos los clientes compran a crédito sin cupo. | — |
| **Requerir autorización para cupo de crédito adicional** | Pide PIN de supervisor si la venta supera el cupo. | — |
| **Precios de venta sin impuestos incluidos** | El precio del producto se toma sin impuestos. | — |
| **Mostrar el PDF de la factura en el POS** | Abre el PDF en vez de imprimir tirilla. | — |
| **Habilitar remisiones de venta** | Entregar mercancía con remisión y facturar después. | — |
| **Exigir vendedor en el POS** | Obliga a elegir vendedor al cobrar. | — |
| **Descuento manual por producto en el POS** | Descuento de 0 % a 99 % por producto. | — |
| **Orden de pedido** | Registrar número y fecha de la orden del cliente. | — |
| **Descuentos financiados por proveedor** | Descuentos que asume el proveedor. | — |
| **Modo Proforma** | Emitir ventas como proforma. | — |

## Inventario

| Opción | Qué hace | Solo aparece si… |
|---|---|---|
| **Permitir stock negativo** | Vender o sacar sin existencias. | — |
| **Seriales** | Serial / IMEI por unidad. | — |
| **Lotes y vencimientos** | Lote y fecha de vencimiento. | — |
| **Presentaciones** | Empaques (caja, paquete) con código y precio. | — |
| **Kits de venta** | Productos que descuentan componentes. | — |
| **Atributos y variantes** | Talla, color, etc. | [Guía](../productos-inventario/variantes.md) |
| **Visibilidad por sede** | Restringir productos a ciertas sedes. | — |

## Productos

| Opción | Qué hace | Solo aparece si… |
|---|---|---|
| **Modelo**, **Fabricante**, **Peso** | Muestra esos campos en el producto. | — |

## Restaurante

| Opción | Qué hace | Solo aparece si… |
|---|---|---|
| **Mostrar desglose en la tirilla** | Subtotal, impuestos y retenciones en la tirilla. | — |
| **Mostrar total con propina en pedidos a mesa** | Suma la propina en el tablero de pedidos. | — |
| **Habilitar pedidos a la mesa** | Tipo de pedido **A la mesa**. | — |
| **Permitir varias cuentas por mesa** | Varias cuentas en la misma mesa. [Guía](../restaurante/varias-cuentas-mesa.md) | **Habilitar pedidos a la mesa** está activo |
| **Habilitar pedidos a domicilio** | Tipo de pedido **Domicilio**. [Guía](../restaurante/domicilios.md) | — |
| **Valor del domicilio obligatorio** | Exige costo de domicilio mayor que 0. | **Habilitar pedidos a domicilio** está activo |
| **Ítem de servicio de domicilio** | Servicio que se factura como domicilio. | **Habilitar pedidos a domicilio** está activo |
| **Pagar el domicilio al repartidor al instante** | Salida de caja automática al repartidor. | **Habilitar pedidos a domicilio** está activo |
| **Cuenta contable de gasto de domicilios** | Cuenta del gasto de domicilios. | Domicilios activo **y** módulo de Contabilidad |
| **Porcentaje de propina** | Propina sugerida (0 = sin propina). | — |
| **Texto de advertencia de propina (prefactura)** | Texto sobre la propina en la prefactura. | — |
| **Cuenta contable de propinas** | Cuenta de propinas recibidas. | Módulo de Contabilidad |

## Fiscal

| Opción | Qué hace | Solo aparece si… |
|---|---|---|
| **Emitir documento electrónico automáticamente** | Envía a la DIAN al validar facturas y notas. | — |

## Bancos

| Opción | Qué hace | Solo aparece si… |
|---|---|---|
| **Tarifa GMF (4x1000)** | Calcula el 4x1000. | — |
| **Cuenta contable del GMF (4x1000)** | Cuenta del gasto GMF. | Módulo de Contabilidad |

## Cartera

| Opción | Qué hace | Solo aparece si… |
|---|---|---|
| **Descuento máximo a clientes** | Descuento máximo permitido a clientes. | — |
| **Cuenta contable de descuentos a clientes** | Cuenta de esos descuentos. | Módulo de Contabilidad |
| **Descuento máximo a proveedores** | Descuento máximo permitido con proveedores. | — |
| **Cuenta contable de descuentos a proveedores** | Cuenta de esos descuentos. | Módulo de Contabilidad |

## Tienda web

| Opción | Qué hace | Solo aparece si… |
|---|---|---|
| **Habilitar tienda web** | Enciende la tienda en línea. | Tienda web incluida en el plan |
| **Sede de la tienda** | Sede que despacha los pedidos web. | — |
| **Recoger en tienda** | Permite recoger en tienda. | — |
| **Domicilio** | Permite pedidos web a domicilio. | — |
| **Costo de domicilio** | Valor del domicilio web. | **Domicilio** está activo |
| **Tema de la tienda**, **Portada de la tienda** | Apariencia de la tienda. | — |

## Relacionados

- [¿Cómo activo o desactivo módulos?](activar-modulos.md)
- [¿Por qué no veo un menú?](../soluciones-rapidas/usuarios.md#no-veo-un-menu-o-una-opcion)
