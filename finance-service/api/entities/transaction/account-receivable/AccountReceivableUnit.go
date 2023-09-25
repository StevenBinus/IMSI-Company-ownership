package accountreceivableentities

import "time"

const TableNameAccountReceivableUnit = "trx_account_receivable_unit"

type AccountReceivableUnit struct {
	IsActive                               bool                          `gorm:"column:is_active;default:true;not null" json:"is_active"`
	CompanyId                              int                           `gorm:"column:company_id;not null" json:"company_id"` // General - Hengky
	InvoiceUnitSystemNumber                int                           `gorm:"column:invoice_unit_system_number;not null;primaryKey" json:"invoice_unit_system_number"`
	InvoiceStatusId                        int                           `gorm:"column:invoice_status_id;null" json:"invoice_status_id"`                                   // Common - Abrian
	AccountReceivableInvoiceTypeId         int                           `gorm:"column:account_receivable_invoice_type_id;null" json:"account_receivable_invoice_type_id"` // Common - Enrico
	InvoiceUnitDocumentNumber              string                        `gorm:"column:invoice_unit_document_number;size:25;null" json:"invoice_unit_document_number"`
	InvoiceDate                            time.Time                     `gorm:"column:invoice_date;null" json:"invoice_date"`
	InvoiceDueDate                         time.Time                     `gorm:"column:invoice_due_date;null" json:"invoice_due_date"`
	TaxInvoiceSystemNumber                 int                           `gorm:"column:tax_invoice_system_number;null" json:"tax_invoice_system_number"` // Finance - Steve (waiting)
	TaxIndustryDocumentNumber              string                        `gorm:"column:tax_industry_document_number;null;size:50;" json:"tax_industry_document_number"`
	TaxIndustryDocumentDate                time.Time                     `gorm:"column:tax_industry_document_date;null" json:"tax_industry_document_date"`
	BrandId                                int                           `gorm:"column:brand_id;not null" json:"brand_id"`                                                                       // Sales - Tyo
	ProfitCenterId                         int                           `gorm:"column:profit_center_id;not null" json:"profit_center_id"`                                                       // General - Tyo
	CostCenterId                           int                           `gorm:"column:cost_center_id;not null" json:"cost_center_id"`                                                           // General - Tyo | Untuk Dealer Rep Code                                                        // General - Tyo
	TransactionTypeAccountReceviableUnitId int                           `gorm:"column:transaction_type_account_receviable_unit_id;not null" json:"transaction_type_account_receviable_unit_id"` // General - Leonardi
	CreditNoteDocumentNumber               string                        `gorm:"column:credit_note_document_number;null;size:25" json:"credit_note_document_number"`
	DebitNoteDocumentNumber                string                        `gorm:"column:debit_note_document_number;null;size:25" json:"debit_note_document_number"`
	CreditNoteBbnDocumentNumber            string                        `gorm:"column:credit_note_bbn_document_number;null;size:25" json:"credit_note_bbn_document_number"`
	CustomerId                             int                           `gorm:"column:customer_id;not null" json:"customer_id"`                               // General - Steve
	FundTypeId                             int                           `gorm:"column:fund_type_id;not null" json:"fund_type_id"`                             // Common - Stephen
	LeasingSupplierId                      int                           `gorm:"column:leasing_supplier_id;null" json:"leasing_supplier_id"`                   // General - Ko Richardo
	PurchaseOrderSystemNumber              int                           `gorm:"column:purchase_order_system_number;null" json:"purchase_order_system_number"` // Aftersales - Steve
	PaymentTypeId                          int                           `gorm:"column:payment_type_id;not null" json:"payment_type_id"`                       // Common - Natanael
	EventId                                int                           `gorm:"column:event_id;not null" json:"event_id"`                                     // Finance - Hengky
	Remark                                 string                        `gorm:"column:remark;null;size:512" json:"remark"`
	BillToCustomerId                       int                           `gorm:"column:bill_to_customer_id;null" json:"bill_to_customer_id"` // General - Steve
	BillToTitlePrefix                      string                        `gorm:"column:bill_to_title_prefix;null;size:15" json:"bill_to_title_prefix"`
	BillToName                             string                        `gorm:"column:bill_to_name;not null;size:100" json:"bill_to_name"`
	BillToTitleSuffix                      string                        `gorm:"column:bill_to_title_suffix;null;size:15" json:"bill_to_title_suffix"`
	BillToTypeId                           int                           `gorm:"column:bill_to_type_id;null" json:"bill_to_type_id"` // Common - Natanael
	BillToIdNo                             string                        `gorm:"column:bill_to_id_no;null;size:50" json:"bill_to_id_no"`
	BillableToId                           int                           `gorm:"column:billable_to_id;null" json:"billable_to_id"`             // Common
	BillToAddressId                        int                           `gorm:"column:bill_to_address_id;not null" json:"bill_to_address_id"` // General
	BillToAddressStreetLine1               string                        `gorm:"column:bill_to_address_street_line_1;null;size:100" json:"bill_to_address_street_line_1"`
	BillToAddressStreetLine2               string                        `gorm:"column:bill_to_address_street_line_2;null;size:100" json:"bill_to_address_street_line_2"`
	BillToAddressStreetLine3               string                        `gorm:"column:bill_to_address_street_line_3;null;size:100" json:"bill_to_address_street_line_3"`
	BillToPhoneNo                          string                        `gorm:"column:bill_to_phone_no;null;size:30" json:"bill_to_phone_no"`
	BillToFaxNo                            string                        `gorm:"column:bill_to_fax_no;null;size:30" json:"bill_to_fax_no"`
	TopId                                  int                           `gorm:"column:top_id;not null" json:"top_id"`                           // General
	BillCodeId                             int                           `gorm:"column:bill_code_id;null" json:"bill_code_id"`                   // Common
	TaxInvoiceTypeId                       int                           `gorm:"column:tax_invoice_type_id;not null" json:"tax_invoice_type_id"` // Common
	BillToTaxRegistrationNumber            string                        `gorm:"column:bill_to_tax_registration_number;not null" json:"bill_to_tax_registration_number"`
	BillToTaxRegistrationDate              time.Time                     `gorm:"column:bill_to_tax_registration_date;not null" json:"bill_to_tax_registration_date"`
	PkpType                                string                        `gorm:"column:pkp_type;null;type:char(1)" json:"pkp_type"`
	PkpNumber                              string                        `gorm:"column:pkp_number;not null;size:30" json:"pkp_number"`
	PkpDate                                time.Time                     `gorm:"column:pkp_date;not null" json:"pkp_date"`
	VatTransactionId                       int                           `gorm:"column:vat_transaction_id;not null" json:"vat_transaction_id"` // Common - Hengky
	TaxName                                string                        `gorm:"column:tax_name;not null;size:100" json:"tax_name"`
	TaxAddressId                           int                           `gorm:"column:tax_address_id;not null" json:"tax_address_id"` // General - Tyo
	TaxAddressStreetLine1                  string                        `gorm:"column:tax_address_street_line_1;null;size:100" json:"tax_address_street_line_1"`
	TaxAddressStreetLine2                  string                        `gorm:"column:tax_address_street_line_2;null;size:100" json:"tax_address_street_line_2"`
	TaxAddressStreetLine3                  string                        `gorm:"column:tax_address_street_line_3;null;size:100" json:"tax_address_street_line_3"`
	TotalCreditNoteBbn                     float64                       `gorm:"column:total_credit_note_bbn;null" json:"total_credit_note_bbn"`
	TotalDp                                float64                       `gorm:"column:total_dp;null" json:"total_dp"`
	TotalDpVat                             float64                       `gorm:"column:total_dp_vat;null" json:"total_dp_vat"`
	TotalDpAfterVat                        float64                       `gorm:"column:total_dp_after_vat;null" json:"total_dp_after_vat"`
	TotalUnitCogs                          float64                       `gorm:"column:total_unit_cogs;null" json:"total_unit_cogs"`
	TotalFreeAccessoriesCogs               float64                       `gorm:"column:total_free_accessories_cogs;null" json:"total_free_accessories_cogs"`
	TotalInsurance                         float64                       `gorm:"column:total_insurance;null" json:"total_insurance"`
	TotalMediatorFee                       float64                       `gorm:"column:total_mediator_fee;null" json:"total_mediator_fee"`
	TotalBbn                               float64                       `gorm:"column:total_bbn;null" json:"total_bbn"`
	Total                                  float64                       `gorm:"column:total;null" json:"total"`
	TotalDiscount                          float64                       `gorm:"column:total_discount;null" json:"total_discount"`
	TotalAfterDiscount                     float64                       `gorm:"column:total_after_discount;null" json:"total_after_discount"`
	TotalVat                               float64                       `gorm:"column:total_vat;null" json:"total_vat"`
	TotalVatBaseAmount                     float64                       `gorm:"column:total_vat_base_amount;null" json:"total_vat_base_amount"`
	TotalAfterVatBaseAmount                float64                       `gorm:"column:total_after_vat_base_amount;null" json:"total_after_vat_base_amount"`
	VatPercent                             float64                       `gorm:"vat_percent;null" json:"vat_percent"`
	TotalPpnbm                             float64                       `gorm:"column:total_ppnbm;null" json:"total_ppnbm"`
	TaxIndustryAmount                      float64                       `gorm:"column:tax_industry_amount;null" json:"tax_industry_amount"`
	Rounding                               float64                       `gorm:"column:rounding;null" json:"rounding"`
	TotalAfterVat                          float64                       `gorm:"column:total_after_vat;null" json:"total_after_vat"`
	AccountReceivableUnitDetail            []AccountReceivableUnitDetail `gorm:"foreignKey:InvoiceUnitSystemNumber;constraint:OnUpdate:CASCADE,OnDelete:CASCADE;references:invoice_unit_system_number" json:"trx_account_receivable_unit_details"`
	// VehicleId                              int       `gorm:"column:vehicle_id;null" json:"vehicle_id"`                                                 // Sales - Tyo
}

func (*AccountReceivableUnit) TableName() string {
	return TableNameAccountReceivableUnit
}
