from fastapi import APIRouter, HTTPException, status, Query, Request
from src.services.common import BillableToService
from src.payloads.schemas.common.BillableToSchema import MtrBillableToGetSchema
from src.payloads.responses.GeneralResponse import payload_response
from src.payloads.responses.PaginationResponse import pagination_response
from src.exceptions.RequestException import ResponseException

router = APIRouter(tags=["Billable To"],prefix="/api/general")

@router.get("/billables-to", status_code=200)
async def get_all_billables_to(page:int, limit:int, query_of:list[str]=Query(None), query_by:list[str]=Query(None)):
    get_results, pages, err = BillableToService.get_all_billables_to(page,limit,query_of,query_by)
    if err == None:
        return pagination_response(200,"Success",page,limit,pages["total_pages"],pages["total_rows"],get_results)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))

@router.get("/billable-to/{billable_to_id}", status_code=200)
async def get_by_id_billable_to(billable_to_id:int):
    get_result, err = BillableToService.get_by_id_billable_to(billable_to_id)
    if not get_result and err == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    return payload_response(200,"Success",get_result)

@router.post("/billable-to",status_code=201)
async def post_billable_to(req:MtrBillableToGetSchema):
    created_data, err = BillableToService.post_billable_to(req)
    if err == None:
        return payload_response(201,"Created",created_data)
    else:
        raise HTTPException(status_code= status.HTTP_409_CONFLICT,detail=ResponseException(409))
    
@router.put("/billable-to/{billable_to_id}",status_code=201)
async def put_billable_to(billable_to_id:int,req:MtrBillableToGetSchema):
    updated_data, err = BillableToService.put_billable_to(billable_to_id,req)
    if err == None:
        return payload_response(201,"Updated",updated_data)
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))
    
@router.delete("/billable-to/{billable_to_id}",status_code=204)
async def delete_billable_to(billable_to_id:int):
    erase_data, err = BillableToService.delete_billable_to(billable_to_id)
    if err == None:
        return payload_response(204,"Deleted",erase_data)
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))

@router.patch("/billable-to/{billable_to_id}",status_code=201)
async def patch_billable_to(billable_to_id:int):
    updated_data, err = BillableToService.patch_billable_to(billable_to_id)
    if err == None:
        return payload_response(201,"Updated",updated_data)
    else:
        print(str(err))
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))
    



