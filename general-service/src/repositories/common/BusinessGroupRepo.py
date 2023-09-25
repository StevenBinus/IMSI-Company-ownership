from fastapi import Request
from sqlalchemy import select, column
from src.entities.common.BusinessGroupEntity import MtrBusinessGroup
from src.payloads.schemas.common import BusinessGroupSchema
from src.configs.database import get_db
from src.utils.AddPagination import get_the_pagination

def get_all_business_groups(page:int, limit:int, query_of:list[str], query_by:list[str]):
    db = get_db()
    
    
    try:
        total_rows = db.query(MtrBusinessGroup).count()
        total_pages  = int(total_rows/limit)

        #for pagination purposes
        query_check = get_the_pagination(MtrBusinessGroup,query_of,query_by)   
        query_final = query_check.order_by(MtrBusinessGroup.business_group_id).offset(page*limit).limit(limit)

        results = db.scalars(query_final).all()

        page_results = {
            "total_rows" : total_rows,
            "total_pages" : total_pages
        }
        
        return results, page_results, None
    except Exception as err:
        return None, None, err
    

def get_by_id_business_group(id: int):
    db = get_db()
    try:
        check_query = select(MtrBusinessGroup).where(MtrBusinessGroup.business_group_id==id)
        result = db.scalars(check_query).first()
        return result, None
    except Exception as err:
        return None, err
    
def post_business_group(req:MtrBusinessGroup):
    db = get_db()
    try:
        db.begin()
        _new_data = MtrBusinessGroup()
        _new_data.business_group_code = req.business_group_code
        _new_data.business_group_name = req.business_group_name
        db.add(_new_data)
        db.commit()


        db.refresh(_new_data)
        return _new_data, None
    except Exception as err:

        db.rollback()
        return None, err



def put_business_group(id:int, req:BusinessGroupSchema.MtrBusinessGroupGetSchema):
    db = get_db()
    try:
        query_check = select(MtrBusinessGroup).where(MtrBusinessGroup.business_group_id==id)
        updated_data = db.scalars(query_check).first()
        updated_data.business_group_code = req.business_group_code
        updated_data.business_group_name = req.business_group_name
        db.commit()
        db.refresh(updated_data)
        return updated_data, None
    
    except Exception as err:
        db.rollback()
        return None, err
    
def delete_business_group(id:int):
    db = get_db()
    try:
        query_check = select(MtrBusinessGroup).where(MtrBusinessGroup.business_group_id==id)
        erase_data = db.scalars(query_check).first()

        db.delete(erase_data)
        db.commit()

        return erase_data, None
    except Exception as err:
        db.rollback()
        return None, err    

def patch_business_group(id:int):
    db = get_db()
    check_active_status = select(MtrBusinessGroup).where(MtrBusinessGroup.business_group_id==id)
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