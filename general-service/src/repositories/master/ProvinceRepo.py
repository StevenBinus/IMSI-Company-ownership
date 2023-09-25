from sqlalchemy import select, column
from src.payloads.schemas.master import ProvinceSchema
from src.utils.AddPagination import get_the_pagination_search_list_with_join
from src.configs.database import get_db
from src.entities.master.CountryEntity import MtrCountry
from src.entities.master.ProvinceEntity import MtrProvince
import math
from sqlalchemy.orm import Session


async def get_provinces_cruds(db:Session, page:int,limit:int,all_params:dict(),sort_params:dict()):
    try:
        query_set = select(
            MtrProvince.is_active,
            MtrProvince.province_id,
            MtrProvince.province_code,
            MtrProvince.province_name,
            MtrProvince.country_id,
            MtrCountry.country_code,
            MtrCountry.country_name).join(
                MtrCountry,MtrProvince.country_id==MtrCountry.country_id
            )
        tables =[MtrProvince,MtrCountry]  
        query_check,counter = get_the_pagination_search_list_with_join(db,query_set,all_params,tables)

        if sort_params["sort_by"] == None or sort_params["sort_of"] == None:
            query_check = query_check.order_by(MtrProvince.province_id.desc())
        else:
            if sort_params["sort_of"] == "desc":
                query_check = query_check.order_by(column(sort_params["sort_by"]).desc())
            else:
                query_check = query_check.order_by(column(sort_params["sort_by"]).asc())

        query_final = query_check.offset(page*limit).limit(limit)
        data = db.execute(query_final).all()
        result=[]
        for is_active,province_id,province_code,province_name,country_id,country_code,country_name in data:
                go_out = {
                    "is_active":is_active,
                    "province_id": province_id,
                    "province_code": province_code,
                    "province_name": province_name,
                    "country_id":country_id,
                    "country_code":country_code,
                    "country_name":country_name}
                result.append(go_out)
        total_rows = counter
        total_pages = math.ceil(total_rows/limit)

        pages = {
            "total_rows" : total_rows,
            "total_pages" : total_pages
        }
        
        return result, pages, None
    except Exception as err:
        return None, None, err

async def get_province_cruds(id:int, db:Session):
    try:
        query_check=select(MtrProvince).where(MtrProvince.province_id==id)
        query_set=db.scalars(query_check).first()
        return query_set,None
    except Exception as err:
        return None, err

async def post_province_cruds(req:ProvinceSchema.MtrProvincePost, db:Session):
    try:
        db.begin()
        new_data = MtrProvince()
        new_data.province_code=req.province_code
        new_data.province_name=req.province_name
        new_data.country_id=req.country_id
        db.add(new_data)
        db.commit()
        db.refresh(new_data)
        return new_data,None
    except Exception as err:
        db.rollback()
        return None, err

async def delete_province(id:int, db:Session):
    try:
        query_check = select(MtrProvince).where(MtrProvince.province_id==id)
        query_set=db.scalars(query_check).first()
        db.delete(query_set)
        db.commit()
        return query_set,None
    except Exception as err:
        db.rollback()
        return None, err

async def put_province_cruds(id:int,req:ProvinceSchema.MtrProvincePost, db:Session):
    try:
        query_check=select(MtrProvince).where(MtrProvince.province_id==id)
        query_set=db.scalars(query_check).first()
        query_set.province_code=req.province_code
        query_set.province_name=req.province_name
        query_set.country_id=req.country_id
        db.commit()
        db.refresh(query_set)
        return query_set,None
    except Exception as err:
        db.rollback()
        return None, err


async def patch_province_cruds(id:int, db:Session):
    check_active=select(MtrProvince).where(MtrProvince.province_id==id)
    current_status=db.scalars(check_active).first()
    active=current_status.is_active
    try:
       if active==True:
           current_status.is_active=False
       else:
           current_status.is_active=True

       db.commit()
       db.refresh(current_status)

       return current_status, None
   
    except Exception as err:
       db.rollback
       return None, err