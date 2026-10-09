---
title: Producción
description: Recetas y producciones para transformar insumos en producto terminado y calcular su costo.
estado: pendiente-validacion
tipo: indice
modulo: produccion
revisado: 2026-10-09
---

# Producción

<p class="tambien-se-busca">También se busca como: fabricar, transformar, elaborar, receta, fórmula, insumos, materia prima, producto terminado, orden de producción, lote, costo de producción, merma.</p>

El módulo **Producción** convierte **insumos** (materia prima, empaques) en un **producto terminado**. Al confirmar una producción, Inventy descuenta los insumos del inventario, suma el producto terminado y calcula su costo unitario. Requiere el módulo **Inventario**.

## ¿Qué hay en el menú Producción?

| Grupo | Opción | Para qué sirve |
|---|---|---|
| Operación | **Producciones** | Registrar, confirmar y anular producciones. Ver [guía](registrar-produccion.md). |
| | **Recetas** | Los insumos y cantidades de un lote estándar de cada producto. Ver [guía](crear-receta.md). |

## Cómo funciona

| Paso | Qué pasa en Inventy |
|---|---|
| **Receta** (opcional) | Define el producto terminado, la **Cantidad de un lote estándar**, la **Merma esperada (%)** y sus insumos. Cada producto tiene una sola receta. |
| **Borrador** | La producción se guarda con sus insumos y un costo estimado. El inventario **no** se mueve todavía. |
| **Confirmada** | Se declara la **Cantidad producida**. Salen los insumos y entra el producto terminado con su **Costo unitario** = costo total de insumos ÷ cantidad producida. |
| **Anulada** | Se devuelve todo: sale el producto terminado y vuelven a entrar los insumos. Solo se anulan producciones confirmadas. |

Si el módulo **Contabilidad** está activo, la producción genera su asiento al confirmarla y lo reversa al anularla. Puedes revisarlo antes con **Ver asientos**.

## Guías

| Guía | Estado |
|---|---|
| [¿Cómo creo una receta de producción?](crear-receta.md) | Disponible |
| [¿Cómo registro una producción?](registrar-produccion.md) | Disponible |
| ¿Qué pasa si no tengo insumos suficientes? (producción parcial) | Por redactar |
| ¿Cómo anulo una producción? | Por redactar |
