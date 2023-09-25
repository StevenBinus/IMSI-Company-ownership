from fastapi import APIRouter, HTTPException, status, Query, Request
from src.services.master import StorageTypeService
from src.payloads.schemas.master.StorageTypeSchema import MtrStorageTypeRequest, MtrStorageTypeUpdateRequest
from src.payloads.responses.GeneralResponse import payload_response
from src.payloads.responses.PaginationResponse import pagination_response
from src.exceptions.RequestException import ResponseException

router = APIRouter(tags=["Storage Type"],prefix="/api/general")

@router.get("/storage-type", status_code=status.HTTP_200_OK)
async def get_storage_type_list(page:int, limit:int, 
                                is_active:bool|None=None,
                                storage_type_id:int|None=None,
                                storage_type_code:str|None=None,
                                storage_type_name:str|None=None,
                                sort_by:str|None=None,
                                sort_of:str|None=None):
    
    get_all_params={"is_active":is_active,
                    "storage_type_id":storage_type_id,
                    "storage_type_code":storage_type_code,
                    "storage_type_name":storage_type_name}
    sort_fields={"sort_of":sort_of,"sort_by":sort_by}
    get_results, pages, err = StorageTypeService.get_storage_type_list(page,limit,get_all_params,sort_fields)
    if not get_results or err != None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=ResponseException(404))
    else:
        return pagination_response(200, "success", page, limit, pages["total_pages"], pages["total_rows"], get_results)
    
@router.post("/storage-type",status_code=status.HTTP_201_CREATED)
async def post_storage_type(req:MtrStorageTypeRequest):
    created_data, err = StorageTypeService.post_storage_type(req)
    if err == None:
        return payload_response(201,"created",created_data)
    else:
        raise HTTPException(status_code= status.HTTP_409_CONFLICT,detail=ResponseException(409))
    
@router.get("/storage-type/{id}", status_code=status.HTTP_200_OK)
async def get_storage_type_by_id(id:int):
    get_result, err = StorageTypeService.get_storage_type_by_id(id)
    if not get_result or err != None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    return payload_response(200,"success",get_result)

@router.patch("/storage-type/{id}",status_code=status.HTTP_201_CREATED)
async def patch_storage_type(id:int):
    updated_data, err = StorageTypeService.patch_storage_type(id)
    if err == None:
        return payload_response(201,"updated",updated_data)
    else:
        print(str(err))
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))
    
@router.put("/storage-type/{id}",status_code=status.HTTP_201_CREATED)
async def update_storage_type(id:int,req:MtrStorageTypeUpdateRequest):
    updated_data, err = StorageTypeService.update_storage_type(id, req)
    if err == None:
        return payload_response(201,"updated",updated_data)
    else:
        print(str(err))
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))