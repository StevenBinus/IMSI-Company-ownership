# DMS User Service Architecture
Membuat clean architecture menggunakan framework Gin Gonic beserta sample penggunaannya menggunakan database mssql

# How to using gin-swagger
1. Install generator swagger menggunakan perintah :
```sh
go get -u github.com/swaggo/swag/cmd/swag
```
2. tambahkan module swagger untuk gin menggunakan perintah :
```sh
go get -u github.com/swaggo/gin-swagger
go get -u github.com/swaggo/files
go get -u github.com/alecthomas/template
```
3. Kemudian, tambahkan General API pada file main.go
 ```sh
// @title DMS User Service
// @version 1.0
// @description DMS User Service Architecture
// @termsOfService http://swagger.io/terms/

// @contact.name Indomobil
// @contact.url https://github.com/Indomobil-Sukses-Internasional-Tbk
// @contact.email indomobil01@gmail.com

// @license.name MIT
// @license.url https://github.com/Indomobil-Sukses-Internasional-Tbk/-/blob/main/LICENSE

// @securityDefinitions.apikey BearerAuth
// @in Header
// @name Authorization

// @host localhost:9000
// @BasePath /api
 ```
atau ingin menggunakan dynamic general API dengan cara seperti ini:
```sh
docs.SwaggerInfo.Title = "DMS User Service"
docs.SwaggerInfo.Description = "DMS User Service"
docs.SwaggerInfo.Version = "1.0"
docs.SwaggerInfo.Host = fmt.Sprintf("%s:%v", "localhost", configs.Config.Server.PORT)
docs.SwaggerInfo.BasePath = "/api"
docs.SwaggerInfo.Schemes = []string{"http", "https"}
```

4. Tambahkan API Operation didalam kode controller seperti ini :
# Untuk Penggunaan Method GET
```sh
// @Summary View All User
// @Description REST API User
// @Accept json
// @Produce json
// @Tags User Controller
// @Security BearerAuth
// @Success 200 {object} payloads.Respons
// @Failure 500,400,401,404,403,422 {object} exceptions.Error
// @Router /User/ViewAllUser [get]
```

# Untuk Penggunaan Method POST
```sh
// @Summary Register User
// @Description REST API User
// @Accept json
// @Produce json
// @Tags Auth Controller
// @Param reqBody body payloads.CreateRequest true "Form Request"
// @Success 200 {object} payloads.Respons
// @Failure 500,400,401,404,403,422 {object} exceptions.Error
// @Router /Auth/Register [post]
```

# Untuk Penggunaan Method PUT
```sh
// @Summary Update User
// @Description REST API User
// @Accept json
// @Produce json
// @Tags User Controller
// @Security BearerAuth
// @Param user_id path string true "User ID"
// @Param reqBody body payloads.CreateRequest true "Form Request"
// @Success 200 {object} payloads.Respons
// @Failure 500,400,401,404,403,422 {object} exceptions.Error
// @Router /User/UpdateUser/{user_id} [put]
```

# Untuk Penggunaan Method DELETE
```sh
// @Summary Delete User
// @Description REST API User
// @Accept json
// @Produce json
// @Tags User Controller
// @Security BearerAuth
// @Param user_id path string true "User ID"
// @Success 200 {object} payloads.Respons
// @Failure 500,400,401,404,403,422 {object} exceptions.Error
// @Router /User/DeleteUser/{user_id} [delete]
```

4. Untuk menjalankan generator gin-swagger menggunakan perintah :
```sh
swag init -g main.go
```

5. Jalankan kembali aplikasi menggunakan perintah :
```sh
go run main.go
```

6. Kemudian bisa diakses melalui url :
```sh
http://localhost:9000/swagger/index.html
```

# How to run Application
clone the repository :
```sh
https://github.com/Indomobil-Sukses-Internasional-Tbk/user-service.git
```

Run application:
```sh
go run main.go
```

# How to generate code
```sh
cd /generate/
go run generate.go
```

# How to migrate
```sh
cd /generate/
go run migrate.go
```

# Library
- Gin Gonic : github.com/gin-gonic/gin
- Logrus : github.com/sirupsen/logrus
- Viper : github.com/spf13/viper
- Validator : github.com/go-playground/validator/v10
- JWT Token : github.com/golang-jwt/jwt/v4
- Swagger : https://github.com/swaggo/gin-swagger
- Gorm : gorm.io/gorm
- Sql Server: gorm.io/driver/sqlserver

