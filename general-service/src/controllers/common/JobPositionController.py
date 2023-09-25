from fastapi import APIRouter, HTTPException, status, Query, Request
from src.services.common import JobPositionService
from src.repositories.common import JobPositionRepo
from src.payloads.schemas.master import JobPositionSchema
from src.payloads.responses.GeneralResponse import payload_response
from src.payloads.responses.PaginationResponse import pagination_response
from src.exceptions.RequestException import ResponseException
router = APIRouter(tags=["Job Position"],prefix="/api/general")

@router.get("/job-positions", status_code=200)
async def get_job_positions(page:int,limit:int,
                            is_active:bool|None=None,
                            job_position_id:int|None=None,
                            job_position_code:str|None=None,
                            job_position_name:str|None=None,
                            sort_of:str|None=None,
                            sort_by:str|None=None):
    get_all_params={"is_active":is_active,"job_position_id":job_position_id,"job_position_code":job_position_code,"job_position_name":job_position_name}
    sort_params={"sort_by":sort_by,"sort_of":sort_of}
    get_all_job_positions,pages,err =JobPositionService.get_job_positions_cruds(page,limit,get_all_params,sort_params)
    if get_all_job_positions!=[] and err == None:
        return pagination_response(200,"Success",page,limit,pages["total_pages"],pages["total_rows"],get_all_job_positions)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=str(err))
    
@router.get("/job-position/{job_position_id}",status_code=200)
async def get_job_position(job_position_id:int):
    get_job_position,err=JobPositionService.get_job_position_cruds(job_position_id)
    if err == None:
        return payload_response(200,"Success",get_job_position)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))

@router.post("/job-position", status_code=201)
async def post_job_position(req:JobPositionSchema.MtrJobPositionGetSchema):
    create_job_position,err= JobPositionService.post_job_position_cruds(req)
    if err == None:
        return payload_response(201,"Success",create_job_position)
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))

@router.delete("/job-position/{job_position_id}", status_code=204)
async def delete_job_position(job_position_id:int):
    erase_job_position, err = JobPositionService.delete_job_position(job_position_id)
    if err == None:
        return payload_response(ResponseException(204), "Success",erase_job_position)
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))

@router.put("/job-position/{job_position_id}", status_code=202)
async def put_job_position(job_position_id:int,req:JobPositionSchema.MtrJobPositionGetSchema):
    update_job_position, err = JobPositionService.put_job_position(job_position_id,req)
    if err == None:
        return payload_response(202,"Success",update_job_position)
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))

@router.patch("/job-position/{job_position_id}", status_code=202)
async def patch_job_positionn(job_position_id:int):
    active_job_position, err  = JobPositionService.patch_job_position_cruds( job_position_id)
    if err == None:
        return payload_response(202,"Success",active_job_position)
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))