from fastapi import Request
from sqlalchemy import select, column
from src.entities.common.ClosingCheckTypeEntity import MtrClosingCheckType
from src.payloads.schemas.common import ClosingCheckTypeSchema
from src.configs.database import get_db
from src.utils.AddPagination import get_the_pagination

def get_all_closing_check_types(page:int, limit:int, query_of:list[str], query_by:list[str]):
    db = get_db()
    
    
    try:
        total_rows = db.query(MtrClosingCheckType).count()
        total_pages  = int(total_rows/limit)

        #for pagination purposes
        query_check = get_the_pagination(MtrClosingCheckType,query_of,query_by)   
        query_final = query_check.order_by(MtrClosingCheckType.closing_check_type_id).offset(page*limit).limit(limit)

        results = db.scalars(query_final).all()

        page_results = {
            "total_rows" : total_rows,
            "total_pages" : total_pages
        }
        
        return results, page_results, None
    except Exception as err:
        return None, None, err
    

def get_by_id_closing_check_type(id: int):
    db = get_db()
    try:
        check_query = select(MtrClosingCheckType).where(MtrClosingCheckType.closing_check_type_id==id)
        result = db.scalars(check_query).first()
        return result, None
    except Exception as err:
        return None, err
    
def post_closing_check_type(req:MtrClosingCheckType):
    db = get_db()
    try:
        db.begin()
        _new_data = MtrClosingCheckType()
        _new_data.closing_check_type_code = req.closing_check_type_code
        _new_data.closing_check_type_description = req.closing_check_type_description
        db.add(_new_data)
        db.commit()


        db.refresh(_new_data)
        return _new_data, None
    except Exception as err:

        db.rollback()
        return None, err



def put_closing_check_type(id:int, req:ClosingCheckTypeSchema.MtrClosingCheckTypeGetSchema):
    db = get_db()
    try:
        query_check = select(MtrClosingCheckType).where(MtrClosingCheckType.closing_check_type_id==id)
        updated_data = db.scalars(query_check).first()
        updated_data.closing_check_type_code = req.closing_check_type_code
        updated_data.closing_check_type_description = req.closing_check_type_description
        db.commit()
        db.refresh(updated_data)
        return updated_data, None
    
    except Exception as err:
        db.rollback()
        return None, err
    
def delete_closing_check_type(id:int):
    db = get_db()
    try:
        query_check = select(MtrClosingCheckType).where(MtrClosingCheckType.closing_check_type_id==id)
        erase_data = db.scalars(query_check).first()

        db.delete(erase_data)
        db.commit()

        return erase_data, None
    except Exception as err:
        db.rollback()
        return None, err    

def patch_closing_check_type(id:int):
    db = get_db()
    check_active_status = select(MtrClosingCheckType).where(MtrClosingCheckType.closing_check_type_id==id)
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