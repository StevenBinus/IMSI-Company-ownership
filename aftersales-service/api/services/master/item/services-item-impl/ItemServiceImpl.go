package masteritemserviceimpl

import (
	masteritempayloads "after-sales/api/payloads/master/item"
	masteritemrepository "after-sales/api/repositories/master/item"
	masteritemservice "after-sales/api/services/master/item"
	"after-sales/api/utils"

	"gorm.io/gorm"
)

type ItemServiceImpl struct {
	itemRepo masteritemrepository.ItemRepository
}

func StartItemService(itemRepo masteritemrepository.ItemRepository) masteritemservice.ItemService {
	return &ItemServiceImpl{
		itemRepo: itemRepo,
	}
}

func (s *ItemServiceImpl) WithTrx(trxHandle *gorm.DB) masteritemservice.ItemService {
	s.itemRepo = s.itemRepo.WithTrx(trxHandle)
	return s
}

func (s *ItemServiceImpl) GetAllItemLookup(queryCriteria []utils.QueryCriteria, sortField utils.SortField, pages utils.Pagination) ([]masteritempayloads.ItemLookup, error) {
	var responses []masteritempayloads.ItemLookup
	results, err := s.itemRepo.GetAllItemLookup(queryCriteria, sortField, pages)
	if err != nil {
		return responses, err
	}
	for _, value := range results {
		response := masteritempayloads.ItemLookup{
			IsActive:    value.IsActive,
			ItemId:      value.ItemId,
			ItemCode:    value.ItemCode,
			ItemClassId: value.ItemClassId,
			ItemName:    value.ItemName,
			ItemGroupId: value.ItemGroupId,
			SupplierId:  value.SupplierId,
		}
		responses = append(responses, response)
	}
	return responses, nil
}

func (s *ItemServiceImpl) GetItemByIdTestingPurposes(id int32) (masteritempayloads.ItemLookupTestingPurposes, error) {
	value, err := s.itemRepo.GetItemByIdTestingPurposes(id)
	if err != nil {
		return masteritempayloads.ItemLookupTestingPurposes{}, err
	}
	return value, nil
}

func (s *ItemServiceImpl) GetAllItemLookupLoopTestingPurposes() ([]masteritempayloads.ItemLookupTestingPurposes, error) {
	var responses []masteritempayloads.ItemLookupTestingPurposes
	results, err := s.itemRepo.GetAllItemLookupLoopTestingPurposes()
	if err != nil {
		return responses, err
	}

	for _, value := range results {
		response := masteritempayloads.ItemLookupTestingPurposes{
			ItemId:      value.ItemId,
			ItemGroupId: value.ItemGroupId,
		}
		responses = append(responses, response)
	}
	return responses, nil
}

func (s *ItemServiceImpl) GetItemCode(code string) (masteritempayloads.ItemResponse, error) {
	results, err := s.itemRepo.GetItemCode(code)
	if err != nil {
		return results, err
	}
	return results, nil
}
