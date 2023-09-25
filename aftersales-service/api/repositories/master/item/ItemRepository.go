package masteritemrepository

import (
	masteritempayloads "after-sales/api/payloads/master/item"
	"after-sales/api/utils"

	"gorm.io/gorm"
)

type ItemRepository interface {
	WithTrx(trxHandle *gorm.DB) ItemRepository
	GetItemCode(string) (masteritempayloads.ItemResponse, error)
	GetItemByIdTestingPurposes(int32) (masteritempayloads.ItemLookupTestingPurposes, error)
	GetAllItemLookupLoopTestingPurposes() ([]masteritempayloads.ItemLookupTestingPurposes, error)
	GetAllItemLookup(queryCriteria []utils.QueryCriteria, sortField utils.SortField, pages utils.Pagination) ([]masteritempayloads.ItemLookup, error)
}
