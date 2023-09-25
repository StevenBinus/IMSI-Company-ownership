package test

import (
	"bufio"
	"encoding/base64"
	"fmt"
	"image/png"
	"io/ioutil"
	"os"
	"testing"
	"user-service/api/config"
	"user-service/api/payloads"
	"user-service/api/repositories/repoimpl"
	"user-service/api/securities"
	"user-service/api/services/serviceimpl"

	"github.com/makiuchi-d/gozxing"
	"github.com/makiuchi-d/gozxing/qrcode"
	"github.com/pquerna/otp/totp"
)

func TestGenerateOTPQrCode(t *testing.T) {
	config.InitEnvConfigs(true, "")
	db, dbRedis := config.InitDB()
	userRepo := repoimpl.CreateUserRepository(db, dbRedis)
	userService := serviceimpl.CreateUserService(userRepo)
	var login payloads.LoginRequest

	login.Username = "string"
	login.Password = "string"
	login.Client = "test"

	findUser, _ := userService.FindUser(login.Username)

	if findUser.Username == "" {
		fmt.Println("Username not exists")
		return
	}

	if findUser.Username != "" {
		hashPwd := findUser.Password
		pwd := login.Password

		hash, err := securities.VerifyPassword(hashPwd, pwd)
		if err != nil {
			fmt.Println("Verify Password Error")
			return
		}
		if !hash {
			fmt.Println("Password not matched")
			return
		}
	} else {
		fmt.Println("Username not found")
		return
	}

	key, err := totp.Generate(totp.GenerateOpts{
		Issuer:      "Indomobil",
		AccountName: "indomobil01@gmail.com",
		SecretSize:  15,
	})

	if err != nil {
		fmt.Println("Something wrong with the otp")
		return
	}

	updateSecretUrl := payloads.SecretUrlRequest{
		Secret: key.Secret(),
		Url:    key.URL(),
	}

	updateUserSecretUrl, err := userService.UpdateUserSecretUrl(updateSecretUrl, findUser.UserId)

	if !updateUserSecretUrl {
		fmt.Println("Update failed")
		return
	}

	if err != nil {
		fmt.Println("Update failed")
		return
	}
	otpResponse := payloads.SecretUrlResponse{
		Secret: key.Secret(),
		Url:    key.URL(),
		UserId: findUser.UserId,
	}

	// ContentTypeHTML := "text/html; charset=utf-8"

	img, _ := qrcode.NewQRCodeWriter().Encode(otpResponse.Url, gozxing.BarcodeFormat_QR_CODE, 250, 50, nil)
	fileName := fmt.Sprintf("%v-*.png", otpResponse.UserId)
	file, err := ioutil.TempFile("../tmp", fileName)
	if err != nil {
		fmt.Println("Cannot create temp file")
		os.Exit(1)
		return
	}

	defer os.Remove(file.Name())

	_ = png.Encode(file, img)

	imgFile, err := os.Open(file.Name())
	if err != nil {
		fmt.Println("QR Code not generated")
		os.Exit(1)
		return
	}
	defer imgFile.Close()

	fInfo, _ := imgFile.Stat()
	var size int64 = fInfo.Size()
	buf := make([]byte, size)

	fReader := bufio.NewReader(imgFile)
	fReader.Read(buf)

	imgBase64Str := base64.StdEncoding.EncodeToString(buf)
	img2html := imgBase64Str
	fmt.Println(img2html)

}
