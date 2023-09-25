from sqlalchemy.orm import Session
from sqlalchemy import select, column
from src.entities.master import ProvinceEntity, MtrCityEntity
from src.entities.master.DistrictEntity import MtrDistrict
from src.payloads.schemas.master import DistrictSchema
from src.utils.BoolConvert import strtobool
import math
from src.configs.database import get_db
from src.utils import AddPagination


def get_all_districts(page:int,limit:int,all_params:dict(),sort_params:dict()):
    db = get_db()
    try:
        query_set=select(
            MtrDistrict.is_active,
            MtrDistrict.district_code,
            MtrDistrict.district_name,
            MtrCityEntity.MtrCity.city_code,
            MtrCityEntity.MtrCity.city_name,
            ProvinceEntity.MtrProvince.province_code,
            ProvinceEntity.MtrProvince.province_name
            ).join(MtrCityEntity.MtrCity,
            MtrDistrict.city_id==MtrCityEntity.MtrCity.city_id
            ).join(ProvinceEntity.MtrProvince,
            MtrDistrict.province_id==ProvinceEntity.MtrProvince.province_id
            )
        tables = [MtrDistrict,MtrCityEntity.MtrCity,ProvinceEntity.MtrProvince]
        query_check,counter = AddPagination.get_the_pagination_search_list_with_join(db,query_set,all_params,tables)
        if sort_params["sort_by"] == None or sort_params["sort_of"] == None:
                query_check = query_check.order_by(MtrDistrict.district_id.desc())
        else:
                if sort_params["sort_of"] == "desc":
                    query_check = query_check.order_by(column(sort_params["sort_by"]).desc())
                else:
                    query_check = query_check.order_by(column(sort_params["sort_by"]).asc())

        query_final =  query_check.offset(page*limit).limit(limit)
        data = db.execute(query_final).all()
        total_rows = counter
        total_pages  = math.ceil(total_rows/limit)
        results=[]
        for is_active,district_code,district_name,city_code,city_name,province_code,province_name in data:
            result={
                "is_active":is_active,
                "district_code":district_code,
                "district_name":district_name,
                "city_code":city_code,
                "city_name":city_name,
                "province_code":province_code,
                "province_name":province_name}
            results.append(result)
        page_result = {
                "total_rows" : total_rows,
                "total_pages" : total_pages
        }
        return results, page_result, None
    except Exception as err:
        return None,None,err


def get_district_by_id(id:int):
    db=get_db()
    try:
        query_check=select(MtrDistrict).where(MtrDistrict.district_id==id)
        query_set=db.scalars(query_check).first()
        return query_set,None
    except Exception as err:
        return None,err
    

def post_district(req:DistrictSchema.MtrDistrict):
    db=get_db()
    try:
        db.begin()
        _new_data=MtrDistrict()
        _new_data.district_code=req.district_code
        _new_data.district_name=req.district_name
        _new_data.city_id=req.city_id
        _new_data.province_id=req.province_id
        db.add(_new_data)
        db.commit()
        db.refresh(_new_data)
        return _new_data,None
    except Exception as err:
        db.rollback()
        return None,err
    

def put_district(id:int,req:DistrictSchema.MtrDistrictUpdate):
    db=get_db()
    try:
        query_check=select(MtrDistrict).where(MtrDistrict.district_id==id)
        updated_data=db.scalars(query_check).first()
        updated_data.district_name=req.district_name
        db.commit()
        db.refresh(updated_data)
        return updated_data,None
    
    except Exception as err:
        return None,err

def delete_district(id:int):
    db=get_db()
    try:
        query_check=select(MtrDistrict).where(MtrDistrict.district_id==id)
        query_set=db.scalars(query_check).first()
        db.delete(query_set)
        db.commit()
        return query_set,None
    except Exception as err:
        db.rollback()
        return None, err

def patch_district(id:int):
    db=get_db()
    check_active=select(MtrDistrict).where(MtrDistrict.district_id==id)
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

    
