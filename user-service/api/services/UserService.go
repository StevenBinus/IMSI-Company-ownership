package services

import (
	"user-service/api/entities"
	"user-service/api/payloads"

	"gorm.io/gorm"
)

type UserService interface {
	WithTrx(trxHandle *gorm.DB) UserService
	ViewUser() ([]entities.User, error)
	FindById(int) (entities.User, error)
	FindUser(string) (entities.User, error)
	FindByEmail(string) (bool, error)
	FindSession(payloads.UserDetail) (string, error)
	FindUserDetailByUsername(string) (payloads.UserDetails, error)
	CheckPasswordResetTime(payloads.UpdateEmailTokenRequest) (bool, error)
	UpdateUser(payloads.CreateRequest, int) (bool, error)
	UpdateUserSecretUrl(payloads.SecretUrlRequest, int) (bool, error)
	UpdateUserOTP(payloads.OTPRequest, int) (bool, error)
	UpdateCredential(payloads.LoginCredential, int) (bool, error)
	UpdatePassword(payloads.ResetPasswordInput, int) (bool, error)
	UpdatePasswordTokenByEmail(payloads.UpdateEmailTokenRequest) (bool, error)
	UpdatePasswordByToken(payloads.UpdatePasswordByTokenRequest) (bool, error)
	UpdatePasswordResetToken(payloads.UpdatePasswordResetTokenRequest) (bool, error)
	DeleteCredential(int) (bool, error)
	DeleteUser(int) (bool, error)
}
