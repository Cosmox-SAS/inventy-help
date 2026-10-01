# Cambios de Inventy ERP que afectan el Centro de Ayuda

> Generado por `scripts/sync_erp.py` después de cada `git pull` en inventy-erp. Lo más reciente, arriba.

## 2026-10-01 12:13 · inventy-erp `8c995488..d6fb7d41`

Último commit: feat(sales): notas crédito a favor del cliente en devoluciones y notas manuales 91-22 (#1534)

**156** archivos de interfaz cambiaron · **32** textos quitados · **0** guías afectadas.

### Cambios en el menú

- ➕ Descuentos de empresa
- ➕ Descuentos de proveedor
- ➕ Importar precios
- ➕ Notas crédito

### Pantallas nuevas (revisar si necesitan guía)

- `resources/js/pages/admin/tenants/clone.tsx`
- `resources/js/pages/expenses/advance-imports/create.tsx`
- `resources/js/pages/expenses/advance-imports/show.tsx`
- `resources/js/pages/expenses/components/CounterLinesEditor.tsx`
- `resources/js/pages/income/advance-imports/create.tsx`
- `resources/js/pages/income/advance-imports/show.tsx`
- `resources/js/pages/income/components/CustomerCreditNotePickerTable.tsx`
- `resources/js/pages/products/parts/CustomerReferencesSection.tsx`
- `resources/js/pages/products/price-imports/components/PriceImportPreviewTable.tsx`
- `resources/js/pages/products/price-imports/create.tsx`
- `resources/js/pages/products/price-imports/show.tsx`
- `resources/js/pages/sales/customer-credit-notes/CreditNoteLinesTable.tsx`
- `resources/js/pages/sales/customer-credit-notes/CustomerCreditNoteForm.tsx`
- `resources/js/pages/sales/customer-credit-notes/create.tsx`
- `resources/js/pages/sales/customer-credit-notes/edit.tsx`
- `resources/js/pages/sales/customer-credit-notes/index.tsx`
- `resources/js/pages/sales/customer-credit-notes/show.tsx`
- `resources/js/pages/sales/report/company-discounts/index.tsx`
- `resources/js/pages/sales/report/supplier-discounts/index.tsx`

<details><summary>Archivos con cambios de texto</summary>

- `resources/js/components/contacts/form/no-taxes-checkbox.tsx` (nuevo): 0 texto(s) quitados, 2 agregados
- `resources/js/components/contacts/location-modal.tsx` (nuevo): 0 texto(s) quitados, 7 agregados
- `resources/js/components/navigation/navigation-registry.ts` (modificado): 0 texto(s) quitados, 4 agregados
- `resources/js/components/pos/payment-modal.tsx` (modificado): 0 texto(s) quitados, 1 agregados
- `resources/js/components/pos/payment-numpad.tsx` (modificado): 0 texto(s) quitados, 1 agregados
- `resources/js/components/pos/purchase-order-modal.tsx` (eliminado): 2 texto(s) quitados, 0 agregados
- `resources/js/components/pos/purchase-order.ts` (eliminado): 3 texto(s) quitados, 0 agregados
- `resources/js/components/products/PresentationSelect.tsx` (modificado): 0 texto(s) quitados, 1 agregados
- `resources/js/components/sales/SaleItemsTable.tsx` (modificado): 0 texto(s) quitados, 1 agregados
- `resources/js/components/sales/credit-note-allocation-modal.tsx` (nuevo): 0 texto(s) quitados, 6 agregados
- `resources/js/components/sales/purchase-order-action.tsx` (nuevo): 0 texto(s) quitados, 1 agregados
- `resources/js/components/sales/purchase-order-modal.tsx` (nuevo): 0 texto(s) quitados, 3 agregados
- `resources/js/components/sales/purchase-order.ts` (nuevo): 0 texto(s) quitados, 2 agregados
- `resources/js/components/sales/returns/SaleReturnRefundSection.tsx` (nuevo): 0 texto(s) quitados, 4 agregados
- `resources/js/components/treasury/AccountCompensationEntryPreviewModal.tsx` (modificado): 0 texto(s) quitados, 1 agregados
- `resources/js/pages/accounting/settings.tsx` (modificado): 0 texto(s) quitados, 2 agregados
- `resources/js/pages/admin/tenants/clone.tsx` (nuevo): 0 texto(s) quitados, 19 agregados
- `resources/js/pages/admin/tenants/index.tsx` (modificado): 0 texto(s) quitados, 3 agregados
- `resources/js/pages/contacts/show.tsx` (modificado): 4 texto(s) quitados, 2 agregados
- `resources/js/pages/distribution/presales/presale-form.tsx` (modificado): 0 texto(s) quitados, 1 agregados
- `resources/js/pages/distribution/sales-routes/route-customer-edit-modal.tsx` (modificado): 1 texto(s) quitados, 3 agregados
- `resources/js/pages/distribution/sales-routes/sales-route-form-modal.tsx` (modificado): 1 texto(s) quitados, 1 agregados
- `resources/js/pages/distribution/sales-routes/show.tsx` (modificado): 1 texto(s) quitados, 1 agregados
- `resources/js/pages/expenses/advance-imports/create.tsx` (nuevo): 0 texto(s) quitados, 10 agregados
- `resources/js/pages/expenses/advance-imports/import-state.ts` (nuevo): 0 texto(s) quitados, 14 agregados
- `resources/js/pages/expenses/advance-imports/show.tsx` (nuevo): 0 texto(s) quitados, 25 agregados
- `resources/js/pages/expenses/components/CounterLinesEditor.tsx` (nuevo): 0 texto(s) quitados, 10 agregados
- `resources/js/pages/expenses/components/VoidExpenseDialog.tsx` (modificado): 1 texto(s) quitados, 0 agregados
- `resources/js/pages/expenses/form.tsx` (modificado): 2 texto(s) quitados, 4 agregados
- `resources/js/pages/expenses/index.tsx` (modificado): 0 texto(s) quitados, 2 agregados
- `resources/js/pages/expenses/movement-type.ts` (nuevo): 0 texto(s) quitados, 9 agregados
- `resources/js/pages/expenses/show.tsx` (modificado): 0 texto(s) quitados, 1 agregados
- `resources/js/pages/expenses/source-account-reference.ts` (nuevo): 0 texto(s) quitados, 6 agregados
- `resources/js/pages/hr/employees/create.tsx` (modificado): 0 texto(s) quitados, 2 agregados
- `resources/js/pages/income/advance-copy.ts` (modificado): 0 texto(s) quitados, 2 agregados
- `resources/js/pages/income/advance-imports/create.tsx` (nuevo): 0 texto(s) quitados, 10 agregados
- `resources/js/pages/income/advance-imports/import-state.ts` (nuevo): 0 texto(s) quitados, 14 agregados
- `resources/js/pages/income/advance-imports/show.tsx` (nuevo): 0 texto(s) quitados, 26 agregados
- `resources/js/pages/income/components/CustomerCreditNotePickerTable.tsx` (nuevo): 0 texto(s) quitados, 9 agregados
- `resources/js/pages/income/form.tsx` (modificado): 0 texto(s) quitados, 3 agregados
- `resources/js/pages/income/index.tsx` (modificado): 0 texto(s) quitados, 3 agregados
- `resources/js/pages/income/show.tsx` (modificado): 0 texto(s) quitados, 2 agregados
- `resources/js/pages/products/index.tsx` (modificado): 0 texto(s) quitados, 1 agregados
- `resources/js/pages/products/parts/CustomerReferencesSection.tsx` (nuevo): 0 texto(s) quitados, 13 agregados
- `resources/js/pages/products/parts/PresentationsTab.tsx` (modificado): 0 texto(s) quitados, 2 agregados
- `resources/js/pages/products/parts/presentation-name.ts` (nuevo): 0 texto(s) quitados, 1 agregados
- `resources/js/pages/products/price-imports/components/PriceImportPreviewTable.tsx` (nuevo): 0 texto(s) quitados, 8 agregados
- `resources/js/pages/products/price-imports/components/price-import-helpers.ts` (nuevo): 0 texto(s) quitados, 7 agregados
- `resources/js/pages/products/price-imports/create.tsx` (nuevo): 0 texto(s) quitados, 15 agregados
- `resources/js/pages/products/price-imports/show.tsx` (nuevo): 0 texto(s) quitados, 23 agregados
- `resources/js/pages/products/show.tsx` (modificado): 11 texto(s) quitados, 0 agregados
- `resources/js/pages/purchases/suppliers/create.tsx` (modificado): 0 texto(s) quitados, 2 agregados
- `resources/js/pages/purchases/suppliers/edit.tsx` (modificado): 0 texto(s) quitados, 2 agregados
- `resources/js/pages/purchases/suppliers/imports/components/ImportPreviewTable.tsx` (modificado): 0 texto(s) quitados, 1 agregados
- `resources/js/pages/purchases/suppliers/show.tsx` (modificado): 0 texto(s) quitados, 1 agregados
- `resources/js/pages/sales/customer-credit-notes/CreditNoteLinesTable.tsx` (nuevo): 0 texto(s) quitados, 7 agregados
- `resources/js/pages/sales/customer-credit-notes/CustomerCreditNoteForm.tsx` (nuevo): 0 texto(s) quitados, 22 agregados
- `resources/js/pages/sales/customer-credit-notes/create.tsx` (nuevo): 0 texto(s) quitados, 1 agregados
- `resources/js/pages/sales/customer-credit-notes/electronic-emission.ts` (nuevo): 0 texto(s) quitados, 2 agregados
- `resources/js/pages/sales/customer-credit-notes/index.tsx` (nuevo): 0 texto(s) quitados, 10 agregados
- `resources/js/pages/sales/customer-credit-notes/show.tsx` (nuevo): 0 texto(s) quitados, 22 agregados
- `resources/js/pages/sales/customers/imports/components/ImportPreviewTable.tsx` (modificado): 0 texto(s) quitados, 2 agregados
- `resources/js/pages/sales/customers/show.tsx` (modificado): 0 texto(s) quitados, 1 agregados
- `resources/js/pages/sales/recurring-sale-invoices/RecurringInvoiceItemsTable.tsx` (modificado): 0 texto(s) quitados, 1 agregados
- `resources/js/pages/sales/report/company-discounts/index.tsx` (nuevo): 0 texto(s) quitados, 17 agregados
- `resources/js/pages/sales/report/supplier-discounts/index.tsx` (nuevo): 0 texto(s) quitados, 13 agregados
- `resources/js/pages/sales/returns/show.tsx` (modificado): 0 texto(s) quitados, 2 agregados
- `resources/js/pages/sales/sale-invoices/create.tsx` (modificado): 0 texto(s) quitados, 2 agregados
- `resources/js/pages/sales/sale-invoices/edit.tsx` (modificado): 0 texto(s) quitados, 2 agregados
- `resources/js/pages/sales/sale-invoices/show.tsx` (modificado): 1 texto(s) quitados, 3 agregados
- `resources/js/pages/settings/components/inventory-section.tsx` (modificado): 0 texto(s) quitados, 8 agregados
- `resources/js/pages/treasury/account-compensations/create.tsx` (modificado): 5 texto(s) quitados, 11 agregados
- `resources/js/pages/treasury/account-compensations/show.tsx` (modificado): 0 texto(s) quitados, 2 agregados
- `resources/js/pages/treasury/account-compensations/void-copy.ts` (nuevo): 0 texto(s) quitados, 2 agregados

</details>

