from fastapi import APIRouter,HTTPException,status,Request
from src.exceptions.RequestException import ResponseException
from src.payloads.schemas.master import LoggingSchema
from src.payloads.responses.GeneralResponse import payload_response
from src.payloads.responses.PaginationResponse import pagination_response 
from datetime import datetime
from src.services.common import LoggingService

router = APIRouter(tags=["Logging"],prefix="/api/general")

@router.get("/loggings", status_code=200)
async def get_loggings(page:int,limit:int,
                       is_active:bool|None=None,
                       logging_id:int|None=None,
                       created_at:datetime|None=None,
                       created_by:str|None=None,
                       changed_at:datetime|None=None,
                       changed_by:str|None=None,
                       hitted_apis:str|None=None,
                       http_requests:str|None=None,
                       http_respons:str|None=None,
                       data_context:str|None=None,
                       trigerred_menu:str|None=None,
                       ip_address:str|None=None,
                       sort_of:str|None=None,
                       sort_by:str|None=None):
    get_all_params={"is_active":is_active,"loging_id":logging_id,"created_at":created_at,"created_by":created_by,"changed_at":changed_at,"changed_by":changed_by,"hitted_apis":hitted_apis,"http_requests":http_requests,"http_respons":http_respons,"data_context":data_context,"triggered_menu":trigerred_menu,"ip_address":ip_address}
    sort_params={"sort_of":sort_of,"sort_by":sort_by}
    get_results,pages,err=LoggingService.get_loggings_cruds(page,limit,get_all_params,sort_params)
    if get_results!=[] and err == None:
        return pagination_response(200,"Success",page,limit,pages["total_pages"],pages["total_rows"],get_results)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=str(err)) 

@router.get("/logging/{logging_id}", status_code=status.HTTP_200_OK)
async def get_logging(logging_id:int):
    get_data,err = LoggingService.get_logging_cruds(logging_id)
    if err == None and get_data != None:
        return payload_response(200,"Success",get_data)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))

@router.post("/logging", status_code=201)
async def post_logging(req:LoggingSchema.MtrLoggingPostSchema):
    post_data,err = LoggingService.post_logging_cruds(req)
    if err == None:
        return payload_response(201,"Created",post_data)
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))

@router.delete("/logging/{logging_id}", status_code=204)
async def delete_logging(logging_id:int):
    delete_data,err=LoggingService.delete_logging(logging_id)
    if err ==None:
        return payload_response(204,"Success",delete_data)
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))

@router.put("/logging/{logging_id}", status_code=202)
async def put_logging(logging_id:int,req:LoggingSchema.MtrLoggingPutSchema):
    update_data,err = LoggingService.put_logging(id,req)
    if err == None:
        return payload_response(202,"Success",update_data)
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))
        

@router.patch("/logging/{logging_id}", status_code=202)
async def patch_logging(logging_id:int):
    patched_data,err=LoggingService.patch_logging_cruds(logging_id)
    if err == None:
        return payload_response(202,"Success",patched_data)
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))
    
