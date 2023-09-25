package masteritemserviceimpl

import (
	masteritempayloads "after-sales/api/payloads/master/item"
	masteritemrepository "after-sales/api/repositories/master/item"
	masteritemservice "after-sales/api/services/master/item"
	"log"
)

type ItemClassServiceImpl struct {
	ItemClassRepo masteritemrepository.ItemClassRepository
}

func StartItemClassService(itemclassrepo masteritemrepository.ItemClassRepository) masteritemservice.ItemClassService {
	return &ItemClassServiceImpl{
		ItemClassRepo: itemclassrepo,
	}
}

func (s *ItemClassServiceImpl) GetAllItemClass() ([]masteritempayloads.ItemClassResponse, error) {
	var results []masteritempayloads.ItemClassResponse

	res, err := s.ItemClassRepo.GetAllItemClass()
	if err != nil {
		log.Fatal(err)
	}

	for _, value := range res {
		response := masteritempayloads.ItemClassResponse{
			IsActive:      value.IsActive,
			ID:            value.ItemClassId,
			ItemClassCode: value.ItemClassCode,
			ItemGroupID:   value.ItemGroupID,
			LineTypeID:    value.LineTypeID,
		}
		results = append(results, response)
	}

	return results, nil
}
