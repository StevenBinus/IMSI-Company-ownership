package taxinvoiceentities

import "time"

const TableNameTaxInvoice = "trx_tax_invoice"

type TaxInvoice struct {
	TaxInvoiceSystemNumber              int32     `gorm:"column:tax_invoice_system_number;not null;primaryKey"        json:"tax_invoice_system_number"`
	CompanyId                           int32     `gorm:"column:company_id ;null"        json:"company_id "` //general
	TaxInvoiceDocumentNumber            string    `gorm:"column:tax_invoice_document_number;null"        json:"tax_invoice_document_number"`
	TaxInvoiceStatus                    string    `gorm:"column:tax_invoice_status;null"        json:"tax_invoice_status"`
	TaxInvoiceDate                      time.Time `gorm:"column:tax_invoice_date;null"        json:"tax_invoice_date"`
	TaxInvoicePeriodYear                string    `gorm:"column:tax_invoice_period_year;null"        json:"tax_invoice_period_year"`
	TaxInvoicePeriodMonth               string    `gorm:"column:tax_invoice_period_month;null"        json:"tax_invoice_period_month"`
	TaxExpirationPeriodYear             string    `gorm:"column:tax_expiration_period_year;null"        json:"tax_expiration_period_year"`
	TaxExpirationPeriodMonth            string    `gorm:"column:tax_expiration_period_month;null"        json:"tax_expiration_period_month"`
	TaxInvoiceId                        int32     `gorm:"column:tax_invoice_id;null"        json:"tax_invoice_id"`                     //common
	TaxInvoiceFlowTypeId                int32     `gorm:"column:tax_invoice_flow_type_id;null"        json:"tax_invoice_flow_type_id"` //common
	TaxInvoiceRevisionType              string    `gorm:"column:tax_invoice_revision_type;null"        json:"tax_invoice_revision_type"`
	TaxInvoiceSalesTypeId               int32     `gorm:"column:tax_invoice_sales_type_id;null"        json:"tax_invoice_sales_type_id"` // common
	ReferenceType                       string    `gorm:"column:reference_type;null"        json:"reference_type"`
	ReferenceSystemNumber               int32     `gorm:"column:reference_system_number;null"        json:"reference_system_number"`
	ReferenceDocumentNumber             string    `gorm:"column:reference_document_number;null"        json:"reference_document_number"`
	ReferenceDocumentDate               time.Time `gorm:"column:reference_document_date;null"        json:"reference_document_date"`
	ReferenceLineNumber                 int32     `gorm:"column:reference_line_number;null"        json:"reference_line_number"`
	Reference2Type                      string    `gorm:"column:reference2_type;null"        json:"reference2_type"`
	Reference2SystemNumber              int32     `gorm:"column:reference2_system_number;null"        json:"reference2_system_number"`
	Reference2DocumentNumber            string    `gorm:"column:reference2_document_number;null"        json:"reference2_document_number"`
	Reference2DocumentDate              time.Time `gorm:"column:reference2_document_date;null"        json:"reference2_document_date"`
	Reference2Line                      int32     `gorm:"column:reference2_line;null"        json:"reference2_line"`
	BrandId                             int32     `gorm:"column:brand_id;null"        json:"brand_id"`                 //sales
	ProfitCenterId                      int32     `gorm:"column:profit_center_id;null"        json:"profit_center_id"` //general
	CompanyTaxRegistrationNumber        string    `gorm:"column:company_tax_registration_number;null"        json:"company_tax_registration_number"`
	CompanyTaxName                      string    `gorm:"column:company_tax_name;null"        json:"company_tax_name"`
	CompanyTaxAddressId                 string    `gorm:"column:COMPANY_TAX_ADDRESS_ID ;null"        json:"COMPANY_TAX_ADDRESS_ID "` //general
	CompanyTaxPkpNumber                 string    `gorm:"column:company_tax_pkp_number;null"        json:"company_tax_pkp_number"`
	CompanyTaxPkpDate                   time.Time `gorm:"column:company_tax_pkp_date;null"        json:"company_tax_pkp_date"`
	CompanyTaxCityCode                  string    `gorm:"column:company_tax_city_code;null"        json:"company_tax_city_code"`
	CompanyTaxZipCode                   string    `gorm:"column:company_tax_zip_code;null"        json:"company_tax_zip_code"`
	SupplierId                          int32     `gorm:"column:supplier_id;null"        json:"supplier_id"` //general
	CustomerId                          int32     `gorm:"column:customer_id;null"        json:"customer_id"` //general
	TaxRegistrationNumber               string    `gorm:"column:tax_registration_number;null"        json:"tax_registration_number"`
	TaxName                             string    `gorm:"column:tax_name;null"        json:"tax_name"`
	TaxAddressId                        string    `gorm:"column:TAX_ADDRESS_ID ;null"        json:"TAX_ADDRESS_ID "` //General
	TaxPkpNumber                        string    `gorm:"column:tax_pkp_number;null"        json:"tax_pkp_number"`
	TaxPkpDate                          time.Time `gorm:"column:tax_pkp_date;null"        json:"tax_pkp_date"`
	TaxInvoiceDateOriginal              time.Time `gorm:"column:tax_invoice_date_original;null"        json:"tax_invoice_date_original"`
	SupplierCodeOriginal                string    `gorm:"column:supplier_code_original;null"        json:"supplier_code_original"`
	SupplierNameOriginal                string    `gorm:"column:supplier_name_original;null"        json:"supplier_name_original"`
	CustomerCodeOriginal                string    `gorm:"column:customer_code_original;null"        json:"customer_code_original"`
	CustomerNameOriginal                string    `gorm:"column:customer_name_original;null"        json:"customer_name_original"`
	TaxAddressOriId                     string    `gorm:"column:TAX_ADDRESS_ORI_ID ;null"        json:"TAX_ADDRESS_ORI_ID "` //General
	TaxRegistrationNumberOriginal       string    `gorm:"column:tax_registration_number_original;null"        json:"tax_registration_number_original"`
	TaxPkpNumberOriginal                string    `gorm:"column:tax_pkp_number_original;null"        json:"tax_pkp_number_original"`
	CurrencyId                          int32     `gorm:"column:currency_id;null"        json:"currency_id"` //Finance
	CurrencyExchangeRateType            string    `gorm:"column:currency_exchange_rate_type;null"        json:"currency_exchange_rate_type"`
	CurrencyExchangeRateDate            time.Time `gorm:"column:currency_exchange_rate_date;null"        json:"currency_exchange_rate_date"`
	CurrencyExchangeRate                float64   `gorm:"column:currency_exchange_rate;null"        json:"currency_exchange_rate"`
	ReferenceTaxInvoiceSystemNumber     int32     `gorm:"column:reference_tax_invoice_system_number;null"        json:"reference_tax_invoice_system_number"`
	ReferenceTaxInvoiceDocumentNumber   string    `gorm:"column:reference_tax_invoice_document_number;null"        json:"reference_tax_invoice_document_number"`
	TaxInvoiceTransactionType           string    `gorm:"column:tax_invoice_transaction_type;null"        json:"tax_invoice_transaction_type"`
	TaxInvoiceTransactionCodeId         int32     `gorm:"column:tax_invoice_transaction_code_id;null"        json:"tax_invoice_transaction_code_id"` //Common
	TaxInvoiceTransactionDocumentNumber string    `gorm:"column:tax_invoice_transaction_document_number;null"        json:"tax_invoice_transaction_document_number"`
	Replaced                            bool      `gorm:"column:replaced;null"        json:"replaced"`
	Exported                            bool      `gorm:"column:exported;null"        json:"exported"`
	Total                               float64   `gorm:"column:total;null"        json:"total"`
	TotalBaseAmount                     float64   `gorm:"column:total_base_amount;null"        json:"total_base_amount"`
	TotalDiscount                       float64   `gorm:"column:total_discount;null"        json:"total_discount"`
	TotalDiscountBaseAmount             float64   `gorm:"column:total_discount_base_amount;null"        json:"total_discount_base_amount"`
	TotalDp                             float64   `gorm:"column:total_dp;null"        json:"total_dp"`
	TotalDpBaseAmount                   float64   `gorm:"column:total_dp_base_amount;null"        json:"total_dp_base_amount"`
	TotalAfterDiscount                  float64   `gorm:"column:total_after_discount;null"        json:"total_after_discount"`
	TotalAfterDiscountBaseAmount        float64   `gorm:"column:total_after_discount_base_amount;null"        json:"total_after_discount_base_amount"`
	TotalVat                            float64   `gorm:"column:total_vat;null"        json:"total_vat"`
	TotalVatBaseAmount                  float64   `gorm:"column:total_vat_base_amount;null"        json:"total_vat_base_amount"`
	TotalAfterVat                       float64   `gorm:"column:total_after_vat;null"        json:"total_after_vat"`
	TotalAfterVatBaseAmount             float64   `gorm:"column:total_after_vat_base_amount;null"        json:"total_after_vat_base_amount"`
	Ppnbm                               float64   `gorm:"column:ppnbm;null"        json:"ppnbm"`
	PpnbmOriginal                       float64   `gorm:"column:ppnbm_original;null"        json:"ppnbm_original"`
	VatCode                             string    `gorm:"column:vat_code;null"        json:"vat_code"`
	VatPercent                          float64   `gorm:"column:vat_percent;null"        json:"vat_percent"`
	VatTaxType                          string    `gorm:"column:vat_tax_type;null"        json:"vat_tax_type"`
	VatTaxServiceCode                   string    `gorm:"column:vat_tax_service_code;null"        json:"vat_tax_service_code"`
	PrintingNumber                      int32     `gorm:"column:printing_number;null"        json:"printing_number"`
	LastPrintedBy                       string    `gorm:"column:last_printed_by;null"        json:"last_printed_by"`
	RevisionReason                      string    `gorm:"column:revision_reason;null"        json:"revision_reason"`
	ReferenceSourceCode                 string    `gorm:"column:reference_source_code;null"        json:"reference_source_code"`
	ReferenceVehicleBrand               string    `gorm:"column:reference_vehicle_brand;null"        json:"reference_vehicle_brand"`
	ReferenceCpcCode                    string    `gorm:"column:reference_cpc_code;null"        json:"reference_cpc_code"`
	ReferenceTransactionCode            string    `gorm:"column:reference_transaction_code;null"        json:"reference_transaction_code"`
	ReferenceBankAccountCode            string    `gorm:"column:reference_bank_account_code;null"        json:"reference_bank_account_code"`
	TaxNameOriginal                     string    `gorm:"column:tax_name_original;null"        json:"tax_name_original"`
	TotalTaxIndustryAmount              float64   `gorm:"column:total_tax_industry_amount;null"        json:"total_tax_industry_amount"`
	TotalTaxIndustryBaseAmount          float64   `gorm:"column:total_tax_industry_base_amount;null"        json:"total_tax_industry_base_amount"`
	LastChangeNumber                    string    `gorm:"column:last_change_number;null"        json:"last_change_number"`
	LastChangeNumberDatetime            time.Time `gorm:"column:last_change_number_datetime;null"        json:"last_change_number_datetime"`
	TaxDirectDocumentNumber             string    `gorm:"column:tax_direct_document_number;null"        json:"tax_direct_document_number"`
	TaxDirectTransactionType            string    `gorm:"column:tax_direct_transaction_type;null"        json:"tax_direct_transaction_type"`
	TaxDirectEventNumber                string    `gorm:"column:tax_direct_event_number;null"        json:"tax_direct_event_number"`
	JournalSystemNumber                 int32     `gorm:"column:journal_system_number;null"        json:"journal_system_number"` //Finance
	CostCenterCode                      string    `gorm:"column:cost_center_code;null"        json:"cost_center_code"`
	Remark                              string    `gorm:"column:remark;null"        json:"remark"`
	Efexported                          bool      `gorm:"column:efexported;null"        json:"efexported"`
	EfexportedId                        string    `gorm:"column:efexported_id;null"        json:"efexported_id"` //General
	EfexportedDate                      time.Time `gorm:"column:efexported_date;null"        json:"efexported_date"`
	EfexportedVoidId                    string    `gorm:"column:efexported_void_id;null"        json:"efexported_void_id"` // General
	EfexportedVoidDate                  time.Time `gorm:"column:efexported_void_date;null"        json:"efexported_void_date"`
}
