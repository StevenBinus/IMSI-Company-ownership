from src.repositories.master import DivisionRepo
from src.payloads.schemas.master.DivisionSchema import MtrDivisionRequest, MtrDivisionUpdateRequest
from fastapi import Request
from sqlalchemy.orm import Session


async def get_division_list(db:Session, page:int,limit:int, all_params: dict(), sort_params: dict(),default_sort_value = any):
    get_data, page_results, err = await DivisionRepo.get_division_list(db, page,limit,all_params,sort_params,default_sort_value)
    if err == None:
        return get_data, page_results, None
    else:
        return get_data, page_results, err
    
async def post_division(db: Session, req:MtrDivisionRequest):
    created_data, err = await DivisionRepo.post_division(db,req)
    if err == None:
        return created_data, None
    else:
        return None, err
    
async def get_divison_by_id(db:Session, id:int):
    result, err = await DivisionRepo.get_division_by_id(db, id)
    if err == None:
        return result, None
    else:
        return result, err
    
async def patch_division(db:Session, id:int):
    updated_data, err = await DivisionRepo.patch_division(db, id)
    if err == None:
        return updated_data, None
    else:
        return None, err
    
async def update_division(db:Session,id: int, req:MtrDivisionUpdateRequest):
    updated_data, err = await DivisionRepo.update_division(db, id, req)
    if err == None:
        return updated_data, None
    else:
        return None, err