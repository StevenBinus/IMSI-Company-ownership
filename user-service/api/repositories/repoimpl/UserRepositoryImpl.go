package repoimpl

import (
	"context"
	"fmt"
	"log"
	"time"
	"user-service/api/config"
	entities "user-service/api/entities"
	"user-service/api/payloads"
	"user-service/api/repositories"

	"gorm.io/gorm"
)

type UserRepositoryImpl struct {
	DB      *gorm.DB
	DBRedis *config.Database
}

type Session struct {
	UserId    int    `json:"user_id"`
	Client    string `json:"client"`
	Token     string `json:"token"`
	IpAddress string `json:"ip_address"`
}

// WithTrx enables repository with transaction
func (r *UserRepositoryImpl) WithTrx(trxHandle *gorm.DB) repositories.UserRepository {
	if trxHandle == nil {
		log.Print("Transaction Database not found")
		return r
	}
	r.DB = trxHandle
	return r
}

func CreateUserRepository(db *gorm.DB, dbRedis *config.Database) repositories.UserRepository {
	return &UserRepositoryImpl{
		DB:      db,
		DBRedis: dbRedis,
	}
}

func (r *UserRepositoryImpl) View() ([]entities.User, error) {
	var user []entities.User
	row, err := r.DB.Model(user).Scan(&user).Rows()

	if err != nil {
		return nil, err
	}
	defer row.Close()

	var users []entities.User
	for row.Next() {
		var user entities.User

		err := row.Scan(
			&user.UserId,
			&user.Username,
			&user.Password)

		if err != nil {
			return nil, err
		}

		users = append(users, user)
	}

	return users, nil
}

func (r *UserRepositoryImpl) FindByUsername(username string) (entities.User, error) {
	var user entities.User

	row, err := r.DB.
		Model(user).
		Where(entities.User{
			Username: username,
		}).Scan(&user).Rows()
	if err != nil {
		return user, err
	}
	defer row.Close()

	return user, nil
}

func (r *UserRepositoryImpl) FindByEmail(email string) (bool, error) {
	var user entities.User

	row, err := r.DB.
		Model(user).
		Where(entities.User{
			Email: email,
		}).Scan(&user).Rows()

	if err != nil {
		return false, err
	}

	if user.Email == "" {
		return false, err
	}
	defer row.Close()

	return true, nil
}

func (r *UserRepositoryImpl) FindUserDetailByUsername(username string) (payloads.UserDetails, error) {
	var user payloads.UserDetails

	row, err := r.DB.Model(entities.User{}).Where(entities.User{Username: username}).Scan(&user).Rows()
	if err != nil {
		return user, err
	}
	defer row.Close()

	return user, nil
}

func (r *UserRepositoryImpl) FindById(userId int) (entities.User, error) {
	var user entities.User

	row, err := r.DB.Model(user).Where(entities.User{
		UserId: userId,
	}).Scan(&user).Rows()
	if err != nil {
		return user, err
	}
	defer row.Close()

	return user, nil
}

func (r *UserRepositoryImpl) CheckPasswordResetTime(emailReq payloads.UpdateEmailTokenRequest) (bool, error) {
	var user payloads.UserDetails
	row, err :=
		r.DB.Model(entities.User{}).
			Where(
				"password_reset_token = ? AND password_reset_at > ?",
				emailReq.PasswordResetToken, emailReq.PasswordResetAt,
			).Scan(&user).Rows()

	if err != nil {
		return false, err
	}

	if user.Username == "" {
		return false, err
	}

	defer row.Close()

	return true, nil
}

func (r *UserRepositoryImpl) Create(userReq payloads.CreateRequest, roleId uint16) (int, error) {
	user := entities.User{
		Username:   userReq.Username,
		Password:   userReq.Password,
		IsActive:   true,
		DateJoined: time.Now(),
		Email:      userReq.Email,
		RoleId:     roleId,
	}
	row, err := r.DB.Create(&user).Rows()
	if err != nil {
		return 0, err
	}

	defer row.Close()

	return user.UserId, nil
}

func (r *UserRepositoryImpl) Update(userReq payloads.CreateRequest, userId int) (bool, error) {
	user := entities.User{
		Username:   userReq.Username,
		Password:   userReq.Password,
		IsActive:   userReq.IsActive,
		Email:      userReq.Email,
		OtpEnabled: true,
	}

	row, err := r.DB.
		Where(userId).
		Updates(&user).
		Rows()
	if err != nil {
		return false, err
	}
	defer row.Close()

	return true, nil
}

