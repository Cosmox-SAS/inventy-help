---
title: "Glosario: ¿qué es…?"
description: Qué significa cada término de Inventy, en dos líneas, y dónde se maneja.
estado: pendiente-validacion
tipo: referencia
modulo: soporte
revisado: 2026-09-29
search:
  boost: 1.5
tags:
  - Glosario
---

# Glosario: ¿qué es…?

<p class="tambien-se-busca">También se busca como: qué significa, definición, qué es, para qué sirve, concepto.</p>

Cada término: **qué es** · **dónde está en Inventy** · guía.

## A

### Ajuste de inventario { #ajuste-de-inventario }
Entrada o salida manual de unidades (pérdidas, daños, sobrantes, inventario inicial). · <span class="ruta">Inventario › Ajuste de inventario</span> · [Guía](productos-inventario/ajuste-inventario.md)

### Anticipo { #anticipo }
Dinero pagado **antes** de la factura. Del cliente queda como **saldo a favor**; al proveedor, como saldo a tu favor. · <span class="ruta">Tesorería › Ingresos / Egresos</span> · [Guía](finanzas/anticipos.md)

### Anular { #anular }
Cancelar un documento validado dejando registro del motivo. No se puede deshacer. No todas las facturas se pueden anular (ver [factura de venta](ventas/crear-factura-venta.md)).

### Arqueo { #arqueo }
Contar el efectivo de la caja al cerrarla y compararlo con lo esperado. · <span class="ruta">Ventas › POS › Cerrar caja</span> · [Guía](pos/cierre-de-caja.md)

### Atributos y variantes { #atributos-y-variantes }
Atributos = características (talla, color). Variantes = cada combinación (camiseta roja talla M), que se maneja como producto propio. Se activa en <span class="ruta">Configuración › Módulos › Inventario</span>.

## B

### Base gravable { #base-gravable }
Valor sobre el que se calcula un impuesto o retención (normalmente, el subtotal sin impuestos).

### Base mínima { #base-minima }
Valor desde el cual se aplica un impuesto o retención. Si la base es menor, no se aplica. Se define al [crear el impuesto](impuestos/crear-impuesto.md).

### Borrador { #borrador }
Documento guardado pero no confirmado. **No afecta** inventario, cartera ni contabilidad. Se puede editar o eliminar.

## C

### Caja { #caja }
Cajón de dinero físico del punto de venta. Se crea una vez y se **abre** y **cierra** en cada turno. · <span class="ruta">Tesorería › Caja › Cajas</span> · [Abrir](pos/abrir-caja.md) · [Cerrar](pos/cierre-de-caja.md)

### Cartera { #cartera }
Lo que te deben los clientes (cuentas por cobrar) y lo que debes a proveedores (cuentas por pagar). · <span class="ruta">Tesorería › Cartera</span>

### Catálogo de impuestos { #catalogo-de-impuestos }
Paquete de impuestos que se asigna a un producto: qué se cobra al venderlo y qué se paga al comprarlo. · <span class="ruta">Fiscal › Catálogo de Impuestos</span> · [Guía](impuestos/catalogo-impuestos.md)

### Centro de costo { #centro-de-costo }
Etiqueta para saber a qué área o negocio pertenece cada venta, compra o gasto (ej. *Tienda centro*, *Mayorista*). Lo piden facturas, ingresos, egresos y cajas. · <span class="ruta">Configuración › Centros de Costo</span>

### Clonar { #clonar }
Crear un documento nuevo en borrador copiando otro (facturas, traslados, productos). Ahorra digitar de nuevo.

### Compensación de cuentas { #compensacion-de-cuentas }
Cruzar lo que te debe un tercero con lo que le debes, sin mover dinero. · <span class="ruta">Tesorería › Compensación de cuentas</span>

### Consignación { #consignacion }
Llevar efectivo de la caja al banco. Se hace al cerrar caja o desde el POS (**Registrar consignación**). · <span class="ruta">Tesorería › Consignaciones</span>

### Consumidor Final { #consumidor-final }
Cliente genérico para ventas sin identificar al comprador. Es el cliente por defecto del POS si la caja no tiene otro.

### Conteo físico { #conteo-fisico }
Contar el inventario real y compararlo con el sistema para corregir diferencias. · <span class="ruta">Inventario › Conteo físico</span>

### Crédito (cupo de crédito) { #credito }
Vender para que el cliente pague después. El **Límite de crédito** del cliente es el máximo que te puede deber. · Ficha del cliente · [Guía](ventas/crear-cliente.md)

### Cuenta auxiliar { #cuenta-auxiliar }
Último nivel del plan de cuentas (subcuenta + 3 dígitos). Es donde se registran los movimientos. · <span class="ruta">Contabilidad › Plan de Cuentas</span> · [Guía](contabilidad/cuentas-auxiliares.md)

