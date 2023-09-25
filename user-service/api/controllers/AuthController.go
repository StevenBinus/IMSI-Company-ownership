package controllers

import (
	"errors"
	"fmt"
	"image/png"
	"net/http"
	"os"
	"strings"
	"time"
	"user-service/api/config"
	"user-service/api/entities"
	"user-service/api/exceptions"
	"user-service/api/middlewares"
	"user-service/api/payloads"
	"user-service/api/securities"
	"user-service/api/services"
	"user-service/api/utils"

	"github.com/gin-gonic/gin"
	"github.com/makiuchi-d/gozxing"
	"github.com/makiuchi-d/gozxing/qrcode"
	"github.com/pquerna/otp/totp"
	"github.com/thanhpk/randstr"
	"gorm.io/gorm"
)

type AuthController struct {
	authService services.AuthService
	userService services.UserService
}

func CreateAuthRoutes(db *gorm.DB, r *gin.RouterGroup, authService services.AuthService, userService services.UserService) {
	authHandler := AuthController{
		authService: authService,
		userService: userService,
	}

	r.POST("/register", middlewares.DBTransactionMiddleware(db), authHandler.DoRegister)
	r.POST("/login", middlewares.DBTransactionMiddleware(db), authHandler.DoLogin)
	r.POST("/verify", middlewares.DBTransactionMiddleware(db), authHandler.VerifyOTP)
	r.POST("/forgot-password", middlewares.DBTransactionMiddleware(db), authHandler.ForgotPassword)
	r.PATCH("/reset-password/:reset_token", middlewares.DBTransactionMiddleware(db), authHandler.ResetPassword)
	r.Use(middlewares.SetupAuthenticationMiddleware(userService))
	r.POST("/generate", middlewares.DBTransactionMiddleware(db), authHandler.GenerateOTP)
	r.POST("/logout", middlewares.DBTransactionMiddleware(db), authHandler.DoLogout)
}

func timePtr(t time.Time) *time.Time {
	return &t
}

func stringPtr(str string) *string {
	return &str
}

// @Summary Register User
// @Description REST API User
// @Accept json
// @Produce json
// @Tags Auth Controller
// @Param reqBody body payloads.CreateRequest true "Form Request"
// @Success 200 {object} payloads.Respons
// @Failure 500,400,401,404,403,422 {object} exceptions.Error
// @Router /auth/register [post]
func (r *AuthController) DoRegister(c *gin.Context) {
	txHandle := c.MustGet("db_trx").(*gorm.DB)

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
		exceptions.ConflictException(c, "Username already exists")
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

	get, err := r.authService.WithTrx(txHandle).DoRegister(register, 2)

	if err != nil {
		exceptions.AppException(c, "Something wrong")
		return
	}

	payloads.HandleSuccess(c, get, "Register Successfully", http.StatusOK)

}

// @Summary Login User
// @Description REST API User
// @Accept json
// @Produce json
// @Tags Auth Controller
// @Param reqBody body payloads.LoginRequest true "Form Request"
// @Success 200 {object} payloads.Respons
// @Failure 500,400,401,404,403,422 {object} exceptions.Error
// @Router /auth/login [post]
func (r *AuthController) DoLogin(c *gin.Context) {
	txHandle := c.MustGet("db_trx").(*gorm.DB)

	var login payloads.LoginRequest
	var loginCre payloads.LoginCredential

	ipAddress := c.ClientIP()
	if ipAddress == "" {
		exceptions.AppException(c, "Cannot detect device")
		return
	}

	if err := c.ShouldBindJSON(&login); err != nil {
		exceptions.EntityException(c, "Something wrong")
		return
	}

	check := utils.ValidationForm(login)

	if check != "" {
		exceptions.BadRequestException(c, check)
		return
	}

	findUser, _ := r.userService.WithTrx(txHandle).FindUser(login.Username)

	loginCre.IpAddress = ipAddress
	loginCre.Client = login.Client
	if findUser.Username != "" {
		hashPwd := findUser.Password
		pwd := login.Password

		hash, err := securities.VerifyPassword(hashPwd, pwd)
		if err != nil {
			exceptions.AppException(c, "Verify Password Error")
			return
		}

		if hash {
			token, err := securities.GenerateToken(findUser.Username, findUser.UserId, login.Client)

			if err != nil {
				exceptions.AppException(c, "Something wrong")
				return
			}
			loginCre.Session = token

			session, err := r.userService.FindSession(payloads.UserDetail{UserId: int(findUser.UserId)})
			if err != nil {
				exceptions.AppException(c, "Something wrong with your session, please log in again")
				return
			}

			if findUser.OtpEnabled && loginCre.Client != session {
				payloads.HandleSuccess(c, findUser.UserId, "Redirecting to 2FA", http.StatusOK)
			} else {
				get, err := r.userService.WithTrx(txHandle).UpdateCredential(loginCre, int(findUser.UserId))

				if !get {
					exceptions.AppException(c, "Something wrong")
					return
				}
				if err != nil {
					exceptions.AppException(c, "Something wrong with your update session, please log in again")
					return
				}
				payloads.ResponseToken(c, "Login Successfully", token, findUser.UserId, http.StatusOK)
			}
		} else {
			exceptions.BadRequestException(c, "Password not matched")
			return
		}
	} else {
		exceptions.NotFoundException(c, "Username not found")
		return
	}
}

