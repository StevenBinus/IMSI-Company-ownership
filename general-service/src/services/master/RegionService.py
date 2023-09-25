from src.repositories.master import RegionRepo
from src.payloads.schemas.master.RegionSchema import MtrRegionRequest
from fastapi import Request

async def get_region_all(page:int, limit:int, get_all_params:dict(),sort_params:dict()):
    get_data, page_results, err = await RegionRepo.get_all_regions(page,limit,get_all_params,sort_params) 
    if err != None:
        get_data = None
        page_results = None
    return get_data, page_results, err
    
def get_region_by_id(id:int):
    result, err = RegionRepo.get_region_by_id(id)
    if err == None:
        return result, None
    else:
        return None, err
    
def get_region_on_by_code(code:str):
    result,err = RegionRepo.get_region_on_by_code(code)
    if err == None:
        return result,None
    else:
        return None,err

def post_new_region(req:MtrRegionRequest, request:Request):
    created_data, err = RegionRepo.post_region(req,request)
    if err == None:
        return created_data, None
    else:
        return None, err
    
def patch_status_region(id:int,request:Request):
    patch_status, err = RegionRepo.patch_status_region(id,request)
    if err == None:
        return patch_status, None
    else:
        return None, err
    
def update_region(id:int,req:MtrRegionRequest, request:Request):
    updated_data, err = RegionRepo.put_region(id,req,request)
    if err == None:
        return updated_data, None
    else:
        return None, err