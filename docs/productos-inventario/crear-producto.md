---
title: ¿Cómo creo un producto?
description: Agrega un producto al catálogo con su precio, impuestos, unidad de medida y código de barras.
estado: pendiente-validacion
tipo: tutorial
modulo: productos-inventario
menu: Inventario › Catálogo › Productos
permisos:
  - Ver productos
  - Crear productos
revisado: 2026-09-29
tags:
  - Productos
  - Inventario
---

# ¿Cómo creo un producto?

<p class="tambien-se-busca">También se busca como: nuevo producto, agregar artículo, crear ítem, registrar mercancía, código de barras, precio de venta, referencia.</p>

## ¿Para qué sirve?

Para agregar a tu catálogo lo que vendes o compras. Con el producto creado podrás venderlo, comprarlo y controlar sus existencias.

## Antes de comenzar

- [ ] Que exista la **unidad de medida** (unidad, kilo, litro…).
- [ ] Si usas contabilidad: que exista el **catálogo de impuestos** que le corresponde (ej. IVA 19 %).
- [ ] Opcional: la **categoría**, el **código de barras** y una **foto**.
- [ ] Permisos: **Ver productos** y **Crear productos**.

## Paso a paso

**Paso 1.** Ingresa a <span class="ruta">Inventario › Productos</span> y haz clic en **Nuevo Producto**. Se abre **Crear producto**.

!!! captura "CAPTURA PENDIENTE"
    Formulario **Crear producto** con las secciones de datos básicos, Precio e impuestos e Ilustración del producto.

**Paso 2. Datos básicos.**

| Campo | Qué escribir | ¿Obligatorio? |
|---|---|---|
| Código de barras | Escanéalo o escríbelo. No puede repetirse. | No |
| **Nombre** | Como quieres que aparezca en facturas y en el POS. | **Sí** |
| Descripción | Descripción corta. | No |
| Categoría | Para agrupar y filtrar productos. | No |
| **Unidad de medida** | Cómo se vende: unidad, kilo, litro… | **Sí** |

**Paso 3. Precio e impuestos.**

| Campo | Qué escribir |
|---|---|
| **Precio de venta** | El texto del campo te indica si es **sin impuestos** (*“El impuesto se suma al momento de la venta.”*) o **con impuestos** (*“El impuesto ya está incluido en este valor.”*). Depende de la configuración de tu empresa. |
| Costo inicial | Cuánto te cuesta el producto. Sirve para calcular rentabilidad y valorizar el inventario. |
| **Catálogo de impuestos** | Los impuestos del producto (ej. IVA 19 %). Es **obligatorio si tu empresa usa contabilidad**. |

**Paso 4. (Opcional) Foto.** En **Ilustración del producto**, sube una imagen **PNG, JPG o WebP de hasta 8 MB**. Se verá en el POS.

**Paso 5. (Opcional) Comportamiento del producto.** Activa solo lo que necesites:

| Opción | Úsala cuando… |
|---|---|
| **Kit de venta** | Vendes varios productos como uno solo (ej. *combo*). Descuenta sus componentes. |
| **Producto de obsequio** | Se regala automáticamente en el POS, sin costo. |
| **Rastrear seriales** | Cada unidad tiene un serial o IMEI único. Solo se activa con stock en cero. |
| **Controlar por lote y vencimiento** | Manejas lotes con fecha de vencimiento (alimentos, medicamentos). |
| Presentaciones | Vendes en empaques con su propio código y precio (caja, blíster). Se configuran después de crear el producto. |
| **No maneja inventario** | Se compra y vende, pero **no** mueve existencias. |

Si tu empresa usa **Restaurante**, también debes elegir el **Tipo de producto** y, si aplica, la **Estación de preparación**.

**Paso 6. (Opcional) Información adicional:** modelo, fabricante y **Peso (kg)**.

**Paso 7.** Haz clic en **Crear Producto**.

## Resultado esperado

El producto aparece en <span class="ruta">Inventario › Productos</span> y ya puedes venderlo y comprarlo.

!!! info "El producto se crea sin existencias"
    Para que tenga stock, registra una [factura de compra](../compras/registrar-factura-compra.md) o un [ajuste de inventario](ajuste-inventario.md) de entrada.

!!! tip "¿Tienes muchos productos?"
    Usa **Importar productos** en la lista de productos para cargarlos desde un archivo.

## Problemas frecuentes

??? question "No me deja guardar el producto"
    Revisa los mensajes en rojo bajo cada campo. Los más comunes:

    - *“El nombre es requerido.”* → Escribe el nombre.
    - *“La unidad de medida es requerida.”* → Selecciona una unidad.
    - *“El código de barras ya existe en el sistema.”* → Otro producto ya usa ese código. Búscalo en la lista.
    - *“El tipo de producto es requerido.”* → Tu empresa usa Restaurante: elige el tipo.
    - Falta el **Catálogo de impuestos** → es obligatorio si usas contabilidad.

??? question "“La imagen no debe superar los 8MB.” / “La imagen no debe superar 4500x4500 píxeles.”"
    Reduce el tamaño de la imagen antes de subirla.

??? question "“La funcionalidad de lotes y vencimientos está deshabilitada.”"
    Lotes, seriales y presentaciones deben activarse primero en <span class="ruta">Configuración › Módulos › Inventario</span>.

??? question "“Debes registrar al menos un componente para el kit.”"
    Un kit necesita al menos un producto componente con su cantidad.

## ¿Necesitas ayuda?

[Contacta a soporte](../soporte.md) si no puedes crear productos después de revisar los mensajes. Envía una **captura del formulario** con el error visible.

## Artículos relacionados

- [¿Cuánto inventario tengo?](consultar-existencias.md)
- [¿Cómo hago un ajuste de inventario?](ajuste-inventario.md)
- [¿Cómo vendo en el POS?](../pos/vender-en-pos.md)
