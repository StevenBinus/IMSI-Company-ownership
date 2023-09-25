from fastapi import APIRouter, HTTPException, status, Query, Request
from src.services.common import RequestForPaymentReferenceTypeService
from src.payloads.schemas.common.RequestForPaymentReferenceTypeSchema import MtrRequestForPaymentReferenceTypeGetSchema
from src.payloads.responses.GeneralResponse import payload_response
from src.payloads.responses.PaginationResponse import pagination_response
from src.exceptions.RequestException import ResponseException

router = APIRouter(tags=["Request For Payment Reference Type"],prefix="/api/general")

@router.get("/request-for-payment-reference-types", status_code=200)
async def get_all_request_for_payment_reference_types(page:int, limit:int, query_of:list[str]=Query(None), query_by:list[str]=Query(None)):
    get_results, pages, err = RequestForPaymentReferenceTypeService.get_all_request_for_payment_reference_types(page,limit,query_of,query_by)
    if err == None:
        return pagination_response(200,"Success",page,limit,pages["total_pages"],pages["total_rows"],get_results)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))

@router.get("/request-for-payment-reference-type/{request_for_payment_reference_type_id}", status_code=200)
async def get_by_id_request_for_payment_reference_type(request_for_payment_reference_type_id:int):
    get_result, err = RequestForPaymentReferenceTypeService.get_by_id_request_for_payment_reference_type(request_for_payment_reference_type_id)
    if not get_result and err == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    return payload_response(200,"Success",get_result)

@router.post("/request-for-payment-reference-type",status_code=201)
async def post_request_for_payment_reference_type(req:MtrRequestForPaymentReferenceTypeGetSchema):
    created_data, err = RequestForPaymentReferenceTypeService.post_request_for_payment_reference_type(req)
    if err == None:
        return payload_response(201,"Created",created_data)
    else:
        raise HTTPException(status_code= status.HTTP_409_CONFLICT,detail=ResponseException(409))
    
@router.put("/request-for-payment-reference-type/{request_for_payment_reference_type_id}",status_code=201)
async def put_request_for_payment_reference_type(request_for_payment_reference_type_id:int,req:MtrRequestForPaymentReferenceTypeGetSchema):
    updated_data, err = RequestForPaymentReferenceTypeService.put_request_for_payment_reference_type(request_for_payment_reference_type_id,req)
    if err == None:
        return payload_response(201,"Updated",updated_data)
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))
    
@router.delete("/request-for-payment-reference-type/{request_for_payment_reference_type_id}",status_code=204)
async def delete_request_for_payment_reference_type(request_for_payment_reference_type_id:int):
    erase_data, err = RequestForPaymentReferenceTypeService.delete_request_for_payment_reference_type(request_for_payment_reference_type_id)
    if err == None:
        return payload_response(204,"Deleted",erase_data)
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))

@router.patch("/request-for-payment-reference-type/{request_for_payment_reference_type_id}",status_code=201)
async def patch_request_for_payment_reference_type(request_for_payment_reference_type_id:int):
    updated_data, err = RequestForPaymentReferenceTypeService.patch_request_for_payment_reference_type(request_for_payment_reference_type_id)
    if err == None:
        return payload_response(201,"Updated",updated_data)
    else:
        print(str(err))
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))