func (r *UserRepositoryImpl) UpdateUserSecretUrl(userReq payloads.SecretUrlRequest, userId int) (bool, error) {
	user := entities.User{
		OtpSecret:  userReq.Secret,
		OtpAuthUrl: userReq.Url,
	}

	row, err := r.DB.
		Where(entities.User{UserId: userId}).
		Updates(&user).
		Rows()
	if err != nil {
		return false, err
	}
	defer row.Close()

	return true, nil
}

func (r *UserRepositoryImpl) UpdateUserOTP(userReq payloads.OTPRequest, userId int) (bool, error) {
	user := entities.User{
		OtpVerified: userReq.OtpVerified,
		OtpEnabled:  userReq.OtpEnabled,
	}

	row, err := r.DB.
		Where(entities.User{UserId: userId}).
		Updates(&user).
		Rows()
	if err != nil {
		return false, err
	}
	defer row.Close()

	return true, nil
}

func (r *UserRepositoryImpl) UpdateCredential(loginCre payloads.LoginCredential, userId int) (bool, error) {
	user := entities.User{
		IpAddress: loginCre.IpAddress,
		LastLogin: time.Now(),
		UserId:    userId,
	}

	row, err := r.DB.
		Where(entities.User{UserId: userId}).
		Updates(&user).
		Rows()
	if err != nil {
		return false, err
	}

	if err != nil {
		return false, nil
	}

	setRedis := r.DBRedis.Client.HSet(
		context.Background(),
		fmt.Sprintf("session:%d", userId),
		"client", loginCre.Client,
		"ip_address", loginCre.IpAddress,
		"session", loginCre.Session,
		"user_id", userId,
	).Err()

	if setRedis != nil {
		return false, setRedis
	}

	defer row.Close()

	return true, nil
}

func (r *UserRepositoryImpl) UpdatePassword(passReq payloads.ResetPasswordInput, userId int) (bool, error) {
	user := entities.User{
		Password: passReq.Password,
	}
	row, err := r.DB.
		Where(entities.User{UserId: userId}).
		Updates(&user).
		Rows()
	if err != nil {
		return false, err
	}
	defer row.Close()

	return true, nil
}

func (r *UserRepositoryImpl) UpdatePasswordByToken(passReq payloads.UpdatePasswordByTokenRequest) (bool, error) {
	user := entities.User{
		Password: passReq.Password,
	}
	row, err := r.DB.
		Where(entities.User{PasswordResetToken: passReq.PasswordResetToken}).
		Updates(&user).
		Rows()
	if err != nil {
		return false, err
	}
	defer row.Close()

	return true, nil
}

func (r *UserRepositoryImpl) UpdatePasswordTokenByEmail(emailReq payloads.UpdateEmailTokenRequest) (bool, error) {
	user := entities.User{
		PasswordResetToken: emailReq.PasswordResetToken,
		PasswordResetAt:    emailReq.PasswordResetAt,
	}

	row, err := r.DB.
		Where(entities.User{Email: emailReq.Email}).
		Updates(&user).
		Rows()
	if err != nil {
		return false, err
	}
	defer row.Close()

	return true, nil
}

func (r *UserRepositoryImpl) UpdatePasswordResetToken(updateReq payloads.UpdatePasswordResetTokenRequest) (bool, error) {
	var user entities.User
	var nullString *string
	var nullTime *time.Time
	row, err := r.DB.
		Model(&user).
		Where(entities.User{PasswordResetToken: updateReq.PasswordResetToken}).
		Updates(map[string]interface{}{
			"password_reset_token": nullString,
			"password_reset_at":    nullTime,
		}).
		Rows()
	if err != nil {
		return false, err
	}
	defer row.Close()

	return true, nil
}

func (r *UserRepositoryImpl) DeleteCredential(userId int) (bool, error) {

	setRedis := r.DBRedis.Client.Del(
		context.Background(),
		fmt.Sprintf("session:%d", userId),
	).Err()
	if setRedis != nil {
		return false, setRedis
	}
	return true, nil
}

func (r *UserRepositoryImpl) Delete(userId int) (bool, error) {

	row, err := r.DB.
		Where(userId).
		Delete(userId).
		Rows()
	if err != nil {
		return false, err
	}
	defer row.Close()
	return true, nil
}

func (r *UserRepositoryImpl) FindSession(sessionReq payloads.UserDetail) (string, error) {

	getRedis := r.DBRedis.Client.HGet(context.Background(), fmt.Sprintf("session:%d", sessionReq.UserId), "client")
	session, err := getRedis.Result()
	if err != nil {
		return "", nil
	}

	if getRedis == nil {
		return "", nil
	}

	return session, nil
}
