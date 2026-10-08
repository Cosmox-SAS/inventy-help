---
title: "¿Cómo registro un celular con su IMEI?"
description: "Pasos para crear un celular que se controla por IMEI y registrar el IMEI de cada unidad por ajuste de inventario o desde el formulario del producto."
estado: pendiente-validacion
tipo: rapida
modulo: productos-inventario
menu: "Inventario › Productos"
permisos:
  - Crear productos
  - Crear ajustes de inventario
  - Editar productos
revisado: 2026-10-05
tags:
  - Inventario
  - Seriales
---

# ¿Cómo registro un celular con su IMEI?

<p class="tambien-se-busca">También se busca como: IMEI, serial, número de serie, celulares, equipos, IMEI1, IMEI2, controlar celulares por IMEI.</p>

**Antes de empezar:** activa **Seriales** en <span class="ruta">Configuración › Módulos › Inventario</span>.

## Pasos

**Crear el celular**

**Paso 1.** Ingresa a <span class="ruta">Inventario › Productos</span>, haz clic en **Nuevo Producto** y completa sus datos ([¿Cómo creo un producto?](crear-producto.md)).

![Paso 1: datos del celular](../assets/capturas/productos-inventario/registrar-imei/paso-1.png)

**Paso 2.** En **Comportamiento del producto**, activa **Rastrear seriales** y haz clic en **Crear Producto**.

![Paso 2: opción Rastrear seriales](../assets/capturas/productos-inventario/registrar-imei/paso-2.png)

**Opción A: registrar los IMEI con un ajuste de inventario**

**Paso 3.** Ingresa a <span class="ruta">Inventario › Ajuste de inventario</span>, haz clic en **Nuevo ajuste**, busca el celular y escribe la **cantidad** y el **costo**. En la línea aparece **0 / 2 seriales**.

![Paso 3: línea del celular en el ajuste](../assets/capturas/productos-inventario/registrar-imei/paso-3.png)

**Paso 4.** Haz clic en **0 / 2 seriales**. En **Captura de seriales**, escribe el **Tipo** (**IMEI1**, **IMEI2** o **SERIAL**) y el **Valor**, y presiona Enter. Agrega todos los identificadores del equipo y haz clic en **Guardar equipo y continuar con el siguiente**. Repite con cada celular.

![Paso 4: ventana Captura de seriales](../assets/capturas/productos-inventario/registrar-imei/paso-4.png)

**Paso 5.** Cuando la línea diga **2 / 2 seriales**, haz clic en **Confirmar ajuste**.

![Paso 5: seriales completos y botón Confirmar ajuste](../assets/capturas/productos-inventario/registrar-imei/paso-5.png)

**Opción B: el celular ya tiene existencias (desde el formulario del producto)**

**Paso 6.** En <span class="ruta">Inventario › Productos</span>, edita el celular y activa **Rastrear seriales**. Aparece **Registro de series por sede**.

![Paso 6: registro de series por sede](../assets/capturas/productos-inventario/registrar-imei/paso-6.png)

**Paso 7.** Haz clic en **Registrar** en cada sede, captura el IMEI de cada unidad como en el paso 4 y haz clic en **Actualizar Producto**.

![Paso 7: captura de IMEI de las unidades en existencia](../assets/capturas/productos-inventario/registrar-imei/paso-7.png)

✅ **Listo:** cada celular queda identificado por su IMEI. Al vender o devolver, Inventy te pide elegir el equipo exacto.

!!! tip "También al comprar"
    En la factura de compra, las líneas de celulares con **Rastrear seriales** también piden capturar el IMEI de cada unidad que entra.

## Si algo falla

| Problema | Solución |
|---|---|
| No aparece **Rastrear seriales**. | Activa **Seriales** en <span class="ruta">Configuración › Módulos › Inventario</span>. |
| No me deja activar **Rastrear seriales** al crear el producto. | Solo se activa con stock en cero. Si ya tiene existencias, usa la Opción B. |
| *Escribe el tipo y el valor del identificador.* | Completa **Tipo** y **Valor** antes de presionar Enter. |
| *Agrega al menos un identificador para este equipo.* | Cada celular necesita al menos un IMEI o serial. |
| No me deja confirmar el ajuste. | La cantidad de seriales debe ser igual a la cantidad de la línea. |

## Relacionados

- [¿Cómo creo un producto?](crear-producto.md)
- [¿Cómo hago un ajuste de inventario?](ajuste-inventario.md)
