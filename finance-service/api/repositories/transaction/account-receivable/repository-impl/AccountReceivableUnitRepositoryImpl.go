package accountreceivablerepoimpl

import (
	accountreceivableentities "finance/api/entities/transaction/account-receivable"
	"finance/api/payloads/pagination"
	accountreceivablepayloads "finance/api/payloads/transaction/account-receivable"
	accountreceivablerepo "finance/api/repositories/transaction/account-receivable"
	"log"

	"gorm.io/gorm"
)

type AccountReceivableRepositoryImpl struct {
	DB *gorm.DB
}

func (r *AccountReceivableRepositoryImpl) WithTrx(trxHandle *gorm.DB) accountreceivablerepo.AccountReceivableUnitRepository {
	if trxHandle == nil {
		log.Println("Transaction Database Not Found!")
		return r
	}

	r.DB = trxHandle
	return r
}

func OpenAccountReceivableRepository(db *gorm.DB) accountreceivablerepo.AccountReceivableUnitRepository {
	return &AccountReceivableRepositoryImpl{
		DB: db,
	}
}

func (r *AccountReceivableRepositoryImpl) SaveHeader(request accountreceivablepayloads.SaveHeaderRequest, vatRequest accountreceivablepayloads.UpdateVatRequest) (bool, error) {
	updatePayload := accountreceivableentities.AccountReceivableUnit{
		// IsActive:                               request.IsActive,
		CompanyId:                              request.CompanyId,
		InvoiceUnitSystemNumber:                request.InvoiceUnitSystemNumber,
		InvoiceStatusId:                        request.InvoiceStatusId,
		AccountReceivableInvoiceTypeId:         request.AccountReceivableInvoiceTypeId,
		InvoiceDate:                            request.InvoiceDate,
		InvoiceDueDate:                         request.InvoiceDueDate,
		TaxIndustryDocumentNumber:              request.TaxIndustryDocumentNumber,
		TaxIndustryDocumentDate:                request.TaxIndustryDocumentDate,
		BrandId:                                request.BrandId,
		ProfitCenterId:                         request.ProfitCenterId,
		CostCenterId:                           request.CostCenterId,
		TransactionTypeAccountReceviableUnitId: request.TransactionTypeAccountReceviableUnitId,
		CustomerId:                             request.CustomerId,
		FundTypeId:                             request.FundTypeId,
		LeasingSupplierId:                      request.LeasingSupplierId,
		PurchaseOrderSystemNumber:              request.PurchaseOrderSystemNumber,
		PaymentTypeId:                          request.PaymentTypeId,
		EventId:                                request.EventId,
		Remark:                                 request.Remark,
		BillToCustomerId:                       request.BillToCustomerId,
		BillToTitlePrefix:                      request.BillToTitlePrefix,
		BillToName:                             request.BillToName,
		BillToTitleSuffix:                      request.BillToTitleSuffix,
		BillToTypeId:                           request.BillToTypeId,
		BillToIdNo:                             request.BillToIdNo,
		BillableToId:                           request.BillableToId,
		BillToAddressId:                        request.BillToAddressId,
		BillToAddressStreetLine1:               request.BillToAddressStreetLine1,
		BillToAddressStreetLine2:               request.BillToAddressStreetLine2,
		BillToAddressStreetLine3:               request.BillToAddressStreetLine3,
		BillToPhoneNo:                          request.BillToPhoneNo,
		BillToFaxNo:                            request.BillToPhoneNo,
		TopId:                                  request.TopId,
		BillCodeId:                             request.BillCodeId,
		TaxInvoiceTypeId:                       request.TaxInvoiceTypeId,
		BillToTaxRegistrationNumber:            request.BillToTaxRegistrationNumber,
		BillToTaxRegistrationDate:              request.BillToTaxRegistrationDate,
		PkpType:                                request.PkpType,
		PkpNumber:                              request.PkpNumber,
		PkpDate:                                request.PkpDate,
		VatTransactionId:                       request.VatTransactionId,
		TaxName:                                request.TaxName,
		TaxAddressId:                           request.TaxAddressId,
		TaxAddressStreetLine1:                  request.TaxAddressStreetLine1,
		TaxAddressStreetLine2:                  request.TaxAddressStreetLine2,
		TaxAddressStreetLine3:                  request.TaxAddressStreetLine3,
	}

	if vatRequest.IsUpdate {
		pointerUpdatePayload := &updatePayload

		pointerUpdatePayload.VatPercent = vatRequest.VatPercent
		pointerUpdatePayload.TotalVat = vatRequest.TotalVat
		pointerUpdatePayload.TotalVatBaseAmount = vatRequest.TotalVatBaseAmount
		pointerUpdatePayload.TotalAfterVatBaseAmount = vatRequest.TotalAfterVatBaseAmount
		pointerUpdatePayload.TotalAfterVat = vatRequest.TotalAfterVat
	}

	rows, err := r.DB.
		Save(&updatePayload).
		Rows()

	if err != nil {
		return false, err
	}

	defer rows.Close()

	return true, err
}

