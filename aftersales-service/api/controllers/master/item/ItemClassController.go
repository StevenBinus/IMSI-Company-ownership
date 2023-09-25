package masteritemcontroller

import masteritemservice "after-sales/api/services/master/item"

type ItemClassController struct {
	ItemClassService masteritemservice.ItemClassService
}

func StartItemClassController(ItemClassService masteritemservice.ItemClassService)
