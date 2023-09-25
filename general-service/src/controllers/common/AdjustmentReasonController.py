from fastapi import APIRouter, HTTPException, status, Query, Request
from src.services.common import AdjustmentReasonService
from src.payloads.schemas.common.AdjustmentReasonSchema import MtrAdjustmentReasonGetSchema
from src.payloads.responses.GeneralResponse import payload_response
from src.payloads.responses.PaginationResponse import pagination_response
from src.exceptions.RequestException import ResponseException

router = APIRouter(tags=["Adjustment Reason"],prefix="/api/general")

@router.get("/adjustment-reasons", status_code=200)
async def get_all_adjustment_reasons(page:int, limit:int, query_of:list[str]=Query(None), query_by:list[str]=Query(None)):
    get_results, pages, err = AdjustmentReasonService.get_all_adjustment_reasons(page,limit,query_of,query_by)
    if err == None:
        return pagination_response(200,"Success",page,limit,pages["total_pages"],pages["total_rows"],get_results)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))

@router.get("/adjustment-reason/{adjustment_reason_id}", status_code=200)
async def get_by_id_adjustment_reason(adjustment_reason_id:int):
    get_result, err = AdjustmentReasonService.get_by_id_adjustment_reason(adjustment_reason_id)
    if not get_result and err == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    return payload_response(200,"Success",get_result)

@router.post("/adjustment-reason",status_code=201)
async def post_adjustment_reason(req:MtrAdjustmentReasonGetSchema):
    created_data, err = AdjustmentReasonService.post_adjustment_reason(req)
    if err == None:
        return payload_response(201,"Created",created_data)
    else:
        raise HTTPException(status_code= status.HTTP_409_CONFLICT,detail=ResponseException(409))
    
@router.put("/adjustment-reason/{adjustment_reason_id}",status_code=201)
async def put_adjustment_reason(adjustment_reason_id:int,req:MtrAdjustmentReasonGetSchema):
    updated_data, err = AdjustmentReasonService.put_adjustment_reason(adjustment_reason_id,req)
    if err == None:
        return payload_response(201,"Updated",updated_data)
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))
    
@router.delete("/adjustment-reason/{adjustment_reason_id}",status_code=204)
async def delete_adjustment_reason(adjustment_reason_id:int):
    erase_data, err = AdjustmentReasonService.delete_adjustment_reason(adjustment_reason_id)
    if err == None:
        return payload_response(204,"Deleted",erase_data)
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))

@router.patch("/adjustment-reason/{adjustment_reason_id}",status_code=201)
async def patch_adjustment_reason(adjustment_reason_id:int):
    updated_data, err = AdjustmentReasonService.patch_adjustment_reason(adjustment_reason_id)
    if err == None:
        return payload_response(201,"Updated",updated_data)
    else:
        print(str(err))
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))
    



