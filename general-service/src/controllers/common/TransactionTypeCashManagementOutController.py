from fastapi import APIRouter, HTTPException, status, Query, Request
from src.services.common import TransactionTypeCashManagementOutService
from src.payloads.schemas.common.TransactionTypeCashManagementOutSchema import MtrTransactionTypeCashManagementOutGetSchema
from src.payloads.responses.GeneralResponse import payload_response
from src.payloads.responses.PaginationResponse import pagination_response
from src.exceptions.RequestException import ResponseException
from src.payloads.responses.GeneralResponse import payload_response

router = APIRouter(tags=["Transaction Type Cash Management Out"],prefix="/api/general")

@router.get("/transaction-type-cash-management-outs", status_code=200)
async def get_all_transaction_type_cash_management_outs(page:int, limit:int, query_of:list[str]=Query(None), query_by:list[str]=Query(None)):
    get_results, pages, err = TransactionTypeCashManagementOutService.get_all_transaction_type_cash_management_outs(page,limit,query_of,query_by)
    if err == None:
        return pagination_response(200,"Success",page,limit,pages["total_pages"],pages["total_rows"],get_results)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))

@router.get("/transaction-type-cash-management-out/{transaction_type_cash_management_out_id}", status_code=200)
async def get_by_id_transaction_type_cash_management_out(transaction_type_cash_management_out_id:int):
    get_result, err = TransactionTypeCashManagementOutService.get_by_id_transaction_type_cash_management_out(transaction_type_cash_management_out_id)
    if not get_result and err == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    return payload_response(200,"Success",get_result)

@router.post("/transaction-type-cash-management-out",status_code=201)
async def post_transaction_type_cash_management_out(req:MtrTransactionTypeCashManagementOutGetSchema):
    created_data, err = TransactionTypeCashManagementOutService.post_transaction_type_cash_management_out(req)
    if err == None:
        return payload_response(201,"Created",created_data)
    else:
        raise HTTPException(status_code= status.HTTP_409_CONFLICT,detail=ResponseException(409))
    
@router.put("/transaction-type-cash-management-out/{transaction_type_cash_management_out_id}",status_code=201)
async def put_transaction_type_cash_management_out(transaction_type_cash_management_out_id:int,req:MtrTransactionTypeCashManagementOutGetSchema):
    updated_data, err = TransactionTypeCashManagementOutService.put_transaction_type_cash_management_out(transaction_type_cash_management_out_id,req)
    if err == None:
        return payload_response(201,"Updated",updated_data)
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))
    
@router.delete("/transaction-type-cash-management-out/{transaction_type_cash_management_out_id}",status_code=204)
async def delete_transaction_type_cash_management_out(transaction_type_cash_management_out_id:int):
    erase_data, err = TransactionTypeCashManagementOutService.delete_transaction_type_cash_management_out(transaction_type_cash_management_out_id)
    if err == None:
        return payload_response(204,"Deleted",erase_data)
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))

@router.patch("/transaction-type-cash-management-out/{transaction_type_cash_management_out_id}",status_code=201)
async def patch_transaction_type_cash_management_out(transaction_type_cash_management_out_id:int):
    updated_data, err = TransactionTypeCashManagementOutService.patch_transaction_type_cash_management_out(transaction_type_cash_management_out_id)
    if err == None:
        return payload_response(201,"Updated",updated_data)
    else:
        print(str(err))
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))