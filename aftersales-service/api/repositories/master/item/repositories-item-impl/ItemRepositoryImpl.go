package masteritemrepositoryimpl

import (
	masteritementities "after-sales/api/entities/master/item"
	masteritempayloads "after-sales/api/payloads/master/item"
	masteritemrepository "after-sales/api/repositories/master/item"
	"after-sales/api/utils"
	"log"
	"time"

	"gorm.io/gorm"
	"gorm.io/gorm/logger"
)

type ItemRepositoryImpl struct {
	myDB *gorm.DB
}

func StartItemRepositoryImpl(db *gorm.DB) masteritemrepository.ItemRepository {
	return &ItemRepositoryImpl{myDB: db}
}

func (r *ItemRepositoryImpl) WithTrx(trxHandle *gorm.DB) masteritemrepository.ItemRepository {
	if trxHandle == nil {
		log.Println("Transaction Database Not Found!")
		return r
	}
	r.myDB = trxHandle
	return r
}

func (r *ItemRepositoryImpl) GetAllItemLookup(queryCriteria []utils.QueryCriteria, sortField utils.SortField, pages utils.Pagination) ([]masteritempayloads.ItemLookup, error) {
	var responses []masteritempayloads.ItemLookup

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
	tableName := "mtr_item"
	// table struct
	tableStruct := masteritempayloads.ItemLookup{}

	// Define the join table using map
	joinTableName := make(map[string]string)

	joinTableName["mtr_item_class"] = "item_class_id"

	paginatedQuery := utils.GetPaginationWithJoin(r.myDB, tableName, tableStruct, joinTableName, queryCriteria, &sortField, &pages)

	rows, err := paginatedQuery.Scan(&responses).Rows()
	if err != nil {
		return responses, err
	}
	defer rows.Close()

	return responses, nil
}

func (r *ItemRepositoryImpl) GetItemCode(code string) (masteritempayloads.ItemResponse, error) {
	entities := masteritementities.Item{}
	response := masteritempayloads.ItemResponse{}

	rows, err := r.myDB.Model(&entities).
		Where(masteritementities.Item{
			ItemCode: code,
		}).First(&response).Rows()
	if err != nil {
		return response, err
	}
	defer rows.Close()

	return response, nil
}

func (r *ItemRepositoryImpl) GetItemByIdTestingPurposes(Id int32) (masteritempayloads.ItemLookupTestingPurposes, error) {
	entities := masteritementities.Item{}
	response := masteritempayloads.ItemLookupTestingPurposes{}

	err := r.myDB.Model(&entities).
		Where(masteritementities.Item{
			ItemId: Id,
		}).
		First(&response).Error
	if err != nil {
		return response, err
	}
	return response, nil
}

func (r *ItemRepositoryImpl) GetAllItemLookupLoopTestingPurposes() ([]masteritempayloads.ItemLookupTestingPurposes, error) {
	entities := masteritementities.Item{}
	response := []masteritempayloads.ItemLookupTestingPurposes{}

	rows, err := r.myDB.Model(&entities).Scan(&response).Rows()
	if err != nil {
		return response, err
	}

	defer rows.Close()

	return response, nil
}
