from fastapi import APIRouter, HTTPException, status, Query, Request
from src.services.common import GeneralLedgerAccountTypeService
from src.payloads.schemas.common.GeneralLedgerAccountTypeSchema import MtrGeneralLedgerAccountTypeGetSchema
from src.payloads.responses.GeneralResponse import payload_response
from src.payloads.responses.PaginationResponse import pagination_response
from src.exceptions.RequestException import ResponseException

router = APIRouter(tags=["General Ledger Account Type"],prefix="/api/general")

@router.get("/general-ledger-account-types", status_code=200)
async def get_all_general_ledger_account_types(page:int, limit:int, query_of:list[str]=Query(None), query_by:list[str]=Query(None)):
    get_results, pages, err = GeneralLedgerAccountTypeService.get_all_general_ledger_account_types(page,limit,query_of,query_by)
    if err == None:
        return pagination_response(200,"Success",page,limit,pages["total_pages"],pages["total_rows"],get_results)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))

@router.get("/general-ledger-account-type/{general_ledger_account_type_id}", status_code=200)
async def get_by_id_general_ledger_account_type(general_ledger_account_type_id:int):
    get_result, err = GeneralLedgerAccountTypeService.get_by_id_general_ledger_account_type(general_ledger_account_type_id)
    if not get_result and err == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    return payload_response(200,"Success",get_result)

@router.post("/general-ledger-account-type",status_code=201)
async def post_general_ledger_account_type(req:MtrGeneralLedgerAccountTypeGetSchema):
    created_data, err = GeneralLedgerAccountTypeService.post_general_ledger_account_type(req)
    if err == None:
        return payload_response(201,"Created",created_data)
    else:
        raise HTTPException(status_code= status.HTTP_409_CONFLICT,detail=ResponseException(409))
    
@router.put("/general-ledger-account-type/{general_ledger_account_type_id}",status_code=201)
async def put_general_ledger_account_type(general_ledger_account_type_id:int,req:MtrGeneralLedgerAccountTypeGetSchema):
    updated_data, err = GeneralLedgerAccountTypeService.put_general_ledger_account_type(general_ledger_account_type_id,req)
    if err == None:
        return payload_response(201,"Updated",updated_data)
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))
    
@router.delete("/general-ledger-account-type/{general_ledger_account_type_id}",status_code=204)
async def delete_general_ledger_account_type(general_ledger_account_type_id:int):
    erase_data, err = GeneralLedgerAccountTypeService.delete_general_ledger_account_type(general_ledger_account_type_id)
    if err == None:
        return payload_response(204,"Deleted",erase_data)
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))

@router.patch("/general-ledger-account-type/{general_ledger_account_type_id}",status_code=201)
async def patch_general_ledger_account_type(general_ledger_account_type_id:int):
    updated_data, err = GeneralLedgerAccountTypeService.patch_general_ledger_account_type(general_ledger_account_type_id)
    if err == None:
        return payload_response(201,"Updated",updated_data)
    else:
        print(str(err))
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))
    