// @Summary Generate OTP User
// @Description REST API OTP User
// @Accept json
// @Produce json
// @Tags Auth Controller
// @Success 200 {object} payloads.Respons
// @Failure 500,400,401,404,403,422 {object} exceptions.Error
// @Router /auth/generate [post]
func (r *AuthController) GenerateOTP(c *gin.Context) {
	txHandle := c.MustGet("db_trx").(*gorm.DB)

	claims, err := securities.ExtractAuthToken(c)

	if err != nil {
		exceptions.AppException(c, "")
		return
	}

	key, err := totp.Generate(totp.GenerateOpts{
		Issuer:      config.EnvConfigs.Issuer,
		AccountName: config.EnvConfigs.AccountName,
		SecretSize:  15,
	})

	if err != nil {
		exceptions.AppException(c, "Something wrong with the otp")
		return
	}

	updateSecretUrl := payloads.SecretUrlRequest{
		Secret: key.Secret(),
		Url:    key.URL(),
	}

	updateUserSecretUrl, err := r.userService.WithTrx(txHandle).UpdateUserSecretUrl(updateSecretUrl, claims.UserId)

	if !updateUserSecretUrl {
		exceptions.AppException(c, "Update failed")
		return
	}

	if err != nil {
		exceptions.AppException(c, "Something wrong")
		return
	}
	otpResponse := payloads.SecretUrlResponse{
		Secret: key.Secret(),
		Url:    key.URL(),
		UserId: claims.UserId,
	}

	img, _ := qrcode.NewQRCodeWriter().Encode(otpResponse.Url, gozxing.BarcodeFormat_QR_CODE, 250, 250, nil)
	fileName := fmt.Sprintf("%v-*.png", otpResponse.UserId)

	file, err := os.CreateTemp("", fileName)
	if err != nil {
		exceptions.AppException(c, errors.New("QR Code not generated").Error())
		os.Exit(500)
		return
	}

	defer os.Remove(file.Name())

	_ = png.Encode(file, img)

	imgFile, err := os.Open(file.Name())
	if err != nil {
		exceptions.NotFoundException(c, errors.New("QR Code not generated").Error())
		os.Exit(500)
		return
	}
	defer imgFile.Close()

	c.File(file.Name())
}

