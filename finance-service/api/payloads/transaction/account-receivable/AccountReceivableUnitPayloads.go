package accountreceivablepayloads

import "time"

type SaveHeaderRequest struct {
	IsActive                               bool      `json:"is_active"`
	CompanyId                              int       `json:"company_id"`
	InvoiceUnitSystemNumber                int       `json:"invoice_unit_system_number"`
	InvoiceStatusId                        int       `json:"invoice_status_id"`
	InvoiceDate                            time.Time `json:"invoice_date"`
	InvoiceDueDate                         time.Time `json:"invoice_due_date"`
	AccountReceivableInvoiceTypeId         int       `json:"account_receivable_invoice_type_id"`
	TaxIndustryDocumentNumber              string    `json:"tax_industry_document_number"`
	TaxIndustryDocumentDate                time.Time `json:"tax_industry_document_date"`
	BrandId                                int       `json:"brand_id"`
	ProfitCenterId                         int       `json:"profit_center_id"`
	CostCenterId                           int       `json:"cost_center_id"`
	TransactionTypeAccountReceviableUnitId int       `json:"transaction_type_account_receviable_unit_id"`
	CustomerId                             int       `json:"customer_id"`
	FundTypeId                             int       `json:"fund_type_id"`
	LeasingSupplierId                      int       `json:"leasing_supplier_id"`
	PurchaseOrderSystemNumber              int       `json:"purchase_order_system_number"`
	PaymentTypeId                          int       `json:"payment_type_id"`
	EventId                                int       `json:"event_id"`
	Remark                                 string    `json:"remark"`
	BillToCustomerId                       int       `json:"bill_to_customer_id"`
	BillToTitlePrefix                      string    `json:"bill_to_title_prefix"`
	BillToName                             string    `json:"bill_to_name"`
	BillToTitleSuffix                      string    `json:"bill_to_title_suffix"`
	BillToTypeId                           int       `json:"bill_to_type_id"`
	BillToIdNo                             string    `json:"bill_to_id_no"`
	BillToAddressId                        int       `json:"bill_to_address_id"`
	BillableToId                           int       `json:"billable_to_id"`
	BillToAddressStreetLine1               string    `json:"bill_to_address_street_line_1"`
	BillToAddressStreetLine2               string    `json:"bill_to_address_street_line_2"`
	BillToAddressStreetLine3               string    `json:"bill_to_address_street_line_3"`
	BillToPhoneNo                          string    `json:"bill_to_phone_no"`
	BillToFaxNo                            string    `json:"bill_to_fax_no"`
	TopId                                  int       `json:"top_id"`
	BillCodeId                             int       `json:"bill_code_id"`
	TaxInvoiceTypeId                       int       `json:"tax_invoice_type_id"`
	BillToTaxRegistrationNumber            string    `json:"bill_to_tax_registration_number"`
	BillToTaxRegistrationDate              time.Time `json:"bill_to_tax_registration_date"`
	PkpType                                string    `json:"pkp_type"`
	PkpNumber                              string    `json:"pkp_number"`
	PkpDate                                time.Time `json:"pkp_date"`
	VatTransactionId                       int       `json:"vat_transaction_id"`
	TaxName                                string    `json:"tax_name"`
	TaxAddressId                           int       `json:"tax_address_id"`
	TaxAddressStreetLine1                  string    `json:"tax_address_street_line_1"`
	TaxAddressStreetLine2                  string    `json:"tax_address_street_line_2"`
	TaxAddressStreetLine3                  string    `json:"tax_address_street_line_3"`
}

