from fastapi import Request
from sqlalchemy import select, column
from src.entities.common.AdjustmentReasonEntity import MtrAdjustmentReason
from src.payloads.schemas.common import AdjustmentReasonSchema
from src.configs.database import get_db
from src.utils.AddPagination import get_the_pagination_search_list
import math

def get_all_adjustment_reasons(page:int, limit:int, all_params:dict(),sort_params:dict()):
    db = get_db()
    try:
        #for pagination purposes
        query_set = select(MtrAdjustmentReason)
        counter =len(db.scalars(query_set).all())
        query_check = get_the_pagination_search_list(MtrAdjustmentReason,all_params,sort_params)   
        query_final = query_check.order_by(MtrAdjustmentReason.adjustment_reason_id).offset(page*limit).limit(limit)

        results = db.scalars(query_final).all()

        total_rows = counter
        total_pages = math.ceil(total_rows/limit)
        page_results = {
            "total_rows" : total_rows,
            "total_pages" : total_pages
        }
        
        return results, page_results, None
    except Exception as err:
        return None, None, err
    

def get_by_id_adjustment_reason(id: int):
    db = get_db()
    try:
        check_query = select(MtrAdjustmentReason).where(MtrAdjustmentReason.adjustment_reason_id==id)
        result = db.scalars(check_query).first()
        return result, None
    except Exception as err:
        return None, err
    
def post_adjustment_reason(req:MtrAdjustmentReason):
    db = get_db()
    try:
        db.begin()
        _new_data = MtrAdjustmentReason()
        _new_data.adjustment_reason_code = req.adjustment_reason_code
        _new_data.adjustment_reason_name = req.adjustment_reason_name
        db.add(_new_data)
        db.commit()


        db.refresh(_new_data)
        return _new_data, None
    except Exception as err:

        db.rollback()
        return None, err



def put_adjustment_reason(id:int, req:AdjustmentReasonSchema.MtrAdjustmentReasonGetSchema):
    db = get_db()
    try:
        query_check = select(MtrAdjustmentReason).where(MtrAdjustmentReason.adjustment_reason_id==id)
        updated_data = db.scalars(query_check).first()
        updated_data.adjustment_reason_code = req.adjustment_reason_code
        updated_data.adjustment_reason_name = req.adjustment_reason_name
        db.commit()
        db.refresh(updated_data)
        return updated_data, None
    
    except Exception as err:
        db.rollback()
        return None, err
    
def delete_adjustment_reason(id:int):
    db = get_db()
    try:
        query_check = select(MtrAdjustmentReason).where(MtrAdjustmentReason.adjustment_reason_id==id)
        erase_data = db.scalars(query_check).first()

        db.delete(erase_data)
        db.commit()

        return erase_data, None
    except Exception as err:
        db.rollback()
        return None, err    

def patch_adjustment_reason(id:int):
    db = get_db()
    check_active_status = select(MtrAdjustmentReason).where(MtrAdjustmentReason.adjustment_reason_id==id)
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