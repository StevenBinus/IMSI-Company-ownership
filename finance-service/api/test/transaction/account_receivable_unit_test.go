package accountreceivableunitest

import (
	"finance/api/config"
	accountreceivablepayloads "finance/api/payloads/transaction/account-receivable"
	accountreceivablerepoimpl "finance/api/repositories/transaction/account-receivable/repository-impl"
	accountreceivableserviceimpl "finance/api/services/transaction/account-receivable/services-impl"
	"fmt"
	"testing"
	"time"
)

// func TestUpdateAccountReceivableUnit(t *testing.T) {
// 	config.InitEnvConfigs(true, "")
// 	db := config.InitDB()
// 	accountReceivableUnitRepo := accountreceivablerepoimpl.OpenAccountReceivableRepository(db)
// 	accountReceivableUnitService := accountreceivableserviceimpl.OpenAccountReceivableUnitService(accountReceivableUnitRepo)

// 	invoiceDate, _ := time.Parse("2006-01-02", "2023-07-08")
// 	invoiceDueDate, _ := time.Parse("2006-01-02", "2023-08-08")
// 	TaxIndustryDocumentDate, _ := time.Parse("2006-01-02", "2023-05-08")
// 	billToTaxRegistrationDate, _ := time.Parse("2006-01-02", "2000-09-11")
// 	pkpDate, _ := time.Parse("2006-01-02", "2000-09-11")
// 	InvoiceStatusId := 1

