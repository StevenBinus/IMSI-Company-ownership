from sqlalchemy.orm import Session
from sqlalchemy import select, column
from src.entities.master import ProvinceEntity
from src.entities.master.MtrCityEntity import MtrCity
from src.payloads.schemas.master.CitySchema import MtrCitySchemaByList,MtrCityUpdate
from src.utils.BoolConvert import strtobool
import math
from src.configs.database import get_db
from src.utils import AddPagination

async def get_all_cities(db: Session, page:int,limit:int, all_params:dict(), sort_params:dict()):
    try:
        query_set = select(
            MtrCity.is_active,
            MtrCity.city_code,
            MtrCity.city_name,
            ProvinceEntity.MtrProvince.province_code,
            ProvinceEntity.MtrProvince.province_name
            ).join( ProvinceEntity.MtrProvince, MtrCity.province_id==ProvinceEntity.MtrProvince.province_id)
        tables=[
            MtrCity,ProvinceEntity.MtrProvince
        ]
        query_check,counter = AddPagination.get_the_pagination_search_list_with_join(db,query_set,all_params,tables)

        if sort_params["sort_by"]==None or sort_params["sort_of"]==None:
            query_check=query_check.order_by(MtrCity.city_id.desc())
        else:
            if sort_params["sort_of"] == "desc":
                query_check = query_check.order_by(column(sort_params["sort_by"]).desc())
            else:
                query_check = query_check.order_by(column(sort_params["sort_by"]).asc())

        query_final = query_check.offset(page*limit).limit(limit)
    
        data = db.execute(query_final).all()

        total_rows = counter
        total_pages=math.ceil(total_rows/limit)

        results=[]
        for is_active,city_code,city_name,province_code,province_name in data:
                go_out = {
                    "is_active":is_active,
                    "city_code": city_code,
                    "city_name": city_name,
                    "province_code": province_code,
                    "province_name":province_name}
                results.append(go_out)
        page_results = {
                "total_pages" : total_pages,
                "total_rows" : total_rows
            }
        print(total_pages,total_rows,limit)
        return results,page_results,None
    except Exception as err:
        return None, None, err
   
async def get_city(db: Session, id:int):
    try:
        check_query=select(MtrCity).where(MtrCity.city_id==id)
        result = db.scalars(check_query).first()
        return result, None
    except Exception as err:
        return None,err


async def post_city(db: Session, req:MtrCitySchemaByList):
    try:
        db.begin()
        _new_data=MtrCity()
        _new_data.city_code=req.city_code
        _new_data.city_name=req.city_name
        _new_data.city_phone_area=req.city_phone_area
        _new_data.province_id=req.province_id
        db.add(_new_data)
        db.commit() 


        db.refresh(_new_data)
        return _new_data,None
    except Exception as err:

        db.rollback()
        return None, err

async def delete_city(db: Session, id:int):
    try:
        check_query=select(MtrCity).where(MtrCity.city_id==id)
        result = db.scalars(check_query).first()
        db.delete(result)
        db.commit()
        return result, None
    except Exception as err:
        db.rollback()
        return None,err


async def put_city(db: Session, id:int, req:MtrCityUpdate):
    try:
        query_check=select(MtrCity).where(MtrCity.city_id==id)
        update_data=db.scalars(query_check).first()
        update_data.city_name=req.city_name
        update_data.city_phone_number=req.city_phone_area
        db.commit()
        db.refresh(update_data)
        return update_data,None

    except Exception as err:
        return None, err

async def patch_city(db: Session, id:int):
   try:
        check_active=select(MtrCity).where(MtrCity.city_id==id)
        current_status=db.scalars(check_active).first()
        active=current_status.is_active
   
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
       