func (r *AccountReceivableRepositoryImpl) UpdateStatus(invoiceUnitSystemNumber int, request accountreceivablepayloads.UpdateStatusRequest) (bool, error) {
	var entities accountreceivableentities.AccountReceivableUnit

	if request.IsActive {
		request.IsActive = false
	} else {
		request.IsActive = true
	}

	rows, err := r.DB.
		Model(&entities).
		Where(accountreceivableentities.AccountReceivableUnit{
			InvoiceUnitSystemNumber: invoiceUnitSystemNumber,
		}).
		Update("is_active", request.IsActive).
		Rows()

	if err != nil {
		return false, err
	}

	defer rows.Close()

	return true, nil
}

func (r *AccountReceivableRepositoryImpl) GetById(invoiceUnitSystemNumber int) (accountreceivableentities.AccountReceivableUnit, error) {
	var entities accountreceivableentities.AccountReceivableUnit

	rows, err := r.DB.
		Preload("AccountReceivableUnitDetail").
		Where(accountreceivableentities.AccountReceivableUnit{
			InvoiceUnitSystemNumber: invoiceUnitSystemNumber,
		}).
		Find(&entities).
		Scan(&entities).
		Rows()

	if err != nil {
		return entities, err
	}

	defer rows.Close()

	return entities, nil
}

func (r *AccountReceivableRepositoryImpl) GetAll(request accountreceivablepayloads.GetAllHeaderRequest, pages pagination.Pagination) (pagination.Pagination, error) {
	var invoiceUnitEntities []accountreceivableentities.AccountReceivableUnit
	var invoiceUnitResponses []accountreceivablepayloads.GetAllHeaderResponse

	tempRows := r.DB.
		Model(&accountreceivableentities.AccountReceivableUnit{}).
		Select(
			"company_id",
			"invoice_unit_system_number",
			"invoice_unit_document_number",
			"invoice_date",
			"invoice_due_date",
			"brand_id",
			"customer_id customer_name",
			"bill_to_customer_id bill_to_customer_name",
			"total_after_vat",
			"invoice_status_id invoice_status",
		).Where("company_id = ?", request.CompanyId)

	if request.InvoiceUnitDocumentNumber != "" {
		tempRows = tempRows.Where("invoice_unit_document_number like ?", "%"+request.InvoiceUnitDocumentNumber+"%")
	}
	if request.BrandId != 0 {
		tempRows = tempRows.Where("brand_id = ?", request.BrandId)
	}
	if request.CustomerId != 0 {
		tempRows = tempRows.Where("customer_id = ?", request.CustomerId)
	}
	if request.BillToCustomerId != 0 {
		tempRows = tempRows.Where("bill_to_customer_id = ?", request.BillToCustomerId)
	}
	if request.TransactionTypeAccountReceviableUnitId != 0 {
		tempRows = tempRows.Where("transaction_type_account_receviable_unit_id = ?", request.TransactionTypeAccountReceviableUnitId)
	}
	if request.InvoiceStatusId != 0 {
		tempRows = tempRows.Where("transaction_type_account_receviable_unit_id = ?", request.InvoiceStatusId)
	}
	if !request.InvoiceDateFrom.IsZero() {
		if !request.InvoiceDateTo.IsZero() {
			tempRows = tempRows.Where("invoice_date between ? and ?", request.InvoiceDateFrom, request.InvoiceDateTo)
		} else {
			tempRows = tempRows.Where("invoice_date >= ?", request.InvoiceDateFrom)
		}
	}
	if !request.InvoiceDueDateFrom.IsZero() {
		if !request.InvoiceDueDateTo.IsZero() {
			tempRows = tempRows.Where("invoice_due_date between ? and ?", request.InvoiceDueDateFrom, request.InvoiceDueDateTo)
		} else {
			tempRows = tempRows.Where("invoice_due_date >= ?", request.InvoiceDueDateFrom)
		}
	}
	rows, err := tempRows.
		Scopes(pagination.Paginate(invoiceUnitEntities, &pages, tempRows)).
		Scan(&invoiceUnitResponses).
		Rows()

	if err != nil {
		return pages, err
	}

	defer rows.Close()
	pages.Rows = invoiceUnitResponses
	return pages, nil
}

