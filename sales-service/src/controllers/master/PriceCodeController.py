from fastapi import APIRouter, HTTPException, status, Query, Request
from src.services.master import PriceCodeService
from src.payloads.schemas.master.PriceCodeSchema import PriceCodeRequest
from src.payloads.responses.CommonResponse import payload_response
from src.payloads.responses.PaginationResponse import pagination_response
from src.exceptions.RequestException import ResponseException
#from src.repositories.master.PriceCodeRepo import get_price_code_search

router = APIRouter(tags=["Master : Price Code"],prefix="/api/sales")

@router.get("/price-code", status_code=status.HTTP_200_OK)
async def get_all(page:int,limit:int,
                  price_code:str|None=None,
                  price_code_name:str|None=None,
                  brand_name:str|None=None
                  ):

    get_all_params = {
        "price_code": price_code,
        "price_code_name": price_code_name,
        "brand_name": brand_name
    }

    get_results, pages, err = PriceCodeService.get_price_code_search(page,limit,get_all_params)
    if err != None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=ResponseException(404))    
    else:
        return pagination_response(200,"success",page,limit,pages["total_pages"],pages["total_rows"],get_results)
  
  
@router.get("/price-code/{id}", status_code=status.HTTP_200_OK)
async def get_price_code_by_id(id:int):
    get_result, err = PriceCodeService.get_price_code_by_id(id)
    if not get_result and err == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    return payload_response(200,"success",get_result)
 
@router.post("/price-code")
async def post_price_code(req_data:PriceCodeRequest,request:Request):
    created_data,err =  PriceCodeService.post_price_code(req_data,request)
    if err == None:
        return payload_response(201,"created",created_data)
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=ResponseException(409))

@router.put("/price-code/{id}", status_code=status.HTTP_201_CREATED)
async def update_price_code(id:int, req:PriceCodeRequest, request:Request):
    updated_data,err = PriceCodeService.update_price_code(id,req,request)
    if err == None:
        return payload_response(201,"updated",updated_data)
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=ResponseException(400))

@router.patch("/price-code",status_code=status.HTTP_201_CREATED)
async def patch_price_code(id:int, request:Request):
    updated_data, err = PriceCodeService.patch_price_code(id,request)
    if err == None:
        return payload_response(201,"updated",updated_data)
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))