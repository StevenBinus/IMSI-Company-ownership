from src.repositories.common import JobPositionRepo
from src.payloads.schemas.master import JobPositionSchema
from fastapi import Request

def get_job_positions_cruds(page:int, limit:int, all_params:dict(), sort_params:dict()):
    get_data, page_results, err = JobPositionRepo.get_job_positions_cruds(page,limit,all_params,sort_params) 
    if err == None:
        return get_data, page_results, None
    else:
        return get_data, page_results, err
    
def get_job_position_cruds(id:int):
    result, err = JobPositionRepo.get_job_position_cruds(id)
    if err == None:
        return result, None
    else:
        return result, err
    
    
def post_job_position_cruds(req:JobPositionSchema.MtrJobPositionGetSchema):
    created_data, err = JobPositionRepo.post_job_position_cruds(req)
    if err == None:
        return created_data, None
    else:
        return None, err
    
def patch_job_position_cruds(id:int):
    updated_data, err = JobPositionRepo.patch_job_position_cruds(id)
    if err == None:
        return updated_data, None
    else:
        return None, err

def put_job_position(id:int,req:JobPositionSchema.MtrJobPositionGetSchema):
    update_data, err= JobPositionRepo.put_job_position_cruds(id,req)
    if err == None:
        return update_data,None
    else:
        return None, err

def delete_job_position(id:int):
    delete_data, err = JobPositionRepo.delete_job_position_cruds(id)
    if err == None:
        return delete_data,None
    else:
        return None, err
    