// 	accountReceivableUnitDetail := []accountreceivablepayloads.SaveAccountReceivableUnitDetailRequest{
// 		{
// 			InvoiceUnitDetailSystemNumber:      1,
// 			InvoiceLineNumber:                  1,
// 			InvoiceLineStatus:                  InvoiceStatusId,
// 			VehicleSalesOrderSystemNumber:      1,
// 			VehicleId:                          1,
// 			SalesRepresentativeId:              1,
// 			MediatorFeeAmount:                  1,
// 			AccYearRemark:                      "Update - 1",
// 			InsuranceSupplierId:                1,
// 			BbnAmount:                          43812000,
// 			OfftrAmount:                        353188000,
// 			OfftrNetAmount:                     353188000,
// 			DiscountAmount:                     100000,
// 			OntrAmount:                         397000000,
// 			CostGroupId:                        1,
// 			ItemGroup:                          "",
// 			ItemId:                             1,
// 			ItemDescription:                    "Test Item Description",
// 			ItemQuantity:                       1,
// 			ItemQuantityReturn:                 0,
// 			ItemUnitOfMeasurement:              "",
// 			ItemDiscountPercent:                0,
// 			ItemDiscountAmount:                 0,
// 			ItemCogs:                           0,
// 			ItemCogsReturn:                     0,
// 			TotalItemCogs:                      0,
// 			TotalItemCogsReturn:                0,
// 			UnitCogs:                           0,
// 			StandardAccesoriesCogs:             0,
// 			FreeAccesoriesCogs:                 0,
// 			TransportCogs:                      0,
// 			FreeAccesoriesAccrued:              0,
// 			TransportAccrued:                   0,
// 			PphTaxServiceCode:                  "",
// 			PphTaxPercent:                      0,
// 			PphAmount:                          0,
// 			PoSystemNumber:                     1,
// 			InvoiceReceiptSystemNumber:         1,
// 			TotalCreditNoteDp:                  0,
// 			TotalCreditNoteDpBaseAmount:        0,
// 			TotalCreditNoteBbn:                 0,
// 			TotalCreditNoteBbnBaseAmount:       0,
// 			TotalPayment:                       0,
// 			TotalPaymentAllocated:              0,
// 			IsReturn:                           true,
// 			VarianceDpBbn:                      0,
// 			OptionId:                           1,
// 			PaymentRetur:                       0,
// 			PaymentReturBbn:                    0,
// 			TotalDiscountReturn:                0,
// 			TotalVatReturn:                     0,
// 			TotalBebanPajak:                    0,
// 			FlagReturn:                         0,
// 			TotalAfterDiscountInvoiceReceiptDp: 0,
// 			TotalVatInvoiceDp:                  0,
// 			TotalAfterVatInvoiceDp:             0,
// 		},
// 		{
// 			InvoiceUnitDetailSystemNumber:      2,
// 			InvoiceLineNumber:                  1,
// 			InvoiceLineStatus:                  InvoiceStatusId,
// 			VehicleSalesOrderSystemNumber:      1,
// 			VehicleId:                          1,
// 			SalesRepresentativeId:              1,
// 			MediatorFeeAmount:                  1,
// 			AccYearRemark:                      "Update - 2",
// 			InsuranceSupplierId:                1,
// 			BbnAmount:                          43812000,
// 			OfftrAmount:                        353188000,
// 			OfftrNetAmount:                     353188000,
// 			DiscountAmount:                     100000,
// 			OntrAmount:                         397000000,
// 			CostGroupId:                        1,
// 			ItemGroup:                          "",
// 			ItemId:                             1,
// 			ItemDescription:                    "Test Item Description",
// 			ItemQuantity:                       1,
// 			ItemQuantityReturn:                 0,
// 			ItemUnitOfMeasurement:              "",
// 			ItemDiscountPercent:                0,
// 			ItemDiscountAmount:                 0,
// 			ItemCogs:                           0,
// 			ItemCogsReturn:                     0,
// 			TotalItemCogs:                      0,
// 			TotalItemCogsReturn:                0,
// 			UnitCogs:                           0,
// 			StandardAccesoriesCogs:             0,
// 			FreeAccesoriesCogs:                 0,
// 			TransportCogs:                      0,
// 			FreeAccesoriesAccrued:              0,
// 			TransportAccrued:                   0,
// 			PphTaxServiceCode:                  "",
// 			PphTaxPercent:                      0,
// 			PphAmount:                          0,
// 			PoSystemNumber:                     1,
// 			InvoiceReceiptSystemNumber:         1,
// 			TotalCreditNoteDp:                  0,
// 			TotalCreditNoteDpBaseAmount:        0,
// 			TotalCreditNoteBbn:                 0,
// 			TotalCreditNoteBbnBaseAmount:       0,
// 			TotalPayment:                       0,
// 			TotalPaymentAllocated:              0,
// 			IsReturn:                           true,
// 			VarianceDpBbn:                      0,
// 			OptionId:                           1,
// 			PaymentRetur:                       0,
// 			PaymentReturBbn:                    0,
// 			TotalDiscountReturn:                0,
// 			TotalVatReturn:                     0,
// 			TotalBebanPajak:                    0,
// 			FlagReturn:                         0,
// 			TotalAfterDiscountInvoiceReceiptDp: 0,
// 			TotalVatInvoiceDp:                  0,
// 			TotalAfterVatInvoiceDp:             0,
// 		},
// 		{
// 			InvoiceUnitDetailSystemNumber:      3,
// 			InvoiceLineNumber:                  1,
// 			InvoiceLineStatus:                  InvoiceStatusId,
// 			VehicleSalesOrderSystemNumber:      1,
// 			VehicleId:                          1,
// 			SalesRepresentativeId:              1,
// 			MediatorFeeAmount:                  1,
// 			AccYearRemark:                      "Update - 3",
// 			InsuranceSupplierId:                1,
// 			BbnAmount:                          43812000,
// 			OfftrAmount:                        353188000,
// 			OfftrNetAmount:                     353188000,
// 			DiscountAmount:                     100000,
// 			OntrAmount:                         397000000,
// 			CostGroupId:                        1,
// 			ItemGroup:                          "",
// 			ItemId:                             1,
// 			ItemDescription:                    "Test Item Description",
// 			ItemQuantity:                       1,
// 			ItemQuantityReturn:                 0,
// 			ItemUnitOfMeasurement:              "",
// 			ItemDiscountPercent:                0,
// 			ItemDiscountAmount:                 0,
// 			ItemCogs:                           0,
// 			ItemCogsReturn:                     0,
// 			TotalItemCogs:                      0,
// 			TotalItemCogsReturn:                0,
// 			UnitCogs:                           0,
// 			StandardAccesoriesCogs:             0,
// 			FreeAccesoriesCogs:                 0,
// 			TransportCogs:                      0,
// 			FreeAccesoriesAccrued:              0,
// 			TransportAccrued:                   0,
// 			PphTaxServiceCode:                  "",
// 			PphTaxPercent:                      0,
// 			PphAmount:                          0,
// 			PoSystemNumber:                     1,
// 			InvoiceReceiptSystemNumber:         1,
// 			TotalCreditNoteDp:                  0,
// 			TotalCreditNoteDpBaseAmount:        0,
// 			TotalCreditNoteBbn:                 0,
// 			TotalCreditNoteBbnBaseAmount:       0,
// 			TotalPayment:                       0,
// 			TotalPaymentAllocated:              0,
// 			IsReturn:                           true,
// 			VarianceDpBbn:                      0,
// 			OptionId:                           1,
// 			PaymentRetur:                       0,
// 			PaymentReturBbn:                    0,
// 			TotalDiscountReturn:                0,
// 			TotalVatReturn:                     0,
// 			TotalBebanPajak:                    0,
// 			FlagReturn:                         0,
// 			TotalAfterDiscountInvoiceReceiptDp: 0,
// 			TotalVatInvoiceDp:                  0,
// 			TotalAfterVatInvoiceDp:             0,
// 		},
// 		{
// 			InvoiceUnitDetailSystemNumber:      4,
// 			InvoiceLineNumber:                  1,
// 			InvoiceLineStatus:                  InvoiceStatusId,
// 			VehicleSalesOrderSystemNumber:      1,
// 			VehicleId:                          1,
// 			SalesRepresentativeId:              1,
// 			MediatorFeeAmount:                  1,
// 			AccYearRemark:                      "Update - 4",
// 			InsuranceSupplierId:                1,
// 			BbnAmount:                          43812000,
// 			OfftrAmount:                        353188000,
// 			OfftrNetAmount:                     353188000,
// 			DiscountAmount:                     100000,
// 			OntrAmount:                         397000000,
// 			CostGroupId:                        1,
// 			ItemGroup:                          "",
// 			ItemId:                             1,
// 			ItemDescription:                    "Test Item Description",
// 			ItemQuantity:                       1,
// 			ItemQuantityReturn:                 0,
// 			ItemUnitOfMeasurement:              "",
// 			ItemDiscountPercent:                0,
// 			ItemDiscountAmount:                 0,
// 			ItemCogs:                           0,
// 			ItemCogsReturn:                     0,
// 			TotalItemCogs:                      0,
// 			TotalItemCogsReturn:                0,
// 			UnitCogs:                           0,
// 			StandardAccesoriesCogs:             0,
// 			FreeAccesoriesCogs:                 0,
// 			TransportCogs:                      0,
// 			FreeAccesoriesAccrued:              0,
// 			TransportAccrued:                   0,
// 			PphTaxServiceCode:                  "",
// 			PphTaxPercent:                      0,
// 			PphAmount:                          0,
// 			PoSystemNumber:                     1,
// 			InvoiceReceiptSystemNumber:         1,
// 			TotalCreditNoteDp:                  0,
// 			TotalCreditNoteDpBaseAmount:        0,
// 			TotalCreditNoteBbn:                 0,
// 			TotalCreditNoteBbnBaseAmount:       0,
// 			TotalPayment:                       0,
// 			TotalPaymentAllocated:              0,
// 			IsReturn:                           true,
// 			VarianceDpBbn:                      0,
// 			OptionId:                           1,
// 			PaymentRetur:                       0,
// 			PaymentReturBbn:                    0,
// 			TotalDiscountReturn:                0,
// 			TotalVatReturn:                     0,
// 			TotalBebanPajak:                    0,
// 			FlagReturn:                         0,
// 			TotalAfterDiscountInvoiceReceiptDp: 0,
// 			TotalVatInvoiceDp:                  0,
// 			TotalAfterVatInvoiceDp:             0,
// 		},
// 		{
// 			InvoiceUnitDetailSystemNumber:      5,
// 			InvoiceLineNumber:                  1,
// 			InvoiceLineStatus:                  InvoiceStatusId,
// 			VehicleSalesOrderSystemNumber:      1,
// 			VehicleId:                          1,
// 			SalesRepresentativeId:              1,
// 			MediatorFeeAmount:                  1,
// 			AccYearRemark:                      "Update - 5",
// 			InsuranceSupplierId:                1,
// 			BbnAmount:                          43812000,
// 			OfftrAmount:                        353188000,
// 			OfftrNetAmount:                     353188000,
// 			DiscountAmount:                     100000,
// 			OntrAmount:                         397000000,
// 			CostGroupId:                        1,
// 			ItemGroup:                          "",
// 			ItemId:                             1,
// 			ItemDescription:                    "Test Item Description",
// 			ItemQuantity:                       1,
// 			ItemQuantityReturn:                 0,
// 			ItemUnitOfMeasurement:              "",
// 			ItemDiscountPercent:                0,
// 			ItemDiscountAmount:                 0,
// 			ItemCogs:                           0,
// 			ItemCogsReturn:                     0,
// 			TotalItemCogs:                      0,
// 			TotalItemCogsReturn:                0,
// 			UnitCogs:                           0,
// 			StandardAccesoriesCogs:             0,
// 			FreeAccesoriesCogs:                 0,
// 			TransportCogs:                      0,
// 			FreeAccesoriesAccrued:              0,
// 			TransportAccrued:                   0,
// 			PphTaxServiceCode:                  "",
// 			PphTaxPercent:                      0,
// 			PphAmount:                          0,
// 			PoSystemNumber:                     1,
// 			InvoiceReceiptSystemNumber:         1,
// 			TotalCreditNoteDp:                  0,
// 			TotalCreditNoteDpBaseAmount:        0,
// 			TotalCreditNoteBbn:                 0,
// 			TotalCreditNoteBbnBaseAmount:       0,
// 			TotalPayment:                       0,
// 			TotalPaymentAllocated:              0,
// 			IsReturn:                           true,
// 			VarianceDpBbn:                      0,
// 			OptionId:                           1,
// 			PaymentRetur:                       0,
// 			PaymentReturBbn:                    0,
// 			TotalDiscountReturn:                0,
// 			TotalVatReturn:                     0,
// 			TotalBebanPajak:                    0,
// 			FlagReturn:                         0,
// 			TotalAfterDiscountInvoiceReceiptDp: 0,
// 			TotalVatInvoiceDp:                  0,
// 			TotalAfterVatInvoiceDp:             0,
// 		},
// 	}

