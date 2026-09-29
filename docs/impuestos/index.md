---
title: Impuestos y retenciones
description: Impuestos, retenciones y catálogos de impuestos en Inventy.
estado: pendiente-validacion
tipo: indice
modulo: impuestos
revisado: 2026-09-29
---

# Impuestos y retenciones

<span class="ruta">Fiscal › Impuestos › Catálogo de Impuestos</span>

Cómo encajan las piezas, en 3 niveles:

```mermaid
flowchart LR
    A["Impuesto o retención<br/>(IVA 19 %, Retefuente 2,5 %…)"] --> B["Catálogo de impuestos<br/>(agrupa impuestos de venta y compra)"]
    B --> C["Producto<br/>(tiene un catálogo)"]
    D["Cliente / Proveedor<br/>(sus retenciones)"] --> E[Factura]
    C --> E
```

| Quiero… | Guía |
|---|---|
| Crear un impuesto o una retención | [¿Cómo creo un impuesto o una retención?](crear-impuesto.md) |
| Crear un catálogo de impuestos | [¿Cómo creo un catálogo de impuestos?](catalogo-impuestos.md) |
| Entender cómo se aplican las retenciones | [¿Cómo se aplican las retenciones?](retenciones.md) |
| Saber qué es cada término | [Glosario](../glosario.md) |

Orden recomendado para configurar: **1.** impuestos y retenciones → **2.** catálogos → **3.** asignar el catálogo a cada producto → **4.** retenciones en clientes y proveedores.
