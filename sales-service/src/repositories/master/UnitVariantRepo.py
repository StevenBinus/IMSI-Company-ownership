from sqlalchemy.orm import Session, load_only
from sqlalchemy import select, column
from sqlalchemy.orm import load_only
from src.entities.master.UnitVariantEntity import MtrUnitVariant
from src.entities.master.UnitModelEntity import MtrUnitModel
from src.payloads.schemas.master.UnitVariantSchema import UnitVariantRequest
from src.utils.AddPagination import get_the_pagination_search_list
from src.utils.Activation import activation
import math

async def get_unit_variants_list_all(db:Session,page:int, limit:int, all_params=dict(), sort_params=dict()):
    if page <= 0:
        page = 1
    try:
        query_set = select(MtrUnitVariant.variant_id,
                           MtrUnitVariant.variant_code,
                           MtrUnitVariant.variant_description,
                           MtrUnitModel.model_code,
                           MtrUnitModel.model_description,
                           MtrUnitVariant.is_active).join(MtrUnitModel,MtrUnitModel.model_id==MtrUnitVariant.model_id)
        query_check,counter = await get_the_pagination_search_list(db,query_set,all_params)
        #for pagination purposes
        if sort_params["sort_by"] == None or sort_params["sort_of"] == None:
            query_check = query_check.order_by(MtrUnitVariant.variant_id.desc())
        else:
            if sort_params["sort_of"] == "desc":
                query_check = query_check.order_by(column(sort_params["sort_by"]).desc())
            else:
                query_check = query_check.order_by(column(sort_params["sort_by"]).asc())

        query_final = query_check.offset((page*limit)-limit).limit(limit)
        results = db.execute(query_final).all()

        final_results = []
        for var_id,variant_code, variant_description, model_code, model_description, record_status in results:
            result = {
                "variant_id":var_id,
                "variant_code":variant_code,
                "variant_description":variant_description,
                "model_code":model_code,
                "model_description":model_description,
                "is_active":record_status
            }
            final_results.append(result)

        total_rows = len(final_results)
        total_pages = math.ceil(counter/limit)

        page_results = {
            "total_rows" : total_rows,
            "total_pages" : total_pages
        }
        return final_results, page_results, None
    except Exception as err:
        return None, None, err

async def get_unit_variant_drop_down(db:Session,model_id:int):
    try:
        query = select(MtrUnitVariant).where(MtrUnitVariant.model_id==model_id).options(load_only(MtrUnitVariant.variant_id, MtrUnitVariant.variant_description))
        result = db.scalars(query).all()
        return result, None
    except Exception as err:
        return None, err
    
async def get_unit_variant_by_id(db:Session,id:int):
    try:
        query_init = select(MtrUnitVariant).where(MtrUnitVariant.variant_id==id)
        results = db.scalars(query_init).first()
        return results,None
    except Exception as err:
        return None, err

async def post_unit_variant(db:Session,req:UnitVariantRequest):
    try:
        db.begin()
        _create_data = MtrUnitVariant()
        _create_data.variant_code = req.variant_code
        _create_data.model_id = req.model_id
        _create_data.variant_description = req.variant_description
        _create_data.release_date = req.release_date
        _create_data.discontinue_date = req.discontinue_date
        _create_data.chassis_prefix = req.chassis_prefix
        _create_data.engine_prefix = req.engine_prefix
        _create_data.production_year = req.prod_year
        _create_data.sales_allow = req.sales_allow
        _create_data.indent_indicator = req.indent_indicator
        _create_data.dp_amount = req.dp_amount
        _create_data.cylinder_id = req.cylinder_id
        _create_data.fuel_id = req.fuel_id
        _create_data.unit_type_id = req.unit_type
        _create_data.transmission_id = req.transmission
        _create_data.wheel_drive_id = req.wheel_drive
        _create_data.vehicle_type_police_invoice = req.vehicle_type_police_invoice
        _create_data.vehicle_kind_police_invoice = req.vehicle_kind_police_invoice
        _create_data.SUT = req.SUT
        _create_data.price = req.price
        db.add(_create_data)
        db.commit()
        db.refresh(_create_data)
        return _create_data,None
    except Exception as err:
        db.rollback()
        return None,err
    
async def update_unit_variant(db:Session,id:int,req:UnitVariantRequest):
    try:
        query_update = select(MtrUnitVariant).where(MtrUnitVariant.variant_id==id)
        _create_data = db.scalars(query_update).first()
        _create_data.variant_code = req.variant_code
        _create_data.model_id = req.model_id
        _create_data.variant_description = req.variant_description
        _create_data.release_date = req.release_date
        _create_data.discontinue_date = req.discontinue_date
        _create_data.chassis_prefix = req.chassis_prefix
        _create_data.engine_prefix = req.engine_prefix
        _create_data.production_year = req.prod_year
        _create_data.sales_allow = req.sales_allow
        _create_data.indent_indicator = req.indent_indicator
        _create_data.dp_amount = req.dp_amount
        _create_data.cylinder_id = req.cylinder_id
        _create_data.fuel_id = req.fuel_id
        _create_data.unit_type_id = req.unit_type
        _create_data.transmission_id = req.transmission
        _create_data.wheel_drive_id = req.wheel_drive
        _create_data.vehicle_type_police_invoice = req.vehicle_type_police_invoice
        _create_data.vehicle_kind_police_invoice = req.vehicle_kind_police_invoice
        _create_data.SUT = req.SUT
        _create_data.price = req.price
        db.commit()
        db.refresh(_create_data)
        return _create_data,None
    except Exception as err:
        db.rollback()
        return None,err

async def patch_unit_variant(db:Session,id:int):
    try:
        db.begin()
        query_activate = select(MtrUnitVariant).where(MtrUnitVariant.variant_id==id)
        activation_status = activation(db,query_activate)
        return activation_status, None
    except Exception as err:
        db.rollback()
        return None, err
    
async def get_all_variants(db:Session,id:int):
    try:
        query_all = select(MtrUnitVariant).where(MtrUnitVariant.model_id==id).options(load_only(MtrUnitVariant.variant_description))
        results = db.scalars(query_all).all()
        return results,None
    except Exception as err:
        return None, err