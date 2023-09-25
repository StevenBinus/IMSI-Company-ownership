from fastapi import APIRouter, HTTPException, status, Query, Request
from src.services.common import RFPPaidInService
from src.payloads.schemas.common.RFPPaidInSchema import MtrRFPPaidInGetSchema
from src.payloads.responses.GeneralResponse import payload_response
from src.payloads.responses.PaginationResponse import pagination_response
from src.exceptions.RequestException import ResponseException

router = APIRouter(tags=["RFP Paid In"],prefix="/api/general")

@router.get("/rfp-paid-ins", status_code=200)
async def get_all_rfp_paid_ins(page:int, limit:int, query_of:list[str]=Query(None), query_by:list[str]=Query(None)):
    get_results, pages, err = RFPPaidInService.get_all_rfp_paid_ins(page,limit,query_of,query_by)
    if err == None:
        return pagination_response(200,"Success",page,limit,pages["total_pages"],pages["total_rows"],get_results)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))

@router.get("/rfp-paid-in/{rfp_paid_in_id}", status_code=200)
async def get_by_id_rfp_paid_in(rfp_paid_in_id:int):
    get_result, err = RFPPaidInService.get_by_id_rfp_paid_in(rfp_paid_in_id)
    if not get_result and err == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    return payload_response(200,"Success",get_result)

@router.post("/rfp-paid-in",status_code=201)
async def post_rfp_paid_in(req:MtrRFPPaidInGetSchema):
    created_data, err = RFPPaidInService.post_rfp_paid_in(req)
    if err == None:
        return payload_response(201,"Created",created_data)
    else:
        raise HTTPException(status_code= status.HTTP_409_CONFLICT,detail=ResponseException(409))
    
@router.put("/rfp-paid-in/{rfp_paid_in_id}",status_code=201)
async def put_rfp_paid_in(rfp_paid_in_id:int,req:MtrRFPPaidInGetSchema):
    updated_data, err = RFPPaidInService.put_rfp_paid_in(rfp_paid_in_id,req)
    if err == None:
        return payload_response(201,"Updated",updated_data)
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))
    
@router.delete("/rfp-paid-in/{rfp_paid_in_id}",status_code=204)
async def delete_rfp_paid_in(rfp_paid_in_id:int):
    erase_data, err = RFPPaidInService.delete_rfp_paid_in(rfp_paid_in_id)
    if err == None:
        return payload_response(204,"Deleted",erase_data)
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))

@router.patch("/rfp-paid-in/{rfp_paid_in_id}",status_code=201)
async def patch_rfp_paid_in(rfp_paid_in_id:int):
    updated_data, err = RFPPaidInService.patch_rfp_paid_in(rfp_paid_in_id)
    if err == None:
        return payload_response(201,"Updated",updated_data)
    else:
        print(str(err))
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))