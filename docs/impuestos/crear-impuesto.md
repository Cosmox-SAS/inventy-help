---
title: ¿Cómo creo un impuesto o una retención?
description: Pasos para crear un impuesto (IVA, INC, ICA) o una retención (Retefuente, ReteIVA, ReteICA).
estado: pendiente-validacion
tipo: rapida
modulo: impuestos
menu: Fiscal › Impuestos › Catálogo de Impuestos › Impuestos y retenciones
permisos:
  - Ver impuestos
  - Crear impuestos
revisado: 2026-09-29
tags:
  - Impuestos
  - Retenciones
---

# ¿Cómo creo un impuesto o una retención?

<p class="tambien-se-busca">También se busca como: crear IVA, crear retención, retefuente, reteiva, reteica, impuesto al consumo, INC, tarifa de impuesto, nuevo impuesto.</p>

**Qué es:** la tarifa individual (ej. *IVA 19 %* o *Retefuente compras 2,5 %*). Después se agrupa en un [catálogo de impuestos](catalogo-impuestos.md).

## Pasos

1. <span class="ruta">Fiscal › Catálogo de Impuestos</span> › **Impuestos y retenciones**.
2. **Nuevo Impuesto**.
3. Completa:
    - **Tipo**: **Impuesto** o **Retención**.
    - **Nombre**: ej. *IVA 19%*.
    - **Tipo de Valor**: **Porcentaje** o **Valor Fijo**.
    - **Valor**: ej. *19.00*.
    - **Tipo DIAN**: IVA, INC, ICA, IC, Excluido, Retención en la Fuente, Retención de IVA o Retención de ICA.
    - **Base Mínima (COP)** (opcional): solo se aplica si la base es igual o mayor a este valor. Útil para retenciones con tope.
4. **Crear Impuesto**.

✅ Listo: el impuesto ya se puede agregar a un catálogo.

!!! warning "Revisa antes de crear"
    Tipo, tipo de valor, valor y tipo DIAN **no se pueden modificar** después. Si te equivocas, crea uno nuevo.

## Si algo falla

| Problema | Solución |
|---|---|
| No veo **Impuestos y retenciones** | Falta el permiso de impuestos en tu rol. |
| Me equivoqué en el porcentaje | No se puede editar: crea un impuesto nuevo y cámbialo en el catálogo. |
| La retención no se aplica en una factura pequeña | Revisa la **Base Mínima**: si la base de la factura es menor, no se aplica. |

## Relacionados

- [¿Cómo creo un catálogo de impuestos?](catalogo-impuestos.md)
- [¿Cómo se aplican las retenciones?](retenciones.md)
