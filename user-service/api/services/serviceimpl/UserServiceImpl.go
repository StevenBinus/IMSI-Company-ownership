package serviceimpl

import (
	"user-service/api/entities"
	"user-service/api/payloads"
	"user-service/api/repositories"
	"user-service/api/services"

	"gorm.io/gorm"
)

type UserServiceImpl struct {
	userRepo repositories.UserRepository
}

func (r *UserServiceImpl) WithTrx(trxHandle *gorm.DB) services.UserService {
	r.userRepo = r.userRepo.WithTrx(trxHandle)
	return r
}

func CreateUserService(userRepo repositories.UserRepository) services.UserService {
	return &UserServiceImpl{
		userRepo: userRepo,
	}
}

func (r *UserServiceImpl) ViewUser() ([]entities.User, error) {
	get, err := r.userRepo.View()

	if err != nil {
		return nil, err
	}

	return get, nil
}

func (r *UserServiceImpl) FindUser(username string) (entities.User, error) {
	get, err := r.userRepo.FindByUsername(username)

	if err != nil {
		return entities.User{}, err
	}

	return get, nil
}

func (r *UserServiceImpl) FindUserDetailByUsername(username string) (payloads.UserDetails, error) {
	get, err := r.userRepo.FindUserDetailByUsername(username)

	if err != nil {
		return payloads.UserDetails{}, err
	}

	return get, nil
}

func (r *UserServiceImpl) FindById(userId int) (entities.User, error) {
	get, err := r.userRepo.FindById(userId)

	if err != nil {
		return entities.User{}, err
	}

	return get, nil
}

func (r *UserServiceImpl) FindByEmail(email string) (bool, error) {
	get, err := r.userRepo.FindByEmail(email)

	if err != nil {
		return false, err
	}

	return get, nil
}

func (r *UserServiceImpl) CheckPasswordResetTime(emailReq payloads.UpdateEmailTokenRequest) (bool, error) {
	get, err := r.userRepo.CheckPasswordResetTime(emailReq)

	if err != nil {
		return false, err
	}

	return get, nil
}

func (r *UserServiceImpl) UpdateUser(userReq payloads.CreateRequest, userId int) (bool, error) {
	update, err := r.userRepo.Update(userReq, userId)

	if err != nil {
		return false, err
	}

	return update, nil
}

func (r *UserServiceImpl) UpdateUserSecretUrl(userReq payloads.SecretUrlRequest, userId int) (bool, error) {
	update, err := r.userRepo.UpdateUserSecretUrl(userReq, userId)

	if err != nil {
		return false, err
	}

	return update, nil
}

func (r *UserServiceImpl) UpdateUserOTP(userReq payloads.OTPRequest, userId int) (bool, error) {
	update, err := r.userRepo.UpdateUserOTP(userReq, userId)

	if err != nil {
		return false, err
	}

	return update, nil
}

func (r *UserServiceImpl) UpdateCredential(loginCre payloads.LoginCredential, userId int) (bool, error) {
	update, err := r.userRepo.UpdateCredential(loginCre, userId)

	if err != nil {
		return false, err
	}

	return update, nil
}

func (r *UserServiceImpl) UpdatePassword(passReq payloads.ResetPasswordInput, userId int) (bool, error) {
	update, err := r.userRepo.UpdatePassword(passReq, userId)

	if err != nil {
		return false, err
	}

	return update, nil
}

func (r *UserServiceImpl) UpdatePasswordTokenByEmail(emailReq payloads.UpdateEmailTokenRequest) (bool, error) {
	update, err := r.userRepo.UpdatePasswordTokenByEmail(emailReq)

	if err != nil {
		return false, err
	}

	return update, nil
}

func (r *UserServiceImpl) UpdatePasswordByToken(passReq payloads.UpdatePasswordByTokenRequest) (bool, error) {
	update, err := r.userRepo.UpdatePasswordByToken(passReq)

	if err != nil {
		return false, err
	}

	return update, nil
}

func (r *UserServiceImpl) UpdatePasswordResetToken(passReq payloads.UpdatePasswordResetTokenRequest) (bool, error) {
	update, err := r.userRepo.UpdatePasswordResetToken(passReq)

	if err != nil {
		return false, err
	}

	return update, nil
}

func (r *UserServiceImpl) DeleteCredential(userId int) (bool, error) {
	update, err := r.userRepo.DeleteCredential(userId)

	if !update {
		return false, err
	}

	return update, nil
}

func (r *UserServiceImpl) DeleteUser(userId int) (bool, error) {
	deleteUser, err := r.userRepo.Delete(userId)

	if err != nil {
		return false, err
	}

	return deleteUser, nil
}

func (r *UserServiceImpl) FindSession(sessionReq payloads.UserDetail) (string, error) {
	session, err := r.userRepo.FindSession(sessionReq)

	if err != nil {
		return "", err
	}

	return session, nil
}
