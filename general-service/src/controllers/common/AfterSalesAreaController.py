from fastapi import APIRouter, HTTPException, status, Query, Request
from src.services.common import AfterSalesAreaService
from src.payloads.schemas.common.AfterSalesAreaSchema import MtrAfterSalesAreaGetSchema
from src.payloads.responses.GeneralResponse import payload_response
from src.payloads.responses.PaginationResponse import pagination_response
from src.exceptions.RequestException import ResponseException

router = APIRouter(tags=["After Sales Area"],prefix="/api/general")

@router.get("/after-sales-areas", status_code=200)
async def get_all_after_sales_areas(page:int, limit:int, query_of:list[str]=Query(None), query_by:list[str]=Query(None)):
    get_results, pages, err = AfterSalesAreaService.get_all_after_sales_areas(page,limit,query_of,query_by)
    if err == None:
        return pagination_response(200,"Success",page,limit,pages["total_pages"],pages["total_rows"],get_results)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))

@router.get("/after-sales-area/{after_sales_area_id}", status_code=200)
async def get_by_id_after_sales_area(after_sales_area_id:int):
    get_result, err = AfterSalesAreaService.get_by_id_after_sales_area(after_sales_area_id)
    if not get_result and err == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    return payload_response(200,"Success",get_result)

@router.post("/after-sales-area",status_code=201)
async def post_after_sales_area(req:MtrAfterSalesAreaGetSchema):
    created_data, err = AfterSalesAreaService.post_after_sales_area(req)
    if err == None:
        return payload_response(201,"Created",created_data)
    else:
        raise HTTPException(status_code= status.HTTP_409_CONFLICT,detail=ResponseException(409))
    
@router.put("/after-sales-area/{after_sales_area_id}",status_code=201)
async def put_after_sales_area(after_sales_area_id:int,req:MtrAfterSalesAreaGetSchema):
    updated_data, err = AfterSalesAreaService.put_after_sales_area(after_sales_area_id,req)
    if err == None:
        return payload_response(201,"Updated",updated_data)
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))
    
@router.delete("/after-sales-area/{after_sales_area_id}",status_code=204)
async def delete_after_sales_area(after_sales_area_id:int):
    erase_data, err = AfterSalesAreaService.delete_after_sales_area(after_sales_area_id)
    if err == None:
        return payload_response(204,"Deleted",erase_data)
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))

@router.patch("/after-sales-area/{after_sales_area_id}",status_code=201)
async def patch_after_sales_area(after_sales_area_id:int):
    updated_data, err = AfterSalesAreaService.patch_after_sales_area(after_sales_area_id)
    if err == None:
        return payload_response(201,"Updated",updated_data)
    else:
        print(str(err))
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))
    



