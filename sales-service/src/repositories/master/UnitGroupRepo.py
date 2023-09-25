from sqlalchemy import select,column
from sqlalchemy.orm import load_only, Session
from src.entities.master.UnitGroupEntity import MtrUnitGroup
from src.payloads.schemas.master import UnitGroupSchema
from src.utils.AddPagination import get_the_pagination_search_list
from src.utils.Activation import activation
import math

async def get_unit_group_all(db:Session,page:int, limit:int, all_param:dict(), sort_params:dict()):
    if page <= 0:
        page = 1
    try:
        #for pagination purposes
        query_init = select(MtrUnitGroup)
        query_check, counter = await get_the_pagination_search_list(db,query_init,all_param)   
        if sort_params["sort_by"] == None or sort_params["sort_of"] == None:
            query_check = query_check.order_by(MtrUnitGroup.unit_group_id.desc())
        else:
            if sort_params["sort_of"] == "desc":
                query_check = query_check.order_by(column(sort_params["sort_by"]).desc())
            else:
                query_check = query_check.order_by(column(sort_params["sort_by"]).asc())
                
        query_final = query_check.offset((page*limit)-limit).limit(limit).options(load_only(
            MtrUnitGroup.unit_group_code,
            MtrUnitGroup.unit_group_name,
            MtrUnitGroup.is_active
        ))
        results = db.scalars(query_final).all()

        total_rows = len(results)
        total_pages  = math.ceil(counter/limit)

        page_results = {
            "total_rows" : total_rows,
            "total_pages" : total_pages
        }
        
        return results, page_results, None
    except Exception as err:
        return None, None, err
    
async def get_unit_group_by_id(db:Session,id:int):
    try:
        query_check = select(MtrUnitGroup).where(MtrUnitGroup.unit_group_id==id)
        result = db.scalars(query_check).first()
        return result, None
    except Exception as err:
        return None, err
    
async def post_unit_group(db:Session, req:UnitGroupSchema.UnitGroupRequest):
    try:
        db.begin()
        created_data = MtrUnitGroup()
        created_data.unit_group_code = req.unit_group_code
        created_data.unit_group_name = req.unit_group_name
        db.add(created_data)
        db.commit()
        db.refresh(created_data)
        return created_data, None
    except Exception as err:
        db.rollback()
        return None, err

async def update_unit_group(db:Session, id:int, req:UnitGroupSchema.UnitGroupSchema):
    try:
        query_check = select(MtrUnitGroup).where(MtrUnitGroup.unit_group_id==id)
        updated_data = db.scalars(query_check).first()
        updated_data.unit_group_code = req.unit_group_code
        updated_data.unit_group_name = req.unit_group_name
        db.commit()
        db.refresh(updated_data)
        return updated_data, None
    except Exception as err:
        db.rollback()
        return None, err
    
async def patch_unit_group_status(db:Session,id:int):
    try:
        db.begin()
        query_activate = select(MtrUnitGroup).where(MtrUnitGroup.unit_group_id==id)
        activation_status = activation(db,query_activate)
        return activation_status, None
    except Exception as err:
        db.rollback()
        return None, err
