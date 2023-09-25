from src.repositories.master import ProvinceRepo
from src.payloads.schemas.master import ProvinceSchema
from sqlalchemy.orm import Session

async def get_provinces_all(db:Session, page:int, limit:int, get_all_params:dict(),sort_fields:dict()):
    get_data, pages, err = await ProvinceRepo.get_provinces_cruds(db, page,limit,get_all_params,sort_fields) 
    if err == None:
        return get_data, pages, None
    else:
        return None, None, err
    
async def get_province_cruds(id:int, db:Session):
    result, err = await ProvinceRepo.get_province_cruds(id, db)
    if err == None:
        return result, None
    else:
        return result, err
    
    
async def post_province_cruds(req:ProvinceSchema.MtrProvinceSchema, db:Session):
    created_data, err = await ProvinceRepo.post_province_cruds(req, db)
    if err == None:
        return created_data, None
    else:
        return None, err
    
async def patch_province_cruds(id:int, db:Session):
    updated_data, err = await ProvinceRepo.patch_province_cruds(id,db)
    if err == None:
        return updated_data, None
    else:
        return None, err
    
async def put_province(id:int,req:ProvinceSchema.MtrProvincePost, db:Session):
    update_data,err = await ProvinceRepo.put_province_cruds(id,req,db)
    if err == None:
        return update_data,None
    else:
        return None, err

async def delete_province(id:int, db:Session):
    delete_data, err = await ProvinceRepo.delete_province(id,db)
    if err == None:
        return delete_data, None
    else:
        return None, err