from fastapi import APIRouter,HTTPException,status,Request
from src.exceptions.RequestException import ResponseException
from src.payloads.schemas.master import JobTitleSchema
from src.payloads.responses.GeneralResponse import payload_response
from src.payloads.responses.PaginationResponse import pagination_response
from src.services.common import JobTitleService


router = APIRouter(tags=["Job Title"],prefix="/api/general")

@router.get("/job-titles", status_code=200)
async def get_job_titles(page:int,limit:int,
                         is_active:bool|None=None,
                         job_title_id:str|None=None,
                         job_title_code:str|None=None,
                         job_title_name:str|None=None,
                         sort_of:str|None=None,
                         sort_by:str|None=None):
    get_all_params={"is_active":is_active,
                    "job_title_id":job_title_id,
                    "job_title_code":job_title_code,
                    "Job_title_name":job_title_name}
    sort_params={"sort_of":sort_of,"sort:by":sort_by}
    get_all_job_title,pages,err= JobTitleService.get_job_titles_cruds(page,limit,get_all_params,sort_params)
    if get_all_job_title !=[] and err == None:
        return pagination_response(200,"Success",page,limit,pages["total_pages"],pages["Total_rows"],get_all_job_title)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=str(err))   

@router.get("/job-title/{job_title_id}", status_code=200)
async def get_job_title(job_title_id:int):
    job_title,err = JobTitleService.get_job_title_cruds(job_title_id)
    if err == None and job_title !=[]:
        return payload_response(200,"Success",job_title)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    

@router.post("/job-title", status_code=201)
async def post_job_title(req:JobTitleSchema.MtrJobTitleGetSchema):
    new_job_title,err = JobTitleService.post_job_title_cruds(req)
    if err == None:
        return payload_response(201,"Seccess",new_job_title)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))

@router.delete("/job-title/{job_title_id}", status_code=204)
async def delete_job_title(job_title_id:int):
    erase_job_title,err = JobTitleService.delete_job_title(job_title_id)
    if err == None:
        return payload_response(204,"Success",erase_job_title)
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))

@router.put("/job-title/{job_title_id}", status_code=202)
async def put_job_title(job_title_id:int,req:JobTitleSchema.MtrJobTitleGetSchema):
    update_data,err = JobTitleService.update_job_title(job_title_id,req)
    if err == None:
        return payload_response(202,"Success",update_data)
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))


@router.patch("/job-title/{job_title_id}", status_code=202)
async def patch_job_title(job_title_id:int):
    patched_data,err = JobTitleService.patch_job_title_cruds(job_title_id)
    if err == None:
        return payload_response(200,"Success",patched_data)
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))