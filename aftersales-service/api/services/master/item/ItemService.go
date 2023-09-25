package masteritemservice

import (
	masteritempayloads "after-sales/api/payloads/master/item"
	"after-sales/api/utils"

	"gorm.io/gorm"
)

type ItemService interface {
	WithTrx(trxHandle *gorm.DB) ItemService
	GetAllItemLookup([]utils.QueryCriteria, utils.SortField, utils.Pagination) ([]masteritempayloads.ItemLookup, error)
	GetItemByIdTestingPurposes(int32) (masteritempayloads.ItemLookupTestingPurposes, error)
	GetAllItemLookupLoopTestingPurposes() ([]masteritempayloads.ItemLookupTestingPurposes, error)
	GetItemCode(string) (masteritempayloads.ItemResponse, error)
}
