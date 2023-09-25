from fastapi import APIRouter, HTTPException, status, Query, Request
from src.services.master import CostProfitMapService
from src.payloads.schemas.master.CostProfitMapSchema import MtrCostProfitMapSchema, mtrCostProfitMapUpdateSchema
from src.payloads.responses.GeneralResponse import payload_response
from src.payloads.responses.PaginationResponse import pagination_response
from src.exceptions.RequestException import ResponseException

router = APIRouter(tags=["cost profit map"],prefix="/api/general")

@router.get("/get-all-cost-profit-maps", status_code=200)
async def get_all_cost_profit_maps(page:int, limit:int, 
                                   company_id:int|None=None, 
                                   company_name:str|None=None, 
                                   profit_center_id:int|None=None, 
                                   cost_center_id:int|None=None, 
                                   mapping_description:str|None=None,
                                   sort_by:str|None=None,
                                   sort_of:str|None=None):
    get_all_params = {
        "company_id": company_id,
        "company_name": company_name,
        "profit_center_id": profit_center_id,
        "cost_center_id": cost_center_id,
        "mapping_description": mapping_description
    }
    sort_fields = {
        "sort_by": sort_by,
        "sort_of": sort_of
    }

    get_results, pages, err = CostProfitMapService.get_all_cost_profit_maps(page,limit,get_all_params,sort_fields)
    if err == None:
        return pagination_response(200,"Success",page,limit,pages["total_pages"],pages["total_rows"],get_results)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))

@router.get("/get-cost-profit-map-by-id/{id}", status_code=200)
async def get_by_id_cost_profit_map(id:int):
    get_result, err = CostProfitMapService.get_by_id_cost_profit_map(id)
    if not get_result and err == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    return payload_response(200,"Success",get_result)

@router.post("/post-cost-profit-map",status_code=status.HTTP_201_CREATED)
async def post_cost_profit_map(req:MtrCostProfitMapSchema):
    created_data, err = CostProfitMapService.post_cost_profit_map(req)
    if err == None:
        return payload_response(201,"Created",created_data)
    else:
        raise HTTPException(status_code= status.HTTP_409_CONFLICT,detail=ResponseException(409))
    
@router.put("/put-cost-profit-map/{id}",status_code=201)
async def put_cost_profit_map(id:int,req:mtrCostProfitMapUpdateSchema):
    updated_data, err = CostProfitMapService.put_cost_profit_map(id,req)
    if err == None:
        return payload_response(201,"Updated",updated_data)
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))
    
@router.patch("/patch-cost-profit-map/{id}",status_code=201)
async def patch_customer(id:int):
    updated_data, err = CostProfitMapService.patch_cost_profit_map(id)
    if err == None:
        return payload_response(201,"Updated",updated_data)
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))