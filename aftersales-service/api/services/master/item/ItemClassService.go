package masteritemservice

import (
	masteritempayloads "after-sales/api/payloads/master/item"
)

type ItemClassService interface {
	GetAllItemClass() ([]masteritempayloads.ItemClassResponse, error)
	// GetItemClassByID(int) (masteritempayloads.ItemClassResponse, error)
	// CreateItemClass(req masteritempayloads.ItemClassRequest) (bool, error)
	// UpdateItemClass(int, req masteritempayloads.ItemClassRequest) (bool, error)
	// PatchStatusItemClass(id int) (bool, error)
}
