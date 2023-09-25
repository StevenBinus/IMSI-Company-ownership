from src.repositories.master import DistrictRepo
from src.payloads.schemas.master.DistrictSchema import MtrDistrict,MtrDistrictUpdate
from fastapi import Request

def get_all_districts(page:int, limit:int, all_params:dict(), sort_by:dict()):
    get_data, page_results, err = DistrictRepo.get_all_districts(page,limit,all_params,sort_by) 
    if err == None:
        return get_data, page_results, None
    else:
        return None, None, err
    
def get_district(id:int):
    result, err = DistrictRepo.get_district_by_id(id)
    if err == None:
        return result, None
    else:
        return result, err
    
def post_district(req:MtrDistrict):
    created_data, err = DistrictRepo.post_district(req)
    if err == None:
        return created_data, None
    else:
        return None, err
    
def patch_district(id:int):
    updated_data, err = DistrictRepo.patch_district(id)
    if err == None:
        return updated_data, None
    else:
        return None, err
    
def put_district(id:int,req:MtrDistrictUpdate):
    updated_data, err = DistrictRepo.put_district(id,req)
    if err == None:
        return updated_data, None
    else:
        return None, err
    
def delete_district(id:int):
    erase_data, err = DistrictRepo.delete_district(id)
    if err == None:
        return erase_data, None
    else:
        return None, err