type AddLineHeaderRequest struct {
	IsActive                               bool                   `json:"is_active"`
	CompanyId                              int                    `json:"company_id"`
	InvoiceUnitSystemNumber                int                    `json:"invoice_unit_system_number"`
	InvoiceStatusId                        int                    `json:"invoice_status_id"`
	InvoiceDate                            time.Time              `json:"invoice_date"`
	InvoiceDueDate                         time.Time              `json:"invoice_due_date"`
	AccountReceivableInvoiceTypeId         int                    `json:"account_receivable_invoice_type_id"`
	TaxIndustryDocumentNumber              string                 `json:"tax_industry_document_number"`
	TaxIndustryDocumentDate                time.Time              `json:"tax_industry_document_date"`
	BrandId                                int                    `json:"brand_id"`
	ProfitCenterId                         int                    `json:"profit_center_id"`
	CostCenterId                           int                    `json:"cost_center_id"`
	TransactionTypeAccountReceviableUnitId int                    `json:"transaction_type_account_receviable_unit_id"`
	CustomerId                             int                    `json:"customer_id"`
	FundTypeId                             int                    `json:"fund_type_id"`
	LeasingSupplierId                      int                    `json:"leasing_supplier_id"`
	PurchaseOrderSystemNumber              int                    `json:"purchase_order_system_number"`
	PaymentTypeId                          int                    `json:"payment_type_id"`
	EventId                                int                    `json:"event_id"`
	Remark                                 string                 `json:"remark"`
	BillToCustomerId                       int                    `json:"bill_to_customer_id"`
	BillToTitlePrefix                      string                 `json:"bill_to_title_prefix"`
	BillToName                             string                 `json:"bill_to_name"`
	BillToTitleSuffix                      string                 `json:"bill_to_title_suffix"`
	BillToTypeId                           int                    `json:"bill_to_type_id"`
	BillToIdNo                             string                 `json:"bill_to_id_no"`
	BillToAddressId                        int                    `json:"bill_to_address_id"`
	BillableToId                           int                    `json:"billable_to_id"`
	BillToAddressStreetLine1               string                 `json:"bill_to_address_street_line_1"`
	BillToAddressStreetLine2               string                 `json:"bill_to_address_street_line_2"`
	BillToAddressStreetLine3               string                 `json:"bill_to_address_street_line_3"`
	BillToPhoneNo                          string                 `json:"bill_to_phone_no"`
	BillToFaxNo                            string                 `json:"bill_to_fax_no"`
	TopId                                  int                    `json:"top_id"`
	BillCodeId                             int                    `json:"bill_code_id"`
	TaxInvoiceTypeId                       int                    `json:"tax_invoice_type_id"`
	BillToTaxRegistrationNumber            string                 `json:"bill_to_tax_registration_number"`
	BillToTaxRegistrationDate              time.Time              `json:"bill_to_tax_registration_date"`
	PkpType                                string                 `json:"pkp_type"`
	PkpNumber                              string                 `json:"pkp_number"`
	PkpDate                                time.Time              `json:"pkp_date"`
	VatTransactionId                       int                    `json:"vat_transaction_id"`
	TaxName                                string                 `json:"tax_name"`
	TaxAddressId                           int                    `json:"tax_address_id"`
	TaxAddressStreetLine1                  string                 `json:"tax_address_street_line_1"`
	TaxAddressStreetLine2                  string                 `json:"tax_address_street_line_2"`
	TaxAddressStreetLine3                  string                 `json:"tax_address_street_line_3"`
	AddLineDetailRequest                   []AddLineDetailRequest `json:"account_receivable_unit_detail"`
}

