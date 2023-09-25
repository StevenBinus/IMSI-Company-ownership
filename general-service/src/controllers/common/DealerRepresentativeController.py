from fastapi import APIRouter, HTTPException, status, Query, Request
from src.services.common import DealerRepresentativeService
from src.payloads.schemas.master.DealerRepresentativeSchema import MtrDealerRepresentativeSchema
from src.payloads.responses.GeneralResponse import payload_response
from src.payloads.responses.PaginationResponse import pagination_response
from src.exceptions.RequestException import ResponseException

router = APIRouter(tags=["dealer representative"],prefix="/api/general")

@router.get("/get-all-dealer-representatives", status_code=200)
async def get_all_dealers_representative(page:int, limit:int, query_of:list[str]=Query(None), query_by:list[str]=Query(None)):
    get_results, pages, err = DealerRepresentativeService.get_all_dealers_representative(page,limit,query_of,query_by)
    if err == None:
        return pagination_response(200,"Success",page,limit,pages["total_pages"],pages["total_rows"],get_results)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))

@router.get("/get-dealer-representative-by-id/{id}", status_code=200)
async def get_by_id_dealer_representative(id:int):
    get_result, err = DealerRepresentativeService.get_by_id_dealer_representative(id)
    if not get_result and err == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    return payload_response(200,"Success",get_result)

@router.post("/post-dealer-representative",status_code=status.HTTP_201_CREATED)
async def post_dealer_representative(req:MtrDealerRepresentativeSchema):
    created_data, err = DealerRepresentativeService.post_dealer_representative(req)
    if err == None:
        return payload_response(201,"Created",created_data)
    else:
        raise HTTPException(status_code= status.HTTP_409_CONFLICT,detail=ResponseException(409))
    
@router.put("/put-dealer-representative/{id}",status_code=201)
async def put_dealer_representative(id:int,req:MtrDealerRepresentativeSchema):
    updated_data, err = DealerRepresentativeService.put_dealer_representative(id,req)
    if err == None:
        return payload_response(201,"Updated",updated_data)
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))
    
@router.delete("/delete-dealer-representative/{id}",status_code=204)
async def delete_dealer_representative(id:int):
    erase_data, err = DealerRepresentativeService.delete_dealer_representative(id)
    if err == None:
        return payload_response(204,"Deleted",erase_data)
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))