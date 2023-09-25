package masteritemcontroller

import (
	"after-sales/api/exceptions"
	"after-sales/api/middlewares"
	"after-sales/api/payloads"
	masteritempayloads "after-sales/api/payloads/master/item"
	"after-sales/api/utils"

	// "after-sales/api/middlewares"

	masteritemservice "after-sales/api/services/master/item"
	"net/http"
	"strconv"

	"github.com/gin-gonic/gin"
	"gorm.io/gorm"
)

type ItemController struct {
	itemservice masteritemservice.ItemService
}

func StartItemRoutes(
	db *gorm.DB,
	r *gin.RouterGroup,
	itemservice masteritemservice.ItemService,
) {
	itemHandler := ItemController{itemservice: itemservice}
	r.GET("/item/get-lookup", middlewares.DBTransactionMiddleware(db), itemHandler.GetAllItemLookup)
	r.GET("/item/:item_code", middlewares.DBTransactionMiddleware(db), itemHandler.GetItemByCode)
}

// @Summary Get Item By Lookup
// @Description REST API Item
// @Accept json
// @Produce json
// @Tags Item
// @Param limit query string true "Limit"
// @Param page query string true "Page"
// @Param sort_of query string false "sort_of"
// @Param sort_by query string false "sort_by"
// @Success 200 {object} payloads.Response
// @Failure 500,400,401,404,403,422 {object} exceptions.Error
// @Router /api/master/item/get-lookup [get]
func (r *ItemController) GetAllItemLookup(c *gin.Context) {
	trxHandle := c.MustGet("db_trx").(*gorm.DB)
	var responses []masteritempayloads.ItemLookupDisplay
	//queryParams sementar masih dikosongin untuk testing
	queryParams := map[string]string{}

	sortField := utils.SortField{
		SortOf: c.Query("sort_of"),
		SortBy: c.Query("sort_by"),
	}

	pagination := utils.Pagination{
		Limit: utils.GetQueryInt(c, "limit"),
		Page:  utils.GetQueryInt(c, "page"),
	}

	criteria := utils.BuildQueryCriteria(queryParams)

	result, err := r.itemservice.WithTrx(trxHandle).GetAllItemLookup(criteria, sortField, pagination)

	for _, value := range result {

		itemGroupName, err := r.GetItemGroup(c, int(value.ItemGroupId), "item_group_name")
		if err != nil {
			exceptions.AppException(c, err.Error())
			return
		}
		//soon mau update codenya buat get 2 key value dengan 1 id yang sama
		// supplierCode, supplierName, err := r.GetSupplier(c, int(value.SupplierId), "supplier_code", "supplier_name")
		// if err != nil {
		// 	exceptions.AppException(c, err.Error())
		// 	return
		// }
		response := masteritempayloads.ItemLookupDisplay{
			ItemId:        value.ItemId,
			ItemCode:      value.ItemCode,
			ItemName:      value.ItemName,
			ItemGroupName: itemGroupName,
			// SupplierCode: supplierCode,
			// SupplierName: supplierName,
		}
		responses = append(responses, response)
	}
	if err != nil {
		exceptions.NotFoundException(c, err.Error())
		return
	}
	payloads.HandleSuccess(c, responses, "success", http.StatusOK)
}

// @Summary Get Item By code
// @Description REST API Item
// @Accept json
// @Produce json
// @Tags Item
// @Param item_code path string true "item_code"
// @Success 200 {object} payloads.Response
// @Failure 500,400,401,404,403,422 {object} exceptions.Error
// @Router /api/master/item/{item_code} [get]
func (r *ItemController) GetItemByCode(c *gin.Context) {
	itemCode := c.Param("item_code")
	result, err := r.itemservice.GetItemCode(itemCode)
	if err != nil {
		exceptions.NotFoundException(c, err.Error())
		return
	}
	payloads.HandleSuccess(c, result, "Get Data Success", http.StatusOK)
}

// target -> mau ambil value apa dari key json responsenya
func (r *ItemController) GetSupplier(c *gin.Context, id int, code string, name string) (string, string, error) {
	var apiResponse utils.APIResponse
	url := "http://10.1.32.26:8000/general-service/api/general/supplier-master/" + strconv.Itoa(id)
	value, err := utils.GetAPIResponse(url, &apiResponse)
	if err != nil {
		exceptions.AppException(c, err.Error())
		return err.Error(), err.Error(), err
	}
	supplierName := value.Data.(map[string]interface{})[name].(string)
	supplierCode := value.Data.(map[string]interface{})[code].(string)

	return supplierName, supplierCode, nil
}

func (r *ItemController) GetItemGroup(c *gin.Context, id int, target string) (string, error) {
	var apiResponse utils.APIResponse
	url := "http://10.1.32.26:8000/general-service/api/general/item-group/" + strconv.Itoa(id)
	value, err := utils.GetAPIResponse(url, &apiResponse)
	if err != nil {
		exceptions.AppException(c, err.Error())
		return err.Error(), err
	}
	values := value.Data.(map[string]interface{})[target].(string)

	return values, nil
}
