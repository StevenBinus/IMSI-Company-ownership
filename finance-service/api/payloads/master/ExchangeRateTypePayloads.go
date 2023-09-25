package masterpayloads

type SaveExchangeRateTypeRequest struct {
	IsActive 			bool	`json:"is_active"`
	ExchangeRateTypeId 	int     `gorm:"column:exchange_rate_type_id;not null;primaryKey" json:"exchange_rate_type_id"`
	ExchangeRateType	string	`json:"exchange_rate_type"`
	Description 		string	`json:"description"`
}

type GetAllExchangeRateTypeRequest struct {
	IsActive           string	`gorm:"column:is_active;default:true;not null" json:"is_active"`
	ExchangeRateTypeId int		`gorm:"column:exchange_rate_type_id;not null;primaryKey" json:"exchange_rate_type_id"`
	ExchangeRateType   string	`gorm:"column:exchange_rate_type;not null;type:varchar(10)" json:"exchange_rate_type"`
	Description        string	`gorm:"column:description;not null;type:varchar(35)" json:"description"`
}

type ChangeExchangeRateTypeStatusRequest struct {
	IsActive           string	`gorm:"column:is_active;default:true;not null" json:"is_active"`
	ExchangeRateTypeId int		`gorm:"column:exchange_rate_type_id;not null;primaryKey" json:"exchange_rate_type_id"`
}

type GetAllExchangeRateTypeHeaderResponse struct {
	IsActive 			string  `json:"is_active"`
	ExchangeRateTypeId  int 	`json:"exchange_rate_type_id"`
	ExchangeRateType   	string	`json:"exchange_rate_type"`
	Description     	string	`json:"description"`
}