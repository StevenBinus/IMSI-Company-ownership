package masteroperationrepositoryimpl

import (
	masteroperationentities "after-sales/api/entities/master/operation"
	masteroperationpayloads "after-sales/api/payloads/master/operation"
	transactionoperationrepository "after-sales/api/repositories/master/operation"
	"log"

	"gorm.io/gorm"
)

type OperationKeyRepositoryImpl struct {
	myDB *gorm.DB
}

func StartOperationKeyRepositoryImpl(db *gorm.DB) transactionoperationrepository.OperationKeyRepository {
	return &OperationKeyRepositoryImpl{myDB: db}
}

func (r *OperationKeyRepositoryImpl) WithTrx(trxHandle *gorm.DB) transactionoperationrepository.OperationKeyRepository {
	if trxHandle == nil {
		log.Println("Transaction Database Not Found!")
		return r
	}
	r.myDB = trxHandle
	return r
}

func (r *OperationKeyRepositoryImpl) GetOperationKeyById(Id int32) (masteroperationpayloads.OperationKeyResponse, error) {
	entities := masteroperationentities.OperationKey{}
	response := masteroperationpayloads.OperationKeyResponse{}

	rows, err := r.myDB.Model(&entities).
		Where(masteroperationentities.OperationKey{
			OperationKeyId: Id,
		}).
		First(&response).
		Rows()

	if err != nil {
		return response, err
	}

	defer rows.Close()

	return response, nil
}

func (r *OperationKeyRepositoryImpl) GetOperationKeyByCode(code string) (masteroperationpayloads.OperationKeyResponse, error) {
	entities := masteroperationentities.OperationKey{}
	response := masteroperationpayloads.OperationKeyResponse{}

	rows, err := r.myDB.Model(&entities).Where(masteroperationentities.OperationKey{OperationKeyCode: code}).First(&response).Rows()
	if err != nil {
		return response, err
	}
	defer rows.Close()

	return response, nil
}
