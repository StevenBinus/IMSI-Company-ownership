from sqlalchemy.orm import Session
from sqlalchemy import select, column
from src.utils.BoolConvert import strtobool
import math
from src.configs.database import get_db
from src.utils import AddPagination
from src.entities.master.CountryEntity import MtrCountry  
from src.payloads.schemas.master import CountrySchema

#get all data
def get_countries_cruds(page:int, limit:int, all_params:dict(),sort_params:dict()):
    db = get_db()
    try:
        query_set = select(MtrCountry)
        counter = len(db.scalars(query_set).all())
        query_check = AddPagination.get_the_pagination_search_list(query_set,all_params,sort_params)

        if sort_params["sort_by"] == None or sort_params["sort_of"] == None:
            query_check = query_check.order_by(MtrCountry.country_id.desc())
        else:
            if sort_params["sort_of"] == "desc":
                query_check = query_check.order_by(column(sort_params["sort_by"]).desc())
            else:
                query_check = query_check.order_by(column(sort_params["sort_by"]).asc())
        query_final =query_check.offset(page*limit).limit(limit)
        result = db.scalars(query_final).all()
        total_rows = counter
        total_page = math.ceil(total_rows/limit)

        page_results={
            "total_rows":total_rows,
            "total_pages":total_page
        }
 
        return result, page_results, None
    except Exception as err:
        return None,None,err


#get data by filtering the primary_key(ID)
def get_country_cruds(id:int):
    db = get_db()
    try:
        query_check = select(MtrCountry).where(MtrCountry.country_id==id)
        query_set = db.scalars(query_check).first()
        return query_set,None
    except Exception as err:
        return None, err

#post / create new data
def post_country_cruds(req:CountrySchema.MtrCountryRequest):
    db=get_db()
    try:
        db.begin()
        new_data = MtrCountry()
        new_data.country_code=req.country_code
        new_data.country_name=req.country_name
        new_data.country_language=req.country_language
        new_data.country_phone = req.country_phone
        new_data.currency_id=req.currency_id
        db.add(new_data)
        db.commit()
        db.refresh(new_data)
        return new_data,None
    except Exception as err:
        db.rollback()
        return None,err

#delete data by primary_key(ID)
def delete_country_cruds(id:int):
    db=get_db()
    try:
        
        query_check = select(MtrCountry).where(MtrCountry.country_id==id)
        query_set = db.scalars(query_check).first()
        db.delete(query_set)
        db.commit()
        return query_set,None
    except Exception as err:
        db.rollback()
        return None, err
    
def put_country_cruds(id:int,req:CountrySchema.MtrCountryRequest):
    db = get_db()
    try:
        query_check = select(MtrCountry).where(MtrCountry.country_id==id)
        update_data = db.scalars(query_check).first()
        update_data.country_code=req.country_code
        update_data.country_name=req.country_name
        update_data.country_language=req.country_language
        update_data.country_phone=req.country_phone
        update_data.currency_id=req.currency_id
        db.commit()
        db.refresh(update_data)
        return update_data,None
    except Exception as err:
        db.rollback()
        return None, err



def patch_country_cruds(id:int):
    db=get_db()
    check_active=select(MtrCountry).where(MtrCountry.country_id==id)
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
