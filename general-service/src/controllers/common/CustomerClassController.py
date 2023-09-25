from fastapi import APIRouter, HTTPException, status, Query, Request
from src.services.common import CustomerClassService
from src.payloads.schemas.common.CustomerClassSchema import MtrCustomerClassGetSchema
from src.payloads.responses.GeneralResponse import payload_response
from src.payloads.responses.PaginationResponse import pagination_response
from src.exceptions.RequestException import ResponseException

router = APIRouter(tags=["Customer Class"],prefix="/api/general")

@router.get("/customers-class", status_code=200)
async def get_all_customers_class(page:int, limit:int, query_of:list[str]=Query(None), query_by:list[str]=Query(None)):
    get_results, pages, err = CustomerClassService.get_all_customers_class(page,limit,query_of,query_by)
    if err == None:
        return pagination_response(200,"Success",page,limit,pages["total_pages"],pages["total_rows"],get_results)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))

@router.get("/customer-class/{customer_class_id}", status_code=200)
async def get_by_id_customer_class(customer_class_id:int):
    get_result, err = CustomerClassService.get_by_id_customer_class(customer_class_id)
    if not get_result and err == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    return payload_response(200,"Success",get_result)

@router.post("/customer-class",status_code=201)
async def post_customer_class(req:MtrCustomerClassGetSchema):
    created_data, err = CustomerClassService.post_customer_class(req)
    if err == None:
        return payload_response(201,"Created",created_data)
    else:
        raise HTTPException(status_code= status.HTTP_409_CONFLICT,detail=ResponseException(409))
    
@router.put("/customer-class/{customer_class_id}",status_code=201)
async def put_customer_class(customer_class_id:int,req:MtrCustomerClassGetSchema):
    updated_data, err = CustomerClassService.put_customer_class(customer_class_id,req)
    if err == None:
        return payload_response(201,"Updated",updated_data)
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))
    
@router.delete("/customer-class/{customer_class_id}",status_code=204)
async def delete_customer_class(customer_class_id:int):
    erase_data, err = CustomerClassService.delete_customer_class(customer_class_id)
    if err == None:
        return payload_response(204,"Deleted",erase_data)
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))

@router.patch("/customer-class/{customer_class_id}",status_code=201)
async def patch_customer_class(customer_class_id:int):
    updated_data, err = CustomerClassService.patch_customer_class(customer_class_id)
    if err == None:
        return payload_response(201,"Updated",updated_data)
    else:
        print(str(err))
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))
    