// for i := range request.AccountReceivableUnitDetail {
// 	accountReceivableUnitDetail = append(accountReceivableUnitDetail, accountreceivableentities.AccountReceivableUnitDetail{
// 		InvoiceUnitDetailSystemNumber:      request.AccountReceivableUnitDetail[i].InvoiceUnitDetailSystemNumber,
// 		InvoiceLineNumber:                  request.AccountReceivableUnitDetail[i].InvoiceLineNumber,
// 		InvoiceLineStatus:                  request.AccountReceivableUnitDetail[i].InvoiceLineStatus,
// 		VehicleSalesOrderSystemNumber:      request.AccountReceivableUnitDetail[i].VehicleSalesOrderSystemNumber,
// 		VehicleId:                          request.AccountReceivableUnitDetail[i].VehicleId,
// 		SalesRepresentativeId:              request.AccountReceivableUnitDetail[i].SalesRepresentativeId,
// 		MediatorFeeAmount:                  request.AccountReceivableUnitDetail[i].MediatorFeeAmount,
// 		AccYearRemark:                      request.AccountReceivableUnitDetail[i].AccYearRemark,
// 		InsuranceSupplierId:                request.AccountReceivableUnitDetail[i].InsuranceSupplierId,
// 		BbnAmount:                          request.AccountReceivableUnitDetail[i].BbnAmount,
// 		OfftrAmount:                        request.AccountReceivableUnitDetail[i].OfftrAmount,
// 		OfftrNetAmount:                     request.AccountReceivableUnitDetail[i].OfftrNetAmount,
// 		DiscountAmount:                     request.AccountReceivableUnitDetail[i].DiscountAmount,
// 		OntrAmount:                         request.AccountReceivableUnitDetail[i].OntrAmount,
// 		CostGroupId:                        request.AccountReceivableUnitDetail[i].CostGroupId,
// 		ItemGroup:                          request.AccountReceivableUnitDetail[i].ItemGroup,
// 		ItemId:                             request.AccountReceivableUnitDetail[i].ItemId,
// 		ItemDescription:                    request.AccountReceivableUnitDetail[i].ItemDescription,
// 		ItemQuantity:                       request.AccountReceivableUnitDetail[i].ItemQuantity,
// 		ItemQuantityReturn:                 request.AccountReceivableUnitDetail[i].ItemQuantityReturn,
// 		ItemUnitOfMeasurement:              request.AccountReceivableUnitDetail[i].ItemUnitOfMeasurement,
// 		ItemDiscountPercent:                request.AccountReceivableUnitDetail[i].ItemDiscountPercent,
// 		ItemDiscountAmount:                 request.AccountReceivableUnitDetail[i].ItemDiscountAmount,
// 		ItemCogs:                           request.AccountReceivableUnitDetail[i].ItemCogs,
// 		ItemCogsReturn:                     request.AccountReceivableUnitDetail[i].ItemCogsReturn,
// 		TotalItemCogs:                      request.AccountReceivableUnitDetail[i].TotalItemCogs,
// 		TotalItemCogsReturn:                request.AccountReceivableUnitDetail[i].TotalItemCogsReturn,
// 		UnitCogs:                           request.AccountReceivableUnitDetail[i].UnitCogs,
// 		StandardAccesoriesCogs:             request.AccountReceivableUnitDetail[i].StandardAccesoriesCogs,
// 		FreeAccesoriesCogs:                 request.AccountReceivableUnitDetail[i].FreeAccesoriesCogs,
// 		TransportCogs:                      request.AccountReceivableUnitDetail[i].TransportCogs,
// 		FreeAccesoriesAccrued:              request.AccountReceivableUnitDetail[i].FreeAccesoriesAccrued,
// 		TransportAccrued:                   request.AccountReceivableUnitDetail[i].TransportAccrued,
// 		PphTaxServiceCode:                  request.AccountReceivableUnitDetail[i].PphTaxServiceCode,
// 		PphTaxPercent:                      request.AccountReceivableUnitDetail[i].PphTaxPercent,
// 		PphAmount:                          request.AccountReceivableUnitDetail[i].PphAmount,
// 		PoSystemNumber:                     request.AccountReceivableUnitDetail[i].PoSystemNumber,
// 		InvoiceReceiptSystemNumber:         request.AccountReceivableUnitDetail[i].InvoiceReceiptSystemNumber,
// 		TotalCreditNoteDp:                  request.AccountReceivableUnitDetail[i].TotalCreditNoteDp,
// 		TotalCreditNoteDpBaseAmount:        request.AccountReceivableUnitDetail[i].TotalCreditNoteDpBaseAmount,
// 		TotalCreditNoteBbn:                 request.AccountReceivableUnitDetail[i].TotalCreditNoteBbn,
// 		TotalCreditNoteBbnBaseAmount:       request.AccountReceivableUnitDetail[i].TotalCreditNoteBbnBaseAmount,
// 		TotalPayment:                       request.AccountReceivableUnitDetail[i].TotalPayment,
// 		TotalPaymentAllocated:              request.AccountReceivableUnitDetail[i].TotalPaymentAllocated,
// 		IsReturn:                           request.AccountReceivableUnitDetail[i].IsReturn,
// 		VarianceDpBbn:                      request.AccountReceivableUnitDetail[i].VarianceDpBbn,
// 		OptionId:                           request.AccountReceivableUnitDetail[i].OptionId,
// 		PaymentRetur:                       request.AccountReceivableUnitDetail[i].PaymentRetur,
// 		PaymentReturBbn:                    request.AccountReceivableUnitDetail[i].PaymentReturBbn,
// 		TotalDiscountReturn:                request.AccountReceivableUnitDetail[i].TotalDiscountReturn,
// 		TotalVatReturn:                     request.AccountReceivableUnitDetail[i].TotalVatReturn,
// 		TotalBebanPajak:                    request.AccountReceivableUnitDetail[i].TotalBebanPajak,
// 		FlagReturn:                         request.AccountReceivableUnitDetail[i].FlagReturn,
// 		TotalAfterDiscountInvoiceReceiptDp: request.AccountReceivableUnitDetail[i].TotalAfterDiscountInvoiceReceiptDp,
// 		TotalVatInvoiceDp:                  request.AccountReceivableUnitDetail[i].TotalVatInvoiceDp,
// 		TotalAfterVatInvoiceDp:             request.AccountReceivableUnitDetail[i].TotalAfterVatInvoiceDp,
// 	})
// }
