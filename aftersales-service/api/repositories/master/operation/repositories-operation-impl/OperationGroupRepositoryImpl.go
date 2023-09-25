package masteroperationrepositoryimpl

import (
	masteroperationentities "after-sales/api/entities/master/operation"
	masteroperationpayloads "after-sales/api/payloads/master/operation"
	transactionoperationrepository "after-sales/api/repositories/master/operation"
	"after-sales/api/utils"
	"log"

	"gorm.io/gorm"
)

type OperationGroupRepositoryImpl struct {
	myDB *gorm.DB
}

func StartOperationGroupRepositoryImpl(db *gorm.DB) transactionoperationrepository.OperationGroupRepository {
	return &OperationGroupRepositoryImpl{myDB: db}
}

func (r *OperationGroupRepositoryImpl) WithTrx(trxHandle *gorm.DB) transactionoperationrepository.OperationGroupRepository {
	if trxHandle == nil {
		log.Println("Transaction Database Not Found!")
		return r
	}

	r.myDB = trxHandle
	return r
}

func (r *OperationGroupRepositoryImpl) GetAllOperationGroup(queryCriteria []utils.QueryCriteria, sortField utils.SortField, pages utils.Pagination) (utils.Pagination, error) {
	entities := []masteroperationentities.OperationGroup{}
	//init logger
	// newLogger := logger.New(
	// 	log.New(log.Writer(), "\r\n", log.LstdFlags),
	// 	logger.Config{
	// 		SlowThreshold: time.Second,
	// 		LogLevel:      logger.Info,
	// 		Colorful:      true,
	// 	},
	// )

	// r.myDB.Logger = newLogger

	paginatedQuery := utils.GetPaginationWithCriteria(r.myDB, &entities, queryCriteria, &sortField, &pages)
	rows, err := paginatedQuery.Scan(&entities).Rows()

	if len(entities) == 0 {
		return pages, gorm.ErrRecordNotFound
	}

	if err != nil {
		return pages, err
	}

	defer rows.Close()

	pages.Rows = entities

	return pages, nil
}

func (r *OperationGroupRepositoryImpl) GetAllOperationGroupIsActive() ([]masteroperationentities.OperationGroup, error) {
	var OperationGroups []masteroperationentities.OperationGroup

	err := r.myDB.Where("is_active = 'true'").Scan(&OperationGroups).Error

	if err != nil {
		return OperationGroups, err
	}

	return OperationGroups, nil
}

func (r *OperationGroupRepositoryImpl) GetOperationGroupById(Id int) (masteroperationpayloads.OperationGroupHeader, error) {
	entities := masteroperationentities.OperationGroup{}
	response := masteroperationpayloads.OperationGroupHeader{}

	rows, err := r.myDB.Model(&entities).
		Where(masteroperationentities.OperationGroup{
			OperationGroupId: Id,
		}).
		First(&response).
		Rows()

	if err != nil {
		return response, err
	}

	defer rows.Close()

	return response, nil
}

func (r *OperationGroupRepositoryImpl) GetOperationGroupByCode(Code string) (masteroperationpayloads.OperationGroupHeader, error) {
	entities := masteroperationentities.OperationGroup{}
	response := masteroperationpayloads.OperationGroupHeader{}

	rows, err := r.myDB.Model(&entities).
		Where(masteroperationentities.OperationGroup{
			OperationGroupCode: Code,
		}).
		First(&response).
		Rows()

	if err != nil {
		return response, err
	}

	defer rows.Close()

	return response, nil
}

func (r *OperationGroupRepositoryImpl) SaveOperationGroup(req masteroperationpayloads.OperationGroupHeader) (bool, error) {
	entities := masteroperationentities.OperationGroup{
		IsActive:                  req.IsActive,
		OperationGroupId:          req.OperationGroupId,
		OperationGroupCode:        req.OperationGroupCode,
		OperationGroupDescription: req.OperationGroupDescription,
	}

	err := r.myDB.Save(&entities).Error

	if err != nil {
		return false, gorm.ErrInvalidValueOfLength
	}

	return true, nil
}

func (r *OperationGroupRepositoryImpl) ChangeStatusOperationGroup(oprId int) (bool, error) {
	var entities masteroperationentities.OperationGroup

	result := r.myDB.Model(&entities).
		Where("operation_group_id = ?", oprId).
		First(&entities)

	if result.Error != nil {
		return false, result.Error
	}

	if entities.IsActive {
		entities.IsActive = false
	} else {
		entities.IsActive = true
	}

	result = r.myDB.Save(&entities)

	if result.Error != nil {
		return false, result.Error
	}

	return true, nil
}