type AddLineDetailRequest struct {
	InvoiceUnitDetailSystemNumber      int     `json:"invoice_unit_detail_system_number"`
	InvoiceLineNumber                  int     `json:"invoice_line_number"`
	InvoiceLineStatus                  int     `json:"invoice_line_status"`
	VehicleSalesOrderSystemNumber      int     `json:"vehicle_sales_order_system_number"`
	VehicleId                          int     `json:"vehicle_id"`
	SalesRepresentativeId              int     `json:"sales_representative_id"`
	MediatorFeeAmount                  float64 `json:"mediator_fee_amount"`
	AccYearRemark                      string  `json:"acc_year_remark"`
	InsuranceSupplierId                int     `json:"insurance_supplier_id"`
	BbnAmount                          float64 `json:"bbn_amount"`
	OfftrAmount                        float64 `json:"offtr_amount"`
	OfftrNetAmount                     float64 `json:"offtr_net_amount"`
	DiscountAmount                     float64 `json:"discount_amount"`
	OntrAmount                         float64 `json:"ontr_amount"`
	CostGroupId                        int     `json:"cost_group_id"`
	ItemGroup                          string  `json:"item_group"`
	ItemId                             int     `json:"item_id"`
	ItemDescription                    string  `json:"item_description"`
	ItemQuantity                       float64 `json:"item_quantity"`
	ItemQuantityReturn                 float64 `json:"item_quantity_return"`
	ItemUnitOfMeasurement              string  `json:"item_unit_of_measurement"`
	ItemDiscountPercent                float64 `json:"item_discount_percent"`
	ItemDiscountAmount                 float64 `json:"item_discount_amount"`
	ItemCogs                           float64 `json:"item_cogs"`
	ItemCogsReturn                     float64 `json:"item_cogs_return"`
	TotalItemCogs                      float64 `json:"total_item_cogs"`
	TotalItemCogsReturn                float64 `json:"total_item_cogs_return"`
	UnitCogs                           float64 `json:"unit_cogs"`
	StandardAccesoriesCogs             float64 `json:"standard_accesories_cogs"`
	FreeAccesoriesCogs                 float64 `json:"free_accesories_cogs"`
	TransportCogs                      float64 `json:"transport_cogs"`
	FreeAccesoriesAccrued              float64 `json:"free_accesories_accrued"`
	TransportAccrued                   float64 `json:"transport_accrued"`
	PphTaxServiceCode                  string  `json:"pph_tax_service_code"`
	PphTaxPercent                      float64 `json:"pph_tax_percent"`
	PphAmount                          float64 `json:"pph_amount"`
	PoSystemNumber                     int     `json:"po_system_number"`
	InvoiceReceiptSystemNumber         int     `json:"invoice_receipt_system_number"`
	TotalCreditNoteDp                  float64 `json:"total_credit_note_dp"`
	TotalCreditNoteDpBaseAmount        float64 `json:"total_credit_note_dp_base_amount"`
	TotalCreditNoteBbn                 float64 `json:"total_credit_note_bbn"`
	TotalCreditNoteBbnBaseAmount       float64 `json:"total_credit_note_bbn_base_amount"`
	TotalPayment                       float64 `json:"total_payment"`
	TotalPaymentAllocated              float64 `json:"total_payment_allocated"`
	IsReturn                           bool    `json:"is_return"`
	VarianceDpBbn                      float64 `json:"variance_dp_bbn"`
	OptionId                           int     `json:"option_id"`
	PaymentRetur                       float64 `json:"payment_retur"`
	PaymentReturBbn                    float64 `json:"payment_retur_bbn"`
	TotalDiscountReturn                float64 `json:"total_discount_return"`
	TotalVatReturn                     float64 `json:"toal_vat_return"`
	TotalBebanPajak                    float64 `json:"total_beban_pajak"`
	FlagReturn                         int     `json:"flag_return"`
	TotalAfterDiscountInvoiceReceiptDp float64 `json:"total_after_discount_invoice_receipt_dp"`
	TotalVatInvoiceDp                  float64 `json:"total_vat_invoice_dp"`
	TotalAfterVatInvoiceDp             float64 `json:"total_after_vat_invoice_dp"`
}

type UpdateStatusRequest struct {
	IsActive bool `json:"is_active"`
}

