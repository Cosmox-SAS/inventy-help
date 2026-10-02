---
title: Preguntas frecuentes
description: Respuestas cortas a las dudas más comunes sobre Inventy, organizadas por tarea.
estado: pendiente-validacion
tipo: faq
modulo: soporte
revisado: 2026-09-29
tags:
  - Preguntas frecuentes
---

# Preguntas frecuentes

## Empezar

??? question "¿Cómo ingreso a Inventy?"
    Con tu correo y contraseña en la pantalla **Inicia sesión**. Ver [¿Cómo ingreso?](primeros-pasos/ingresar.md).

??? question "¿Cómo recupero mi contraseña?"
    En **Inicia sesión**, haz clic en **¿Olvidaste tu contraseña?** y sigue el enlace que llega a tu correo. Ver [guía](primeros-pasos/recuperar-contrasena.md).

??? question "¿Por dónde empiezo a configurar mi empresa?"
    Sigue la lista de [Recomendaciones para comenzar](primeros-pasos/recomendaciones.md).

??? question "¿Dónde está «Ajustes» en Ventas? (o cualquier ruta del manual)"
    Las rutas como <span class="ruta">Ventas › Ajustes › Tipos de clientes</span> se leen: ícono **Ventas** de la barra izquierda → título de sección **AJUSTES** en su menú → opción **Tipos de clientes**. En Ventas, *Ajustes* tiene **Vendedores**, **Tipos de clientes**, **Medios de Pago** y **Listas de precios**. Atajo: <kbd>Ctrl</kbd> + <kbd>K</kbd> y escribe el nombre. Ver [Conociendo la pantalla principal](primeros-pasos/pantalla-principal.md#como-leer-las-rutas-del-manual).

??? question "¿Puedo usar Inventy desde el celular?"
    Sí. Inventy funciona en el navegador del celular o la tableta. Los vendedores y repartidores de **Distribución** usan además la app móvil. [PENDIENTE DE VALIDACIÓN FUNCIONAL: pantallas optimizadas para celular.]

## Vender

??? question "¿Cómo hago una factura?"
    Para ventas rápidas, usa el [POS](pos/vender-en-pos.md). Para ventas de oficina o a crédito, usa [Ventas › Facturas](ventas/crear-factura-venta.md).

??? question "Al validar una venta a crédito me pide configurar una cuenta contable"
    Al cliente le falta el **Tipo de cliente**, o su tipo no tiene **Cuenta por cobrar**. Arréglalo en el cliente (**Editar › Datos del rol de cliente › Tipo de cliente**) o en <span class="ruta">Ventas › Ajustes › Tipos de clientes</span> (elige la **Cuenta por cobrar**). Luego abre la factura con **Editar** y valídala desde ahí para que tome la cuenta. Ver [la solución paso a paso](soluciones-rapidas/ventas.md#al-validar-la-factura-a-credito-me-pide-configurar-la-cuenta-contable).

??? question "¿Puedo editar una factura después de validarla?"
    No. Una factura validada no se edita: se corrige con una [devolución](ventas/devolucion-venta.md). Por eso, antes de validar, Inventy te pide confirmar.

??? question "¿Puedo tener varias ventas abiertas al tiempo en el POS?"
    Sí. Usa **Nuevo pedido** para abrir otra venta en una pestaña aparte.

??? question "¿Cómo le doy descuento a un producto en el POS?"
    Usa **Editar descuento** en la línea del carrito. Si no aparece, el administrador debe activar **Descuento manual por producto en el POS** en <span class="ruta">Configuración › Módulos › Ventas</span>.

??? question "¿Cómo le doy un precio especial a un cliente?"
    Con una **lista de precios**: actívala en <span class="ruta">Configuración › Módulos › Ventas</span>, créala, ponle precio a los productos (pestaña **Precios** del producto) y asígnala en la ficha del cliente. Ver [¿Cómo manejo las listas de precios?](ventas/listas-de-precios.md).

??? question "¿Qué precio cobra Inventy si el cliente tiene lista de precios?"
    El de la **lista del cliente** para ese producto y tu sede; si no tiene, en el POS el de la **lista de la caja**; si tampoco, el **precio base**. Si el cajero eligió una lista en la venta, manda esa. El descuento del tipo de cliente se aplica encima.

## Caja

??? question "¿Cómo cierro la caja?"
    Desde el POS con **Cerrar caja**: escribe el **Efectivo contado**, decide el destino del dinero y confirma. Ver [¿Cómo cierro la caja?](pos/cierre-de-caja.md).

??? question "¿Un cajero puede usar la caja principal?"
    Sí. Las cajas no se asignan a personas: cualquier usuario puede abrir cualquier caja **de su sede**, si está **libre** (nadie más la tiene abierta) y él no tiene otra caja abierta. Para vender necesita el permiso **Acceder al POS**. Solo vende en la caja que **él mismo** abrió, y solo quien la abrió puede cerrarla. El permiso **Usar caja de otro usuario** solo sirve para registrar ingresos y egresos en efectivo (Tesorería) sobre la caja abierta de otra persona de la misma sede; no sirve para vender en el POS. Ver [¿Cómo abro la caja?](pos/abrir-caja.md).

??? question "Cerré la caja con un valor equivocado, ¿qué hago?"
    Un supervisor puede usar **Corregir arqueo** o **Reabrir cierre** en <span class="ruta">Tesorería › Caja › Sesiones</span>.

## Inventario

??? question "¿Cómo puedo saber cuánto inventario tengo?"
    En <span class="ruta">Inventario › Stock</span>. Ver [¿Cuánto inventario tengo?](productos-inventario/consultar-existencias.md).

??? question "¿Cómo cargo el inventario inicial?"
    Con un [ajuste de inventario](productos-inventario/ajuste-inventario.md) de entrada. Si son muchos productos, usa **Importar ajuste**.

??? question "¿Cómo paso mercancía de una sede a otra?"
    Con un traslado: se **solicita**, lo **aprueba** la sede de origen y lo **recibe** la sede de destino. Ver [¿Cómo hago un traslado entre sedes?](productos-inventario/traslados.md).

??? question "¿Puedo vender si no tengo existencias?"
    Solo si el administrador activó **Permitir stock negativo** en <span class="ruta">Configuración › Módulos › Inventario</span>. Con esa opción activa, el POS también deja agregar productos, presentaciones y variantes sin existencias.

## Utilidad y reportes

??? question "¿Por qué la utilidad me sale en cero?"
    En **Inicio**, *Utilidad del mes* = ventas sin impuestos − costo de ventas − gastos, contando solo documentos **Validados** o **Pagados** con **fecha de emisión** en el mes. Sale en cero cuando:

    - No hay facturas de venta validadas o pagadas en el mes (solo borradores o anuladas), por ejemplo al inicio del mes.
    - Las facturas tienen fecha de emisión de otro mes.
    - Las ventas, el costo y los gastos se compensan exactamente (raro).

    En **Ventas › Reportes › Rentabilidad por ítem**, la utilidad de un producto es 0 cuando se devolvió completo en el período o cuando se vendió al mismo valor de su costo.

    Ojo: si los productos **no tienen costo** (costo inicial en 0 o *No maneja inventario*), la utilidad **no** sale en cero: sale igual a la venta, es decir, inflada. Revisa el costo de tus productos.

## Facturación electrónica

??? question "¿Cómo sé si la DIAN aceptó mi factura?"
    En <span class="ruta">Fiscal › Documentos</span>. Si dice **Aceptado** o **Aceptado con observaciones**, es válida. Ver [estados](facturacion-electronica/estados-documento.md).

??? question "Mi factura fue rechazada, ¿la hago de nuevo?"
    **No.** Revisa **Ver error**, corrige la causa y usa **Reenviar documento electrónico**. Ver [guía](facturacion-electronica/documento-rechazado.md).

??? question "¿Cómo genero un documento soporte?"
    Se genera desde la **factura de compra** de un proveedor marcado como **No obligado a facturar**. Ver [¿Cómo emito un documento soporte electrónico?](facturacion-electronica/documento-soporte.md).

??? question "¿Cómo le reenvío la factura al cliente?"
    En <span class="ruta">Fiscal › Documentos</span>, usa **Enviar email**.

## Usuarios

??? question "¿Cómo creo un usuario?"
    En <span class="ruta">Configuración › Usuarios</span>, con **Invitar usuario** o **Nuevo usuario**. Ver [guía](primeros-pasos/crear-usuarios.md).

??? question "¿Por qué no veo un menú que mi compañero sí ve?"
    Depende del plan, de los módulos activos y de los permisos de tu rol. Ver [solución](soluciones-rapidas/usuarios.md#no-veo-un-menu-o-una-opcion).

## Conceptos

??? question "¿Qué es el catálogo de impuestos?"
    Un paquete de impuestos que se asigna a cada producto: qué se cobra al venderlo y qué se paga al comprarlo. Ver [guía](impuestos/catalogo-impuestos.md).

??? question "¿Cómo se aplican las retenciones?"
    Se configuran en la ficha del cliente o proveedor (Retefuente, Reteiva, Reteica) y Inventy las calcula solo en cada factura. Ver [guía](impuestos/retenciones.md).

??? question "¿Qué es una compensación de cuentas?"
    Cruzar lo que un tercero te debe como **cliente** contra lo que le debes como **proveedor**, sin mover dinero. Se hace en <span class="ruta">Tesorería › Compensación de cuentas</span>. Ver [¿Cómo hago una compensación de cuentas?](finanzas/compensacion-cuentas.md).

??? question "¿Cómo hago que un proveedor también sea cliente (o al revés)?"
    En <span class="ruta">Configuración › Contactos</span> abre el tercero y usa la pestaña **Rol Cliente** › **Asignar como Cliente** (o **Rol Proveedor**). Para venderle a crédito, ponle además el **Tipo de cliente** en <span class="ruta">Ventas › Clientes › Editar</span>. Ver [¿Para qué sirve el rol de cliente y cuál elijo?](ventas/rol-de-cliente.md).

??? question "¿Qué es un centro de costo?"
    Una etiqueta para separar en qué área del negocio entra o sale cada peso (ej. *Mostrador*, *Domicilios*). Cada sede trae uno llamado **Principal**; si no necesitas separar áreas, no tienes que tocar nada. Ver [¿Qué es un centro de costo y cómo lo uso?](primeros-pasos/centros-de-costo.md).

??? question "¿Qué es un anticipo?"
    Dinero pagado antes de la factura. Queda como saldo a favor y luego se aplica. Ver [guía](finanzas/anticipos.md).

??? question "No entiendo un término"
    Búscalo en el [Glosario](glosario.md).

## Soporte

??? question "¿Qué información envío a soporte?"
    Nombre de la empresa, tu correo, pantalla, número del documento, fecha y hora, y una captura del error. **Nunca tu contraseña.** Ver [Contactar a soporte](soporte.md).
