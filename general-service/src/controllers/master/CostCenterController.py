
from src.payloads.schemas.master import CostCenterSchema
from fastapi import APIRouter, HTTPException, status, Query, Request
from src.services.master import CostCenterService
from src.payloads.responses.GeneralResponse import payload_response
from src.payloads.responses.PaginationResponse import pagination_response
from src.exceptions.RequestException import ResponseException



router = APIRouter(tags=["Master Cost Center"],prefix="/api/general")

@router.get("/get-master-cost-centers", status_code=200)
def get_master_cost_centers(page:int,limit:int,cost_center_code:str|None=None,cost_center_name:str|None=None,status_active:bool|None=None,sort_by:str|None=None,sort_of:str|None=None):
    get_all_params={"cost_center_code":cost_center_code,"Cost_center_name":cost_center_name,"is_active":status_active}
    sort_fields={"sort_by":sort_by,"sort_of":sort_of}
    get_results,pages,err = CostCenterService.get_cost_center_all(page,limit,get_all_params,sort_fields)
    if get_results !=[] and err == None:
        return pagination_response(200,'Success', page, limit,pages["total_pages"],pages["total_rows"],get_results)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=str(err))
    

@router.get("/get-master-cost-center/{cost_center_id}", status_code=status.HTTP_200_OK)
def get_master_cost_center(cost_center_id:int):
    master_cost_center,err = CostCenterService.get_cost_center_by_id(cost_center_id)
    if err == None:
        return payload_response(200,"Success",master_cost_center)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))

@router.post("/create-master-cost-center", status_code=201)
def post_master_cost_center(req:CostCenterSchema.MtrCostCenterPost):
    post_cost_center,err=CostCenterService.post_cost_center(req)
    if err == None:
        return payload_response(201,"Success",post_cost_center)
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))

@router.put("/update-master-cost-center/{cost_center_id}",status_code=202)
def update_cost_center(cost_center_id: int,req:CostCenterSchema.MtrCostCenterPost):
    update_data, err = CostCenterService.put_cost_center(cost_center_id,req)
    if err == None:
        return payload_response(202,"Success",update_cost_center)
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))

@router.delete("/delete-master-cost-center/{cost_center_id}", status_code=202)
def delete_master_cost_center(cost_center_id:int):
    erase_master_cost_center,err = CostCenterService.delete_cost_center(cost_center_id)
    if err == None:
        return payload_response(204,"Success",erase_master_cost_center)
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=str(err))
    
@router.patch("/patch-master-cost-center/{cost_center_id}",status_code=202)
def patch_master_cost_center(cost_center_id:int):
    patch_master_cost_center,err=CostCenterService.patch_cost_center(cost_center_id)
    if err == None:
        return payload_response(202,"Success",patch_master_cost_center)
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))