// @Summary Verify OTP User
// @Description REST API Verify OTP User
// @Accept json
// @Produce json
// @Tags Auth Controller
// @Param reqBody body entities.OTPInput true "Form Request"
// @Success 200 {object} payloads.Respons
// @Failure 500,400,401,404,403,422 {object} exceptions.Error
// @Router /auth/verify [post]
func (r *AuthController) VerifyOTP(c *gin.Context) {
	txHandle := c.MustGet("db_trx").(*gorm.DB)

	var payload entities.OTPInput
	var loginCre payloads.LoginCredential

	if err := c.ShouldBindJSON(&payload); err != nil {
		exceptions.EntityException(c, "Something wrong")
		return
	}

	ipAddress := c.ClientIP()
	if ipAddress == "" {
		exceptions.AppException(c, "Cannot detect device")
		return
	}
	loginCre.IpAddress = ipAddress
	loginCre.Client = payload.Client

	findUser, _ := r.userService.WithTrx(txHandle).FindById(payload.UserId)

	if findUser.Username == "" {
		exceptions.ConflictException(c, "User not exists")
		return
	}

	token, err := securities.GenerateToken(findUser.Username, findUser.UserId, loginCre.Client)

	if err != nil {
		exceptions.AppException(c, "Something wrong")
		return
	}
	loginCre.Session = token

	get, _ := r.userService.WithTrx(txHandle).UpdateCredential(loginCre, int(findUser.UserId))

	if !get {
		exceptions.AppException(c, "Something wrong")
		return
	}

	valid := totp.Validate(payload.Token, findUser.OtpSecret)
	if !valid {
		exceptions.BadRequestException(c, "Token is invalid or user doesn't exist")
		return
	}

	updateOTP := payloads.OTPRequest{
		OtpVerified: true,
		OtpEnabled:  true,
	}

	updateUserOTP, err := r.userService.WithTrx(txHandle).UpdateUserOTP(updateOTP, findUser.UserId)

	if !updateUserOTP {
		exceptions.AppException(c, "Update failed")
		return
	}

	if err != nil {
		exceptions.AppException(c, "Something wrong")
		return
	}

	// otpResponse := payloads.OTPResponse{
	// 	OtpVerified: true,
	// 	OtpEnabled:  true,
	// }

	payloads.ResponseToken(c, "Login Successfully", token, findUser.UserId, http.StatusOK)
}

func (r *AuthController) ValidateOTP(c *gin.Context, txHandle *gorm.DB, userReq payloads.LoginRequest) {

	var payload *entities.OTPInput

	if err := c.ShouldBindJSON(&payload); err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"status": "fail", "message": err.Error()})
		return
	}

	findUser, _ := r.userService.WithTrx(txHandle).FindUser(userReq.Username)

	if findUser.Username == "" {
		exceptions.NotFoundException(c, errors.New("Username not exists").Error())
		return
	}

	valid := totp.Validate(payload.Token, findUser.OtpSecret)
	if !valid {
		exceptions.BadRequestException(c, "Bad Request")
		return
	}

	payloads.HandleSuccess(c, gin.H{"otp_valid": true}, "OTP Valid", http.StatusOK)
}

// @Summary Forgot Password User
// @Description REST API Password User
// @Accept json
// @Produce json
// @Tags Auth Controller
// @Param reqBody body payloads.ForgotPasswordInput true "Form Request"
// @Success 200 {object} payloads.Respons
// @Failure 500,400,401,404,403,422 {object} exceptions.Error
// @Router /auth/forgot-password [post]
func (r *AuthController) ForgotPassword(c *gin.Context) {
	txHandle := c.MustGet("db_trx").(*gorm.DB)
	var payload *payloads.ForgotPasswordInput

	if err := c.ShouldBindJSON(&payload); err != nil {
		exceptions.EntityException(c, "Something wrong")
		return
	}

	message := "You will receive a reset email if user with that email exist"

	findUser, _ := r.userService.WithTrx(txHandle).FindByEmail(payload.Email)

	if !findUser {
		exceptions.NotFoundException(c, "Email not found")
		return
	}

	config.InitEnvConfigs(true, "")

	// Generate Verification Code
	resetToken := randstr.String(100)

	passwordResetToken := utils.Encode(resetToken)

	updateUserPasswordReset, err := r.userService.WithTrx(txHandle).UpdatePasswordTokenByEmail(payloads.UpdateEmailTokenRequest{
		Email:              payload.Email,
		PasswordResetToken: stringPtr(passwordResetToken),
		PasswordResetAt:    timePtr(time.Now().Add(time.Minute * 15)),
	})

	if !updateUserPasswordReset {
		exceptions.AppException(c, "Update failed")
		return
	}

	if err != nil {
		exceptions.AppException(c, "Something wrong")
		return
	}

	// ? Send Email
	emailData := utils.EmailData{
		URL:     config.EnvConfigs.ClientOrigin + "/reset-password/" + resetToken,
		Subject: "Your password reset token (valid for 10min)",
	}

	sendEmail, err := utils.SendEmail(payload.Email, &emailData, "ResetPassword.html")
	if !sendEmail {
		exceptions.AppException(c, "Send Email failed")
		return
	}

	if err != nil {
		exceptions.AppException(c, "Send Email failed")
		return
	}
	payloads.HandleSuccess(c, true, message, http.StatusOK)
}

