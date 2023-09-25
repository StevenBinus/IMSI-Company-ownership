from fastapi import Request
from sqlalchemy import select, column
from src.entities.common.AccessoriesTypeEntity import MtrAccessoriesType
from src.payloads.schemas.common import AccessoriesTypeSchema
from src.configs.database import get_db
from src.utils.AddPagination import get_the_pagination_search_list
import math

def get_all_accessories_types(page:int, limit:int, all_params=dict(), sort_params=dict()):
    db = get_db()
    try:
        #for pagination purposes
        query_set = select(MtrAccessoriesType)
        counter = len(db.scalars(MtrAccessoriesType).all())
        query_check = get_the_pagination_search_list(query_set,all_params,sort_params)   
        if sort_params["sort_by"]==None or sort_params["sort_of"]==None:
            query_check=query_check.order_by(MtrAccessoriesType.accessories_type_id.desc())
        else:
            if sort_params["sort_of"] == "desc":
                query_check = query_check.order_by(MtrAccessoriesType.accessories_type_id.desc())
            else:
                query_check = query_check.order_by(MtrAccessoriesType.accessories_type_id.asc())
        query_final = query_check.offset(page*limit).limit(limit)
        results = db.scalars(query_final).all()
        total_rows=counter
        total_pages = math.ceil(total_rows/limit)
        page_results = {
            "total_rows" : total_rows,
            "total_pages" : total_pages
        }
        
        return results, page_results, None
    except Exception as err:
        return None, None, err
    

def get_by_id_accessories_type(id: int):
    db = get_db()
    try:
        check_query = select(MtrAccessoriesType).where(MtrAccessoriesType.accessories_type_id==id)
        result = db.scalars(check_query).first()
        return result, None
    except Exception as err:
        return None, err
    
def post_accessories_type(req:MtrAccessoriesType):
    db = get_db()
    try:
        db.begin()
        _new_data = MtrAccessoriesType()
        _new_data.accessories_type_code = req.accessories_type_code
        _new_data.accessories_type_description = req.accessories_type_description
        db.add(_new_data)
        db.commit()

  

        db.refresh(_new_data)
        return _new_data, None
    except Exception as err:

        db.rollback()
        return None, err



def put_accessories_type(id:int, req:AccessoriesTypeSchema.MtrAccessoriesTypeGetSchema):
    db = get_db()
    try:
        query_check = select(MtrAccessoriesType).where(MtrAccessoriesType.accessories_type_id==id)
        updated_data = db.scalars(query_check).first()
        updated_data.accessories_type_code = req.accessories_type_code
        updated_data.accessories_type_description = req.accessories_type_description
        db.commit()
        db.refresh(updated_data)
        return updated_data, None
    
    except Exception as err:
        db.rollback()
        return None, err
    
def delete_accessories_type(id:int):
    db = get_db()
    try:
        query_check = select(MtrAccessoriesType).where(MtrAccessoriesType.accessories_type_id==id)
        erase_data = db.scalars(query_check).first()

        db.delete(erase_data)
        db.commit()

        return erase_data, None
    except Exception as err:
        db.rollback()
        return None, err    

def patch_accessories_type(id:int):
    db = get_db()
    check_active_status = select(MtrAccessoriesType).where(MtrAccessoriesType.accessories_type_id==id)
    active_status = db.scalars(check_active_status).first()
    current_status = active_status.is_active
    try:
        if current_status == True:
            active_status.is_active = False
        else :
            active_status.is_active = True
            
        db.commit()
        db.refresh(active_status)

        return active_status, None


    except Exception as err:
        db.rollback()
        return None, err