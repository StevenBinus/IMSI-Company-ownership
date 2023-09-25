from sqlalchemy import select,column
from sqlalchemy.orm import load_only, Session
from src.entities.master.BrandEntity import MtrBrand
from src.payloads.schemas.master.UnitBrandSchema import UnitBrandRequest
from src.utils.AddPagination import get_the_pagination_search_list
from src.utils.Activation import activation

# Unit Brand
async def get_unit_brand_all(db:Session,page:int, limit:int,all_params=dict(),sort_params=dict()):
    try:
        #for pagination purposes
        query_init = select(MtrBrand)
        query_check,counter = await get_the_pagination_search_list(db,query_init,all_params)   
        if sort_params["sort_by"] == None or sort_params["sort_of"] == None:
            query_check = query_check.order_by(MtrBrand.brand_id.desc())
        else:
            if sort_params["sort_of"] == "desc":
                query_check = query_check.order_by(column(sort_params["sort_by"]).desc())
            else:
                query_check = query_check.order_by(column(sort_params["sort_by"]).asc())

        query_final = query_check.offset(page*limit).limit(limit).options(load_only(
            MtrBrand.brand_code,
            MtrBrand.brand_name,
            MtrBrand.is_active
        ))
        
        results = db.scalars(query_final).all()

        total_rows = counter
        total_pages  = int(total_rows/limit)

        page_results = {
            "total_rows" : total_rows,
            "total_pages" : total_pages
        }
        return results, page_results, None
    except Exception as err:
        return None, None, err
    
async def get_unit_brand_drop_down(db:Session):
    try:
        query = select(MtrBrand).options(load_only(MtrBrand.brand_name))
        result = db.scalars(query).all()
        return result, None
    except Exception as err:
        return None, err
        
async def get_unit_brand_by_id(db:Session,id:int):
    try:
        check_query = select(MtrBrand).where(MtrBrand.brand_id==id)
        result = db.scalars(check_query).first()
        return result, None
    except Exception as err:
        return None, err
    
async def post_unit_brand(db:Session,req:UnitBrandRequest):
    try:
        _new_data = MtrBrand()
        _new_data.supplier_id = req.supplier_id
        _new_data.warehouse_id = req.warehouse_id
        _new_data.brand_code = req.brand_code
        _new_data.brand_abbreviation = req.brand_abbreviation
        _new_data.brand_name = req.brand_name
        _new_data.brand_must_withdrawl = req.brand_must_withdrawl
        _new_data.atpm_unit  = req.atpm_unit
        _new_data.atpm_workshop = req.atpm_workshop
        _new_data.atpm_sparepart = req.atpm_sparepart
        _new_data.atpm_finance = req.atpm_finance
        db.add(_new_data)
        db.commit()
        db.refresh(_new_data)
        return _new_data,None
    except Exception as err:
        db.rollback()
        return None, err

async def update_unit_brand(db:Session, id:int, req:UnitBrandRequest):
    try:
        db.begin()
        result = select(MtrBrand).where(MtrBrand.brand_id==id)
        _data_update = db.scalars(result).first()
        _data_update.supplier_id = req.supplier_id
        _data_update.warehouse_id = req.warehouse_id
        _data_update.brand_code = req.brand_code
        _data_update.brand_abbreviation = req.brand_abbreviation
        _data_update.brand_name = req.brand_name
        _data_update.brand_must_withdrawl = req.brand_must_withdrawl
        _data_update.atpm_unit  = req.atpm_unit
        _data_update.atpm_workshop = req.atpm_workshop
        _data_update.atpm_sparepart = req.atpm_sparepart
        _data_update.atpm_finance = req.atpm_finance
        db.add(_data_update)
        db.commit()
        db.refresh(_data_update)
        return _data_update, None
    except Exception as err:
        db.rollback()
        return None, err

async def patch_unit_brand(db:Session,id:int):
    try:
        db.begin()
        query_activate = select(MtrBrand).where(MtrBrand.brand_id==id)
        activation_status = activation(db,query_activate)
        return activation_status, None
    except Exception as err:
        db.rollback()
        return None, err