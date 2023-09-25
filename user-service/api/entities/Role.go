package entities

const TableNameRoles = "roles"

// role mapped from table <role>
type Role struct {
	IsActive bool   `gorm:"column:is_active;not null" json:"is_active"`
	RoleId   uint16 `gorm:"column:role_id;primaryKey" json:"role_id"`
	RoleCode string `gorm:"size:10;column:role_code;unique;not null;index:idx_role_code,unique" json:"role_code"`
	RoleName string `gorm:"size:50;column:role_name;unique;not null;index:idx_role_name,unique" json:"role_name"`
	Role     User   `gorm:"foreignKey:RoleId;constraint:OnUpdate:CASCADE,OnDelete:CASCADE;references:role_id"`
}

// custom tablename
func (e *Role) TableName() string {
	return TableNameRoles
}
