from fastapi import APIRouter, HTTPException, status, Query, Request
from src.services.common import TransferStatusService
from src.payloads.responses.GeneralResponse import payload_response
from src.payloads.responses.PaginationResponse import pagination_response
from src.exceptions.RequestException import ResponseException
from src.payloads.schemas.common import TransferStatusSchema


router = APIRouter(tags=["Transfer Status"],prefix="/api/general")

@router.get("/transfer-statuses", status_code=200)
async def get_all_transfer_statuses(page:int, limit:int, query_of:list[str]=Query(None), query_by:list[str]=Query(None)):
    get_results, pages, err = TransferStatusService.get_all_transfer_statuses(page,limit,query_of,query_by)
    if err == None:
        return pagination_response(200,"Success",page,limit,pages["total_pages"],pages["total_rows"],get_results)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))

@router.get("/transfer-status/{transfer_status_id}", status_code=200)
async def get_by_id_transfer_status(transfer_status_id:int):
    get_result, err = TransferStatusService.get_by_id_transfer_status(transfer_status_id)
    if not get_result and err == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    return payload_response(200,"Success",get_result)

@router.post("/transfer-status",status_code=201)
async def post_transfer_status(req:TransferStatusSchema.MtrTransferStatusGetSchema):
    created_data, err = TransferStatusService.post_transfer_status(req)
    if err == None:
        return payload_response(201,"Created",created_data)
    else:
        raise HTTPException(status_code= status.HTTP_409_CONFLICT,detail=ResponseException(409))
    
@router.put("/transfer-status/{transfer_status_id}",status_code=201)
async def put_transfer_status(transfer_status_id:int,req:TransferStatusSchema.MtrTransferStatusGetSchema):
    updated_data, err = TransferStatusService.put_transfer_status(transfer_status_id,req)
    if err == None:
        return payload_response(201,"Updated",updated_data)
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))
    
@router.delete("/transfer-status/{transfer_status_id}",status_code=204)
async def delete_transfer_status(transfer_status_id:int):
    erase_data, err = TransferStatusService.delete_transfer_status(transfer_status_id)
    if err == None:
        return payload_response(204,"Deleted",erase_data)
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))

@router.patch("/transfer-status/{transfer_status_id}",status_code=201)
async def patch_transfer_status(transfer_status_id:int):
    updated_data, err = TransferStatusService.patch_transfer_status(transfer_status_id)
    if err == None:
        return payload_response(201,"Updated",updated_data)
    else:
        print(str(err))
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))