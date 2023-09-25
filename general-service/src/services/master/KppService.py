from src.repositories.master import KppRepo
from src.payloads.schemas.master.KppSchema import MtrKppPost,MtrKppUpdate
from fastapi import Request
from sqlalchemy.orm import Session

async def get_all_kpps(db:Session,page:int, limit:int, all_params:dict(), sort_params:dict()):
    get_data, page_results, err =await KppRepo.get_all_kpps(db,page,limit,all_params,sort_params) 
    if err == None:
        return get_data, page_results, None
    else:
        return get_data, page_results, err
    
async def get_kpp(db:Session,id:int):
    result, err =await KppRepo.get_kpp(db,id)
    if err == None:
        return result, None
    else:
        return result, err
    
async def post_kpp(db:Session,req:MtrKppPost):
    created_data, err = await KppRepo.post_kpp(db, req)
    if err == None:
        return created_data, None
    else:
        return None, err
    
async def patch_kpp(db:Session,id:int):
    updated_data, err =await KppRepo.patch_kpp(db,id)
    if err == None:
        return updated_data, None
    else:
        return None, err
    
async def put_kpp(db:Session,id:int,req:MtrKppUpdate):
    updated_data, err =await KppRepo.put_kpp(db,id,req)
    if err == None:
        return updated_data, None
    else:
        return None, err