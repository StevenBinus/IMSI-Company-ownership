from fastapi import APIRouter, HTTPException, status, Query, Request
from src.services.common import ShippingMethodService
from src.payloads.schemas.common.ShippingMethodSchema import MtrShippingMethodGetSchema
from src.payloads.responses.GeneralResponse import payload_response
from src.payloads.responses.PaginationResponse import pagination_response
from src.exceptions.RequestException import ResponseException

router = APIRouter(tags=["Shipping Method"],prefix="/api/general")

@router.get("/shipping-methods", status_code=200)
async def get_all_shipping_methods(page:int, limit:int, query_of:list[str]=Query(None), query_by:list[str]=Query(None)):
    get_results, pages, err = ShippingMethodService.get_all_shipping_methods(page,limit,query_of,query_by)
    if err == None:
        return pagination_response(200,"Success",page,limit,pages["total_pages"],pages["total_rows"],get_results)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))

@router.get("/shipping-method/{shipping_method_id}", status_code=200)
async def get_by_id_shipping_method(shipping_method_id:int):
    get_result, err = ShippingMethodService.get_by_id_shipping_method(shipping_method_id)
    if not get_result and err == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    return payload_response(200,"Success",get_result)

@router.post("/shipping-method",status_code=201)
async def post_shipping_method(req:MtrShippingMethodGetSchema):
    created_data, err = ShippingMethodService.post_shipping_method(req)
    if err == None:
        return payload_response(201,"Created",created_data)
    else:
        raise HTTPException(status_code= status.HTTP_409_CONFLICT,detail=ResponseException(409))
    
@router.put("/shipping-method/{shipping_method_id}",status_code=201)
async def put_shipping_method(shipping_method_id:int,req:MtrShippingMethodGetSchema):
    updated_data, err = ShippingMethodService.put_shipping_method(shipping_method_id,req)
    if err == None:
        return payload_response(201,"Updated",updated_data)
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))
    
@router.delete("/shipping-method/{shipping_method_id}",status_code=204)
async def delete_shipping_method(shipping_method_id:int):
    erase_data, err = ShippingMethodService.delete_shipping_method(shipping_method_id)
    if err == None:
        return payload_response(204,"Deleted",erase_data)
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))

@router.patch("/shipping-method/{shipping_method_id}",status_code=201)
async def patch_shipping_method(shipping_method_id:int):
    updated_data, err = ShippingMethodService.patch_shipping_method(shipping_method_id)
    if err == None:
        return payload_response(201,"Updated",updated_data)
    else:
        print(str(err))
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))