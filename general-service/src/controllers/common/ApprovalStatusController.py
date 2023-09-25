from fastapi import APIRouter, HTTPException, status, Query, Request
from src.services.common import ApprovalStatusService
from src.payloads.schemas.common.ApprovalStatusSchema import MtrApprovalStatusGetSchema
from src.payloads.responses.GeneralResponse import payload_response
from src.payloads.responses.PaginationResponse import pagination_response
from src.exceptions.RequestException import ResponseException

router = APIRouter(tags=["Approval Status"],prefix="/api/general")

@router.get("/approvals-status", status_code=200)
async def get_all_approvals_status(page:int, limit:int, query_of:list[str]=Query(None), query_by:list[str]=Query(None)):
    get_results, pages, err = ApprovalStatusService.get_all_approvals_status(page,limit,query_of,query_by)
    if err == None:
        return pagination_response(200,"Success",page,limit,pages["total_pages"],pages["total_rows"],get_results)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))

@router.get("/approval-status/{approval_status_id}", status_code=200)
async def get_by_id_approval_status(approval_status_id:int):
    get_result, err = ApprovalStatusService.get_by_id_approval_status(approval_status_id)
    if not get_result and err == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    return payload_response(200,"Success",get_result)

@router.post("/approval-status",status_code=201)
async def post_approval_status(req:MtrApprovalStatusGetSchema):
    created_data, err = ApprovalStatusService.post_approval_status(req)
    if err == None:
        return payload_response(201,"Created",created_data)
    else:
        raise HTTPException(status_code= status.HTTP_409_CONFLICT,detail=ResponseException(409))
    
@router.put("/approval-status/{approval_status_id}",status_code=201)
async def put_approval_status(approval_status_id:int,req:MtrApprovalStatusGetSchema):
    updated_data, err = ApprovalStatusService.put_approval_status(approval_status_id,req)
    if err == None:
        return payload_response(201,"Updated",updated_data)
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))
    
@router.delete("/approval-status/{approval_status_id}",status_code=204)
async def delete_approval_status(approval_status_id:int):
    erase_data, err = ApprovalStatusService.delete_approval_status(approval_status_id)
    if err == None:
        return payload_response(204,"Deleted",erase_data)
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))

@router.patch("/approval-status/{approval_status_id}",status_code=201)
async def patch_approval_status(approval_status_id:int):
    updated_data, err = ApprovalStatusService.patch_approval_status(approval_status_id)
    if err == None:
        return payload_response(201,"Updated",updated_data)
    else:
        print(str(err))
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))
    



