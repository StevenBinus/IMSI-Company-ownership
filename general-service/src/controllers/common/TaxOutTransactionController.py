from fastapi import APIRouter, HTTPException, status, Query, Request
from src.services.common import TaxOutTransactionService
from src.payloads.schemas.common.TaxOutTransactionSchema import MtrTaxOutTransactionGetSchema
from src.payloads.responses.GeneralResponse import payload_response
from src.payloads.responses.PaginationResponse import pagination_response
from src.exceptions.RequestException import ResponseException

router = APIRouter(tags=["Tax Out Transaction SPM"],prefix="/api/general")

@router.get("/tax-out-transaction-types", status_code=200)
async def get_all_tax_out_transaction_types(page:int, limit:int, query_of:list[str]=Query(None), query_by:list[str]=Query(None)):
    get_results, pages, err = TaxOutTransactionService.get_all_tax_out_transaction_types(page,limit,query_of,query_by)
    if err == None:
        return pagination_response(200,"Success",page,limit,pages["total_pages"],pages["total_rows"],get_results)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))

@router.get("/tax-out-transaction-type/{tax_out_transaction_type_id}", status_code=200)
async def get_by_id_tax_out_transaction_type(tax_out_transaction_type_id:int):
    get_result, err = TaxOutTransactionService.get_by_id_tax_out_transaction_type(tax_out_transaction_type_id)
    if not get_result and err == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    return payload_response(200,"Success",get_result)

@router.post("/tax-out-transaction-type",status_code=201)
async def post_tax_out_transaction_type(req:MtrTaxOutTransactionGetSchema):
    created_data, err = TaxOutTransactionService.post_tax_out_transaction_type(req)
    if err == None:
        return payload_response(201,"Created",created_data)
    else:
        raise HTTPException(status_code= status.HTTP_409_CONFLICT,detail=ResponseException(409))
    
@router.put("/tax-out-transaction-type/{tax_out_transaction_type_id}",status_code=201)
async def put_tax_out_transaction_type(tax_out_transaction_type_id:int,req:MtrTaxOutTransactionGetSchema):
    updated_data, err = TaxOutTransactionService.put_tax_out_transaction_type(tax_out_transaction_type_id,req)
    if err == None:
        return payload_response(201,"Updated",updated_data)
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))
    
@router.delete("/tax-out-transaction-type/{tax_out_transaction_type_id}",status_code=204)
async def delete_tax_out_transaction_type(tax_out_transaction_type_id:int):
    erase_data, err = TaxOutTransactionService.delete_tax_out_transaction_type(tax_out_transaction_type_id)
    if err == None:
        return payload_response(204,"Deleted",erase_data)
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))

@router.patch("/tax-out-transaction-type/{tax_out_transaction_type_id}",status_code=201)
async def patch_tax_out_transaction_type(tax_out_transaction_type_id:int):
    updated_data, err = TaxOutTransactionService.patch_tax_out_transaction_type(tax_out_transaction_type_id)
    if err == None:
        return payload_response(201,"Updated",updated_data)
    else:
        print(str(err))
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))