type GetByIdHeaderResponse struct {
	IsActive                               bool                    `json:"is_active"`
	CompanyId                              int                     `json:"company_id"`
	InvoiceUnitSystemNumber                int                     `json:"invoice_unit_system_number"`
	InvoiceStatusId                        int                     `json:"invoice_status_id"`
	AccountReceivableInvoiceTypeId         int                     `json:"account_receivable_invoice_type_id"`
	InvoiceUnitDocumentNumber              string                  `json:"invoice_unit_document_number"`
	InvoiceDate                            time.Time               `json:"invoice_date"`
	InvoiceDueDate                         time.Time               `json:"invoice_due_date"`
	TaxInvoiceSystemNumber                 int                     `json:"tax_invoice_system_number"`
	TaxIndustryDocumentNumber              string                  `json:"tax_industry_document_number"`
	TaxIndustryDocumentDate                time.Time               `json:"tax_industry_document_date"`
	BrandId                                int                     `json:"brand_id"`
	ProfitCenterId                         int                     `json:"profit_center_id"`
	CostCenterId                           int                     `json:"cost_center_id"`
	TransactionTypeAccountReceviableUnitId int                     `json:"transaction_type_account_receviable_unit_id"`
	CreditNoteDocumentNumber               string                  `json:"credit_note_document_number"`
	DebitNoteDocumentNumber                string                  `json:"debit_note_document_number"`
	CreditNoteBbnDocumentNumber            string                  `json:"credit_note_bbn_document_number"`
	CustomerId                             int                     `json:"customer_id"`
	FundTypeId                             int                     `json:"fund_type_id"`
	LeasingSupplierId                      int                     `json:"leasing_supplier_id"`
	PurchaseOrderSystemNumber              int                     `json:"purchase_order_system_number"`
	PaymentTypeId                          int                     `json:"payment_type_id"`
	EventId                                int                     `json:"event_id"`
	Remark                                 string                  `json:"remark"`
	BillToCustomerId                       int                     `json:"bill_to_customer_id"`
	BillToTitlePrefix                      string                  `json:"bill_to_title_prefix"`
	BillToName                             string                  `json:"bill_to_name"`
	BillToTitleSuffix                      string                  `json:"bill_to_title_suffix"`
	BillToTypeId                           int                     `json:"bill_to_type_id"`
	BillToIdNo                             string                  `json:"bill_to_id_no"`
	BillableToId                           int                     `json:"billable_to_id"`
	BillToAddressId                        int                     `json:"bill_to_address_id"`
	BillToAddressStreetLine1               string                  `json:"bill_to_address_street_line_1"`
	BillToAddressStreetLine2               string                  `json:"bill_to_address_street_line_2"`
	BillToAddressStreetLine3               string                  `json:"bill_to_address_street_line_3"`
	BillToPhoneNo                          string                  `json:"bill_to_phone_no"`
	BillToFaxNo                            string                  `json:"bill_to_fax_no"`
	TopId                                  int                     `json:"top_id"`
	BillCodeId                             int                     `json:"bill_code_id"`
	TaxInvoiceTypeId                       int                     `json:"tax_invoice_type_id"`
	BillToTaxRegistrationNumber            string                  `json:"bill_to_tax_registration_number"`
	BillToTaxRegistrationDate              time.Time               `json:"bill_to_tax_registration_date"`
	PkpType                                string                  `json:"pkp_type"`
	PkpNumber                              string                  `json:"pkp_number"`
	PkpDate                                time.Time               `json:"pkp_date"`
	VatTransactionId                       int                     `json:"vat_transaction_id"`
	TaxName                                string                  `json:"tax_name"`
	TaxAddressId                           int                     `json:"tax_address_id"`
	TaxAddressStreetLine1                  string                  `json:"tax_address_street_line_1"`
	TaxAddressStreetLine2                  string                  `json:"tax_address_street_line_2"`
	TaxAddressStreetLine3                  string                  `json:"tax_address_street_line_3"`
	TotalCreditNoteBbn                     float64                 `json:"total_credit_note_bbn"`
	TotalDp                                float64                 `json:"total_dp"`
	TotalDpVat                             float64                 `json:"total_dp_vat"`
	TotalDpAfterVat                        float64                 `json:"total_dp_after_vat"`
	TotalUnitCogs                          float64                 `json:"total_unit_cogs"`
	TotalFreeAccessoriesCogs               float64                 `json:"total_free_accessories_cogs"`
	TotalInsurance                         float64                 `json:"total_insurance"`
	TotalMediatorFee                       float64                 `json:"total_mediator_fee"`
	TotalBbn                               float64                 `json:"total_bbn"`
	Total                                  float64                 `json:"total"`
	TotalDiscount                          float64                 `json:"total_discount"`
	TotalAfterDiscount                     float64                 `json:"total_after_discount"`
	TotalVat                               float64                 `json:"total_vat"`
	TotalVatBaseAmount                     float64                 `json:"total_vat_base_amount"`
	TotalAfterVatBaseAmount                float64                 `json:"total_after_vat_base_amount"`
	VatPercent                             float64                 `json:"vat_percent"`
	TotalPpnbm                             float64                 `json:"total_ppnbm"`
	TaxIndustryAmount                      float64                 `json:"tax_industry_amount"`
	Rounding                               float64                 `json:"rounding"`
	TotalAfterVat                          float64                 `json:"total_after_vat"`
	AccountReceivableUnitDetail            []GetByIdDetailResponse `json:"account_receivable_unit_details"`
}

