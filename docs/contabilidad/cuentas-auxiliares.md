---
title: "¿Cómo se implementan las cuentas auxiliares?"
description: "Pasos para cargar las cuentas auxiliares por defecto y crear las propias en el plan de cuentas."
estado: pendiente-validacion
tipo: rapida
modulo: contabilidad
menu: "Contabilidad › Plan de Cuentas"
permisos:
  - Ver plan de cuentas
  - Crear plan de cuentas
revisado: 2026-09-30
search:
  boost: 2
tags:
  - Contabilidad
  - Plan de cuentas
---

# ¿Cómo se implementan las cuentas auxiliares?

<p class="tambien-se-busca">También se busca como: cuenta auxiliar, auxiliares, crear cuenta contable, PUC, plan de cuentas, subcuenta, código contable, caja menor, cuentas por defecto.</p>

**Qué es:** el último nivel del plan de cuentas (PUC). Es la cuenta donde Inventy registra los movimientos; las de nivel superior solo agrupan.

**Antes de empezar:** el módulo **Contabilidad** debe estar activo.

## Pasos

**Paso 1.** Ingresa a <span class="ruta">Contabilidad › Plan de Cuentas</span>.

![Paso 1: pantalla Plan de Cuentas](../assets/capturas/contabilidad/cuentas-auxiliares/paso-1.webp)

**Paso 2.** *(Solo la primera vez)* Haz clic en **Cargar auxiliares por defecto**.

![Paso 2: botón Cargar auxiliares por defecto](../assets/capturas/contabilidad/cuentas-auxiliares/paso-2.webp)

**Paso 3.** Revisa la vista previa (**Cuentas a crear**, **Asignaciones a completar**), haz clic en **Confirmar** y luego en **Sí, aplicar**. Esto se hace una sola vez.

![Paso 3: vista previa del catálogo por defecto](../assets/capturas/contabilidad/cuentas-auxiliares/paso-3.webp)

**Paso 4.** Para crear una cuenta propia, haz clic en **Nueva Cuenta Auxiliar**.

![Paso 4: botón Nueva Cuenta Auxiliar](../assets/capturas/contabilidad/cuentas-auxiliares/paso-4.webp)

**Paso 5.** En **Cuenta padre**, busca la **Subcuenta** del PUC donde va la cuenta (ej. *110505 Caja general*).

![Paso 5: campo Cuenta padre](../assets/capturas/contabilidad/cuentas-auxiliares/paso-5.webp)

**Paso 6.** Escribe el **Nombre de la cuenta** (ej. *CAJA MENOR SEDE NORTE*). El código se genera solo; si quieres, escribe un **Sufijo personalizado** de 3 dígitos. Revisa **Naturaleza** y **Tipo fiscal**.

![Paso 6: nombre, sufijo, naturaleza y tipo fiscal](../assets/capturas/contabilidad/cuentas-auxiliares/paso-6.webp)

**Paso 7.** Haz clic en **Crear cuenta**.

![Paso 7: botón Crear cuenta](../assets/capturas/contabilidad/cuentas-auxiliares/paso-7.webp)

✅ **Listo:** la cuenta aparece en el plan de cuentas con nivel **Auxiliar** y ya se puede elegir en todos los campos **Buscar cuenta auxiliar...** (cajas, bancos, catálogos de impuestos, medios de pago, nómina…).

!!! info "Cómo se forma el código"
    Clase (1 dígito) › Grupo (2) › Cuenta (4) › Subcuenta (6) › **Auxiliar** = subcuenta + 3 dígitos.
    Ejemplo: subcuenta `110505` → auxiliares `110505001`, `110505002`… Los movimientos se registran siempre en cuentas **auxiliares**.

## Si algo falla

| Problema | Solución |
|---|---|
| *Solo se pueden crear cuentas auxiliares bajo una Subcuenta.* | Elige como cuenta padre una **Subcuenta** (6 dígitos), no una Clase, Grupo o Cuenta. |
| *El código de cuenta … ya existe. Intenta con un sufijo diferente.* | Cambia el **Sufijo personalizado** o déjalo vacío para que se genere solo. |
| *El catálogo por defecto ya fue aplicado.* | Ya se cargó antes. Crea las cuentas que falten con **Nueva Cuenta Auxiliar**. |
| No encuentro una subcuenta del PUC | Actívala en **Catálogo PUC** (en la misma pantalla) y vuelve a intentar. |
| No veo el botón **Nueva Cuenta Auxiliar** | Tu rol necesita el permiso **Crear plan de cuentas**. |
| *El asiento contable no está balanceado* al facturar | Falta asignar una cuenta auxiliar en la configuración. **Cargar auxiliares por defecto** completa las que faltan. |
| ¿Tengo muchas cuentas? | Usa la importación de cuentas desde Excel del plan de cuentas. |

## Relacionados

- [Contabilidad](index.md)
- [¿Qué es y cómo creo un catálogo de impuestos?](../impuestos/catalogo-impuestos.md)
