from fastapi import APIRouter, HTTPException, status, Query, Request
from src.services.common import TransportService
from src.payloads.responses.GeneralResponse import payload_response
from src.payloads.responses.PaginationResponse import pagination_response
from src.exceptions.RequestException import ResponseException
from src.payloads.schemas.common.TransportSchema import MtrTransportGetSchema


router = APIRouter(tags=["Transport"],prefix="/api/general")

@router.get("/transports", status_code=200)
async def get_all_transports(page:int, limit:int, query_of:list[str]=Query(None), query_by:list[str]=Query(None)):
    get_results, pages, err = TransportService.get_all_transports(page,limit,query_of,query_by)
    if err == None:
        return pagination_response(200,"Success",page,limit,pages["total_pages"],pages["total_rows"],get_results)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))

@router.get("/transport/{transport_id}", status_code=200)
async def get_by_id_transport(transport_id:int):
    get_result, err = TransportService.get_by_id_transport(transport_id)
    if not get_result and err == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    return payload_response(200,"Success",get_result)

@router.post("/transport",status_code=201)
async def post_transport(req:MtrTransportGetSchema):
    created_data, err = TransportService.post_transport(req)
    if err == None:
        return payload_response(201,"Created",created_data)
    else:
        raise HTTPException(status_code= status.HTTP_409_CONFLICT,detail=ResponseException(409))
    
@router.put("/transport/{transport_id}",status_code=201)
async def put_transport(transport_id:int,req:MtrTransportGetSchema):
    updated_data, err = TransportService.put_transport(transport_id,req)
    if err == None:
        return payload_response(201,"Updated",updated_data)
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))
    
@router.delete("/transport/{transport_id}",status_code=204)
async def delete_transport(transport_id:int):
    erase_data, err = TransportService.delete_transport(transport_id)
    if err == None:
        return payload_response(204,"Deleted",erase_data)
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))

@router.patch("/transport/{transport_id}",status_code=201)
async def patch_transport(transport_id:int):
    updated_data, err = TransportService.patch_transport(transport_id)
    if err == None:
        return payload_response(201,"Updated",updated_data)
    else:
        print(str(err))
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))