package masterpayloads

type CurrencyCodeRequest struct {
	CurrencyCode          string `json:"currency_code"`
	Description           string `json:"description"`
	CompanyBankFormatType int    `json:"comp_bank_format_type"`
}

type CurrencyCodeResponses struct {
	IsActive           bool   `json:"is_active"`
	CurrencyID         int    `json:"currency_id"`
	CurrencyCode       string `json:"currency_code"`
	CurrencyName       string `json:"currency_name"`
	CompBankFormatType int    `json:"comp_bank_format_type"`
}
