from src.repositories.master import CostProfitMapRepo
from src.payloads.schemas.master import CostProfitMapSchema
from fastapi import Request

def get_all_cost_profit_maps(page:int, limit:int, all_params:dict(), sort_params:dict()):
    get_data, page_results, err = CostProfitMapRepo.get_all_cost_profit_maps(page,limit,all_params,sort_params) 
    if err == None:
        return get_data, page_results, None
    else:
        return get_data, page_results, err
    
def get_by_id_cost_profit_map(id:int):
    result, err = CostProfitMapRepo.get_by_id_cost_profit_map(id)
    if err == None:
        return result, None
    else:
        return result, err
    
    
def post_cost_profit_map(req:CostProfitMapSchema.MtrCostProfitMapSchema):
    created_data, err = CostProfitMapRepo.post_cost_profit_map(req)
    if err == None:
        return created_data, None
    else:
        return None, err
    
def put_cost_profit_map(id:int,request:Request):
    updated_data, err = CostProfitMapRepo.put_cost_profit_map(id,request)
    if err == None:
        return updated_data, None
    else:
        return None, err
    
def delete_cost_profit_map(id:int):
    delete_data, err = CostProfitMapRepo.delete_cost_profit_map(id)
    if err == None:
        return delete_data, None
    else:
        return None, err
    
def patch_cost_profit_map(id:int):
    delete_data, err = CostProfitMapRepo.patch_cost_profit_map(id)
    if err == None:
        return delete_data, None
    else:
        return None, err