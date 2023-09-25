from fastapi import APIRouter,HTTPException,status,Request
from src.exceptions.RequestException import ResponseException
from src.services.common import VatCompanyService
from src.payloads.schemas.master import VatSchema
from src.payloads.responses.GeneralResponse import payload_response
from src.payloads.responses.PaginationResponse import pagination_response

router = APIRouter(tags=["Vat Company"],prefix="/api/general")

@router.get("/vat-company", status_code=200)
def get_all(page:int, limit:int,
            is_active:bool|None=None,
            vat_company_id:int|None=None,
            company_id:int|None=None,
            vat_npwp_no:int|None=None,
            vat_npwp_date:str|None=None,
            vat_tax_out_transaction_id:int|None=None,
            vat_tax_branch_code:str|None=None,
            vat_name:str|None=None,
            vat_address_id:int|None=None,
            vat_reserve:str|None=None,
            vat_pkp_type:str|None=None,
            vat_pkp_no:str|None=None,
            vat_pkp_date:str|None=None,
            vat_tax_office_id:int|None=None,
            sort_of:str|None=None,
            sort_by:str|None=None):
    get_all_params={"is_active":is_active,
                    "vat_company_id":vat_company_id,
                    "company_id":company_id,
                    "vat_npwp_no":vat_npwp_no,
                    "vat_npwp_date":vat_npwp_date,
                    "vat_tax_out_transaction_id":vat_tax_out_transaction_id,
                    "vat_tax_branch_code":vat_tax_branch_code,
                    "vat_name":vat_name,
                    "vat_address_id":vat_address_id,
                    "vat_reserve":vat_reserve,
                    "vat_pkp_type":vat_pkp_type,
                    "vat_pkp_no":vat_pkp_no,
                    "vat_pkp_date":vat_pkp_date,
                    "vat_tax_office_id":vat_tax_office_id}
    sort_fields={"sort_by":sort_by,"sort_of":sort_of}
    get_results,pages,err= VatCompanyService.get_vat_companies(page,limit,get_all_params,sort_fields)
    if get_results != [] and err == None:
        return pagination_response(200,"success",page,limit,pages["total_pages"],pages["total_rows"],get_results)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))

@router.get("/vat-company/{vat_id}", status_code=200)
def get_by_id(vat_id:int):
    result = VatCompanyService.get_vat_company(vat_id)
    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    return payload_response(ResponseException(200), "Success",result)

@router.post("/vat-company", status_code=201)
def post_data(req:VatSchema.VatCompanyRequest):
    created_data,err=VatCompanyService.post_vat_company(req)
    if err == None:
        return payload_response(201,"Success",created_data)
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=str(err))

@router.delete("/vat-company/{vat_id}", status_code=202)
def delete_vat_company(vat_id:int):
    delete_data,err = VatCompanyService.delete_vat_company(id)
    if err == None:
        return payload_response(204,"Success",delete_data)
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))

@router.put("/vat-company/{vat_id}", status_code=202)
def put_vat_company(vat_id:int,req:VatSchema.VatCompanyRequest):
    updated_data,err=VatCompanyService.put_vat_company(id,req)
    if err == None:
        return payload_response(202,"Success",updated_data)
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))
    

@router.patch("/vat-company/{vat_id}", status_code=202)
def patch_vat_company(vat_id:int):
    patched_data,err = VatCompanyService.patch_vat_company(vat_id)
    if err == None:
        return payload_response(202,"Success",patched_data)
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))
    
