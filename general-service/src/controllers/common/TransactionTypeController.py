from fastapi import APIRouter, HTTPException, status, Query, Request
from src.services.common import TransactionTypeService
from src.payloads.responses.GeneralResponse import payload_response
from src.payloads.responses.PaginationResponse import pagination_response
from src.exceptions.RequestException import ResponseException
from src.payloads.schemas.common.TransactionTypeSchema import MtrTransactionTypeGetSchema


router = APIRouter(tags=["Transaction Type"],prefix="/api/general")


@router.get("/transaction-types", status_code=200)
async def get_all_transaction_types(page:int, limit:int, query_of:list[str]=Query(None), query_by:list[str]=Query(None)):
    get_results, pages, err = TransactionTypeService.get_all_transaction_types(page,limit,query_of,query_by)
    if err == None:
        return pagination_response(200,"Success",page,limit,pages["total_pages"],pages["total_rows"],get_results)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))

@router.get("/transaction-type/{transaction_type_id}", status_code=200)
async def get_by_id_transaction_type(transaction_type_id:int):
    get_result, err = TransactionTypeService.get_by_id_transaction_type(transaction_type_id)
    if not get_result and err == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    return payload_response(200,"Success",get_result)

@router.post("/transaction-type",status_code=201)
async def post_transaction_type(req:MtrTransactionTypeGetSchema):
    created_data, err = TransactionTypeService.post_transaction_type(req)
    if err == None:
        return payload_response(201,"Created",created_data)
    else:
        raise HTTPException(status_code= status.HTTP_409_CONFLICT,detail=ResponseException(409))
    
@router.put("/transaction-type/{transaction_type_id}",status_code=201)
async def put_transaction_type(transaction_type_id:int,req:MtrTransactionTypeGetSchema):
    updated_data, err = TransactionTypeService.put_transaction_type(transaction_type_id,req)
    if err == None:
        return payload_response(201,"Updated",updated_data)
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))
    
@router.delete("/transaction-type/{transaction_type_id}",status_code=204)
async def delete_transaction_type(transaction_type_id:int):
    erase_data, err = TransactionTypeService.delete_transaction_type(transaction_type_id)
    if err == None:
        return payload_response(204,"Deleted",erase_data)
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))

@router.patch("/transaction-type/{transaction_type_id}",status_code=201)
async def patch_transaction_type(transaction_type_id:int):
    updated_data, err = TransactionTypeService.patch_transaction_type(transaction_type_id)
    if err == None:
        return payload_response(201,"Updated",updated_data)
    else:
        print(str(err))
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))
    


