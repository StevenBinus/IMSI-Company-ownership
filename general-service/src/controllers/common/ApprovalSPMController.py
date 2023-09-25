from fastapi import APIRouter, HTTPException, status, Query, Request
from src.services.common import ApprovalSPMService
from src.payloads.schemas.common.ApprovalSPMSchema import MtrApprovalSPMGetSchema
from src.payloads.responses.GeneralResponse import payload_response
from src.payloads.responses.PaginationResponse import pagination_response
from src.exceptions.RequestException import ResponseException

router = APIRouter(tags=["Approval SPM"],prefix="/api/general")

@router.get("/approvals-spm", status_code=200)
async def get_all_approvals_spm(page:int, limit:int, query_of:list[str]=Query(None), query_by:list[str]=Query(None)):
    get_results, pages, err = ApprovalSPMService.get_all_approvals_spm(page,limit,query_of,query_by)
    if err == None:
        return pagination_response(200,"Success",page,limit,pages["total_pages"],pages["total_rows"],get_results)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))

@router.get("/approval-spm/{approval_spm_id}", status_code=200)
async def get_by_id_approval_spm(approval_spm_id:int):
    get_result, err = ApprovalSPMService.get_by_id_approval_spm(approval_spm_id)
    if not get_result and err == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    return payload_response(200,"Success",get_result)

@router.post("/approval-spm",status_code=201)
async def post_approval_spm(req:MtrApprovalSPMGetSchema):
    created_data, err = ApprovalSPMService.post_approval_spm(req)
    if err == None:
        return payload_response(201,"Created",created_data)
    else:
        raise HTTPException(status_code= status.HTTP_409_CONFLICT,detail=ResponseException(409))
    
@router.put("/approval-spm/{approval_spm_id}",status_code=201)
async def put_approval_spm(approval_spm_id:int,req:MtrApprovalSPMGetSchema):
    updated_data, err = ApprovalSPMService.put_approval_spm(approval_spm_id,req)
    if err == None:
        return payload_response(201,"Updated",updated_data)
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))
    
@router.delete("/approval-spm/{approval_spm_id}",status_code=204)
async def delete_approval_spm(approval_spm_id:int):
    erase_data, err = ApprovalSPMService.delete_approval_spm(approval_spm_id)
    if err == None:
        return payload_response(204,"Deleted",erase_data)
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))

@router.patch("/approval-spm/{approval_spm_id}",status_code=201)
async def patch_approval_spm(approval_spm_id:int):
    updated_data, err = ApprovalSPMService.patch_approval_spm(approval_spm_id)
    if err == None:
        return payload_response(201,"Updated",updated_data)
    else:
        print(str(err))
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))
    



