from sqlalchemy.orm import Session
from sqlalchemy import select, column
from src.entities.master import VillageEntity, DistrictEntity,MtrCityEntity,ProvinceEntity
from src.entities.master.VillageEntity import MtrVillage
from src.payloads.schemas.master.VillageSchema import MtrVillageGetSchema,MtrVillagePost
from src.utils.BoolConvert import strtobool
import math
from src.configs.database import get_db
from src.utils import AddPagination

def get_all_villages(page:int,limit:int, all_params:dict(), sort_params:dict()):
    db = get_db()
    try:
        query_set = select(
            MtrVillage.is_active,
            MtrVillage.village_id,
            MtrVillage.village_code,
            MtrVillage.village_name,
            MtrVillage.village_zip_code,
            MtrVillage.district_id,
            DistrictEntity.MtrDistrict.district_name,
            DistrictEntity.MtrDistrict.city_id,
            MtrCityEntity.MtrCity.city_name,
            MtrCityEntity.MtrCity.city_phone_area,
            MtrCityEntity.MtrCity.province_id,
            ProvinceEntity.MtrProvince.province_name
            ).join(
            DistrictEntity.MtrDistrict, DistrictEntity.MtrDistrict.district_id==MtrVillage.district_id
            ).join(
            MtrCityEntity.MtrCity,MtrCityEntity.MtrCity.city_id==DistrictEntity.MtrDistrict.district_id
            ).join(
            ProvinceEntity.MtrProvince,ProvinceEntity.MtrProvince.province_id==MtrCityEntity.MtrCity.city_id
            )
        counter = len(db.scalars(query_set).all())
        query_check = AddPagination.get_the_pagination_search_list(db,query_set,all_params)

        if sort_params["sort_by"] == None or sort_params["sort_of"] == None:
            query_check = query_check.order_by(MtrVillage.village_id.desc())
        else:
            if sort_params["sort_of"] == "desc":
                query_check = query_check.order_by(column(sort_params["sort_by"]).desc())
            else:
                query_check = query_check.order_by(column(sort_params["sort_by"]).asc())

        query_final = query_check.order_by(MtrVillage.village_id).offset(page*limit).limit(limit)
    
        data = db.execute(query_final).all()

        total_rows = counter
        total_pages=int(total_rows/limit)

        results=[]
        for is_active,village_id,village_code,village_name,village_zip_code,district_id,district_name,city_name,province_name,city_phone_area in data:
                go_out = {
                    "is_active":is_active,
                    "village_id": village_id,
                    "village_code": village_code,
                    "village_name": village_name,
                    "village_zip_code": village_zip_code,
                    "district_id": district_id,
                    "district_name":district_name,
                    "city_name":city_name,
                    "province_name":province_name,
                    "phone_area":city_phone_area}
                results.append(go_out)
        page_results = {
                "total_rows" : total_rows,
                "total_pages" : total_pages
            }
        return results,page_results,None
    except Exception as err:
        return None, None, err
   
def get_village(id:int):
    db = get_db()
    try:
        check_query=select(MtrVillage).where(MtrVillage.village_id==id)
        result = db.scalars(check_query).first()
        return result, None
    except Exception as err:
        return None,err


def post_village(req:MtrVillagePost):
    db=get_db()
    try:
        db.begin()
        _new_data=MtrVillage()
        _new_data.village_code=req.village_code
        _new_data.village_name=req.village_name
        _new_data.village_zip_code=req.village_zip_code
        _new_data.district_id=req.district_id
        db.add(_new_data)
        db.commit() 


        db.refresh(_new_data)
        return _new_data,None
    except Exception as err:

        db.rollback()
        return None, err

def delete_village(id:int):
    db=get_db()
    try:
        check_query=select(MtrVillage).where(MtrVillage.village_id==id)
        result = db.scalars(check_query).first()
        db.delete(result)
        db.commit()
        return result, None

    except Exception as err:
        db.rollback()
        return None,err


def put_village(id:int, req:MtrVillageGetSchema):
    db =get_db()
    try:
        query_check=select(MtrVillage).where(MtrVillage.village_id==id)
        update_data=db.scalars(query_check).first()
        update_data.village_name=req.village_code
        update_data.village_name=req.village_name
        db.commit()
        db.refresh(update_data)
        return update_data,None

    except Exception as err:
        return None, err

def patch_village(id:int):
   db = get_db()
   check_active=select(MtrVillage).where(MtrVillage.village_id==id)
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
       
