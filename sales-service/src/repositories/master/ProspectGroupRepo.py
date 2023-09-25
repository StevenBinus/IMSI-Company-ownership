from sqlalchemy import select
from sqlalchemy.orm import Session
from src.entities.master.ProspectGroupEntity import MtrProspectGroup
from src.payloads.schemas.master.ProspectGroupSchema import ProspectGroupRequest
import math


async def get_prospect_group_all(db:Session, page: int, limit: int):
    try:
        query_set = select(MtrProspectGroup)
        total_data = len(db.scalars(query_set).all())
        query_final = query_set.order_by(MtrProspectGroup.prospect_group_id).offset(page * limit).limit(limit)
        
        results = db.scalars(query_final).all()

        total_rows = len(results)
        total_pages = math.ceil(total_data/ limit)

        page_results = {"total_rows": total_rows, "total_pages": total_pages}
        return results, page_results, None

    except Exception as err:
        return None, None, err


async def get_prospect_group_by_id(db:Session, id: int):
    try:
        check_query = select(MtrProspectGroup).where(
            MtrProspectGroup.prospect_group_id == id
        )
        result = db.scalars(check_query).first()
        return result, None
    except Exception as err:
        return None, err


async def post_prospect_group(db:Session, req: ProspectGroupRequest):
    try:
        db.begin()
        _new_data = MtrProspectGroup()
        _new_data.prospect_group_code = req.prospect_group_code
        _new_data.prospect_group_name = req.prospect_group_name
        db.add(_new_data)
        db.commit()
        db.refresh(_new_data)
        return _new_data, None
    except Exception as err:
        db.rollback()
        return None, err


async def put_prospect_group(db:Session, id: int, req: ProspectGroupRequest):
    try:
        query_check = select(MtrProspectGroup).where(
            MtrProspectGroup.prospect_group_id == id
        )
        update_data = db.scalars(query_check).first()
        update_data.prospect_group_code = req.prospect_group_code
        update_data.prospect_group_name = req.prospect_group_name
        db.commit()
        db.refresh(update_data)
        return update_data, None

    except Exception as err:
        db.rollback()
        return None, err