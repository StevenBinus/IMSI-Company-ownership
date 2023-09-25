from fastapi import APIRouter, HTTPException, status, Query, Request
from src.services.common import CustomerTypeFlagListService
from src.payloads.schemas.common.CustomerTypeFlagListSchema import MtrCustomerTypeFlagListGetSchema
from src.payloads.responses.GeneralResponse import payload_response
from src.payloads.responses.PaginationResponse import pagination_response
from src.exceptions.RequestException import ResponseException

router = APIRouter(tags=["Customer Type Flag List"],prefix="/api/general")

@router.get("/customer-type-flag-list", status_code=200)
async def get_all_customer_type_flag_lists(page:int, limit:int, query_of:list[str]=Query(None), query_by:list[str]=Query(None)):
    get_results, pages, err = CustomerTypeFlagListService.get_all_customer_type_flag_lists(page,limit,query_of,query_by)
    if err == None:
        return pagination_response(200,"Success",page,limit,pages["total_pages"],pages["total_rows"],get_results)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))

@router.get("/customer-type-flag-list/{customer_type_flag_list_id}", status_code=200)
async def get_by_id_customer_type_flag_list(customer_type_flag_list_id:int):
    get_result, err = CustomerTypeFlagListService.get_by_id_customer_type_flag_list(customer_type_flag_list_id)
    if not get_result and err == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    return payload_response(200,"Success",get_result)

@router.post("/customer-type-flag-list",status_code=201)
async def post_customer_type_flag_list(req:MtrCustomerTypeFlagListGetSchema):
    created_data, err = CustomerTypeFlagListService.post_customer_type_flag_list(req)
    if err == None:
        return payload_response(201,"Created",created_data)
    else:
        raise HTTPException(status_code= status.HTTP_409_CONFLICT,detail=ResponseException(409))
    
@router.put("/customer-type-flag-list/{customer_type_flag_list_id}",status_code=201)
async def put_customer_type_flag_list(customer_type_flag_list_id:int,req:MtrCustomerTypeFlagListGetSchema):
    updated_data, err = CustomerTypeFlagListService.put_customer_type_flag_list(customer_type_flag_list_id,req)
    if err == None:
        return payload_response(201,"Updated",updated_data)
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))
    
@router.delete("/customer-type-flag-list/{customer_type_flag_list_id}",status_code=204)
async def delete_customer_type_flag_list(customer_type_flag_list_id:int):
    erase_data, err = CustomerTypeFlagListService.delete_customer_type_flag_list(customer_type_flag_list_id)
    if err == None:
        return payload_response(204,"Deleted",erase_data)
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))

@router.patch("/customer-type-flag-list/{customer_type_flag_list_id}",status_code=201)
async def patch_customer_type_flag_list(customer_type_flag_list_id:int):
    updated_data, err = CustomerTypeFlagListService.patch_customer_type_flag_list(customer_type_flag_list_id)
    if err == None:
        return payload_response(201,"Updated",updated_data)
    else:
        print(str(err))
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))
    



