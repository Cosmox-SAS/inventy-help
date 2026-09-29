# Inventario funcional de Inventy ERP (Fase 1)

> Documento interno del equipo de documentación. No se publica en el Centro de Ayuda.
>
> **Fuente:** auditoría del código de `inventy-erp` (rama `main`, commit `8c995488`, 29-sep-2026): menú lateral (`resources/js/components/navigation/navigation-registry.ts`), pantallas (`resources/js/pages`), textos visibles, validaciones y estados.
>
> **Limitación:** la auditoría se hizo sobre el código, no sobre la aplicación en funcionamiento. Todo lo aquí descrito debe confirmarse en la interfaz real (Fase 7) antes de marcar una guía como *Validado funcionalmente*.

## 1. Cómo se organiza la navegación

- **Menú lateral** con 13 entradas, en este orden fijo: Inicio, Ventas, Restaurante, Tienda web, Compras, Inventario, Producción, Distribución, Tesorería, Contabilidad, Nómina, Fiscal, Configuración.
- Al hacer clic en una entrada se abre un **submenú** con grupos (Operación, Reportes, Ajustes, Configuración…).
- **Búsqueda en el menú:** atajo <kbd>Ctrl</kbd>+<kbd>K</kbd> (<kbd>⌘</kbd>+<kbd>K</kbd> en Mac), campo “Buscar en el menú…”.
- **Lo que ve cada usuario depende de tres cosas:**
    1. Los **módulos incluidos en la suscripción** / activos (Restaurante, Compras, Inventario, Producción, Distribución, Tesorería, Contabilidad, Nómina, Tienda web, POS).
    2. Las **opciones activadas** en <span>Configuración › Módulos</span> (promociones, listas de precios, atributos, remisiones, lotes, seriales, presentaciones, domicilios).
    3. Los **permisos del rol** del usuario (<span>Configuración › Roles y Permisos</span>).

    ⚠️ Impacto en la documentación: toda guía debe incluir en “Antes de comenzar” el módulo/opción y el permiso necesarios, y la sección “No veo el menú X” es un problema frecuente obligatorio.

## 2. Mapa de menús y funciones

