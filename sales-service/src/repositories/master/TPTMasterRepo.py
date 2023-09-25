from fastapi import Request
from sqlalchemy import select, column
from src.entities.master.TPTEntity import MtrTPT
from src.entities.master.TPTChassisEntity import MtrTPTChassis
from src.payloads.schemas.master.TPTMasterSchema import MtrTPTRequest, MtrTPTChassisRequest
from src.configs.database import get_db
from src.utils.AddPagination import get_the_pagination

def get_tpt_master_all(page:int, limit:int, query_of:list[str], query_by:list[str]):
    db = get_db()
    try:
        total_rows = db.query(MtrTPT).count()
        total_pages  = int(total_rows/limit)

        #for pagination purposes
        query_check = get_the_pagination(MtrTPT,query_of,query_by)   
        query_final = query_check.order_by(MtrTPT.tpt_id).offset(page*limit).limit(limit)
        results = db.scalars(query_final).all()

        page_results = {
            "total_rows" : total_rows,
            "total_pages" : total_pages
        }
        
        return results, page_results, None
    except Exception as err:
        return None, None, err
    

def get_tpt_master_by_id(id: int):
    db = get_db()
    try:
        check_query = select(MtrTPT).where(MtrTPT.tpt_id==id)
        result = db.scalars(check_query).first()
        return result, None
    except Exception as err:
        return None, err
    
def post_tpt_master(req:MtrTPTRequest, request:Request):
    db = request.state.db
    try:
        db.begin()
        _new_data = MtrTPT()
        _new_data.tpt_type = req.tpt_type
        _new_data.tpt_quota = req.tpt_quota
        _new_data.tpt_remaining = req.tpt_remaining
        _new_data.tpt_used = req.tpt_used
        _new_data.tpt_status = req.tpt_status
        _new_data.unit_variant_id = req.unit_variant_id
        db.add(_new_data)
        db.commit()

        # post_data_detail(idheader)
        # _new_data.tpt_id

        db.refresh(_new_data)
        return _new_data, None
    except Exception as err:
        db.rollback()
        return None, err

def post_data_tpt_chassis(req: MtrTPTChassisRequest):
    new_detail = MtrTPTChassis()
    new_detail.tpt_id = req.tpt_id
    new_detail.vehicle_id = req.vehicle_id
    new_detail.chassis_no_status = req.chassis_no_status
    return new_detail


def get_tpt_chassis(id: int):
    db = get_db()
    try:
        check_query = select(MtrTPTChassis).where(MtrTPTChassis.tpt_id==id)
        result = db.scalars(check_query).all()
        return result, None
    except Exception as err:
        return None, err

def patch_tpt_chassis(id: int, request: Request):
    db = request.state.db
    check_active_chassis_status = select(MtrTPTChassis).where(MtrTPTChassis.tpt_chassis_id==id)
    active_chassis_status = db.scalars(check_active_chassis_status).first()
    current_status = active_chassis_status.chassis_no_status
    try:
        if current_status != "D":
            active_chassis_status.chassis_no_status = "D"
            db.commit()
            db.refresh(active_chassis_status)
            return active_chassis_status, None
    except Exception as err:
        db.rollback()
        return None, err