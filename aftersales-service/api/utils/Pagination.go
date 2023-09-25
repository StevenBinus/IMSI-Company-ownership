package utils

import (
	"math"
	"reflect"

	"strings"

	"gorm.io/gorm"
)

type Pagination struct {
	Limit      int         `json:"limit,omitempty;query:limit"`
	Page       int         `json:"page,omitempty;query:page"`
	Sort       string      `json:"sort,omitempty;query:sort"`
	TotalRows  int64       `json:"total_rows"`
	TotalPages int         `json:"total_pages"`
	Rows       interface{} `json:"rows"`
}

type QueryCriteria struct {
	QueryOf string
	QueryBy string
}

type SortField struct {
	SortOf string
	SortBy string
}

// pagination function
func (p *Pagination) GetOffset() int {
	return (p.GetPage() - 1) * p.GetLimit()
}

func (p *Pagination) GetLimit() int {
	if p.Limit == 0 {
		p.Limit = 10
	}
	return p.Limit
}

func (p *Pagination) GetPage() int {
	if p.Page == 0 {
		p.Page = 1
	}
	return p.Page
}

func (p *Pagination) GetSort() string {
	// if p.Sort == "" {
	// 	p.Sort = "Id desc"
	// }
	return p.Sort
}

// sort function
func AddSort(SortOf string, SortBy string) string {
	return SortOf + " " + SortBy
}

// query of query by function
// QueryOfQueryBy function is to generate where conditions to match values from queryOf/values agains queryBy/columns
func QueryOfQueryBy(criteria []QueryCriteria) string {
	var queryWhere []string
	var queryOf, queryBy []string

	for _, c := range criteria {
		queryOf, queryBy = append(queryOf, c.QueryOf), append(queryBy, c.QueryBy)
	}

	for i := 0; i < len(queryOf); i++ {
		if queryBy[i] == "is_active" {
			n := map[string]string{"true": "1", "false": "0"}
			queryOf[i] = n[queryOf[i]]
		}
		condition := queryBy[i] + " LIKE " + "'%" + queryOf[i] + "%'"
		queryWhere = append(queryWhere, condition)
	}

	return strings.Join(queryWhere, " AND ")
}

// QueryOfQueryBy function is to generate where conditions to match values from queryOf/values agains queryBy/columns
// where it take struct tags from responseType (in this case entity tags and json tags) to make queryBy/columns (eg. <entity_name>.<column_name>)
// to prevent ambiguous column name when generate where conditions with joins
func QueryOfQueryByWithJoin(criteria []QueryCriteria, responseType reflect.Type) string {
	var queryOf, queryBy []string

	for _, c := range criteria {
		for i := 0; i < responseType.NumField(); i++ {
			if c.QueryBy == responseType.Field(i).Tag.Get("json") {
				queryOf = append(queryOf, c.QueryOf)
				queryBy = append(queryBy, responseType.Field(i).Tag.Get("entity")+"."+c.QueryBy)
			}
		}
	}
	var queryWhere []string
	for i := 0; i < len(queryOf); i++ {
		if queryBy[i] == "is_active" {
			n := map[string]string{"true": "1", "false": "0"}
			queryOf[i] = n[queryOf[i]]
		}
		condition := queryBy[i] + " LIKE " + "'%" + queryOf[i] + "%'"
		queryWhere = append(queryWhere, condition)
	}
	return strings.Join(queryWhere, " AND ")
}

// GetPaginationWithCriteria generates a paginated query for a GORM database based on provided criteria, sorting options, and pagination settings.
// It returns a GORM DB instance that you can further chain for querying.
func GetPaginationWithCriteria(db *gorm.DB, tableName interface{}, criteria []QueryCriteria, sortField *SortField, pagination *Pagination) *gorm.DB {
	var totalRows int64
	queryCheck := db.Model(tableName)

	//query of query by
	if len(criteria) > 0 {
		queryCheck.Where(QueryOfQueryBy(criteria))
	}

	//order by
	if sortField.SortOf != "" && sortField.SortBy != "" {
		queryCheck.Order(AddSort(sortField.SortOf, sortField.SortBy))
	}

	//pagination
	db.Model(tableName).Count(&totalRows)
	pagination.TotalRows = totalRows
	totalPages := int(math.Ceil(float64(totalRows) / float64(pagination.Limit)))
	pagination.TotalPages = totalPages

	queryCheck.Offset(pagination.GetOffset()).Limit(pagination.GetLimit())

	return queryCheck
}

// GetPaginationWithJoin generates a paginated query with JOIN operations for a GORM database based on provided criteria, sorting options, and pagination settings.
// It returns a GORM DB instance that you can further chain for querying.
func GetPaginationWithJoin(db *gorm.DB, tableName string, tableStruct interface{}, joinTableName map[string]string, criteria []QueryCriteria, sortField *SortField, pagination *Pagination) *gorm.DB {
	keyAttribute := []string{}
	responseType := reflect.TypeOf(tableStruct)
	joinTable := []string{}

	for i := 0; i < responseType.NumField(); i++ {
		keyAttribute = append(keyAttribute, responseType.Field(i).Tag.Get("entity")+"."+responseType.Field(i).Tag.Get("json"))
	}

	//query Table with select
	query := db.Table(tableName).Select(keyAttribute)

	//join Table
	for key, value := range joinTableName {
		joinTable = append(joinTable, "join "+key+" on "+tableName+"."+value+" = "+key+"."+value) 
	}
	query = query.Joins(strings.Join(joinTable, " "))

	//query of query by
	if len(criteria) > 0 {
		query.Where(QueryOfQueryByWithJoin(criteria, responseType))
	}

	//order by
	if sortField.SortOf != "" && sortField.SortBy != "" {
		query.Order(AddSort(sortField.SortOf, sortField.SortBy))
	}

	//pagination
	var totalRows int64
	db.Table(tableName).Joins(strings.Join(joinTable, " ")).Count(&totalRows)
	pagination.TotalRows = totalRows
	totalPages := int(math.Ceil(float64(totalRows) / float64(pagination.Limit)))
	pagination.TotalPages = totalPages
	query.Offset(pagination.GetOffset()).Limit(pagination.GetLimit())

	return query
}
