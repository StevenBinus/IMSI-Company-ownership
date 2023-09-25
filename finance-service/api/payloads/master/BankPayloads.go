package masterpayloads

type SaveBankRequests struct {
	IsActive bool   `json:"is_active"`
	BankId   int    `json:"bank_id"`
	BankCode string `json:"bank_code"`
	BankName string `json:"bank_name"`
	BankAbbr string `json:"bank_abbr"`
}

type GetBankRequests struct {
	IsActive *bool  `json:"is_active"`
	BankId   int    `json:"bank_id"`
	BankCode string `json:"bank_code"`
	BankName string `json:"bank_name"`
	BankAbbr string `json:"bank_abbr"`
}

type GetBankResponses struct {
	IsActive *bool  `json:"is_active"`
	BankId   int    `json:"bank_id"`
	BankCode string `json:"bank_code"`
	BankName string `json:"bank_name"`
	BankAbbr string `json:"bank_abbr"`
}

type ChangeStatusBankRequests struct {
	IsActive bool `json:"is_active"`
	BankId   int  `json:"bank_id"`
}
