package masterentities

import accountreceivableentities "finance/api/entities/transaction/account-receivable"

const TableNameEvent = "mtr_event"

type Event struct {
	IsActive               bool                                              `gorm:"column:is-active;default:true;not null;" json:"is_active"`
	EventId                int                                               `gorm:"column:event_id;not null;primaryKey;type:int" json:"event_id"`
	CpcType                string                                            `gorm:"column:cpc_type;default:null;type:char(1);" json:"cpc_type"`
	GeneralLedgerProcessId int                                               `gorm:"column:general_ledger_process_id;type:int;not null;" json:"general_ledger_process_id"`
	ProcessMapId           int                                               `gorm:"column:process_map_id;type:int;not null;" json:"process_map_id"`
	EventNo                string                                            `gorm:"column:event_no;index:idx_mtr_event,unique;type:varchar(10);not null;" json:"event_no"`
	EventDescription       string                                            `gorm:"column:event_description;type:varchar(150)" json:"event_description"`
	ContentFilter          string                                            `gorm:"content_filter;size:20;default:null;" json:"content_filter"`
	ContentFilter2         string                                            `gorm:"content_filter2;size:20;default:null;" json:"content_filter2"`
	AccountReceivableUnit  []accountreceivableentities.AccountReceivableUnit `gorm:"foreignKey:EventId;constraint:OnUpdate:CASCADE,OnDelete:CASCADE;references:event_id" json:"trx_account_receivable_units"`
}

func (*Event) TableName() string {
	return TableNameEvent
}
