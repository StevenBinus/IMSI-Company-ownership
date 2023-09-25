package entities

import (
	"time"
	approverentities "user-service/api/entities/approval/approver"
)

const TableNameUser = "users"

// User mapped from table <user>
type User struct {
	IsActive           bool                             `gorm:"column:is_active;not null" json:"is_active"`
	UserId             int                              `gorm:"size:30;column:user_id;primaryKey;autoIncrement" json:"user_id"`
	Password           string                           `gorm:"size:100;column:password;not null" json:"password"`
	Username           string                           `gorm:"size:30;column:username;not null" json:"username"`
	Email              string                           `gorm:"size:255;column:email;not null" json:"email"`
	RoleId             uint16                           `gorm:"column:role_id;not null" json:"role_id"`
	LastLogin          time.Time                        `gorm:"column:last_login" json:"last_login"`
	DateJoined         time.Time                        `gorm:"column:date_joined;not null" json:"date_joined"`
	PasswordResetToken *string                          `gorm:"column:password_reset_token" json:"password_reset_token"`
	PasswordResetAt    *time.Time                       `gorm:"column:password_reset_at" json:"password_reset_at"`
	IpAddress          string                           `gorm:"size:20;ip_address;null" json:"ip_address"`
	UserDetail         UserDetail                       `gorm:"foreignKey:UserId;constraint:OnUpdate:CASCADE,OnDelete:CASCADE;references:user_id"`
	Approver           approverentities.ApproverDetails `gorm:"foreignKey:UserId;constraint:OnUpdate:CASCADE,OnDelete:CASCADE;references:user_id"`
	OtpEnabled         bool                             `gorm:"column:otp_enabled;default:false;"`
	OtpVerified        bool                             `gorm:"column:otp_verified;default:false;"`
	OtpSecret          string                           `gorm:"column:otp_secret;default:false;"`
	OtpAuthUrl         string                           `gorm:"column:otp_auth_url;default:false;"`
	// VerificationCode   string                           `gorm:"column:verification_token;not null" json:"verification_token"`

}

type OTPInput struct {
	UserId int    `json:"user_id"`
	Token  string `json:"token"`
	Client string `json:"client"`
}

// custom tablename
func (e *User) TableName() string {
	return TableNameUser
}
