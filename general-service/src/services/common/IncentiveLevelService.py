from src.repositories.common import IncentiveLevelRepo
from src.payloads.schemas.common import IncentiveLevelSchema
from fastapi import Request

def get_incentive_levels_cruds(page:int, limit:int, query_of:list[str], query_by:list[str]):
    get_data, page_results, err = IncentiveLevelRepo.get_incentive_levels_cruds(page,limit,query_of,query_by) 
    if err == None:
        return get_data, page_results, None
    else:
        return get_data, page_results, err
    
def get_incentive_level_cruds(id:int):
    result, err = IncentiveLevelRepo.get_incentive_level_cruds(id)
    if err == None:
        return result, None
    else:
        return result, err
    
def post_incentive_level_cruds(req:IncentiveLevelSchema.MtrIncentiveLevelGetSchema,request:Request):
    created_data, err = IncentiveLevelRepo.post_incentive_level_cruds(req,request)
    if err == None:
        return created_data, None
    else:
        return None, err
    
def patch_incentive_level_cruds(id:int,request:Request):
    updated_data, err = IncentiveLevelRepo.patch_incentive_level_cruds(id,request)
    if err == None:
        return updated_data, None
    else:
        return None, err