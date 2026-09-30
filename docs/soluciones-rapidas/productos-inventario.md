---
title: "Soluciones rápidas: productos e inventario"
description: No me deja guardar un producto, stock insuficiente, el inventario no cuadra.
estado: pendiente-validacion
tipo: solucion
modulo: productos-inventario
revisado: 2026-09-29
tags:
  - Productos
  - Inventario
  - Soluciones rápidas
---

# Soluciones rápidas: productos e inventario

## "¿Por qué no me deja guardar un producto?"

**PROBLEMA:** al hacer clic en **Crear Producto** aparecen mensajes en rojo.

**CAUSA:** falta un dato obligatorio o hay un dato repetido. Los más comunes: *“El nombre es requerido.”*, *“La unidad de medida es requerida.”*, *“El código de barras ya existe en el sistema.”*, catálogo de impuestos vacío (obligatorio si usas contabilidad).

**SOLUCIÓN:** revisa cada mensaje en rojo. Ver [¿Cómo creo un producto?](../productos-inventario/crear-producto.md#si-algo-falla).

**ESCALAR A SOPORTE:** si no aparece ningún mensaje y el producto no se guarda.

**INFORMACIÓN PARA SOPORTE:** captura del formulario completo.

## "Dice stock insuficiente"

**PROBLEMA:** al vender, trasladar o ajustar aparece *“Stock insuficiente para «Producto»: disponible X, requerido Y.”*

**CAUSA:** no hay existencias suficientes del producto **en esa sede**.

**SOLUCIÓN:**

1. Revisa el [stock](../productos-inventario/consultar-existencias.md) del producto en la sede.
2. Si la mercancía sí está físicamente, registra la compra pendiente o un [ajuste de entrada](../productos-inventario/ajuste-inventario.md).
3. Si está en otra sede, haz un [traslado](../productos-inventario/traslados.md).
4. Si tu negocio necesita vender sin existencias, el administrador puede activar **Permitir stock negativo** en <span class="ruta">Configuración › Módulos › Inventario</span>. Úsalo con precaución.

**ESCALAR A SOPORTE:** si el stock mostrado no se explica con los movimientos del **Kardex**.

**INFORMACIÓN PARA SOPORTE:** producto, sede, cantidad esperada y cantidad mostrada.

## "El inventario de Inventy no coincide con la bodega"

**PROBLEMA:** las existencias del sistema son diferentes a las reales.

**CAUSA:** compras o ventas sin registrar, ajustes pendientes en borrador, traslados sin recibir, errores de conteo.

**SOLUCIÓN:**

1. Revisa el **Kardex** del producto.
2. Revisa si hay **ajustes en borrador** o [traslados](../productos-inventario/traslados.md) **aprobados sin recibir** (el menú Traslados muestra un contador).
3. Haz un **Conteo físico** o un [ajuste de inventario](../productos-inventario/ajuste-inventario.md).

**ESCALAR A SOPORTE:** si hay movimientos que nadie reconoce.

**INFORMACIÓN PARA SOPORTE:** producto, sede, fechas aproximadas.

## "No puedo aprobar o recibir un traslado"

**PROBLEMA:** no aparecen los botones **Aprobar** o **Recibir** en un traslado.

**CAUSA:** para aprobar hay que estar asignado a la **sede de origen**, tener el permiso y **no** ser quien lo solicitó. Para recibir hay que estar en la **sede de destino** con permiso, o ser quien lo solicitó.

**SOLUCIÓN:** revisa la sede asignada al usuario en <span class="ruta">Configuración › Usuarios</span> y los permisos de su rol. Ver [¿Cómo hago un traslado entre sedes?](../productos-inventario/traslados.md#si-algo-falla).

**ESCALAR A SOPORTE:** si todo está bien configurado y los botones no aparecen.

**INFORMACIÓN PARA SOPORTE:** código del traslado, sedes de origen y destino, correo del usuario.

## "No puedo activar lotes, seriales o presentaciones en un producto"

**PROBLEMA:** aparece *“La funcionalidad de … está deshabilitada.”*

**CAUSA:** la función no está activa para tu empresa.

**SOLUCIÓN:** el administrador debe activarla en <span class="ruta">Configuración › Módulos › Inventario</span>. Para **seriales**, el producto además debe tener stock en cero.

**ESCALAR A SOPORTE:** si la opción no aparece en Módulos.

**INFORMACIÓN PARA SOPORTE:** función que necesitas y plan actual.
