package serviceimpl

import (
	"time"
	"user-service/api/entities"
	"user-service/api/payloads"
	"user-service/api/repositories"
	"user-service/api/services"

	"gorm.io/gorm"
)

type AuthServiceImpl struct {
	LastLogin time.Time `json:"last_login"`
	userRepo  repositories.UserRepository
}

func (r *AuthServiceImpl) WithTrx(trxHandle *gorm.DB) services.AuthService {
	r.userRepo = r.userRepo.WithTrx(trxHandle)
	return r
}

func CreateAuthService(userRepo repositories.UserRepository) services.AuthService {
	return &AuthServiceImpl{
		userRepo: userRepo,
	}
}

func (s *AuthServiceImpl) DoLogin(userReq payloads.LoginRequest) (entities.User, error) {
	get, err := s.userRepo.FindByUsername(userReq.Username)

	if err != nil {
		return entities.User{}, err
	}

	return get, nil
}

func (s *AuthServiceImpl) DoRegister(userReq payloads.CreateRequest, roleId uint16) (int, error) {
	get, err := s.userRepo.Create(userReq, roleId)

	if err != nil {
		return 0, err
	}

	return get, nil
}
