from fastapi import APIRouter, HTTPException, status, Query, Request
from src.services.common import StockOpnameStatusService
from src.payloads.schemas.common.StockOpnameStatusSchema import MtrStockOpnameStatusGetSchema
from src.payloads.responses.GeneralResponse import payload_response
from src.payloads.responses.PaginationResponse import pagination_response
from src.exceptions.RequestException import ResponseException

router = APIRouter(tags=["Stock Opname Status"],prefix="/api/general")

@router.get("/stock-opnames", status_code=200)
async def get_all_stock_opnames(page:int, limit:int, query_of:list[str]=Query(None), query_by:list[str]=Query(None)):
    get_results, pages, err = StockOpnameStatusService.get_all_stock_opnames(page,limit,query_of,query_by)
    if err == None:
        return pagination_response(200,"Success",page,limit,pages["total_pages"],pages["total_rows"],get_results)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))

@router.get("/stock-opname/{stock_opname_id}", status_code=200)
async def get_by_id_stock_opname(stock_opname_id:int):
    get_result, err = StockOpnameStatusService.get_by_id_stock_opname(stock_opname_id)
    if not get_result and err == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    return payload_response(200,"Success",get_result)

@router.post("/stock-opname",status_code=201)
async def post_stock_opname(req:MtrStockOpnameStatusGetSchema):
    created_data, err = StockOpnameStatusService.post_stock_opname(req)
    if err == None:
        return payload_response(201,"Created",created_data)
    else:
        raise HTTPException(status_code= status.HTTP_409_CONFLICT,detail=ResponseException(409))
    
@router.put("/stock-opname/{stock_opname_id}",status_code=201)
async def put_stock_opname(stock_opname_id:int,req:MtrStockOpnameStatusGetSchema):
    updated_data, err = StockOpnameStatusService.put_stock_opname(stock_opname_id,req)
    if err == None:
        return payload_response(201,"Updated",updated_data)
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))
    
@router.delete("/stock-opname/{stock_opname_id}",status_code=204)
async def delete_stock_opname(stock_opname_id:int):
    erase_data, err = StockOpnameStatusService.delete_stock_opname(stock_opname_id)
    if err == None:
        return payload_response(204,"Deleted",erase_data)
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))

@router.patch("/stock-opname/{stock_opname_id}",status_code=201)
async def patch_stock_opname(stock_opname_id:int):
    updated_data, err = StockOpnameStatusService.patch_stock_opname(stock_opname_id)
    if err == None:
        return payload_response(201,"Updated",updated_data)
    else:
        print(str(err))
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))
    