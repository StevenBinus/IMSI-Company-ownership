package repositories

import (
	entities "user-service/api/entities"
	"user-service/api/payloads"

	"gorm.io/gorm"
)

type UserRepository interface {
	WithTrx(trxHandle *gorm.DB) UserRepository
	View() ([]entities.User, error)
	FindById(int) (entities.User, error)
	FindByUsername(string) (entities.User, error)
	FindByEmail(string) (bool, error)
	FindSession(payloads.UserDetail) (string, error)
	FindUserDetailByUsername(string) (payloads.UserDetails, error)
	CheckPasswordResetTime(payloads.UpdateEmailTokenRequest) (bool, error)
	Create(payloads.CreateRequest, uint16) (int, error)
	Update(payloads.CreateRequest, int) (bool, error)
	UpdateUserSecretUrl(payloads.SecretUrlRequest, int) (bool, error)
	UpdateUserOTP(payloads.OTPRequest, int) (bool, error)
	UpdateCredential(payloads.LoginCredential, int) (bool, error)
	UpdatePassword(payloads.ResetPasswordInput, int) (bool, error)
	UpdatePasswordByToken(payloads.UpdatePasswordByTokenRequest) (bool, error)
	UpdatePasswordTokenByEmail(payloads.UpdateEmailTokenRequest) (bool, error)
	UpdatePasswordResetToken(payloads.UpdatePasswordResetTokenRequest) (bool, error)
	DeleteCredential(int) (bool, error)
	Delete(int) (bool, error)
}
