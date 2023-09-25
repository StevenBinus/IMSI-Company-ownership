package masterpayloads

type SaveBankContactRequests struct {
	IsActive        bool   `json:"is_active"`
	BankContactId   int    `json:"bank_contact_id"`
	BankBranchId    int    `json:"bank_branch_id"`
	ContactName     string `json:"contact_name"`
	ContactPosition string `json:"contact_posiion"`
	ContactPhone    string `json:"contact_phone"`
}

type SaveBankContactResponses struct {
	IsActive        bool   `json:"is_active"`
	BankContactId   int    `json:"bank_contact_id"`
	BankBranchId    int    `json:"bank_branch_id"`
	ContactName     string `json:"contact_name"`
	ContactPosition string `json:"contact_posiion"`
	ContactPhone    string `json:"contact_phone"`
}

type GetBankContactRequests struct {
	BankBranchId int `json:"bank_branch_id"`
}

type GetBankContactResponses struct {
	IsActive        *bool  `json:"is_active"`
	BankContactId   int    `json:"bank_contact_id"`
	BankBranchId    int    `json:"bank_branch_id"`
	ContactName     string `json:"contact_name"`
	ContactPosition string `json:"contact_posiion"`
	ContactPhone    string `json:"contact_phone"`
}

type ChangeStatusBankContactRequests struct {
	IsActive      bool `json:"is_active"`
	BankContactId int  `json:"bank_contact_id"`
}
