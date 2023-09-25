from src.repositories.master import AreaRepo
from src.payloads.schemas.master import AreaSchema
from fastapi import Request

def get_all_areas_list(page:int,limit:int,get_all_params:dict(),sort_fields:dict()):
    get_data, page_results, err = AreaRepo.get_all_areas_list(page,limit,get_all_params,sort_fields) 
    if err == None:
        return get_data, page_results, None
    else:
        return None, None, err
    
def get_area_by_id(id:int):
    result, err = AreaRepo.get_area_by_id(id)
    if err == None:
        return result, None
    else:
        return None, err
    
def get_area_by_code(code:str):
    result, err = AreaRepo.get_area_by_code(code)
    if err == None:
        return result,None
    else:
        return None, err
    
def post_area(req:AreaSchema.MtrAreaSchema,request:Request):
    created_data, err = AreaRepo.post_area(req,request)
    if err == None:
        return created_data, None
    else:
        return None, err
    
def update_area(id:int,req:AreaSchema.MtrAreaUpdate):
    updated_data,err = AreaRepo.update_area(id,req)
    if err == None:
        return updated_data,None
    else:
        return None, err
    
def patch_status_area(id:int,request:Request):
    change_status, err = AreaRepo.patch_status_area(id,request)
    if err == None:
        return change_status, None
    else:
        return None, err