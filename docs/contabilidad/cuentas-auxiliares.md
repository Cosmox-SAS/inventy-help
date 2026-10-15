---
title: "¿Cómo cargo y creo cuentas auxiliares?"
description: "Pasos para cargar las cuentas auxiliares por defecto y crear las propias en el plan de cuentas."
estado: pendiente-validacion
tipo: rapida
modulo: contabilidad
menu: "Contabilidad › Plan de Cuentas"
permisos:
  - Ver plan de cuentas
  - Crear plan de cuentas
revisado: 2026-10-14
search:
  boost: 2
tags:
  - Contabilidad
  - Plan de cuentas
---

# ¿Cómo cargo y creo cuentas auxiliares?

<p class="tambien-se-busca">También se busca como: cuenta auxiliar, auxiliares, crear cuenta contable, cuenta propia, PUC, plan de cuentas, subcuenta, código contable, caja menor, cuentas por defecto.</p>

**Antes de empezar:** el módulo **Contabilidad** debe estar activo.

## Pasos

**Cargar las cuentas por defecto** (solo la primera vez)

**Paso 1.** Ingresa a <span class="ruta">Contabilidad › Plan de Cuentas</span>.

![Paso 1: pantalla Plan de Cuentas](../assets/capturas/contabilidad/cuentas-auxiliares/paso-1.webp)

**Paso 2.** Haz clic en **Cargar auxiliares por defecto**.

![Paso 2: botón Cargar auxiliares por defecto](../assets/capturas/contabilidad/cuentas-auxiliares/paso-2.webp)

**Paso 3.** Revisa la vista previa (**Cuentas auxiliares** y **Asignaciones de cuentas**), haz clic en **Confirmar** y luego en **Sí, aplicar**.

![Paso 3: vista previa de las cuentas por defecto](../assets/capturas/contabilidad/cuentas-auxiliares/paso-3.webp)

**Crear una cuenta propia**

**Paso 4.** En <span class="ruta">Contabilidad › Plan de Cuentas</span>, haz clic en **Nueva cuenta propia**.

![Paso 4: botón Nueva cuenta propia](../assets/capturas/contabilidad/cuentas-auxiliares/paso-4.webp)

**Paso 5.** Deja **Tipo de cuenta** en **Auxiliar** y, en **Cuenta padre**, busca la subcuenta del PUC donde va la cuenta (ej. *110510 Caja menor*).

![Paso 5: tipo de cuenta y cuenta padre](../assets/capturas/contabilidad/cuentas-auxiliares/paso-5.webp)

**Paso 6.** Completa **Nombre de la cuenta** (ej. *CAJA MENOR SEDE NORTE*) y revisa **Naturaleza** y **Tipo fiscal**. El código se genera solo; si quieres, escribe un **Sufijo personalizado** de 3 dígitos.

![Paso 6: nombre de la cuenta, naturaleza y tipo fiscal](../assets/capturas/contabilidad/cuentas-auxiliares/paso-6.webp)

**Paso 7.** Haz clic en **Crear cuenta auxiliar**.

![Paso 7: botón Crear cuenta auxiliar](../assets/capturas/contabilidad/cuentas-auxiliares/paso-7.webp)

✅ **Listo:** la cuenta aparece en el plan de cuentas con nivel **Auxiliar** y la etiqueta *personalizada*, y ya se puede elegir en los campos **Buscar cuenta auxiliar...** (cajas, bancos, catálogos de impuestos, medios de pago, nómina…).

## Si algo falla

| Problema | Solución |
|---|---|
| No aparece **Cargar auxiliares por defecto** | Ya se cargaron antes. Crea las cuentas que falten con **Nueva cuenta propia**. |
| *Solo se pueden crear cuentas auxiliares bajo una Subcuenta.* | Elige como **Cuenta padre** una subcuenta de 6 dígitos, no una clase, grupo o cuenta. |
| La subcuenta que necesito no existe en el PUC | En **Tipo de cuenta** elige **Subcuenta**: se crea bajo una cuenta de 4 dígitos. |
| *El código de cuenta … ya existe. Intenta con un sufijo diferente.* | Cambia el **Sufijo personalizado** o déjalo vacío para que se genere solo. |
| No encuentro una subcuenta del PUC | Actívala en la pestaña **Catálogo PUC** de la misma pantalla y vuelve a intentar. |
| No veo el botón **Nueva cuenta propia** | Tu rol necesita el permiso **Crear plan de cuentas**. |
| *El asiento contable no está balanceado* al facturar | Falta asignar una cuenta auxiliar. **Cargar auxiliares por defecto** completa las que faltan. |
| Tengo muchas cuentas para crear | Usa **Importar** en la misma pantalla para cargarlas desde Excel. |

## Relacionados

- [¿Cómo hago la configuración contable inicial?](configuracion-contable.md)
- [¿Cómo funciona la contabilidad en Inventy?](como-funciona.md)
- [¿Qué es y cómo creo un catálogo de impuestos?](../impuestos/catalogo-impuestos.md)
