package accountreceivableentities

const TableNameAccountReceivableUnitDetail = "trx_account_receivable_unit_detail"

type AccountReceivableUnitDetail struct {
	InvoiceUnitDetailSystemNumber      int     `gorm:"column:invoice_unit_detail_system_number;not null;primaryKey" json:"invoice_unit_detail_system_number"`
	InvoiceUnitSystemNumber            int     `gorm:"column:invoice_unit_system_number;not null;" json:"invoice_unit_system_number"`
	InvoiceLineNumber                  int     `gorm:"column:invoice_line_number;not null" json:"invoice_line_number"`
	InvoiceLineStatus                  int     `gorm:"column:invoice_line_status;" json:"invoice_line_status"`
	VehicleSalesOrderSystemNumber      int     `gorm:"column:vehicle_sales_order_system_number;" json:"vehicle_sales_order_system_number"`
	VehicleId                          int     `gorm:"column:vehicle_id;not null" json:"vehicle_id"`
	SalesRepresentativeId              int     `gorm:"column:sales_representative_id;" json:"sales_representative_id"`
	MediatorFeeAmount                  float64 `gorm:"column:mediator_fee_amount;" json:"mediator_fee_amount"`
	AccYearRemark                      string  `gorm:"column:acc_year_remark;size:20;" json:"acc_year_remark"`
	InsuranceSupplierId                int     `gorm:"column:insurance_supplier_id;" json:"insurance_supplier_id"`
	BbnAmount                          float64 `gorm:"column:bbn_amount;" json:"bbn_amount"`
	OfftrAmount                        float64 `gorm:"column:offtr_amount;" json:"offtr_amount"`
	OfftrNetAmount                     float64 `gorm:"column:offtr_net_amount;" json:"offtr_net_amount"`
	DiscountAmount                     float64 `gorm:"column:discount_amount;" json:"discount_amount"`
	OntrAmount                         float64 `gorm:"column:ontr_amount;" json:"ontr_amount"`
	CostGroupId                        int     `gorm:"column:cost_group_id;" json:"cost_group_id"`
	ItemGroup                          string  `gorm:"column:item_group;" json:"item_group"`
	ItemId                             int     `gorm:"column:item_id;" json:"item_id"`
	ItemDescription                    string  `gorm:"column:item_description;size:200" json:"item_description"`
	ItemQuantity                       float64 `gorm:"column:item_quantity;" json:"item_quantity"`
	ItemQuantityReturn                 float64 `gorm:"column:item_quantity_return;" json:"item_quantity_return"`
	ItemUnitOfMeasurement              string  `gorm:"column:item_unit_of_measurement;type:char;size:3;" json:"item_unit_of_measurement"`
	ItemDiscountPercent                float64 `gorm:"column:item_discount_percent;" json:"item_discount_percent"`
	ItemDiscountAmount                 float64 `gorm:"column:item_discount_amount;" json:"item_discount_amount"`
	ItemCogs                           float64 `gorm:"column:item_cogs;" json:"item_cogs"`
	ItemCogsReturn                     float64 `gorm:"column:item_cogs_return;" json:"item_cogs_return"`
	TotalItemCogs                      float64 `gorm:"column:total_item_cogs;" json:"total_item_cogs"`
	TotalItemCogsReturn                float64 `gorm:"column:total_item_cogs_return;" json:"total_item_cogs_return"`
	UnitCogs                           float64 `gorm:"column:unit_cogs;" json:"unit_cogs"`
	StandardAccesoriesCogs             float64 `gorm:"column:standard_accesories_cogs;" json:"standard_accesories_cogs"`
	FreeAccesoriesCogs                 float64 `gorm:"column:free_accesories_cogs;" json:"free_accesories_cogs"`
	TransportCogs                      float64 `gorm:"column:transport_cogs;" json:"transport_cogs"`
	FreeAccesoriesAccrued              float64 `gorm:"column:free_accesories_accrued;" json:"free_accesories_accrued"`
	TransportAccrued                   float64 `gorm:"column:transport_accrued;" json:"transport_accrued"`
	PphTaxServiceCode                  string  `gorm:"column:pph_tax_service_code;size:10;" json:"pph_tax_service_code"`
	PphTaxPercent                      float64 `gorm:"column:pph_tax_percent;" json:"pph_tax_percent"`
	PphAmount                          float64 `gorm:"column:pph_amount;" json:"pph_amount"`
	PoSystemNumber                     int     `gorm:"column:po_system_number;" json:"po_system_number"`
	InvoiceReceiptSystemNumber         int     `gorm:"column:invoice_receipt_system_number;" json:"invoice_receipt_system_number"`
	TotalCreditNoteDp                  float64 `gorm:"column:total_credit_note_dp;" json:"total_credit_note_dp"`
	TotalCreditNoteDpBaseAmount        float64 `gorm:"column:total_credit_note_dp_base_amount;" json:"total_credit_note_dp_base_amount"`
	TotalCreditNoteBbn                 float64 `gorm:"column:total_credit_note_bbn;" json:"total_credit_note_bbn"`
	TotalCreditNoteBbnBaseAmount       float64 `gorm:"column:total_credit_note_bbn_base_amount;" json:"total_credit_note_bbn_base_amount"`
	TotalPayment                       float64 `gorm:"column:total_payment;" json:"total_payment"`
	TotalPaymentAllocated              float64 `gorm:"column:total_payment_allocated;" json:"total_payment_allocated"`
	IsReturn                           bool    `gorm:"column:is_return;" json:"is_return"`
	VarianceDpBbn                      float64 `gorm:"column:variance_dp_bbn;" json:"variance_dp_bbn"`
	OptionId                           int     `gorm:"column:option_id;" json:"option_id"` // mtr_accessoris_option
	PaymentRetur                       float64 `gorm:"column:payment_retur;" json:"payment_retur"`
	PaymentReturBbn                    float64 `gorm:"column:payment_retur_bbn;" json:"payment_retur_bbn"`
	TotalDiscountReturn                float64 `gorm:"column:total_discount_return;" json:"total_discount_return"`
	TotalVatReturn                     float64 `gorm:"column:toal_vat_return;" json:"toal_vat_return"`
	TotalBebanPajak                    float64 `gorm:"column:total_beban_pajak;" json:"total_beban_pajak"`
	FlagReturn                         int     `gorm:"column:flag_return;" json:"flag_return"`
	TotalAfterDiscountInvoiceReceiptDp float64 `gorm:"column:total_after_discount_invoice_receipt_dp;" json:"total_after_discount_invoice_receipt_dp"`
	TotalVatInvoiceDp                  float64 `gorm:"column:total_vat_invoice_dp;" json:"total_vat_invoice_dp"`
	TotalAfterVatInvoiceDp             float64 `gorm:"column:total_after_vat_invoice_dp;" json:"total_after_vat_invoice_dp"`
}

func (r *AccountReceivableUnitDetail) TableName() string {
	return TableNameAccountReceivableUnitDetail
}
