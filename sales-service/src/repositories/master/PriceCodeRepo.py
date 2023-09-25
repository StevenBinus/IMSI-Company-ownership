from fastapi import Request
from sqlalchemy import select
from sqlalchemy.orm import load_only
from src.entities.master.PriceCodeEntity import MtrPriceCode
from src.entities.master.PriceCodeEntity import MtrPriceCode as pricecode
from src.entities.master.BrandEntity import MtrBrand as brand
from src.payloads.schemas.master.PriceCodeSchema import PriceCodeRequest
from src.configs.database import get_db
from src.utils.AddPagination import get_the_pagination_search

def get_price_code_search(page:int,limit:int,all_params:dict()):
    db = get_db()
    try:
        query_set = select(
                        pricecode.price_code,
                        pricecode.price_code_name,
                        pricecode.price_code_modifiabled,
                        pricecode.price_code_customized,
                        pricecode.price_code_dp_modifiabled,
                        pricecode.price_code_otr_modifiabled,
                        brand.brand_name
                     ).join(brand, pricecode.brand_id == brand.brand_id )      
        query_check,counter = get_the_pagination_search(db,query_set,all_params)
        query_check =  query_check.order_by(pricecode.price_code_id).offset(page*limit).limit(limit)
        results = db.execute(query_check).all()

        total_rows = counter
        total_pages = int(total_rows/limit)

        page_results = {
            "total_rows" : total_rows,
            "total_pages" : total_pages
        }

        finalresults = []
        for code,name,is_modifiabled,is_customized,is_dp_modifiabled, is_otr_modifiabled,brand_name in results:
            data = {
                "code": code,
                "name": name,
                "is_modifiabled": is_modifiabled,
                "is_customized": is_customized,
                "is_dp_modifiabled":is_dp_modifiabled,
                "is_otr_modifiabled":is_otr_modifiabled,
                "brand_name":brand_name
            }
            finalresults.append(data)

        return finalresults, page_results, None
    except Exception as err:
        return None, None, err     
        
      
   
def get_price_code_by_id(id:int):
    db = get_db()
    try:
        check_query = select(MtrPriceCode).where(MtrPriceCode.price_code_id==id)
        result = db.scalars(check_query).first()
        return result, None
    except Exception as err:
        return None, err


def post_price_code(req:PriceCodeRequest, request:Request):
    db = request.state.db
    try:
        db.begin()
        _new_data = MtrPriceCode()
        _new_data.brand_id = req.brand_id
        _new_data.price_code = req.price_code
        _new_data.price_code_name   = req.price_code_name
        _new_data.price_code_modifiabled  = req.price_code_modifiabled
        _new_data.price_code_customized = req.price_code_customized
        _new_data.price_code_otr_modifiabled = req.price_code_otr_modifiabled
        _new_data.price_code_dp_modifiabled = req.price_code_dp_modifiabled
        db.add(_new_data)
        db.commit()
        db.refresh(_new_data)
        return _new_data, None
    except Exception as err:
        db.rollback()
        return None, err



def update_price_code(id:int, req:PriceCodeRequest, request:Request):
    db = request.state.db
    try:
        db.begin()
        result = select(MtrPriceCode).where(MtrPriceCode.price_code_id==id)
        _data_update = db.scalars(result).first()
        _data_update.brand_id = req.brand_id
        _data_update.price_code = req.price_code
        _data_update.price_code_name = req.price_code_name
        _data_update.price_code_modifiabled = req.price_code_modifiabled
        _data_update.price_code_customized = req.price_code_customized
        _data_update.price_code_otr_modifiabled  = req.price_code_otr_modifiabled
        _data_update.price_code_dp_modifiabled = req.price_code_dp_modifiabled
        db.add(_data_update)
        db.commit()
        db.refresh(_data_update)
        return _data_update, None
    except Exception as err:
        db.rollback()
        return None, err

def patch_price_code(id:int, request:Request):
    db = request.state.db
    check_active_status = select(MtrPriceCode).where(MtrPriceCode.price_code_id==id)
    active_status = db.scalars(check_active_status).first()
    current_status = active_status.is_active
    try:
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