// 	update, err := accountReceivableUnitService.UpdateAccountReceivableUnit(accountreceivablepayloads.SaveAccountReceivableUnitHeaderRequest{
// 		IsActive:                               true,
// 		CompanyId:                              1,
// 		InvoiceStatusId:                        InvoiceStatusId,
// 		InvoiceUnitSystemNumber:                1,
// 		AccountReceivableInvoiceTypeId:         1,
// 		InvoiceDate:                            invoiceDate,
// 		InvoiceDueDate:                         invoiceDueDate,
// 		TaxIndustryDocumentNumber:              "000033/NMDI/PPH22/II/2023",
// 		TaxIndustryDocumentDate:                TaxIndustryDocumentDate,
// 		BrandId:                                1,
// 		ProfitCenterId:                         1,
// 		CostCenterId:                           1,
// 		TransactionTypeAccountReceviableUnitId: 1,
// 		CustomerId:                             1,
// 		FundTypeId:                             1,
// 		LeasingSupplierId:                      1,
// 		PurchaseOrderSystemNumber:              1,
// 		PaymentTypeId:                          1,
// 		EventId:                                5,
// 		Remark:                                 "Test Remark",
// 		BillToCustomerId:                       1,
// 		BillToTitlePrefix:                      "Test Prefix",
// 		BillToName:                             "Test Bill To Name",
// 		BillToTitleSuffix:                      "Test Suffix",
// 		BillToTypeId:                           1,
// 		BillToIdNo:                             "015/517/NGS/BTM/I/2023",
// 		BillableToId:                           1,
// 		BillToAddressId:                        1,
// 		BillToAddressStreetLine1:               "Test Bil Address 1",
// 		BillToAddressStreetLine2:               "Test Bil Address 2",
// 		BillToAddressStreetLine3:               "Test Bil Address 3",
// 		BillToPhoneNo:                          "082344432133",
// 		BillToFaxNo:                            "089958873244",
// 		TopId:                                  1,
// 		BillCodeId:                             1,
// 		TaxInvoiceTypeId:                       1,
// 		BillToTaxRegistrationNumber:            "31.456.665.4-215.000",
// 		BillToTaxRegistrationDate:              billToTaxRegistrationDate,
// 		PkpType:                                "N",
// 		PkpNumber:                              "00.000.000.0-000.000",
// 		PkpDate:                                pkpDate,
// 		VatTransactionId:                       1,
// 		TaxName:                                "Test Tax Name",
// 		TaxAddressId:                           1,
// 		TaxAddressStreetLine1:                  "Test Tax Address 1",
// 		TaxAddressStreetLine2:                  "Test Tax Address 2",
// 		TaxAddressStreetLine3:                  "Test Tax Address 3",
// 		AccountReceivableUnitDetail:            accountReceivableUnitDetail,
// 	})

