package masteroperationrepositoryimpl

import (
	masteroperationentities "after-sales/api/entities/master/operation"
	masteroperationpayloads "after-sales/api/payloads/master/operation"
	transactionoperationrepository "after-sales/api/repositories/master/operation"
	"log"

	"gorm.io/gorm"
)

type OperationEntriesRepositoryImpl struct {
	myDB *gorm.DB
}

func StartOperationEntriesRepositoryImpl(db *gorm.DB) transactionoperationrepository.OperationEntriesRepository {
	return &OperationEntriesRepositoryImpl{myDB: db}
}

func (r *OperationEntriesRepositoryImpl) WithTrx(trxHandle *gorm.DB) transactionoperationrepository.OperationEntriesRepository {
	if trxHandle == nil {
		log.Println("Transaction Database Not Found!")
		return r
	}
	r.myDB = trxHandle
	return r
}

func (r *OperationEntriesRepositoryImpl) GetOperationEntriesById(Id int32) (masteroperationpayloads.OperationEntriesResponse, error) {
	entities := masteroperationentities.OperationEntries{}
	response := masteroperationpayloads.OperationEntriesResponse{}

	rows, err := r.myDB.Model(&entities).
		Where(masteroperationentities.OperationEntries{
			OperationEntriesId: Id,
		}).
		First(&response).
		Rows()

	if err != nil {
		return response, err
	}

	defer rows.Close()

	return response, nil
}
