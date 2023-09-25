package services

import (
	"user-service/api/entities"
	"user-service/api/payloads"

	"gorm.io/gorm"
)

type AuthService interface {
	WithTrx(trxHandle *gorm.DB) AuthService
	DoLogin(payloads.LoginRequest) (entities.User, error)
	DoRegister(payloads.CreateRequest, uint16) (int, error)
}
