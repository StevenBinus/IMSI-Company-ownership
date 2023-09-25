from src.repositories.master import CostCenterRepo
from src.payloads.schemas.master import CostCenterSchema
from fastapi import Request

def get_cost_center_all(page:int, limit:int, all_params:dict(),sort_params:dict()):
    get_data, page_results, err = CostCenterRepo.get_mtr_cost_centers_cruds(page,limit,all_params,sort_params) 
    if err == None:
        return get_data, page_results, None
    else:
        return None, None, err
    
def get_cost_center_by_id(id:int):
    result, err = CostCenterRepo.get_mtr_cost_center_cruds(id)
    if err == None:
        return result, None
    else:
        return result, err
    
def post_cost_center(req:CostCenterSchema.MtrCostCenterPost):
    created_data, err = CostCenterRepo.post_mtr_cost_center(req)
    if err == None:
        return created_data, None
    else:
        return None, err
    
def patch_cost_center(id:int):
    updated_data, err = CostCenterRepo.patch_mtr_cost_center(id)
    if err == None:
        return updated_data, None
    else:
        return None, err
    
def put_cost_center(id:int,req:CostCenterSchema.MtrCostCenterPost):
    patched_data, err =CostCenterRepo.update_mtr_cost_center(id,req)
    if err == None:
        return patched_data, None
    else:
        return None,err

def delete_cost_center(id:int):
    delete_data,err=CostCenterRepo.del_mtr_cost_center(id)
    if err == None:
        return delete_data,None
    else:
        return None,err