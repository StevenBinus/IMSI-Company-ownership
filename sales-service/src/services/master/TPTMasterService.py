from src.repositories.master import TPTMasterRepo
from src.payloads.schemas.master import TPTMasterSchema
from fastapi import Request

def get_tpt_master_all(page:int, limit:int, query_of:list[str], query_by:list[str]):
    get_data, page_results, err = TPTMasterRepo.get_tpt_master_all(page,limit,query_of,query_by) 
    if err == None:
        return get_data, page_results, None
    else:
        return get_data, page_results, err

def get_tpt_master_by_id(id: int):
    result, err = TPTMasterRepo.get_tpt_master_by_id(id)
    if err == None:
        return result, None
    else:
        return result, err
    
def post_tpt_master(req:TPTMasterSchema.MtrTPTRequest,request:Request):
    created_data, err = TPTMasterRepo.post_tpt_master(req,request)
    if err == None:
        return created_data, None
    else:
        return None, err
    

def get_tpt_chassis(id: int):
    result, err = TPTMasterRepo.get_tpt_chassis(id)
    if err == None:
        return result, None
    else:
        return result, err
    
def patch_tpt_chassis(id:int,request:Request):
    updated_data, err = TPTMasterRepo.patch_tpt_chassis(id,request)
    if err == None:
        return updated_data, None
    else:
        return None, err