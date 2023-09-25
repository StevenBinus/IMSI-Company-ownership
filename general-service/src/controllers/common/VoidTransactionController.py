from fastapi import APIRouter,Depends,HTTPException,status,Query
from src.repositories.common import VoidTransactionRepo
from src.exceptions.RequestException import ResponseException
from src.payloads.schemas.common import VoidTransactionSchema
from src.services.common import VoidTransactionService
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from src.configs.database import get_db
from src.payloads.responses.GeneralResponse import payload_response
from src.payloads.responses.PaginationResponse import pagination_response

router = APIRouter(tags=["Void Transaction"],prefix="/api/general")

@router.get("/void-transactions", status_code=200)
def get_void_transactions(page:int, limit:int, query_of:list[str]=Query(None), query_by:list[str]=Query(None)):
    get_results, pages, err = VoidTransactionService.get_all_void_transactions(page,limit,query_of,query_by)
    if err == None:
        return pagination_response(200,"Success",page,limit,pages["total_pages"],pages["total_rows"],get_results)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    
@router.get("/void-transaction/{void_transaction_id}", status_code=200)
def get_void_transaction(void_transaction_id:int):
    get_result, err = VoidTransactionService.get_void_transaction(void_transaction_id)
    if not get_result and err == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    return payload_response(200,"Success",get_result)

@router.post("/void-transaction", status_code=201)
def post_void_transaction(req:VoidTransactionSchema.MtrVoidTransactionGetSchema):
    created_data, err = VoidTransactionService.post_void_transaction(req)
    if err == None:
        return payload_response(201,"Created",created_data)
    else:
        raise HTTPException(status_code= status.HTTP_409_CONFLICT,detail=ResponseException(409))

@router.delete("/void-transaction/{void_transaction_id}", status_code=204)
def delete_void_transaction(void_transaction_id:int):
    erase_data, err = VoidTransactionService.delete_void_transaction_type(void_transaction_id)
    if err == None:
        return payload_response(204,"Deleted",erase_data)
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))

@router.put("/void-transaction/{void_transaction_id}", status_code=201)
def put_void_transaction(void_transaction_id:int,req:VoidTransactionSchema.MtrVoidTransactionGetSchema):
    updated_data, err = VoidTransactionService.put_void_transaction(void_transaction_id,req)
    if err == None:
        return payload_response(201,"Updated",updated_data)
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))

@router.patch("/void-transaction/{void_transaction_id}", status_code=201)
def patch_void_transaction(void_transaction_id,db:Session=Depends(get_db)):
    updated_data, err = VoidTransactionService.patch_void_transaction(void_transaction_id)
    if err == None:
        return payload_response(201,"Updated",updated_data)
    else:
        print(str(err))
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))