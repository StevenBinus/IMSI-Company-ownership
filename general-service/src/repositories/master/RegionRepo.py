from src.configs.database import get_db
from src.utils.AddPagination import get_the_pagination_search_list
from fastapi import Request
from src.entities.master.RegionEntity import MtrRegion 
from src.payloads.schemas.master.RegionSchema import MtrRegionRequest
from sqlalchemy import select, column
from src.utils.Activation import activation
import math

async def get_all_regions(page:int,limit:int,all_params:dict(),sort_params:dict()):
    db = get_db()
    try:
        query_set = select(MtrRegion)
        total_data = len(db.scalars(query_set).all())
        query_check = get_the_pagination_search_list(query_set,all_params,sort_params,MtrRegion.region_id)

        query_final = query_check.offset(page*limit).limit(limit)
        
        results = db.scalars(query_final).all()

        if sort_params["sort_by"]==None or sort_params["sort_of"]==None:
            query_check = query_check.order_by(MtrRegion.region_id.desc())
        else:
            if sort_params["sort_by"]=="desc":
                query_check = query_check.order_by(column(sort_params["sort_by"]).desc())
            else:
                query_check = query_check.order_by(column(sort_params["sort_by"]).asc())
        query_final=query_check.offset(page*limit).limit(limit)
        total_rows = len(results)
        total_pages = math.ceil(total_data/limit)
        

        page_results = {
            "total_rows" : total_rows,
            "total_pages" : total_pages,
        }
        return results, page_results, None
    except Exception as err:
       return None, None, err
    
def get_region_by_id(id: int):
    db = get_db()
    try:
        check_query = select(MtrRegion).where(MtrRegion.region_id==id)
        result = db.scalars(check_query).first()
        return result, None
    except Exception as err:
        return None, err
    
def get_region_on_by_code(code:str):
    db = get_db()
    try:
        check_query = select(MtrRegion).where(MtrRegion.region_code==code)
        result = db.scalars(check_query).first()
        return result,None
    except Exception as err:
        return None, err
    
def post_region(req:MtrRegionRequest,request:Request):
    db = request.state.db
    #try:
    db.begin()
    _new_data = MtrRegion()
    _new_data.region_code = req.region_code
    _new_data.region_name = req.region_name
    db.add(_new_data)
    db.commit()
    db.refresh(_new_data)
    return _new_data, None
    # except Exception as err:
    #     db.rollback()
    #     return None, err

def put_region(id:int, req:MtrRegionRequest, request:Request):
    db = request.state.db
    try:
        query_check = select(MtrRegion).where(MtrRegion.region_id==id)
        updated_data = db.scalars(query_check).first()
        updated_data.region_code = req.region_code
        updated_data.region_name = req.region_name
        db.commit()
        db.refresh(updated_data)
        return updated_data, None
    except Exception as err:
        db.rollback()
        return None, err

def patch_status_region(id:int,request:Request):
    db = request.state.db
    query_activation = select(MtrRegion).where(MtrRegion.region_id==id)
    activation_status = activation(db,query_activation)
    return activation_status,None