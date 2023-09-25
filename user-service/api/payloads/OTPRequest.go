package payloads

type SecretUrlRequest struct {
	Secret string
	Url    string
}
type OTPRequest struct {
	OtpVerified bool
	OtpEnabled  bool
}

type SecretUrlResponse struct {
	Secret string `json:"base32"`
	Url    string `json:"otpauth_url"`
	UserId int    `json:"user_id"`
}

type OTPResponse struct {
	OtpVerified bool   `json:"OtpVerified"`
	OtpEnabled  bool   `json:"OtpEnabled"`
	Token       string `json:"token"`
}
