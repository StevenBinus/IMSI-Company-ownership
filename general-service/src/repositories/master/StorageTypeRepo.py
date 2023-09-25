from fastapi import Request
from sqlalchemy import select, column, join, func
from sqlalchemy.orm import load_only, joinedload, subqueryload, Bundle
from src.entities.master.StorageTypeEntity import MtrStorageType
from src.payloads.schemas.master.StorageTypeSchema import MtrStorageTypeRequest, MtrStorageTypeUpdateRequest
from datetime import datetime
import calendar
from src.configs.database import get_db
from src.utils.AddPagination import get_the_pagination,get_the_pagination_search_list
import math


def get_storage_type_list(page: int, limit: int, all_params: dict(), sort_params: dict()):
    db = get_db()
    try:
        query_set=select(MtrStorageType)
        counter = len(db.scalars(query_set).all())
        query_check = get_the_pagination_search_list(query_set,all_params,sort_params)
            
        if sort_params["sort_by"]==None or sort_params["sort_of"]==None:
                    query_check = query_check.order_by(MtrStorageType.storage_type_id.desc())
        else:
                    if sort_params["sort_by"]=="desc":
                        query_check = query_check.order_by(column(sort_params["sort_by"]).desc())
                    else:
                        query_check = query_check.order_by(column(sort_params["sort_by"]).asc())
        query_final=query_check.offset(page*limit).limit(limit)
                
        result = db.scalars(query_final).all()

        total_rows = counter
        total_pages = int(total_rows/limit)

        page_results = {
                    "total_rows" : total_rows,
                    "total_pages" : total_pages
                }
        return result, page_results, None
    except Exception as err:
         return None,None,err
    
def get_storage_type_by_id(id:int):
    db = get_db()
    try:
        check_query = select(MtrStorageType).where(MtrStorageType.storage_type_id==id)
        result = db.scalars(check_query).first()
        return result, None
    except Exception as err:
        return None, err
    
def patch_storage_type(id:int):
    db = get_db()
    try:
        check_active_status = select(MtrStorageType).where(MtrStorageType.storage_type_id==id)
        active_status = db.scalars(check_active_status).first()
        current_status = active_status.is_active
    
        if current_status == True:
            active_status.is_active = False
            db.commit()
            db.refresh(active_status)
            return active_status, None
        else:
            active_status.is_active = True
            db.commit()
            db.refresh(active_status)
            return active_status, None
    except Exception as err:
        db.rollback()
        return None, err
    
def update_storage_type(id:int, req:MtrStorageTypeUpdateRequest):
    db = get_db()
    check_data = select(MtrStorageType).where(MtrStorageType.storage_type_id == id)
    updated_data = db.scalars(check_data).first()
    try:
        updated_data.storage_type_name = req.storage_type_name
        db.commit()
        db.refresh(updated_data)
        return updated_data, None
    except Exception as err:
        db.rollback()
        return None, err
    
def post_storage_type(req:MtrStorageTypeRequest):
    db=get_db()
    try:
        db.begin()
        new_data=MtrStorageType()
        new_data.storage_type_code=req.storage_type_code
        new_data.storage_type_name=req.storage_type_name
        db.add(new_data)
        db.commit()
        db.refresh(new_data)
        return new_data,None
    except Exception as err:
        db.rollback
        return None,err