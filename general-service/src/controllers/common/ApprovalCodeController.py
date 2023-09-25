from fastapi import APIRouter, HTTPException, status, Query, Request
from src.services.common import ApprovalCodeService
from src.payloads.schemas.common.ApprovalCodeSchema import MtrApprovalCodeGetSchema
from src.payloads.responses.GeneralResponse import payload_response
from src.payloads.responses.PaginationResponse import pagination_response
from src.exceptions.RequestException import ResponseException

router = APIRouter(tags=["Approval Code"],prefix="/api/general")

@router.get("/approval-codes", status_code=200)
async def get_all_approval_codes(page:int, limit:int, query_of:list[str]=Query(None), query_by:list[str]=Query(None)):
    get_results, pages, err = ApprovalCodeService.get_all_approval_codes(page,limit,query_of,query_by)
    if err == None:
        return pagination_response(200,"Success",page,limit,pages["total_pages"],pages["total_rows"],get_results)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))

@router.get("/approval-code/{approval_code_id}", status_code=200)
async def get_by_id_approval_code(approval_code_id:int):
    get_result, err = ApprovalCodeService.get_by_id_approval_code(approval_code_id)
    if not get_result and err == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    return payload_response(200,"Success",get_result)

@router.post("/approval-code",status_code=201)
async def post_approval_code(req:MtrApprovalCodeGetSchema):
    created_data, err = ApprovalCodeService.post_approval_code(req)
    if err == None:
        return payload_response(201,"Created",created_data)
    else:
        raise HTTPException(status_code= status.HTTP_409_CONFLICT,detail=ResponseException(409))
    
@router.put("/approval-code/{approval_code_id}",status_code=201)
async def put_approval_code(approval_code_id:int,req:MtrApprovalCodeGetSchema):
    updated_data, err = ApprovalCodeService.put_approval_code(approval_code_id,req)
    if err == None:
        return payload_response(201,"Updated",updated_data)
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))
    
@router.delete("/approval-code/{approval_code_id}",status_code=204)
async def delete_approval_code(approval_code_id:int):
    erase_data, err = ApprovalCodeService.delete_approval_code(approval_code_id)
    if err == None:
        return payload_response(204,"Deleted",erase_data)
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))

@router.patch("/approval-code/{approval_code_id}",status_code=201)
async def patch_approval_code(approval_code_id:int):
    updated_data, err = ApprovalCodeService.patch_approval_code(approval_code_id)
    if err == None:
        return payload_response(201,"Updated",updated_data)
    else:
        print(str(err))
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))
    



