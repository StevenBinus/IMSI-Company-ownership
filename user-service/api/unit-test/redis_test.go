package test

import (
	"fmt"
	"testing"
	config "user-service/api/config"
	"user-service/api/payloads"
	redisrepo "user-service/api/repositories/repoimpl"
	"user-service/api/securities"
	redisservices "user-service/api/services/serviceimpl"
	"user-service/api/utils"
)

func TestFindUserDetail(t *testing.T) {
	config.InitEnvConfigs(true, "")
	db, dbRedis := config.InitDB()
	redisRepo := redisrepo.CreateUserRepository(db, dbRedis)
	userService := redisservices.CreateUserService(redisRepo)

	create, err := userService.FindSession(payloads.UserDetail{
		UserId: 3,
	})
	if err != nil {
		panic(err)
	}

	fmt.Println(create)

}

func TestLogin(t *testing.T) {
	config.InitEnvConfigs(true, "")
	db, dbRedis := config.InitDB()
	redisRepo := redisrepo.CreateUserRepository(db, dbRedis)
	userService := redisservices.CreateUserService(redisRepo)

	var login payloads.LoginRequest
	var loginCre payloads.LoginCredential
	login.Username = "string"
	login.Password = "string"
	login.Client = "haaaaaaaaaa"

	loginCre.Client = login.Client
	loginCre.IpAddress = "10.1.1.1"

	// ipAddress := c.ClientIP()
	// if ipAddress == "" {
	// 	fmt.Println("Cannot detect device")
	// 	return
	// }

	// if err := c.ShouldBindJSON(&login); err != nil {
	// 	fmt.Println(err.Error())
	// 	return
	// }

	check := utils.ValidationForm(login)

	if check != "" {
		fmt.Println("check")
		return
	}

	findUser, _ := userService.FindUser(login.Username)

	if findUser.Username != "" {
		hashPwd := findUser.Password
		pwd := login.Password

		hash, err := securities.VerifyPassword(hashPwd, pwd)
		if err != nil {
			fmt.Println("Verify Password Error")
			return
		}

		if hash == true {
			token, err := securities.GenerateToken(findUser.Username, findUser.UserId, login.Client)

			if err != nil {
				fmt.Println(err.Error())
				return
			}
			loginCre.Session = token
			get, _ := userService.UpdateCredential(loginCre, int(findUser.UserId))

			if !get {
				fmt.Println(err.Error())
				return
			}

			fmt.Println("Login Successfully", token)
		} else {
			fmt.Println("Password not matched")
			return
		}
	} else {
		fmt.Println("Username not found")
		return
	}

}

func TestDeleteUser(t *testing.T) {
	config.InitEnvConfigs(true, "")
	db, dbRedis := config.InitDB()
	redisRepo := redisrepo.CreateUserRepository(db, dbRedis)
	userService := redisservices.CreateUserService(redisRepo)

	test, err := userService.DeleteUser(4)
	if err != nil {
		fmt.Println("Error")
	}
	if test {
		fmt.Println(test)
	}
}