| Menú | Grupo | Opción | Requiere módulo / opción | Notas funcionales |
|---|---|---|---|---|
| **Inicio** | — | Panel principal | — | Indicadores: ventas, compras, cartera vencida, por pagar 7 días, costo de ventas, gastos, utilidad, rentabilidad, clientes y proveedores activos, tendencia 6 meses, top clientes/productos. Sin permiso de estadísticas muestra “Tu espacio de trabajo está listo”. |
| **Ventas** | Operación | POS | POS | Punto de venta de pantalla completa. |
| | | Facturas | — | Estados: Borrador, Validada, Pagada, Anulada. Contado o Crédito. Emisión electrónica desde el detalle. |
| | | Facturas recurrentes | — | Estados: Activa, Pausada, Finalizada. |
| | | Devoluciones | — | Sobre factura validada. Parcial o total. Motivos: Defectuoso, Artículo incorrecto, Exceso, No entregado en despacho, Otro. |
| | Clientes | Clientes | — | Lectura automática de RUT en PDF. Cupo de crédito, plazo, lista de precios, vendedor, tipo de cliente, retención. Casilla “No genera documentos electrónicos”. |
| | Ajustes | Vendedores, Tipos de clientes, Medios de Pago | — | |
| | | Promociones | Opción “promociones” | |
| | | Listas de precios | Opción “listas de precios” | Desactivada por defecto. |
| | Reportes | Productos vendidos, Rentabilidad por ítem, Ventas | — | |
| | | Remisiones por facturar, Historial de remisiones | Opción “remisiones” | Desactivada por defecto. |
| **Restaurante** | Restaurante | Pedidos, Tablero de pedidos, Estaciones de preparación, Mesas | Restaurante (+POS para pedidos) | Mesas con editor visual (lienzo). |
| | Domicilios | Repartidores, Liquidación | Opción “domicilios” + POS | |
| | Propinas | Colaboradores, Liquidación, Reporte | Restaurante | |
| **Tienda web** | — | Catálogo web, Pedidos web, Configuración | Tienda web | Se enciende en Configuración › Módulos › Tienda web. |
| **Compras** | Resumen | Dashboard | Compras | |
| | Operación | Órdenes de Compra, Facturas, Legalización de gastos, Pendientes, Devoluciones | Compras | Factura de compra: Compra Directa / Con Orden de Compra / Asiento Manual. **Lectura de documento del proveedor** (XML, ZIP, PDF o imagen) con IA. Marca “Requiere documento soporte electrónico”. |
| | Proveedores | Proveedores | Compras | Importación masiva. |
| | Reportes | Compras | Compras | |
| **Inventario** | Catálogo | Productos | — (siempre visible) | Incluye Categorías y Unidades de medida. Importar productos. Variantes. Kit, obsequio, seriales, lotes, presentaciones, “No maneja inventario”. |
| | | Servicios | — | |
| | | Atributos | Opción “atributos” | Desactivada por defecto. |
| | Existencias | Stock, Niveles de stock, Movimientos, Kardex, Alertas de stock, Ajuste de inventario, Conteo físico, Traslados, Etiquetas de productos | Inventario | Stock exportable a Excel. Ajustes: borrador → confirmado (no editable después). Importar ajuste. |
| | Lotes | Lotes y vencimientos, Lotes por vencer, Importar lotes | Opción “lotes” | |
| | Seriales | Seriales, Discrepancias, Importar seriales | Opción “seriales” | |
| | Presentaciones | Importar presentaciones | Opción “presentaciones” | |
| **Producción** | Operación | Producciones, Recetas | Producción (requiere Inventario) | |
| **Distribución** | Operación | Preventas, Despachos, Rutas de venta | Distribución (requiere Inventario) | Vendedores y repartidores trabajan desde la **app móvil**. |
| | Reportes | Clientes venta cero | Distribución | |
| | Configuración | Vehículos | Distribución | |
| **Tesorería** | Operación | Ingresos, Egresos, Traslados, Compensación de cuentas, Consignaciones | Tesorería | **Ingresos** = recaudo de cartera o anticipo de cliente. **Egresos** = pago o anticipo a proveedor. |
| | Caja | Cajas, Sesiones, Movimientos de caja, Reporte de caja | Tesorería | Sesiones: Abierta / Cerrada. Cierre con arqueo, reapertura y corrección de arqueo. |
| | Bancos | Cuentas bancarias, Movimientos bancarios | Tesorería | |
| | Cartera | Saldos de clientes, Saldos de proveedores | Tesorería | Importación de saldos iniciales. |
| **Contabilidad** | Plan de cuentas | Plan de Cuentas | Contabilidad | PUC. Importar cuentas. |
| | Movimientos | Asientos Contables | Contabilidad | Importar asientos. |
| | Reportes | Reporte de Asientos, Balance de Prueba, Libro Auxiliar, Estado de Resultados, Balance General, Reporte de Impuestos | Contabilidad | |
| | Configuración | Configuración | Contabilidad | |
| **Nómina** | Personal | Cargos, Empleados | Nómina | Importación de empleados; campos de seguridad social obligatorios. |
| | Nómina | Dashboard, Incapacidades, Vacaciones, Novedades, Período Nómina, Pagos Nómina, Nóminas Pagadas, Provisiones, Liquidaciones, Nómina Electrónica | Nómina | |
| | Configuración | Configuración Nómina, Cuentas Contables de Nómina | Nómina | |
| **Fiscal** | Doc Electrónicos | Documentos, Resoluciones | — | Ver §3. |
| | Impuestos | Catálogo de Impuestos, Reporte de Impuestos | — | |
| **Configuración** | General | Módulos, Contactos, Empresa, Suscripción, Sedes, Centros de Costo | — | |
| | Accesos | Usuarios, Roles y Permisos | — | Usuarios por creación directa o por invitación por correo. |

