from src.repositories.common import LandedCostTypeRepo
from src.payloads.schemas.common import LandedCostTypeSchema
from fastapi import Request

def get_landed_cost_types_cruds(page:int, limit:int, query_of:list[str], query_by:list[str]):
    get_data, page_results, err = LandedCostTypeRepo.get(page,limit,query_of,query_by) 
    if err == None:
        return get_data, page_results, None
    else:
        return get_data, page_results, err
    
def get_landed_cost_type_cruds(id:int):
    result, err = LandedCostTypeRepo.get_landed_cost_type_cruds(id)
    if err == None:
        return result, None
    else:
        return result, err
    
def post_landed_cost_type_cruds(req:LandedCostTypeSchema.MtrLandedCostTypeGetSchema,request:Request):
    created_data, err = LandedCostTypeRepo.post_landed_cost_type_cruds(req,request)
    if err == None:
        return created_data, None
    else:
        return None, err
    
def patch_landed_cost_type_cruds(id:int,request:Request):
    updated_data, err = LandedCostTypeRepo.patch_landed_cost_type_cruds(id,request)
    if err == None:
        return updated_data, None
    else:
        return None, err