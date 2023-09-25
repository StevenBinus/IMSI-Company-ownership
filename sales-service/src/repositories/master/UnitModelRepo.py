from sqlalchemy.orm import Session, load_only
from sqlalchemy import select, column
from sqlalchemy.orm import load_only
from src.entities.master.UnitModelEntity import MtrUnitModel
from src.payloads.schemas.master.UnitModelSchema import MtrUnitModelRequest
from src.utils.AddPagination import get_the_pagination_search_list
from src.utils.Activation import activation
import math

async def get_unit_model_list_all(db:Session,page:int, limit:int, all_params=dict(), sort_params=dict()):
    if page <= 0:
        page = 1
    try:
        query_set = select(MtrUnitModel)
        #for pagination purposes
        query_check,counter = await get_the_pagination_search_list(db,query_set,all_params)

        #for sorting purpose
        if sort_params["sort_by"] == None or sort_params["sort_of"] == None:
            query_check = query_check.order_by(MtrUnitModel.model_id.desc())
        else:
            if sort_params["sort_of"] == "desc":
                query_check = query_check.order_by(column(sort_params["sort_by"]).desc())
            else:
                query_check = query_check.order_by(column(sort_params["sort_by"]).asc())

        query_final = query_check.offset((page*limit)-limit).limit(limit)
        results = db.scalars(query_final).all()

        total_rows = len(results)
        total_pages = math.ceil(counter/limit)

        page_results = {
            "total_rows" : total_rows,
            "total_pages" : total_pages
        }
        
        return results, page_results, None
    except Exception as err:
        return None, None, err

async def get_unit_model_drop_down(db:Session, brand_id:int):
    try:
        query = select(MtrUnitModel).options(load_only(MtrUnitModel.model_description, MtrUnitModel.model_id)).where(MtrUnitModel.vehicle_brand_id==brand_id)
        result = db.scalars(query).all()
        return result, None
    except Exception as err:
        return None, err
    
async def get_unit_model_by_id(db:Session,id:int):
    try:
        query_check = select(MtrUnitModel).where(MtrUnitModel.model_id==id)
        result = db.scalars(query_check).first()
        return result, None
    except Exception as err:
        return None, err
    
async def post_unit_model(db:Session,req:MtrUnitModelRequest):
    try:
        db.begin()
        created_data = MtrUnitModel()
        created_data.vehicle_brand_id = req.vehicle_brand_id
        created_data.model_code = req.model_code
        created_data.model_description = req.model_description
        created_data.unit_group_id = req.unit_group_id
        created_data.discontinue_date = req.discontinue_date
        created_data.sales_allow = req.sales_allow
        created_data.indent_indicator = req.indent_indicator
        created_data.warranty_expired_year = req.warranty_expired_year
        created_data.warranty_expired_mileage = req.warranty_expired_mileage
        created_data.free_service_expired_month = req.free_service_expired_month
        created_data.free_service_expired_mileage = req.free_service_expired_mileage
        db.add(created_data)
        db.commit()
        db.refresh(created_data)
        return created_data, None
    except Exception as err:
        db.rollback()
        return None, err
    
async def patch_unit_model(db:Session,id:int):
    try:
        db.begin()
        query_activate = select(MtrUnitModel).where(MtrUnitModel.model_id==id)
        activation_status = activation(db,query_activate)
        return activation_status, None
    except Exception as err:
        db.rollback()
        return None, err

async def get_all_model(db:Session,id:int):
    try:
        query_all = select(MtrUnitModel).where(MtrUnitModel.vehicle_brand_id==id).options(load_only(MtrUnitModel.model_description))
        results = db.scalars(query_all).all()
        return results,None
    except Exception as err:
        return None, err