**Ocultas del menú a pedido del cliente (no documentar):** Planilla PILA, Tipos de contratos, Contratos laborales, Guía del Proceso de Nómina, Conceptos de Nómina (accesible dentro de Configuración Nómina).

**Menú de usuario:** Perfil (nombre, correo, PIN de autorización), Contraseña, Autenticación de dos factores, Apariencia, Cerrar sesión.

## 3. Facturación electrónica

- **Tipos de documento:** Factura electrónica de venta, Nota crédito electrónica, Documento soporte electrónico, Nota de ajuste al documento soporte, Documento equivalente POS, Nota de ajuste al documento equivalente POS, Nómina electrónica (+ nota de ajuste y anulación).
- **Estados de un documento:** Pendiente, Aceptado, Aceptado con observaciones, Rechazado por proveedor, Rechazado por DIAN, Desconocido, Falló prevalidación.
- **Acciones en Fiscal › Documentos:** Ver observaciones, Ver error, Ver en DIAN, Enviar email (varios correos separados por `;`), Reenviar documento electrónico (reusa el mismo consecutivo).
- **Resoluciones:** tipo de documento, prefijo, número, rango desde/hasta, próximo consecutivo, vigencia, estado (Activa, Inactiva, Agotada, Vencida), clave técnica, sedes.
- **Habilitación ante la DIAN:** la hace el **equipo de Inventy** desde el panel de administración (estados: Pendiente de registro, Registrado, En pruebas, Habilitado en producción, Suspendido). El cliente no la ve → la guía debe indicar que se solicita a soporte. *Pendiente confirmar el proceso comercial.*
- **Integración:** proveedor tecnológico Alegra. No mencionar el nombre al cliente salvo que el equipo comercial lo apruebe.

## 4. Hallazgos que afectan la redacción

| Hallazgo | Decisión editorial |
|---|---|
| “Egresos” en Tesorería es **pago a proveedor**, no “gasto” genérico. | La pregunta “¿Cómo registro un gasto?” se responde con: factura de compra (gasto con factura), Legalización de gastos (varias facturas de servicios) y Egresos (el pago). |
| Los nombres de menú mezclan mayúsculas (“Órdenes de Compra”, “Medios de Pago”, “Plan de Cuentas”). | Se citan **exactamente** como aparecen en pantalla. |
| Algunas pantallas técnicas (autenticación de dos factores) están en inglés. | Guía de 2FA marcada como pendiente hasta que se traduzca. |
| El POS exige caja abierta para vender y puede exigir consignación si la caja supera su monto máximo. | Documentado en POS y en soluciones rápidas. |
| El cierre de caja detecta montos anómalos y pide reescribir el monto y un motivo. | Documentado en Cierre de caja. |
| Las facturas **validadas** no se pueden editar; se corrigen con devolución/nota crédito o anulación. | Advertencia en todas las guías de ventas. |
| La app móvil (vendedores y repartidores) consume la misma cuenta. | Sección de Distribución debe incluir la app. Pendiente acceso a la app para capturas. |

## 5. Priorización de guías

Criterio: frecuencia de uso × volumen esperado de consultas a soporte × riesgo de error (fiscal/dinero).

| Prioridad | Guías |
|---|---|
| **P1 — primera entrega** | Ingresar, Recuperar contraseña, Pantalla principal, Configurar empresa, Usuarios, Roles, Abrir caja, Vender en POS, Cierre de caja, Crear producto, Existencias, Crear cliente, Factura de venta, Emitir factura electrónica, Estados de documento electrónico, Documento rechazado, Soluciones rápidas (acceso, POS/caja, facturación electrónica) |
| **P2** | Factura de compra, Ajuste de inventario, Devolución de venta, Resoluciones DIAN, Ingresos (recaudo), Egresos (pago a proveedor), Activar módulos |
| **P3** | Traslados, Conteo físico, Kardex, Órdenes de compra, Proveedores, Legalización de gastos, Medios de pago, Promociones, Reportes de ventas, Cartera |
| **P4** | Contabilidad, Nómina, Distribución y app móvil, Restaurante, Producción, Tienda web, Bancos, importaciones masivas |
