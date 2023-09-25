package masteroperationrepositoryimpl

import (
	masteroperationentities "after-sales/api/entities/master/operation"
	masteroperationpayloads "after-sales/api/payloads/master/operation"
	transactionoperationrepository "after-sales/api/repositories/master/operation"
	"time"

	"after-sales/api/utils"
	"log"

	"gorm.io/gorm"
	"gorm.io/gorm/logger"
)

type OperationSectionRepositoryImpl struct {
	myDB *gorm.DB
}

func StartOperationSectionRepositoryImpl(db *gorm.DB) transactionoperationrepository.OperationSectionRepository {
	return &OperationSectionRepositoryImpl{myDB: db}
}

func (r *OperationSectionRepositoryImpl) GetAllOperationSection() ([]masteroperationentities.OperationSection, error) {
	var OperationSections []masteroperationentities.OperationSection
	err := r.myDB.Find(&OperationSections).Error
	if err != nil {
		log.Fatal(err)
	}
	return OperationSections, nil
}

func (r *OperationSectionRepositoryImpl) GetAllOperationSectionList(queryCriteria []utils.QueryCriteria, sortField utils.SortField, pages utils.Pagination) (utils.Pagination, error) {

	var responses []masteroperationpayloads.OperationSectionListResponse

	//init logger
	newLogger := logger.New(
		log.New(log.Writer(), "\r\n", log.LstdFlags),
		logger.Config{
			SlowThreshold: time.Second,
			LogLevel:      logger.Info,
			Colorful:      true,
		},
	)

	r.myDB.Logger = newLogger

	// table name
	tableName := "mtr_operation_section"
	// table struct
	tableStruct := masteroperationpayloads.OperationSectionListResponse{}

	// Define the join table using map
	joinTableName := make(map[string]string)
	//key = "join entity name" || value = "join entity id name
	joinTableName["mtr_operation_group"] = "operation_group_id"

	paginatedQuery := utils.GetPaginationWithJoin(r.myDB, tableName, tableStruct, joinTableName, queryCriteria, &sortField, &pages)

	rows, err := paginatedQuery.Scan(&responses).Rows()

	if err != nil {
		return pages, err
	}

	defer rows.Close()

	pages.Rows = responses

	return pages, nil

}

func (r *OperationSectionRepositoryImpl) GetOperationSectionDescription(groupCode string, sectionCode string) (masteroperationpayloads.OperationSectionDescriptionResponse, error) {
	entities := masteroperationentities.OperationSection{}
	response := masteroperationpayloads.OperationSectionDescriptionResponse{}

	row, err := r.myDB.Model(&entities).
		Table("mtr_operation_section").
		Select("operation_section_description").
		Joins("join mtr_operation_group on mtr_operation_section.operation_section_id = mtr_operation_group.operation_group_id").
		Where("operation_section_code = ? AND operation_group_code = ?", sectionCode, groupCode).
		First(&response).
		Rows()

	if err != nil {
		return response, err
	}

	defer row.Close()

	return response, nil
}

// func (r *OperationSectionRepositoryImpl) GetAllOperationSectionList(queryCriteria []utils.QueryCriteria, sortField utils.SortField, pages utils.Pagination) ([]masteroperationpayloads.OperationSectionListResponse, error) {

// 	var response []masteroperationpayloads.OperationSectionListResponse

// 	//init logger
// 	newLogger := logger.New(
// 		log.New(log.Writer(), "\r\n", log.LstdFlags),
// 		logger.Config{
// 			SlowThreshold: time.Second,
// 			LogLevel:      logger.Info,
// 			Colorful:      true,
// 		},
// 	)

// 	r.myDB.Logger = newLogger

// 	// Define the table name and fields you want to select
// 	tableName := "mtr_operation_section mos"
// 	selectFields := []string{
// 		"operation_section_description",
// 		"mos.is_active",
// 		"mos.operation_section_id",
// 		"mos.operation_section_code",
// 		"mos.operation_group_id",
// 		"mos.operation_section_description",
// 		"mog.operation_group_code",
// 		"mog.operation_group_description",
// 	}

// 	// Define the join table and condition
// 	joinTable := []string{"join mtr_operation_group mog on mog.operation_group_id = mos.operation_group_id"}

// 	paginatedQuery := utils.GetPaginationWithJoin(r.myDB, tableName, selectFields, joinTable, queryCriteria, &sortField, &pages)

// 	rows, err := paginatedQuery.Scan(&response).Rows()

// 	//row, err := r.myDB.
// 	// 	Table("mtr_operation_section mos").
// 	// 	Select("operation_section_description",
// 	// 		"mos.is_active",
// 	// 		"mos.operation_section_id",
// 	// 		"mos.operation_section_code",
// 	// 		"mos.operation_group_id",
// 	// 		"mos.operation_section_description",
// 	// 		"mog.operation_group_code",
// 	// 		"mog.operation_group_description").
// 	// 	Joins("join mtr_operation_group mog on mog.operation_group_id = mos.operation_group_id").
// 	// 	Scan(&response).
// 	// 	Rows()

// 	if err != nil {
// 		return response, err
// 	}

// 	defer rows.Close()

// 	return response, nil

// }

func (r *OperationSectionRepositoryImpl) GetOperationSectionById(Id int) (masteroperationpayloads.OperationSectionResponse, error) {
	entities := masteroperationentities.OperationSection{}
	response := masteroperationpayloads.OperationSectionResponse{}

	rows, err := r.myDB.Model(&entities).
		Where(masteroperationentities.OperationSection{
			OperationSectionId: Id,
		}).
		First(&response).
		Rows()

	if err != nil {
		return response, err
	}

	defer rows.Close()

	return response, nil
}

func (r *OperationSectionRepositoryImpl) SaveOperationSection(req masteroperationpayloads.OperationSectionRequest) (bool, error) {
	entities := masteroperationentities.OperationSection{
		IsActive:                    req.IsActive,
		OperationSectionId:          req.OperationSectionId,
		OperationSectionCode:        req.OperationSectionCode,
		OperationGroupId:            req.OperationGroupId,
		OperationSectionDescription: req.OperationSectionDescription,
	}

	err := r.myDB.Save(&entities).Error

	if err != nil {
		return false, gorm.ErrInvalidValueOfLength
	}

	return true, nil

}

func (r *OperationSectionRepositoryImpl) ChangeStatusOperationSection(Id int) (bool, error) {
	var entities masteroperationentities.OperationSection
	result := r.myDB.Model(&entities).
		Where("operation_section_id = ?", Id).
		First(&entities)

	if result.Error != nil {
		return false, result.Error
	}

	// Toggle the IsActive value
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
