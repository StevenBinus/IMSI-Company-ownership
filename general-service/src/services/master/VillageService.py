from src.repositories.master import VillageRepo
from src.payloads.schemas.master.VillageSchema import MtrVillagePost,MtrVillageGetSchema
from fastapi import Request

def get_all_villages(page:int, limit:int, all_params:dict(),sort_params:dict()):
    get_data, page_results, err = VillageRepo.get_all_villages(page,limit,all_params,sort_params) 
    if err == None:
        return get_data, page_results, None
    else:
        return get_data, page_results, err
    
def get_village(id:int):
    result, err = VillageRepo.get_village_by_id(id)
    if err == None:
        return result, None
    else:
        return result, err
    
def post_village(req:MtrVillagePost):
    created_data, err = VillageRepo.post_village(req)
    if err == None:
        return created_data, None
    else:
        return None, err
    
def patch_village(id:int):
    updated_data, err = VillageRepo.patch_village(id)
    if err == None:
        return updated_data, None
    else:
        return None, err
    
def put_village(id:int,req:MtrVillageGetSchema):
    updated_data, err = VillageRepo.put_village(id,req)
    if err == None:
        return updated_data, None
    else:
        return None, err
    
def delete_village(id:int):
    erase_data, err = VillageRepo.delete_village(id)
    if err == None:
        return erase_data, None
    else:
        return None, err