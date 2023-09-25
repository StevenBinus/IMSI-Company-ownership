from fastapi import Request
from sqlalchemy import select, column, join, func
from sqlalchemy.orm import load_only, joinedload, subqueryload, Bundle, Session
from src.entities.master.DivisionEntity import MtrDivision
from src.payloads.schemas.master.DivisionSchema import MtrDivisionRequest, MtrDivisionUpdateRequest
from datetime import datetime
import calendar
import math
from src.configs.database import get_db
from src.utils.AddPagination import get_the_pagination_search_list


async def get_division_list(db: Session, page:int, limit:int, all_params=dict(), sort_params=dict(), default_sort_value = any):
    try:
        #for pagination purposes
        query_set = select(MtrDivision)
        default_sort_value = MtrDivision.division_id
        query_check = get_the_pagination_search_list(query_set,all_params,sort_params,default_sort_value)   
        query_final = query_check.offset(page*limit).limit(limit)
        results = db.scalars(query_final).all()
        counter = len(results)
        total_rows=counter
        total_pages = math.ceil(total_rows/limit)
        page_results = {
            "total_rows" : total_rows,
            "total_pages" : total_pages
        }
        
        return results, page_results, None
    except Exception as err:
        return None, None, err
    
async def post_division(db: Session, req:MtrDivisionRequest):
    try:
        db.begin()
        _new_data = MtrDivision()
        _new_data.division_code = req.division_code
        _new_data.division_name = req.division_name
        db.add(_new_data)
        db.commit()
        db.refresh(_new_data)
        return _new_data, None
    except Exception as err:
        db.rollback()
        return None, err
    
async def get_division_by_id(db: Session,id:int):
    try:
        check_query = select(MtrDivision).where(MtrDivision.division_id==id)
        result = db.scalars(check_query).first()
        return result, None
    except Exception as err:
        return None, err
    
async def patch_division(db:Session,id:int):
    try:
        check_active_status = select(MtrDivision).where(MtrDivision.division_id==id)
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
    
async def update_division(db: Session, id:int, req:MtrDivisionUpdateRequest):
    check_data = select(MtrDivision).where(MtrDivision.division_id == id)
    updated_data = db.scalars(check_data).first()
    try:
        updated_data.division_name = req.division_name
        db.commit()
        db.refresh(updated_data)
        return updated_data, None
    except Exception as err:
        db.rollback()
        return None, err