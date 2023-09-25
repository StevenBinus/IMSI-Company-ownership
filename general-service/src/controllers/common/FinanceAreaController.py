from fastapi import APIRouter, HTTPException, status, Query, Request
from src.services.common import FinanceAreaService
from src.payloads.schemas.common.FinanceAreaSchema import MtrFinanceAreaGetSchema
from src.payloads.responses.GeneralResponse import payload_response
from src.payloads.responses.PaginationResponse import pagination_response
from src.exceptions.RequestException import ResponseException

router = APIRouter(tags=["Finance Area"],prefix="/api/general")

@router.get("/finance-area", status_code=200)
async def get_all_finance_areas(page:int, limit:int, query_of:list[str]=Query(None), query_by:list[str]=Query(None)):
    get_results, pages, err = FinanceAreaService.get_all_finance_areas(page,limit,query_of,query_by)
    if err == None:
        return pagination_response(200,"Success",page,limit,pages["total_pages"],pages["total_rows"],get_results)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))

@router.get("/finance-area/{finance_area_id}", status_code=200)
async def get_by_id_finance_area(finance_area_id:int):
    get_result, err = FinanceAreaService.get_by_id_finance_area(finance_area_id)
    if not get_result and err == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    return payload_response(200,"Success",get_result)

@router.post("/finance-area",status_code=201)
async def post_finance_area(req:MtrFinanceAreaGetSchema):
    created_data, err = FinanceAreaService.post_finance_area(req)
    if err == None:
        return payload_response(201,"Created",created_data)
    else:
        raise HTTPException(status_code= status.HTTP_409_CONFLICT,detail=ResponseException(409))
    
@router.put("/finance-area/{finance_area_id}",status_code=201)
async def put_finance_area(finance_area_id:int,req:MtrFinanceAreaGetSchema):
    updated_data, err = FinanceAreaService.put_finance_area(finance_area_id,req)
    if err == None:
        return payload_response(201,"Updated",updated_data)
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))
    
@router.delete("/finance-area/{finance_area_id}",status_code=204)
async def delete_finance_area(finance_area_id:int):
    erase_data, err = FinanceAreaService.delete_finance_area(finance_area_id)
    if err == None:
        return payload_response(204,"Deleted",erase_data)
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))

@router.patch("/finance-area/{finance_area_id}",status_code=201)
async def patch_finance_area(finance_area_id:int):
    updated_data, err = FinanceAreaService.patch_finance_area(finance_area_id)
    if err == None:
        return payload_response(201,"Updated",updated_data)
    else:
        print(str(err))
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))
    