### CUFE / CUDE { #cufe-cude }
Código único que la DIAN asigna a una factura electrónica (CUFE) o a otros documentos como notas crédito (CUDE). Sirve para verificarlos. · <span class="ruta">Fiscal › Documentos</span>

## D

### Despacho { #despacho }
Grupo de facturas que se entregan en un vehículo con un repartidor. · <span class="ruta">Distribución › Despachos</span>

### Devolución { #devolucion }
Mercancía que regresa: del cliente a ti (venta) o de ti al proveedor (compra). Reingresa o saca inventario y ajusta la cartera. · [Guía de venta](ventas/devolucion-venta.md)

### Documento equivalente POS { #documento-equivalente-pos }
Documento electrónico que reemplaza la tirilla del POS ante la DIAN. · <span class="ruta">Fiscal › Documentos</span>

### Documento soporte { #documento-soporte }
Documento electrónico que **tú** generas cuando le compras a un proveedor **no obligado a facturar**. · [Guía](facturacion-electronica/documento-soporte.md)

### Domicilio { #domicilio }
Pedido del restaurante que se entrega en la dirección del cliente, con un costo de domicilio. · <span class="ruta">Ventas › POS › Domicilio</span> · [Guía](restaurante/domicilios.md)

## E

### Egreso { #egreso }
Pago que haces a un proveedor (o anticipo a proveedor). · <span class="ruta">Tesorería › Egresos</span> · [Guía](finanzas/registrar-egreso.md)

### Emisión automática { #emision-automatica }
Opción para que las facturas y notas se envíen solas a la DIAN al validarlas. · <span class="ruta">Configuración › Módulos › Fiscal</span>

### Estación de preparación { #estacion-de-preparacion }
Lugar del restaurante donde se prepara un producto (cocina, bar). La comanda llega ahí. · <span class="ruta">Restaurante › Estaciones de preparación</span>

## F

### Factura recurrente { #factura-recurrente }
Plantilla de factura que se repite cada cierto tiempo (ej. mensualidad). Estados: Activa, Pausada, Finalizada. · <span class="ruta">Ventas › Facturas recurrentes</span>

## I

### Impuesto { #impuesto }
Valor que se suma al precio y se paga al Estado (IVA, INC, ICA). · [Guía](impuestos/crear-impuesto.md)

### Ingreso { #ingreso }
Pago que recibes de un cliente: recaudo de facturas o anticipo. · <span class="ruta">Tesorería › Ingresos</span> · [Guía](finanzas/registrar-ingreso.md)

## K

### Kardex { #kardex }
Historial de entradas, salidas y saldo de un producto, con costos. Sirve para saber por qué cambió el stock. · <span class="ruta">Inventario › Kardex</span>

### Kit { #kit }
Producto que se vende como una línea pero descuenta varios componentes (ej. combo). Se marca en el producto (**Kit de venta**).

## L

### Legalización de gastos { #legalizacion-de-gastos }
Registrar juntas varias facturas de gastos pagadas con un mismo dinero (ej. caja menor). · <span class="ruta">Compras › Legalización de gastos</span>

### Lista de precios { #lista-de-precios }
Precios especiales para ciertos clientes o sedes. Orden: lista del cliente → lista de la sede → precio base. Se activa en <span class="ruta">Configuración › Módulos › Ventas</span>.

### Lote { #lote }
Grupo de unidades con la misma fecha de vencimiento. Se activa en Módulos › Inventario y en el producto (**Controlar por lote y vencimiento**).

### Liquidación de domicilios { #liquidacion-de-domicilios }
Pago al repartidor de la suma de los costos de domicilio de sus pedidos en un rango de fechas. · <span class="ruta">Restaurante › Domicilios › Liquidación</span> · [Guía](restaurante/domicilios.md)

## M

### Medio de pago { #medio-de-pago }
Forma en que se paga: efectivo, transferencia, tarjeta, crédito o anticipo de cliente. · <span class="ruta">Ventas › Ajustes › Medios de Pago</span>

### Módulo { #modulo }
Parte de Inventy que se activa según el plan (Restaurante, Contabilidad, Nómina…). · <span class="ruta">Configuración › Módulos</span> · [Guía](primeros-pasos/activar-modulos.md)

### Monto base { #monto-base }
Efectivo con el que se abre la caja (el “sencillo”). · [Guía](pos/abrir-caja.md)

## N

### No obligado a facturar { #no-obligado-a-facturar }
Proveedor que no expide factura. Sus compras generan **documento soporte**. Se marca en la ficha del proveedor.

### Nota crédito { #nota-credito }
Documento electrónico que corrige o anula total o parcialmente una factura de venta. En Inventy nace de una **devolución de venta**.

