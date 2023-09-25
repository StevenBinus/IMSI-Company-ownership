package masteritemrepository

import (
	masteritementities "after-sales/api/entities/master/item"
	masteritempayloads "after-sales/api/payloads/master/item"
)

type ItemClassRepository interface {
	GetAllItemClass() ([]masteritementities.ItemClass, error)
	GetItemClassByID(id int) (masteritementities.ItemClass, error)
	CreateItemClass(req masteritempayloads.ItemClassRequest) (bool, error)
	UpdateItemClass(id int, req masteritempayloads.ItemClassRequest) (bool, error)
	PatchStatusItemClass(id int) (bool, error)
}
