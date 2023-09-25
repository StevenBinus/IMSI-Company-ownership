package masterpayloads

type SaveBankBranchRequests struct {
	IsActive       bool   `json:"is_active"`
	BankBranchId   int    `json:"bank_branch_id"`
	BankId         int    `json:"bank_id"`
	BankBranchCode string `json:"bank_branch_code"`
	BankBranchName string `json:"bank_branch_name"`
	AddressId      int    `json:"address_id"`
}

type SaveBankBranchResponses struct {
	IsActive       bool   `json:"is_active"`
	BankBranchId   int    `json:"bank_branch_id"`
	BankId         int    `json:"bank_id"`
	BankBranchCode string `json:"bank_branch_code"`
	BankBranchName string `json:"bank_branch_name"`
	AddressId      int    `json:"address_id"`
}

type GetBankBranchRequests struct {
	IsActive       *bool  `json:"is_active"`
	BankBranchId   int    `json:"bank_branch_id"`
	BankId         int    `json:"bank_id"`
	BankCode       string `json:"bank_code"`
	BankBranchCode string `json:"bank_branch_code"`
	BankBranchName string `json:"bank_branch_name"`
	AddressId      int    `json:"address_id"`
}

type GetBankBranchResponses struct {
	IsActive       *bool  `json:"is_active"`
	BankBranchId   int    `json:"bank_branch_id"`
	BankId         int    `json:"bank_id"`
	BankCode       string `json:"bank_code"`
	BankBranchCode string `json:"bank_branch_code"`
	BankBranchName string `json:"bank_branch_name"`
	AddressId      int    `json:"address_id"`
}

type ChangeStatusBankBranchRequests struct {
	IsActive     bool `json:"is_active"`
	BankBranchId int  `json:"bank_id"`
}
