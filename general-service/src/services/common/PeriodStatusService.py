from src.repositories.common import PeriodStatusRepo
from src.payloads.schemas.common.PeriodStatusSchema import MtrPeriodStatusGetSchema
from fastapi import Request

def get_period_statuss_cruds(page:int, limit:int, query_of:list[str], query_by:list[str]):
    get_data, page_results, err = PeriodStatusRepo.get_period_statuss_cruds(page,limit,query_of,query_by) 
    if err == None:
        return get_data, page_results, None
    else:
        return get_data, page_results, err
    
def get_period_status_cruds(id:int):
    result, err = PeriodStatusRepo.get_period_status_cruds(id)
    if err == None:
        return result, None
    else:
        return result, err
    
def post_period_status_cruds(req:MtrPeriodStatusGetSchema,request:Request):
    created_data, err = PeriodStatusRepo.post_period_status_cruds(req,request)
    if err == None:
        return created_data, None
    else:
        return None, err
    
def patch_period_status_cruds(id:int,request:Request):
    updated_data, err = PeriodStatusRepo.patch_period_status_cruds(id,request)
    if err == None:
        return updated_data, None
    else:
        return None, err