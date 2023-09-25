from src.repositories.master import UnitColourRepo
from src.payloads.schemas.master.UnitColourSchema import UnitColourRequest
from sqlalchemy.orm import Session

async def get_unit_colour_list_all(db:Session,page:int, limit:int, all_params=dict(), sort_params=dict()):
    results,page_results,err = await UnitColourRepo.get_unit_colour_list_all(db,page,limit,all_params,sort_params)
    if err != None:
        results = None
        page_results = None
    return results, page_results, err

async def get_unit_colour_by_id(db:Session,id:int):
    result, err = await UnitColourRepo.get_unit_colour_by_id(db,id)
    if err != None:
        result = None
    return result, err
    
async def post_unit_colour(db:Session,req:UnitColourRequest):
    created_data, err = await UnitColourRepo.post_unit_colour(db,req)
    if err != None:
        created_data = None
    return created_data,err
    
async def patch_unit_colour(db:Session,id:int):
    active_status, err = await UnitColourRepo.patch_unit_colour(db,id)
    if err != None:
        active_status = None
    return active_status, err