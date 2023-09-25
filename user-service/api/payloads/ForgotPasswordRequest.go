package payloads

import "time"

type ForgotPasswordInput struct {
	Email string `json:"email" binding:"required"`
}

type ResetPasswordInput struct {
	Password        string `json:"password" binding:"required"`
	PasswordConfirm string `json:"password_confirm" binding:"required"`
}

type UpdateEmailTokenRequest struct {
	Email              string     `json:"email"`
	PasswordResetToken *string    `json:"password_reset_token"`
	PasswordResetAt    *time.Time `json:"password_reset_at"`
}

type UpdatePasswordResetTokenRequest struct {
	PasswordResetToken *string    `json:"password_reset_token"`
	PasswordResetAt    *time.Time `json:"password_reset_at"`
}

type UpdatePasswordByTokenRequest struct {
	PasswordResetToken *string `json:"password_reset_token"`
	Password           string  `json:"password"`
}
