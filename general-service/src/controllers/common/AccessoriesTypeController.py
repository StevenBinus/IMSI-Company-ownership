from fastapi import APIRouter, HTTPException, status, Query, Request
from src.services.common import AccessoriesTypeService
from src.payloads.schemas.common.AccessoriesTypeSchema import MtrAccessoriesTypeGetSchema
from src.payloads.responses.GeneralResponse import payload_response
from src.payloads.responses.PaginationResponse import pagination_response
from src.exceptions.RequestException import ResponseException

router = APIRouter(tags=["Accessories Type"],prefix="/api/general")

@router.get("/accessories-types", status_code=200)
async def get_all_accessories_types(page:int, limit:int,is_active:bool|None=None,accesories_type_id:int|None=None,accessories_type_code:str|None=None,accesories_type_name:str|None=None,sort_by:str|None=None,sort_of:str|None=None):
    get_all_params = {"is_active":is_active,"accesories_type_id":accesories_type_id,"accesories_type_code":accessories_type_code,"accessories_type_name":accesories_type_name}
    sort_params = {"sort_of":sort_of,"sort_by":sort_by}
    get_results, pages, err = AccessoriesTypeService.get_all_accessories_types(page,limit,get_all_params,sort_params)
    if err == None:
        return pagination_response(200,"Success",page,limit,pages["total_pages"],pages["total_rows"],get_results)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))

@router.get("/accessories-type/{accessories_type_id}", status_code=200)
async def get_by_id_accessories_type(accessories_type_id:int):
    get_result, err = AccessoriesTypeService.get_by_id_accessories_type(accessories_type_id)
    if not get_result and err == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    return payload_response(200,"Success",get_result)

@router.post("/accessories-type",status_code=201)
async def post_accessories_type(req:MtrAccessoriesTypeGetSchema):
    created_data, err = AccessoriesTypeService.post_accessories_type(req)
    if err == None:
        return payload_response(201,"Created",created_data)
    else:
        raise HTTPException(status_code= status.HTTP_409_CONFLICT,detail=ResponseException(409))
    
@router.put("/accessories-type/{accessories_type_id}",status_code=201)
async def put_accessories_type(accessories_type_id:int,req:MtrAccessoriesTypeGetSchema):
    updated_data, err = AccessoriesTypeService.put_accessories_type(accessories_type_id,req)
    if err == None:
        return payload_response(201,"Updated",updated_data)
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))
    
@router.delete("/accessories-type/{accessories_type_id}",status_code=204)
async def delete_accessories_type(accessories_type_id:int):
    erase_data, err = AccessoriesTypeService.delete_accessories_type(accessories_type_id)
    if err == None:
        return payload_response(204,"Deleted",erase_data)
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))

@router.patch("/accessories-type/{accessories_type_id}",status_code=201)
async def patch_accessories_type(accessories_type_id:int):
    updated_data, err = AccessoriesTypeService.patch_accessories_type(accessories_type_id)
    if err == None:
        return payload_response(201,"Updated",updated_data)
    else:
        print(str(err))
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))
    



