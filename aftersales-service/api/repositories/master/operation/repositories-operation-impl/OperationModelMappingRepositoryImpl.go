package masteroperationrepositoryimpl

import (
	masteroperationentities "after-sales/api/entities/master/operation"
	masteroperationpayloads "after-sales/api/payloads/master/operation"
	transactionoperationrepository "after-sales/api/repositories/master/operation"

	"gorm.io/gorm"
)

type OperationModelMappingRepositoryImpl struct {
	myDB *gorm.DB
}

func StartOperationModelMappingRepositoryImpl(db *gorm.DB) transactionoperationrepository.OperationModelMappingRepository {
	return &OperationModelMappingRepositoryImpl{myDB: db}
}

func (r *OperationModelMappingRepositoryImpl) GetOperationModelMappingById(Id int32) (masteroperationpayloads.OperationModelMappingResponse, error) {
	entities := masteroperationentities.OperationModelMapping{}
	response := masteroperationpayloads.OperationModelMappingResponse{}

	rows, err := r.myDB.Model(&entities).
		Where(masteroperationentities.OperationModelMapping{
			OperationModelMappingId: Id,
		}).
		First(&response).
		Rows()

	if err != nil {
		return response, err
	}

	defer rows.Close()

	return response, nil
}
