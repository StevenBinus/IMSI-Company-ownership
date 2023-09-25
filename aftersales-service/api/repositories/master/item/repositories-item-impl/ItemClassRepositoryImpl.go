package masteritemrepositoryimpl

import (
	masteritementities "after-sales/api/entities/master/item"
	masteritempayloads "after-sales/api/payloads/master/item"
	masteritemrepository "after-sales/api/repositories/master/item"
	"log"

	"gorm.io/gorm"
)

type ItemClassImpl struct {
	myDB *gorm.DB
}

func OpenItemClassRepoImpl(db *gorm.DB) masteritemrepository.ItemClassRepository {
	return &ItemClassImpl{myDB: db}
}

func (r *ItemClassImpl) GetAllItemClass() ([]masteritementities.ItemClass, error) {
	var results []masteritementities.ItemClass

	err := r.myDB.Find(&results)
	if err != nil {
		log.Fatal(err)
	}

	return results, nil
}

func (r *ItemClassImpl) GetItemClassByID(id int) (masteritementities.ItemClass, error) {
	var result masteritementities.ItemClass
	err := r.myDB.Find(&result, id)
	if err != nil {
		log.Fatal(err)
	}
	return result, nil
}

func (r *ItemClassImpl) CreateItemClass(reqdata masteritempayloads.ItemClassRequest) (bool, error) {
	var inp_data masteritementities.ItemClass
	inp_data.ItemClassCode = reqdata.ItemClassCode
	inp_data.ItemGroupID = reqdata.ItemGroupID
	inp_data.LineTypeID = reqdata.LineTypeID

	err := r.myDB.Create(&inp_data)
	if err != nil {
		log.Fatal(err)
	}
	return true, nil
}

func (r *ItemClassImpl) UpdateItemClass(id int, req masteritempayloads.ItemClassRequest) (bool, error) {
	res, _ := r.GetItemClassByID(id)

	res.ItemClassCode = req.ItemClassCode
	res.ItemGroupID = req.ItemGroupID
	res.LineTypeID = req.LineTypeID

	err := r.myDB.Save(&res)
	if err != nil {
		log.Fatal(err)
	}
	return true, nil
}

func (r *ItemClassImpl) PatchStatusItemClass(id int) (bool, error) {
	res, _ := r.GetItemClassByID(id)
	check_status := res.IsActive
	if check_status == true {
		res.IsActive = false
	} else {
		res.IsActive = true
	}
	err := r.myDB.Save(&res)
	if err != nil {
		log.Fatal((err.Error.Error()))
	}
	return true, nil
}