type GetByIdDetailResponse struct {
	InvoiceUnitDetailSystemNumber      int     `json:"invoice_unit_detail_system_number"`
	InvoiceLineNumber                  int     `json:"invoice_line_number"`
	InvoiceLineStatus                  int     `json:"invoice_line_status"`
	VehicleSalesOrderSystemNumber      int     `json:"vehicle_sales_order_system_number"`
	VehicleId                          int     `json:"vehicle_id"`
	SalesRepresentativeId              int     `json:"sales_representative_id"`
	MediatorFeeAmount                  float64 `json:"mediator_fee_amount"`
	AccYearRemark                      string  `json:"acc_year_remark"`
	InsuranceSupplierId                int     `json:"insurance_supplier_id"`
	BbnAmount                          float64 `json:"bbn_amount"`
	OfftrAmount                        float64 `json:"offtr_amount"`
	OfftrNetAmount                     float64 `json:"offtr_net_amount"`
	DiscountAmount                     float64 `json:"discount_amount"`
	OntrAmount                         float64 `json:"ontr_amount"`
	CostGroupId                        int     `json:"cost_group_id"`
	ItemGroup                          string  `json:"item_group"`
	ItemId                             int     `json:"item_id"`
	ItemDescription                    string  `json:"item_description"`
	ItemQuantity                       float64 `json:"item_quantity"`
	ItemQuantityReturn                 float64 `json:"item_quantity_return"`
	ItemUnitOfMeasurement              string  `json:"item_unit_of_measurement"`
	ItemDiscountPercent                float64 `json:"item_discount_percent"`
	ItemDiscountAmount                 float64 `json:"item_discount_amount"`
	ItemCogs                           float64 `json:"item_cogs"`
	ItemCogsReturn                     float64 `json:"item_cogs_return"`
	TotalItemCogs                      float64 `json:"total_item_cogs"`
	TotalItemCogsReturn                float64 `json:"total_item_cogs_return"`
	UnitCogs                           float64 `json:"unit_cogs"`
	StandardAccesoriesCogs             float64 `json:"standard_accesories_cogs"`
	FreeAccesoriesCogs                 float64 `json:"free_accesories_cogs"`
	TransportCogs                      float64 `json:"transport_cogs"`
	FreeAccesoriesAccrued              float64 `json:"free_accesories_accrued"`
	TransportAccrued                   float64 `json:"transport_accrued"`
	PphTaxServiceCode                  string  `json:"pph_tax_service_code"`
	PphTaxPercent                      float64 `json:"pph_tax_percent"`
	PphAmount                          float64 `json:"pph_amount"`
	PoSystemNumber                     int     `json:"po_system_number"`
	InvoiceReceiptSystemNumber         int     `json:"invoice_receipt_system_number"`
	TotalCreditNoteDp                  float64 `json:"total_credit_note_dp"`
	TotalCreditNoteDpBaseAmount        float64 `json:"total_credit_note_dp_base_amount"`
	TotalCreditNoteBbn                 float64 `json:"total_credit_note_bbn"`
	TotalCreditNoteBbnBaseAmount       float64 `json:"total_credit_note_bbn_base_amount"`
	TotalPayment                       float64 `json:"total_payment"`
	TotalPaymentAllocated              float64 `json:"total_payment_allocated"`
	IsReturn                           bool    `json:"is_return"`
	VarianceDpBbn                      float64 `json:"variance_dp_bbn"`
	OptionId                           int     `json:"option_id"`
	PaymentRetur                       float64 `json:"payment_retur"`
	PaymentReturBbn                    float64 `json:"payment_retur_bbn"`
	TotalDiscountReturn                float64 `json:"total_discount_return"`
	TotalVatReturn                     float64 `json:"toal_vat_return"`
	TotalBebanPajak                    float64 `json:"total_beban_pajak"`
	FlagReturn                         int     `json:"flag_return"`
	TotalAfterDiscountInvoiceReceiptDp float64 `json:"total_after_discount_invoice_receipt_dp"`
	TotalVatInvoiceDp                  float64 `json:"total_vat_invoice_dp"`
	TotalAfterVatInvoiceDp             float64 `json:"total_after_vat_invoice_dp"`
}

