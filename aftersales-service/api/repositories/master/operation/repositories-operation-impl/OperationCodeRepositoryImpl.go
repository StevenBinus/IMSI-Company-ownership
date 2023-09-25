package masteroperationrepositoryimpl

import (
	masteroperationentities "after-sales/api/entities/master/operation"
	masteroperationpayloads "after-sales/api/payloads/master/operation"
	transactionoperationrepository "after-sales/api/repositories/master/operation"
	"log"

	"gorm.io/gorm"
)

type OperationCodeRepositoryImpl struct {
	myDB *gorm.DB
}

func StartOperationCodeRepositoryImpl(db *gorm.DB) transactionoperationrepository.OperationCodeRepository {
	return &OperationCodeRepositoryImpl{myDB: db}
}

func (r *OperationCodeRepositoryImpl) WithTrx(trxHandle *gorm.DB) transactionoperationrepository.OperationCodeRepository {
	if trxHandle == nil {
		log.Println("Transaction Database Not Found!")
		return r
	}
	r.myDB = trxHandle
	return r
}

func (r *OperationCodeRepositoryImpl) GetOperationCodeById(Id int32) (masteroperationpayloads.OperationCodeResponse, error) {
	entities := masteroperationentities.OperationCode{}
	response := masteroperationpayloads.OperationCodeResponse{}

	rows, err := r.myDB.Model(&entities).
		Where(masteroperationentities.OperationCode{
			OperationId: Id,
		}).
		First(&response).
		Rows()

	if err != nil {
		return response, err
	}

	defer rows.Close()

	return response, nil
}
