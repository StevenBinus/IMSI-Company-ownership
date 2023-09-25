from src.repositories.common import JobTitleRepo
from src.payloads.schemas.master import JobTitleSchema
from fastapi import Request

def get_job_titles_cruds(page:int, limit:int, all_parms:dict(), sort_params:dict()):
    get_data, page_results, err = JobTitleRepo.get_job_titles_cruds(page,limit,all_parms,sort_params) 
    if err == None:
        return get_data, page_results, None
    else:
        return get_data, page_results, err
    
def get_job_title_cruds(id:int):
    result, err = JobTitleRepo.get_job_title_cruds(id)
    if err == None:
        return result, None
    else:
        return result, err
    
    
def post_job_title_cruds(req:JobTitleSchema.MtrJobTitleGetSchema):
    created_data, err = JobTitleRepo.post_job_title_cruds(req)
    if err == None:
        return created_data, None
    else:
        return None, err
    
def patch_job_title_cruds(id:int):
    updated_data, err = JobTitleRepo.patch_job_title_cruds(id)
    if err == None:
        return updated_data, None
    else:
        return None, err

def delete_job_title(id:int):
    delete_data,err = JobTitleRepo.delete_job_title_cruds(id)
    if err == None:
        return delete_data,None
    else:
        return None,err
    
def update_job_title(id:int,req:JobTitleSchema.MtrJobTitleGetSchema):
    update_data,err = JobTitleRepo.put_job_title_cruds(id,req)
    if err == None:
        return update_data,None
    else:
        return None,err 