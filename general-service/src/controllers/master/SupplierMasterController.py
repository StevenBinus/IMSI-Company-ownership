from fastapi import APIRouter, HTTPException, status, Query, Request
from src.services.master import SupplierMasterService
from src.repositories.master import SupplierMasterRepo
from src.payloads.responses.GeneralResponse import payload_response
from src.payloads.responses.PaginationResponse import pagination_response
from src.exceptions.RequestException import ResponseException
from src.payloads.schemas.master.SupplierMasterSchema import MtrSupplierResponse

router = APIRouter(tags=["Supplier Master"],prefix="/api/general")

@router.get("/supplier-master",status_code=200)
async def get_supplier_list(
                    page:int, 
                    limit:int, 
                    supplier_code:str|None=None, 
                    supplier_name:str|None=None,
                    supplier_type:int|None=None,
                    address_1:str|None=None,
                    address_2:str|None=None,
                    is_active:bool|None=None,
                    sort_by:str|None=None,
                    sort_of:str|None=None):
    get_all_params = {
            "supplier_code": supplier_code,
            "supplier_name": supplier_name,
            "supplier_type_id": supplier_type,
            "address_street_1": address_1,
            "address_street_2": address_2,
            "is_active": is_active
        }
    sort_fields = {"sort_by":sort_by,"sort_of":sort_of}

    get_results, pages, err = SupplierMasterService.get_supplier_list(page,limit,get_all_params,sort_fields)
    if not get_results or err != None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(err))
    else:
        return pagination_response(200, "success", page, limit, pages["total_pages"], pages["total_rows"], get_results)
    
@router.get("/supplier-master/{id}")
async def get_supplier_by_id(id:int):
    header, pic_detail, bank_acc_detail, err = SupplierMasterService.get_supplier_by_id(id)
    if not header or err != None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=ResponseException(404))
    else:
        return payload_response(200,"success",MtrSupplierResponse(
            company_id= header.company_id,
            is_active= header.is_active,
            effective_date= str(header.effective_date),
            supplier_id= header.supplier_address_id,
            supplier_code= header.supplier_code,
            supplier_title_prefix= header.supplier_title_prefix,
            supplier_name= header.supplier_name,
            supplier_title_suffix= header.supplier_title_suffix,
            supplier_type_id= header.supplier_type_id,
            term_of_payment_id= header.term_of_payment_id,
            default_currency_id= header.default_currency_id,
            via_binning= header.via_binning,
            is_import_supplier= header.is_import_supplier,
            supplier_invoice_type_id= header.supplier_invoice_type_id,
            supplier_unique_id= header.supplier_unique_id,
            supplier_address_id= header.supplier_address_id,
            supplier_phone_no= header.supplier_phone_no,
            supplier_fax_no= header.supplier_fax_no,
            supplier_mobile_phone= header.supplier_mobile_phone,
            supplier_email_address= header.supplier_email_address,
            minimum_down_payment= header.minimum_down_payment,
            supplier_behaviour_id= header.supplier_behaviour_id,
            supplier_class_id= header.supplier_class_id,
            vat_npwp_no= header.vat_npwp_no,
            vat_npwp_date= str(header.vat_npwp_date),
            vat_pkp_type= header.vat_pkp_type,
            vat_pkp_no= header.vat_pkp_no,
            vat_pkp_date= str(header.vat_pkp_date),
            vat_transaction_id= header.vat_transaction_id,
            vat_name= header.vat_name,
            vat_address_id= header.vat_address_id,
            vat_tax_office= header.vat_tax_office,
            tax_npwp_no= header.tax_npwp_no,
            tax_npwp_date= str(header.tax_npwp_date),
            tax_pkp_type= header.tax_pkp_type,
            tax_pkp_no= header.tax_pkp_no,
            tax_pkp_date= str(header.tax_pkp_date),
            tax_name= header.tax_name,
            tax_address_id= header.tax_address_id,
            tax_tax_office_id= header.tax_tax_office_id,
            supplier_pic= pic_detail,
            supplier_bank_account= bank_acc_detail
        ))