// 	if err != nil {
// 		panic(err)
// 	}

// 	fmt.Println(update)
// }

func TestInsertAccountReceivableUnit(t *testing.T) {
	config.InitEnvConfigs(true, "")
	db := config.InitDB()
	accountReceivableUnitRepo := accountreceivablerepoimpl.OpenAccountReceivableRepository(db)
	accountReceivableUnitService := accountreceivableserviceimpl.OpenAccountReceivableUnitService(accountReceivableUnitRepo)

	invoiceDate, _ := time.Parse("2006-01-02", "2023-07-08")
	invoiceDueDate, _ := time.Parse("2006-01-02", "2023-08-08")
	TaxIndustryDocumentDate, _ := time.Parse("2006-01-02", "2023-05-08")
	billToTaxRegistrationDate, _ := time.Parse("2006-01-02", "2000-09-11")
	pkpDate, _ := time.Parse("2006-01-02", "2000-09-11")
	InvoiceStatusId := 1

	saveHeader, err := accountReceivableUnitService.SaveHeader(accountreceivablepayloads.SaveHeaderRequest{
		InvoiceUnitSystemNumber:                0,
		IsActive:                               true,
		CompanyId:                              1,
		InvoiceStatusId:                        InvoiceStatusId,
		AccountReceivableInvoiceTypeId:         1,
		InvoiceDate:                            invoiceDate,
		InvoiceDueDate:                         invoiceDueDate,
		TaxIndustryDocumentNumber:              "000033/NMDI/PPH22/II/2023",
		TaxIndustryDocumentDate:                TaxIndustryDocumentDate,
		BrandId:                                1,
		ProfitCenterId:                         1,
		CostCenterId:                           1,
		TransactionTypeAccountReceviableUnitId: 1,
		CustomerId:                             1,
		FundTypeId:                             1,
		LeasingSupplierId:                      1,
		PurchaseOrderSystemNumber:              1,
		PaymentTypeId:                          1,
		EventId:                                5,
		Remark:                                 "Test Remark - Update	",
		BillToCustomerId:                       1,
		BillToTitlePrefix:                      "Test Prefix",
		BillToName:                             "Test Bill To Name",
		BillToTitleSuffix:                      "Test Suffix",
		BillToTypeId:                           1,
		BillToIdNo:                             "015/517/NGS/BTM/I/2023",
		BillableToId:                           1,
		BillToAddressId:                        1,
		BillToAddressStreetLine1:               "Test Bil Address 1",
		BillToAddressStreetLine2:               "Test Bil Address 2",
		BillToAddressStreetLine3:               "Test Bil Address 3",
		BillToPhoneNo:                          "082344432133",
		BillToFaxNo:                            "089958873244",
		TopId:                                  1,
		BillCodeId:                             1,
		TaxInvoiceTypeId:                       1,
		BillToTaxRegistrationNumber:            "31.456.665.4-215.000",
		BillToTaxRegistrationDate:              billToTaxRegistrationDate,
		PkpType:                                "N",
		PkpNumber:                              "00.000.000.0-000.000",
		PkpDate:                                pkpDate,
		VatTransactionId:                       1,
		TaxName:                                "Test Tax Name",
		TaxAddressId:                           1,
		TaxAddressStreetLine1:                  "Test Tax Address 1",
		TaxAddressStreetLine2:                  "Test Tax Address 2",
		TaxAddressStreetLine3:                  "Test Tax Address 3",
	}, accountreceivablepayloads.UpdateVatRequest{
		VatPercent:              0,
		TotalVat:                0,
		TotalVatBaseAmount:      10000,
		TotalAfterVatBaseAmount: 10000,
		TotalAfterVat:           15000,
		IsUpdate:                true,
	})

	if err != nil {
		panic(err)
	}

	fmt.Println(saveHeader)
}

func TestUpdateStatusAccountReceivableUnit(t *testing.T) {
	config.InitEnvConfigs(true, "")
	db := config.InitDB()
	accountReceivableUnitRepo := accountreceivablerepoimpl.OpenAccountReceivableRepository(db)
	accountReceivableUnitService := accountreceivableserviceimpl.OpenAccountReceivableUnitService(accountReceivableUnitRepo)

	changeStatus, err := accountReceivableUnitService.UpdateStatus(6, accountreceivablepayloads.UpdateStatusRequest{IsActive: true})

	if err != nil {
		panic(err)
	}

	fmt.Println(changeStatus)
}

func TestGetAccountReceivableUnitById(t *testing.T) {
	config.InitEnvConfigs(true, "")
	db := config.InitDB()
	accountReceivableUnitRepo := accountreceivablerepoimpl.OpenAccountReceivableRepository(db)
	accountReceivableUnitService := accountreceivableserviceimpl.OpenAccountReceivableUnitService(accountReceivableUnitRepo)

	get, err := accountReceivableUnitService.GetById(1)

	if err != nil {
		panic(err)
	}

	fmt.Println(get)
}
