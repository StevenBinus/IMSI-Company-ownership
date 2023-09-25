from fastapi import APIRouter, HTTPException, status, Query, Request
from src.services.common import BankTypeService
from src.payloads.schemas.common.BankTypeSchema import MtrBankTypeGetSchema
from src.payloads.responses.GeneralResponse import payload_response
from src.payloads.responses.PaginationResponse import pagination_response
from src.exceptions.RequestException import ResponseException

router = APIRouter(tags=["Bank Type"],prefix="/api/general")

@router.get("/bank-types", status_code=200)
async def get_all_bank_types(page:int, limit:int, query_of:list[str]=Query(None), query_by:list[str]=Query(None)):
    get_results, pages, err = BankTypeService.get_all_bank_types(page,limit,query_of,query_by)
    if err == None:
        return pagination_response(200,"Success",page,limit,pages["total_pages"],pages["total_rows"],get_results)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))

@router.get("/bank-type/{bank_type_id}", status_code=200)
async def get_by_id_bank_type(bank_type_id:int):
    get_result, err = BankTypeService.get_by_id_bank_type(bank_type_id)
    if not get_result and err == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    return payload_response(200,"Success",get_result)

@router.post("/bank-type",status_code=201)
async def post_bank_type(req:MtrBankTypeGetSchema):
    created_data, err = BankTypeService.post_bank_type(req)
    if err == None:
        return payload_response(201,"Created",created_data)
    else:
        raise HTTPException(status_code= status.HTTP_409_CONFLICT,detail=ResponseException(409))
    
@router.put("/bank-type/{bank_type_id}",status_code=201)
async def put_bank_type(bank_type_id:int,req:MtrBankTypeGetSchema):
    updated_data, err = BankTypeService.put_bank_type(bank_type_id,req)
    if err == None:
        return payload_response(201,"Updated",updated_data)
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))
    
@router.delete("/bank-type/{bank_type_id}",status_code=204)
async def delete_bank_type(bank_type_id:int):
    erase_data, err = BankTypeService.delete_bank_type(bank_type_id)
    if err == None:
        return payload_response(204,"Deleted",erase_data)
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))

@router.patch("/bank-type/{bank_type_id}",status_code=201)
async def patch_bank_type(bank_type_id:int):
    updated_data, err = BankTypeService.patch_bank_type(bank_type_id)
    if err == None:
        return payload_response(201,"Updated",updated_data)
    else:
        print(str(err))
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))
    



