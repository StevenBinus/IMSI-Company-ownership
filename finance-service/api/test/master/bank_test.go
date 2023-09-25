package mastertest

import (
	"finance/api/config"
	masterpayloads "finance/api/payloads/master"
	masterrepoimpl "finance/api/repositories/master/repository-impl"
	masterserviceimpl "finance/api/services/master/service-impl"
	"fmt"
	"testing"
)

func TestSaveBank(t *testing.T) {
	config.InitEnvConfigs(true, "")
	db := config.InitDB()
	bankrepo := masterrepoimpl.OpenBankRepoImpl(db)
	bankservice := masterserviceimpl.OpenBankService(bankrepo)

	save, err := bankservice.Save(masterpayloads.SaveBankRequests{
		IsActive: true,
		BankId:   0,
		BankCode: "HKY",
		BankName: "Hengwie",
		BankAbbr: "Heng",
	})

	if err != nil {
		panic(err)
	}
	fmt.Println(save)
}
