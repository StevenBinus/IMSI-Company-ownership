from src.repositories.master import CityRepo
from src.payloads.schemas.master.CitySchema import MtrCitySchemaByList
from fastapi import Request
from sqlalchemy.orm import Session

async def get_all_cities(db: Session, page:int, limit:int, all_params:dict(),sort_params:dict()):
    get_data, page_results, err = await CityRepo.get_all_cities(db, page,limit,all_params,sort_params) 
    if err == None:
        return get_data, page_results, None
    else:
        return None, None, err
    
async def get_city(db: Session, id:int):
    result, err = await CityRepo.get_city(db, id)
    if err == None:
        return result, None
    else:
        return result, err
    
async def post_city(db: Session, req:MtrCitySchemaByList):
    created_data, err = await CityRepo.post_city(db, req)
    if err == None:
        return created_data, None
    else:
        return None, err
    
async def patch_City(db: Session, id:int):
    updated_data, err = await CityRepo.patch_city(db, id)
    if err == None:
        return updated_data, None
    else:
        return None, err
    
async def put_city(db: Session, id:int,req:MtrCitySchemaByList):
    updated_data, err = await CityRepo.put_city(db, id,req)
    if err == None:
        return updated_data, None
    else:
        return None, err
    
async def delete_city(db: Session, id:int):
    erase_data, err = await CityRepo.delete_city(db, id)
    if err == None:
        return erase_data, None
    else:
        return None, err