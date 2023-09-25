from fastapi import APIRouter,HTTPException,status,Request
from src.exceptions.RequestException import ResponseException
from src.payloads.schemas.master import AreaSchema
from src.payloads.responses.GeneralResponse import payload_response
from src.payloads.responses.PaginationResponse import pagination_response
from src.services.master import AreaService

router = APIRouter(tags=["Area"],prefix="/api/general")

@router.get("/areas",status_code=200)
async def get_all_areas(page:int, 
                             limit:int, 
                             area_code:str|None=None, 
                             description:str|None=None,
                             is_active:bool|None=None,
                             sort_by:str|None=None,
                             sort_of:str|None=None):
    get_all_params = {"area_code":area_code,
                      "description":description,
                      "is_active":is_active}
    sort_fields = {"sort_by":sort_by,"sort_of":sort_of}
    get_results, pages, err = AreaService.get_all_areas_list(page,limit,get_all_params,sort_fields)
    if get_results != [] and err == None:
        return pagination_response(200,"success",page,limit,pages["total_pages"],pages["total_rows"],get_results)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))

@router.get("/area/{id}",status_code=200)
async def get_area_by_id(id:int):
    area,err = AreaService.get_area_by_id(id)
    if area != [] and err == None:
        return payload_response(ResponseException(200), "Success",area)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))

@router.get("/area-by-code/{code}",status_code=status.HTTP_200_OK)
async def get_area_by_code(code:str):
    area, err = AreaService.get_area_by_code(code)
    if area != [] and err == None:
         return payload_response(ResponseException(200), "Success",area)
    else:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    
@router.post("/area",status_code=201)
async def post_area(req:AreaSchema.MtrAreaRequest):
    created_area, err = AreaService.post_area(req)
    if err == None:
        return payload_response(201,"created",created_area)
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))

@router.put("/area/{id}",status_code=202)
async def update_area(id:int,req:AreaSchema.MtrAreaUpdate):
    updated_data, err = AreaService.update_area(id,req)
    if err == None:
        return payload_response(202,"created",updated_data)
    else:
        
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=ResponseException(404))

@router.patch("/area/{id}",status_code=202)
async def patch_status_area(id:int,request:Request):
    change_status,err = AreaService.patch_status_area(id,request)
    if err == None:
        return payload_response(202,"success",change_status)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))