// @Summary Forgot Password User
// @Description REST API Password User
// @Accept json
// @Produce json
// @Tags Auth Controller
// @Param reqBody body payloads.ResetPasswordInput true "Form Request"
// @Param reset_token path string true "Reset Token"
// @Success 200 {object} payloads.Respons
// @Failure 500,400,401,404,403,422 {object} exceptions.Error
// @Router /auth/reset-password/{reset_token} [patch]
func (r *AuthController) ResetPassword(c *gin.Context) {
	txHandle := c.MustGet("db_trx").(*gorm.DB)
	var payload *payloads.ResetPasswordInput
	resetToken := c.Params.ByName("reset_token")
	var nullTime *time.Time

	if err := c.ShouldBindJSON(&payload); err != nil {
		exceptions.EntityException(c, "Something wrong")
		return
	}

	if payload.Password != payload.PasswordConfirm {
		exceptions.BadRequestException(c, "Passwords do not match")
		return
	}
	hashedPassword, err := securities.HashPassword(payload.Password)

	if err != nil {
		exceptions.AppException(c, "Something wrong")
		return
	}

	passwordResetToken := utils.Encode(resetToken)

	checkResetTokenTime, _ := r.userService.WithTrx(txHandle).CheckPasswordResetTime(payloads.UpdateEmailTokenRequest{
		PasswordResetToken: stringPtr(passwordResetToken),
		PasswordResetAt:    timePtr(time.Now()),
	})
	if !checkResetTokenTime {
		exceptions.BadRequestException(c, "The reset token is invalid or has expired")
		return
	}

	updatePassword, err := r.userService.WithTrx(txHandle).UpdatePasswordByToken(payloads.UpdatePasswordByTokenRequest{
		Password:           hashedPassword,
		PasswordResetToken: stringPtr(passwordResetToken),
	})
	if err != nil {
		exceptions.AppException(c, "Password update failed")
		return
	}

	if !updatePassword {
		exceptions.BadRequestException(c, "Password update failed")
		return
	}

	updateToken, err := r.userService.WithTrx(txHandle).UpdatePasswordResetToken(payloads.UpdatePasswordResetTokenRequest{
		PasswordResetToken: stringPtr(passwordResetToken),
		PasswordResetAt:    nullTime,
	})
	if err != nil {
		exceptions.AppException(c, "")
		return
	}

	if !updateToken {
		exceptions.BadRequestException(c, "")
		return
	}

	c.SetCookie("token", "", -1, "/", "localhost", false, true)

	payloads.HandleSuccess(c, true, "Password reset Successfully", http.StatusOK)

}

// @Summary Logout User
// @Description REST API Logout User
// @Accept json
// @Produce json
// @Tags Auth Controller
// @Success 200 {object} payloads.Respons
// @Failure 500,400,401,404,403,422 {object} exceptions.Error
// @Router /auth/logout [post]
func (r *AuthController) DoLogout(c *gin.Context) {
	txHandle := c.MustGet("db_trx").(*gorm.DB)
	check, err := securities.ExtractAuthToken(c)

	if err != nil {
		exceptions.AppException(c, "Something wrong")
		return
	}

	delete, err := r.userService.WithTrx(txHandle).DeleteCredential(check.UserId)

	if !delete {
		exceptions.AppException(c, "")
		return
	}

	if err != nil {
		exceptions.AppException(c, "")
		return
	}

	payloads.HandleSuccess(c, delete, "Logout Success", http.StatusOK)
}
