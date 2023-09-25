from src.repositories.master import UnitModelRepo
from src.payloads.schemas.master.UnitModelSchema import MtrUnitModelRequest
from sqlalchemy.orm import Session

async def get_unit_model_list_all(db:Session,page:int, limit:int, all_params=dict(), sort_params=dict()):
    results,page_results,err = await UnitModelRepo.get_unit_model_list_all(db,page,limit,all_params,sort_params)
    if err != None:
        results = None
        page = None
    return results,page_results,err
 
async def get_unit_model_by_id(db:Session,id:int):
    result, err = await UnitModelRepo.get_unit_model_by_id(db,id)
    if err != None:
        result = None,
    return result, err
    
async def get_unit_model_drop_down(db:Session, brand_id:int):
    result, err = await UnitModelRepo.get_unit_model_drop_down(db, brand_id)
    if err != None:
        result = None
    return result, err

async def post_unit_model(db:Session, req:MtrUnitModelRequest):
    created_data, err = await UnitModelRepo.post_unit_model(db,req)
    if err != None:
        created_data = None
    return created_data,err
    
async def patch_unit_model(db:Session, id:int):
    active_status, err = await UnitModelRepo.patch_unit_model(db,id)
    if err != None:
        active_status = None
    return active_status, err