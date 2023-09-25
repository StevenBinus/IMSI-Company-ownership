from fastapi import APIRouter, HTTPException, status, Query, Request
from src.services.master import TPTMasterService
from src.payloads.schemas.master import TPTMasterSchema
from src.payloads.responses.CommonResponse import payload_response
from src.payloads.responses.PaginationResponse import pagination_response
from src.exceptions.RequestException import ResponseException

router = APIRouter(tags=["Master : TPT Master"],prefix="/api/sales")

@router.get("/tpt-master", status_code=status.HTTP_200_OK)
async def get_tpt_master_all(page:int, limit:int, query_of:list[str]=Query(None), query_by:list[str]=Query(None)):
    get_results, pages, err = TPTMasterService.get_tpt_master_all(page,limit,query_of,query_by)
    if err == None:
        return pagination_response(200,"success",page,limit,pages["total_pages"],pages["total_rows"],get_results)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))

@router.get("/tpt-master/{id}", status_code=status.HTTP_200_OK)
async def get_tpt_master_by_id(id:int):
    get_result, err = TPTMasterService.get_tpt_master_by_id(id)
    if not get_result and err == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    return payload_response(200,"success",get_result)

@router.post("/tpt-master",status_code=status.HTTP_201_CREATED)
async def post_tpt_master(req:TPTMasterSchema.MtrTPTRequest,request:Request):
    created_data, err = TPTMasterService.post_tpt_master(req,request)
    if err == None:
        return payload_response(201,"created",created_data)
    else:
        raise HTTPException(status_code= status.HTTP_409_CONFLICT,detail=ResponseException(409))
    
@router.get("tpt-master-detail/{id}", status_code=status.HTTP_200_OK)
async def get_tpt_master_by_id(id:int):
    get_result, err = TPTMasterService.get_tpt_chassis(id)
    if not get_result and err == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    return payload_response(200,"success",get_result)


@router.patch("/tpt-master-detail",status_code=status.HTTP_201_CREATED)
async def patch_unit_brand(id:int, request:Request):
    updated_data, err = TPTMasterService.patch_tpt_chassis(id,request)
    if err == None:
        return payload_response(201,"updated",updated_data)
    else:
        print(str(err))
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))