type UpdateVatRequest struct {
	VatPercent              float64 `json:"vat_percent"`
	TotalVat                float64 `json:"total_vat"`
	TotalVatBaseAmount      float64 `json:"total_vat_base_amount"`
	TotalAfterVatBaseAmount float64 `json:"total_after_vat_base_amount"`
	TotalAfterVat           float64 `json:"total_after_vat"`
	IsUpdate                bool    `json:"is_update"`
}

type GetBrandResponse struct {
	IsActive  bool   `json:"is_active"`
	BrandId   int    `json:"brand_id"`
	BrandCode string `json:"brand_code"`
	BrandName string `json:"brand_name"`
}
type GetAllHeaderRequest struct {
	CompanyId                              int       `json:"company_id"`
	InvoiceUnitDocumentNumber              string    `json:"invoice_unit_document_number"`
	InvoiceDateFrom                        time.Time `json:"invoice_date_from"`
	InvoiceDateTo                          time.Time `json:"invoice_date_to"`
	InvoiceDueDateFrom                     time.Time `json:"invoice_due_date_from"`
	InvoiceDueDateTo                       time.Time `json:"invoice_due_date_to"`
	BrandId                                int       `json:"brand_id"`
	CustomerId                             int       `json:"customer_id"`
	BillToCustomerId                       int       `json:"bill_to_customer_id"`
	TransactionTypeAccountReceviableUnitId int       `json:"transaction_type_account_receviable_unit_id"`
	InvoiceStatusId                        int       `json:"invoice_status_id"`
	VehicleChassisNo                       string    `json:"vehicle_chassis_no"`
}

type GetAllHeaderResponse struct {
	CompanyId                 int       `json:"company_id"`
	InvoiceUnitSystemNumber   int       `json:"invoice_unit_system_number"`
	InvoiceUnitDocumentNumber string    `json:"invoice_unit_document_number"`
	BrandName                 string    `json:"brand_name"`
	InvoiceDate               time.Time `json:"invoice_date"`
	InvoiceDueDate            time.Time `json:"invoice_due_date"`
	CustomerName              string    `json:"customer_name"`
	BillToCustomerName        string    `json:"bill_to_customer_name"`
	TotalAfterVat             int       `json:"total_after_vat"`
	InvoiceStatus             string    `json:"invoice_status"`
	VehicleChassisNo          string    `json:"vehicle_chassis_no"`
	BrandId                   int       `json:"brand_id"`
	CustomerId                int       `json:"customer_id"`
	BillToCustomerId          int       `json:"bill_to_customer_id"`
}