## O

### Obsequio { #obsequio }
Producto que se entrega gratis en una venta. Requiere permiso **Autorizar obsequios en venta**. Una venta no puede ser solo de obsequios.

### Orden de compra { #orden-de-compra }
Pedido al proveedor antes de recibir la mercancía. Luego se convierte en factura de compra. · <span class="ruta">Compras › Órdenes de Compra</span>

## P

### Permiso / Rol { #permiso-rol }
Permiso = una acción permitida. Rol = conjunto de permisos que se asigna a usuarios. · [Guía](primeros-pasos/roles-y-permisos.md)

### PIN de autorización { #pin-de-autorizacion }
Clave corta del supervisor para aprobar operaciones especiales (ej. venta a crédito por encima del cupo). Se define en el perfil.

### Plan de cuentas (PUC) { #plan-de-cuentas }
Lista de cuentas contables de la empresa. · <span class="ruta">Contabilidad › Plan de Cuentas</span>

### Presentación { #presentacion }
Empaque de un producto con su propio código y precio (caja × 12, blíster). Se activa en Módulos › Inventario.

### Preventa { #preventa }
Pedido que toma un vendedor en ruta (app móvil) y la oficina luego factura. · <span class="ruta">Distribución › Preventas</span>

### Proforma (modo) { #proforma }
Opción para emitir las ventas como proforma, con consecutivo propio y sin datos de la empresa. Inventario, cartera y contabilidad funcionan igual. · <span class="ruta">Configuración › Módulos › Ventas</span>

### Promoción { #promocion }
Descuento o beneficio automático sobre ciertos productos. · <span class="ruta">Ventas › Ajustes › Promociones</span>

## R

### Recaudo { #recaudo }
Cobro de facturas a crédito. Se registra como **Ingreso** tipo *Recaudo de cartera*. · [Guía](finanzas/registrar-ingreso.md)

### Remisión { #remision }
Documento para entregar mercancía **antes** de facturarla. Luego se factura en una o varias facturas. Se activa en Módulos › Ventas.

### Repartidor { #repartidor }
Domiciliario que entrega pedidos. Se crea a partir de un proveedor (tercero). · <span class="ruta">Restaurante › Repartidores</span> · [Guía](restaurante/domicilios.md)

### Resolución { #resolucion }
Autorización de la DIAN con el prefijo y rango de números para documentos electrónicos. · <span class="ruta">Fiscal › Resoluciones</span> · [Guía](facturacion-electronica/resoluciones.md)

### Retención (Retefuente, ReteIVA, ReteICA) { #retencion }
Parte del pago que se retiene para pagarla a la DIAN o al municipio. Retefuente (renta), ReteIVA (sobre el IVA), ReteICA (industria y comercio). · [Guía](impuestos/retenciones.md)

## S

### Sede { #sede }
Cada local, tienda o bodega de la empresa. El inventario se controla por sede. · <span class="ruta">Configuración › Sedes</span>

### Serial { #serial }
Identificador único de cada unidad (IMEI, número de serie). Se activa en Módulos › Inventario y en el producto.

### Sesión de caja { #sesion-de-caja }
El turno de una caja: desde que se abre hasta que se cierra. · <span class="ruta">Tesorería › Caja › Sesiones</span>

### Stock negativo { #stock-negativo }
Permitir vender o sacar productos sin existencias. Se activa en <span class="ruta">Configuración › Módulos › Inventario</span>.

### Stock reservado { #stock-reservado }
Unidades apartadas (por un traslado aprobado o un pedido) que no se pueden vender. · [Traslados](productos-inventario/traslados.md)

## T

### Tipo de cliente { #tipo-de-cliente }
Clasificación de clientes (mayorista, minorista…) que puede tener un descuento propio. · <span class="ruta">Ventas › Ajustes › Tipos de clientes</span>

### Traslado { #traslado }
Mover mercancía de una sede a otra: solicitar → aprobar → recibir. · [Guía](productos-inventario/traslados.md)

## V

### Varias cuentas por mesa { #varias-cuentas-por-mesa }
Que cada cliente de una mesa tenga su propia cuenta y pague por separado. Solo aparece tras activar **Habilitar pedidos a la mesa**. · <span class="ruta">Configuración › Módulos › Restaurante</span> · [Guía](restaurante/varias-cuentas-mesa.md)

### Validar { #validar }
Confirmar un documento. Desde ese momento afecta inventario, cartera y contabilidad, y **ya no se puede editar**.

### Vendedor { #vendedor }
Persona a la que se le asignan ventas y clientes. En Distribución, debe estar asociado a un usuario para usar la app móvil. · <span class="ruta">Ventas › Ajustes › Vendedores</span>
