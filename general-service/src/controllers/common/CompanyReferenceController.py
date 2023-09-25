from fastapi import APIRouter, HTTPException, status, Query, Request
from src.payloads.schemas.master.CompanyReferenceSchema import MtrCompanyreferenceGet
from src.repositories.common import CompanyReferenceRepo
from src.services.common import CompanyReferenceServices
from src.payloads.responses.GeneralResponse import payload_response
from src.payloads.responses.PaginationResponse import pagination_response
from src.exceptions.RequestException import ResponseException


router = APIRouter(tags=["Company Reference"],prefix="/api/general")

@router.get("/company_references",status_code=200)
async def get_all_company_reference(page:int,limit:int,
                                    is_active:bool|None=None,
                                    company_id:int|None=None,
                                    currency_id:int|None=None,
                                    margin_outer_kpp:int|None=None,
                                    adjustment_reason_id:int|None=None,
                                    lead_time_unit_etd:int|None=None,
                                    bank_acc_receive_company_id:int|None=None,
                                    vat_code:str|None=None,
                                    item_broken_warehouse_id:int|None=None,
                                    unit_warehouse_id:int|None=None,
                                    use_dms:bool|None=None,
                                    time_difference:int|None=None,
                                    operation_discount_outer_kpp:int|None=None,
                                    check_month_end:bool|None=None,
                                    coa_group_id:int|None=None,
                                    with_vat:bool|None=None,
                                    approval_spm_id:int|None=None,
                                    is_use_tax_industry:bool|None=None,
                                    markup_percentage:int|None=None,
                                    is_external_pdi:bool|None=None,
                                    hide_cost:bool|None=None,
                                    use_price_code:bool|None=None,
                                    disable_edit_draft:bool|None=None,
                                    sort_of:str|None=None,
                                    sort_by:str|None=None):
    get_all_params={
        "is_active":is_active,
        "company_id":company_id,
        "currency_id":currency_id,
        "margin_outer_kpp":margin_outer_kpp,
        "adjustmenat_reason_id":adjustment_reason_id,
        "lead_time_unit_etd":lead_time_unit_etd,
        "bank_acc_receive_company_id":bank_acc_receive_company_id,
        "vat_code":vat_code,
        "item_broken_warehouse_id":item_broken_warehouse_id,
        "unit_warehouse_id":unit_warehouse_id,
        "use_dms":use_dms,
        "time_difference":time_difference,
        "operation_discount_outer_kpp":operation_discount_outer_kpp,
        "check_month_end":check_month_end,
        "coa_group_id":coa_group_id,
        "with_vat":with_vat,
        "approval_spm_id":approval_spm_id,
        "is_use_tax_industry":is_use_tax_industry,
        "markup_percentage":markup_percentage,
        "is_external_pdi":is_external_pdi,
        "hide_cost":hide_cost,
        "use_price_code":use_price_code,
        "disable_edit_draft":disable_edit_draft
    }
    sort_params={
        "sort_by":sort_by,
        "sort_of":sort_of
    }
    get_company_references,pages,err = CompanyReferenceServices.get_all_company_references(page,limit,get_all_params,sort_params)
    if err == None and get_company_references!=[]:
        return pagination_response(200,"Success",page,limit,pages["total_pages"],pages["total_rows"],get_company_references)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))

@router.get("/companyreference/{company_id}",status_code=200)
async def get_all_is_use_tax_invoice(company_id:int):
    get_result,err =CompanyReferenceServices.get_tax_industry_by_company_id(company_id)
    if not get_result and err ==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(err))
    else:
        return payload_response(200,"Success",get_result)
    

@router.get("/company_reference/{company_id}",status_code=200)
async def get_all_company_reference_by_id(company_id:int):
    get_result,err=CompanyReferenceServices.get_company_reference_by_company_id(company_id)
    if not get_result and err ==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=str(err))
    else:
        return payload_response(200,"Success",get_result)
    

@router.post("/company_reference",status_code=201)
async def post_company_reference(req:MtrCompanyreferenceGet):
    created_data,err=CompanyReferenceServices.post_company_reference(req)
    if err == None:
        return payload_response(201,"Created",created_data)
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=str(err))

@router.put("/company_reference/{company_id}",status_code=201)
async def put_company_reference(company_id:int,req:MtrCompanyreferenceGet):
    updated_data,err=CompanyReferenceServices.put_company_reference(company_id,req)
    if err == None:
        return payload_response(201,"Success",updated_data)
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=str(err))
    
@router.patch("/company_reference/{company_id}",status_code=201)
async def patch_company_reference(company_id:int):
        updated_data, err = CompanyReferenceServices.patch_company_reference(company_id)
        if err == None:
            return payload_response(201,"Updated", updated_data)
        else:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=str(err))
        

