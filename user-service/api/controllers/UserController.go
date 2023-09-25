package controllers

import (
	"errors"
	"net/http"
	"strings"
	"user-service/api/exceptions"
	"user-service/api/middlewares"
	"user-service/api/payloads"
	"user-service/api/securities"
	"user-service/api/services"
	"user-service/api/utils"

	"github.com/gin-gonic/gin"
	"gorm.io/gorm"
)

type UserController struct {
	userService services.UserService
}

func CreateUserRoutes(db *gorm.DB, r *gin.RouterGroup, userService services.UserService) {
	userHandler := UserController{
		userService: userService,
	}

	r.Use(middlewares.SetupAuthenticationMiddleware(userService))
	r.GET("/find-me", middlewares.DBTransactionMiddleware(db), userHandler.FindMe)
	r.POST("/update-user", middlewares.DBTransactionMiddleware(db), userHandler.UpdateUser)
}

// @Summary Find Me
// @Description REST API User
// @Accept json
// @Produce json
// @Tags User Controller
// @Security BearerAuth
// @Success 200 {object} payloads.Respons
// @Failure 500,400,401,404,403,422 {object} exceptions.Error
// @Router /user/find-me [get]
func (r *UserController) FindMe(c *gin.Context) {
	txHandle := c.MustGet("db_trx").(*gorm.DB)
	check, err := securities.ExtractAuthToken(c)

	if err != nil {
		exceptions.AppException(c, "Something wrong")
		return
	}
	get, err := r.userService.WithTrx(txHandle).FindUserDetailByUsername(check.Username)

	if err != nil {
		exceptions.AppException(c, "Something wrong")
		return
	}

	payloads.HandleSuccess(c, get, "Get Data Successfully", http.StatusOK)
}

// @Summary Update User
// @Description REST API User
// @Accept json
// @Produce json
// @Tags User Controller
// @Param user_id path string true "User ID"
// @Param reqBody body payloads.CreateRequest true "Form Request"
// @Success 200 {object} payloads.Respons
// @Failure 500,400,401,404,403,422 {object} exceptions.Error
// @Router /user/update-user [post]
func (r *UserController) UpdateUser(c *gin.Context) {

	claims, err := securities.ExtractAuthToken(c)
	txHandle := c.MustGet("db_trx").(*gorm.DB)

	if err != nil {
		exceptions.AppException(c, "Something wrong")
		return
	}

	var updateData payloads.CreateRequest

	if err := c.ShouldBindJSON(&updateData); err != nil {
		exceptions.EntityException(c, "Something wrong")
		return
	}

	check := utils.ValidationForm(updateData)

	if check != "" {
		exceptions.BadRequestException(c, check)
		return
	}

	findUser, _ := r.userService.WithTrx(txHandle).FindById(int(claims.UserId))

	if findUser.Username == "" {
		exceptions.NotFoundException(c, errors.New("User not found").Error())
		return
	}

	hash, err := securities.HashPassword(updateData.Password)

	if err != nil {
		exceptions.AppException(c, "Something wrong")
		return
	}

	updateData.Username = strings.ToLower(strings.ReplaceAll(updateData.Username, " ", ""))
	updateData.Password = strings.ReplaceAll(updateData.Password, " ", "")
	updateData.Password = hash

	get, err := r.userService.WithTrx(txHandle).UpdateUser(updateData, int(claims.UserId))

	if err != nil {
		exceptions.AppException(c, "Something wrong")
		return
	}

	payloads.HandleSuccess(c, get, "Update Data Successfully", http.StatusOK)
}
