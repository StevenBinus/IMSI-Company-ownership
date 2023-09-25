from src.repositories.master import UnitGroupRepo
from src.payloads.schemas.master.UnitGroupSchema import UnitGroupRequest
from sqlalchemy.orm import Session

async def get_unit_group_all(db:Session,page:int, limit:int, all_params:dict(), sort_params:dict()):
    get_data, page_results, err = await UnitGroupRepo.get_unit_group_all(db,page,limit,all_params,sort_params) 
    if err != None:
        get_data = None
        page_results = None
    return get_data, page_results, err
    
async def get_unit_group_by_id(db:Session,id:int):
    result, err = await UnitGroupRepo.get_unit_group_by_id(db,id)
    if err != None:
        result = None
    return result, err
    
async def post_unit_group(db:Session,req:UnitGroupRequest):
    created_data, err = await UnitGroupRepo.post_unit_group(db,req)
    if err == None:
        return created_data, None
    else:
        return None, err
    
async def update_unit_group(db:Session,id:int,req_data:UnitGroupRequest):
    updated_data, err = await UnitGroupRepo.update_unit_group(db,id,req_data)
    if err == None:
        return updated_data, None
    else:
        return None, err
    
async def patch_unit_group_status(db:Session,id:int):
    active_status, err = await UnitGroupRepo.patch_unit_group_status(db,id)
    if err == None:
        return active_status, None
    else:
        return None, err