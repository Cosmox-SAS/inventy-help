---
title: "¿Cómo calculo y pago las comisiones de los vendedores?"
description: "Pasos para sacar las ventas de cada vendedor y pagarle su comisión en la nómina."
estado: pendiente-validacion
tipo: rapida
modulo: recursos-humanos
menu: "Ventas › Reportes › Rentabilidad por ítem"
permisos:
  - Ver reporte de rentabilidad por ítem
  - Gestionar nómina (parámetros, períodos, novedades)
revisado: 2026-10-14
tags:
  - Nómina
  - Ventas
---

# ¿Cómo calculo y pago las comisiones de los vendedores?

<p class="tambien-se-busca">También se busca como: comisión de ventas, comisiones de vendedores, liquidar comisiones, ventas por vendedor, pagar comisión en nómina.</p>

**Antes de empezar:** Inventy no calcula la comisión por ti. Cada venta guarda el vendedor que la hizo; con eso sacas lo que vendió cada uno y registras su comisión como una [novedad de nómina](registrar-novedad.md). El vendedor debe estar registrado como [empleado](registrar-empleado.md).

## Pasos

**Paso 1.** Ingresa a <span class="ruta">Ventas › Reportes › Rentabilidad por ítem</span> y elige en **Periodo** las fechas del período de nómina.

![Paso 1: reporte Rentabilidad por ítem con el campo Periodo](../assets/capturas/recursos-humanos/comisiones-vendedores/paso-1.png)

**Paso 2.** Haz clic en **Filtros**, selecciona el **Vendedor** y haz clic en **Aplicar**.

![Paso 2: filtro Vendedor](../assets/capturas/recursos-humanos/comisiones-vendedores/paso-2.png)

**Paso 3.** Toma el total de **Venta neta** (o de **Utilidad**, si así lo acordaste con el vendedor) y multiplícalo por su porcentaje de comisión. Si necesitas el detalle, haz clic en **Exportar Excel**.

![Paso 3: totales del reporte y botón Exportar Excel](../assets/capturas/recursos-humanos/comisiones-vendedores/paso-3.png)

**Paso 4.** Ingresa a <span class="ruta">Nómina › Nómina › Novedades</span> y haz clic en **Nueva Novedad**.

![Paso 4: botón Nueva Novedad](../assets/capturas/recursos-humanos/comisiones-vendedores/paso-4.png)

**Paso 5.** Elige el **Empleado**, en **Novedad** selecciona **Comisión** y escribe en **Valor** el monto que calculaste.

![Paso 5: novedad Comisión con su valor](../assets/capturas/recursos-humanos/comisiones-vendedores/paso-5.png)

**Paso 6.** Haz clic en **Guardar**.

![Paso 6: botón Guardar](../assets/capturas/recursos-humanos/comisiones-vendedores/paso-6.png)

✅ **Listo:** la comisión se paga en el período de nómina que incluye su fecha y sale en la nómina electrónica.

## Si algo falla

| Problema | Solución |
|---|---|
| El vendedor no aparece en **Filtros**. | Revisa que esté creado en <span class="ruta">Ventas › Ajustes › Vendedores</span>. |
| Faltan ventas del vendedor. | Solo cuentan las ventas que tienen ese vendedor asignado. Revisa el vendedor en la factura. |
| La comisión no suma a la seguridad social. | En <span class="ruta">Nómina › Configuración Nómina</span>, pestaña **Conceptos de Nómina**, revisa que **Comisión** tenga **Opera sobre IBC** en **Sí**. |
| El vendedor no es empleado. | Esta guía no aplica: su comisión se paga por fuera de la nómina. |

## Relacionados

- [¿Cómo registro una novedad de nómina?](registrar-novedad.md)
- [¿Cómo liquido y pago la nómina?](liquidar-nomina.md)
