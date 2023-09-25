package payloads

type CreateRequest struct {
	Username string `json:"username"`
	Email    string `json:"email"`
	IsActive bool   `json:"is_active"`
	Password string `json:"password"`
}

type UserDetails struct {
	Username    string `json:"username"`
	Name        string `json:"name"`
	Role        uint8  `json:"role"`
	CompanyCode string `json:"company_code"`
}

type LoginRequest struct {
	Username string `json:"username"`
	Password string `json:"password"`
	Client   string `json:"client"`
}

type LoginCredential struct {
	Client    string `json:"client"`
	IpAddress string `json:"ip_address"`
	Session   string `json:"session"`
}

type UserDetail struct {
	UserId      int    `json:"user_id"`
	Username    string `json:"username"`
	Authorize   string `json:"authorized"`
	CompanyCode string `json:"company_code"`
	Role        uint16 `json:"role"`
	IpAddress   string `json:"ip_address"`
	Client      string `json:"client"`
}
