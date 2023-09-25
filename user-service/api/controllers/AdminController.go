package controllers

import (
	"errors"
	"net/http"
	"strconv"
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

type AdminController struct {
	authService services.AuthService
	userService services.UserService
}

func CreateAdminRoutes(db *gorm.DB, r *gin.RouterGroup, authService services.AuthService, userService services.UserService) {
	userHandler := AdminController{
		authService: authService,
		userService: userService,
	}

	r.Use(middlewares.SetupAuthenticationMiddleware(userService))
	r.POST("/register-admin", middlewares.DBTransactionMiddleware(db), userHandler.RegisterAdmin)
	r.GET("/view-all-user", middlewares.DBTransactionMiddleware(db), userHandler.ViewAllUser)
	r.GET("/find-by-username/:username", middlewares.DBTransactionMiddleware(db), userHandler.FindByUser)
	r.POST("/update-user/:user_id", middlewares.DBTransactionMiddleware(db), userHandler.UpdateUser)
	r.POST("/delete-user/:user_id", middlewares.DBTransactionMiddleware(db), userHandler.DeleteUser)
}

// @Summary Register User Admin
// @Description REST API User
// @Accept json
// @Produce json
// @Tags Admin Controller
// @Security BearerAuth
// @Param reqBody body payloads.CreateRequest true "Form Request"
// @Success 200 {object} payloads.Respons
// @Failure 500,400,401,404,403,422 {object} exceptions.Error
// @Router /admin/user/register-admin [post]
func (r *AdminController) RegisterAdmin(c *gin.Context) {
	txHandle := c.MustGet("db_trx").(*gorm.DB)
	claims, _ := securities.ExtractAuthToken(c)

	if claims.Role != 1 {
		exceptions.RoleException(c, "")
		return
	}

	var register payloads.CreateRequest

	if err := c.ShouldBindJSON(&register); err != nil {
		exceptions.EntityException(c, "Something wrong")
		return
	}

	check := utils.ValidationForm(register)

	if check != "" {
		exceptions.BadRequestException(c, check)
		return
	}

	findUser, _ := r.userService.WithTrx(txHandle).FindUser(register.Username)

	if findUser.Username != "" {
		exceptions.ConflictException(c, errors.New("Username already exists").Error())
		return
	}

	hash, err := securities.HashPassword(register.Password)

	if err != nil {
		exceptions.AppException(c, "Something wrong")
		return
	}

	register.Username = strings.ToLower(strings.ReplaceAll(register.Username, " ", ""))
	register.Password = strings.ReplaceAll(register.Password, " ", "")
	register.Password = hash

	get, err := r.authService.WithTrx(txHandle).DoRegister(register, 1)

	if err != nil {
		exceptions.AppException(c, "Something wrong")
		return
	}

	payloads.HandleSuccess(c, get, "Register Successfully", http.StatusOK)
}

// @Summary View All User
// @Description REST API User
// @Accept json
// @Produce json
// @Tags Admin Controller
// @Security BearerAuth
// @Success 200 {object} payloads.Respons
// @Failure 500,400,401,404,403,422 {object} exceptions.Error
// @Router /admin/user/view-all-user [get]
func (r *AdminController) ViewAllUser(c *gin.Context) {
	txHandle := c.MustGet("db_trx").(*gorm.DB)

	claims, _ := securities.ExtractAuthToken(c)

	if claims.Role != 1 {
		exceptions.RoleException(c, "")
		return
	}

	get, err := r.userService.WithTrx(txHandle).ViewUser()

	if err != nil {
		exceptions.AppException(c, "Something wrong")
		return
	}

	payloads.HandleSuccess(c, get, "Get Data Successfully", http.StatusOK)
}

// @Summary Find User
// @Description REST API User
// @Accept json
// @Produce json
// @Tags Admin Controller
// @Security BearerAuth
// @Success 200 {object} payloads.Respons
// @Param username path string true "Username"
// @Failure 500,400,401,404,403,422 {object} exceptions.Error
// @Router /admin/user/find-by-username/{username} [get]
func (r *AdminController) FindByUser(c *gin.Context) {
	txHandle := c.MustGet("db_trx").(*gorm.DB)
	claims, _ := securities.ExtractAuthToken(c)

	if claims.Role != 1 {
		exceptions.RoleException(c, "")
		return
	}
	username := c.Param("username")

	get, err := r.userService.WithTrx(txHandle).FindUser(username)

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
// @Tags Admin Controller
// @Security BearerAuth
// @Param user_id path string true "User ID"
// @Param reqBody body payloads.CreateRequest true "Form Request"
// @Success 200 {object} payloads.Respons
// @Failure 500,400,401,404,403,422 {object} exceptions.Error
// @Router /admin/user/update-user/{user_id} [post]
func (r *AdminController) UpdateUser(c *gin.Context) {
	txHandle := c.MustGet("db_trx").(*gorm.DB)
	claims, _ := securities.ExtractAuthToken(c)

	if claims.Role != 1 {
		exceptions.RoleException(c, "")
		return
	}
	userId, _ := strconv.Atoi(c.Param("user_id"))

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

	findUser, _ := r.userService.WithTrx(txHandle).FindById(int(userId))

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

	get, err := r.userService.WithTrx(txHandle).UpdateUser(updateData, int(userId))

	if err != nil {
		exceptions.AppException(c, "Something wrong")
		return
	}

	payloads.HandleSuccess(c, get, "Update Data Successfully", http.StatusOK)
}

// @Summary Delete User
// @Description REST API User
// @Accept json
// @Produce json
// @Tags Admin Controller
// @Security BearerAuth
// @Param user_id path string true "User ID"
// @Success 200 {object} payloads.Respons
// @Failure 500,400,401,404,403,422 {object} exceptions.Error
// @Router /admin/user/delete-user/{user_id} [post]
func (r *AdminController) DeleteUser(c *gin.Context) {
	txHandle := c.MustGet("db_trx").(*gorm.DB)
	claims, _ := securities.ExtractAuthToken(c)

	if claims.Role != 1 {
		exceptions.RoleException(c, "")
		return
	}
	userId, _ := strconv.Atoi(c.Param("user_id"))

	get, err := r.userService.WithTrx(txHandle).DeleteUser(int(userId))

	if err != nil {
		exceptions.AppException(c, "Something wrong")
		return
	}

	payloads.HandleSuccess(c, get, "Delete Data Successfully", http.StatusOK)
}
