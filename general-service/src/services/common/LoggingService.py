from src.repositories.common import LoggingRepo
from src.payloads.schemas.master import LoggingSchema
from fastapi import Request

def get_loggings_cruds(page:int, limit:int,all_params:dict(), sort_params:dict()):
    get_data, page_results, err = LoggingRepo.get_loggings_cruds(page,limit,all_params,sort_params) 
    if err == None:
        return get_data, page_results, None
    else:
        return get_data, page_results, err
    
def get_logging_cruds(id:int):
    result, err = LoggingRepo.get_logging_cruds(id)
    if err == None:
        return result, None
    else:
        return result, err
    
    
def post_logging_cruds(req:LoggingSchema.MtrLoggingPostSchema):
    created_data, err = LoggingRepo.post_logging_cruds(req)
    if err == None:
        return created_data, None
    else:
        return None, err
    
def patch_logging_cruds(id:int):
    updated_data, err = LoggingRepo.patch_logging_cruds(id)
    if err == None:
        return updated_data, None
    else:
        return None, err

def put_logging(id:int,req:LoggingSchema.MtrLoggingPutSchema):
    update_data,err=LoggingRepo.put_logging_cruds(id,req)
    if err ==None:
        return update_data,None
    else:
        return None,err

def delete_logging(id:int):
    delete_data,err=LoggingRepo.delete_logging_cruds(id)
    if err == None:
        return delete_data,None
    else:
        return None,err