from src.repositories.master import UnitBrandRepo
from src.payloads.schemas.master.UnitBrandSchema import UnitBrandRequest, UnitBrandMultiRequest
from sqlalchemy.orm import Session
import ast

async def get_unit_brand_all(db:Session,page:int, limit:int, all_params=dict(), sort_params=dict()):
    get_data, page_results, err = await UnitBrandRepo.get_unit_brand_all(db,page,limit,all_params,sort_params) 
    if err != None:
        get_data = None
        page_results = None
    return get_data, page_results, err

async def get_unit_brand_drop_down(db:Session):
    result, err = await UnitBrandRepo.get_unit_brand_drop_down(db)
    if err != None:
        result = None
    return result, err
    
async def get_unit_brand_by_id(db:Session,id:int):
    result, err = await UnitBrandRepo.get_unit_brand_by_id(db,id)
    if err != None:
        result = None
    return result, err

async def get_unit_brand_multi_id(db:Session,req:str):
    results = []
    res_str = ast.literal_eval(req)
    for brand_id in res_str:
        try:
            result, err = await get_unit_brand_by_id(db,brand_id)
            get_brand = {
                "brand_id":result.brand_id,
                "brand_name":result.brand_name
            }
            results.append(get_brand)
            err == None
        except:
            results = None
            err = "unrecognized ID, please check your input"
            break
    return results, err

async def post_unit_brand(db:Session,req:UnitBrandRequest):
    created_data, err = await UnitBrandRepo.post_unit_brand(db,req)
    if err != None:
        created_data = None
    return created_data, err
    
async def update_unit_brand(db:Session,id:int, req:UnitBrandRequest):
    updated_data,err = await UnitBrandRepo.update_unit_brand(db,id,req)
    if err != None:
        updated_data = None
    return updated_data, err
    
async def patch_unit_brand(db:Session,id:int):
    updated_data, err = await UnitBrandRepo.patch_unit_brand(db,id)
    if err != None:
        updated_data = None 
    return updated_data, err

async def get_all_brands(db:Session):
    results,err = UnitBrandRepo.get_all_brands(db)
    