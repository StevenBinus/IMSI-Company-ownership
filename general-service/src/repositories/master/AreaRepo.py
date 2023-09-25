from fastapi import Request
from sqlalchemy import select, column
from src.entities.master.AreaEntity import MtrArea
from src.payloads.schemas.master import AreaSchema
from src.utils.AddPagination import get_the_pagination_search_list
from src.configs.database import get_db
from src.utils.Activation import activation
import math

def get_all_areas_list(page:int,limit:int,all_params:dict(),sort_params:dict()):
    db = get_db()
    query_set = select(MtrArea)
    total_data = len(db.scalars(query_set).all())
    query_check = get_the_pagination_search_list(query_set,all_params,sort_params)
    query_final = query_check.offset((page*limit)-limit).limit(limit)
    
    if sort_params["sort_by"]==None or sort_params["sort_of"]==None:
        query_check=query_check.order_by(MtrArea.area_id.desc())
    else:
        if sort_params["sort_of"] == "desc":
            query_check = query_check.order_by(column(sort_params["sort_by"]).desc())
        else:
            query_check = query_check.order_by(column(sort_params["sort_by"]).asc())
    query_final = query_check.order_by(MtrArea.area_id).offset(page*limit).limit(limit)

    results = db.scalars(query_final).all()

    total_rows = len(results)
    total_pages = math.ceil(total_data/limit)
    print(total_rows/limit)

    page_results = {
        "total_rows" : total_rows,
        "total_pages" : total_pages,
    }

    return results,page_results,None
    
def get_area_by_id(id:int):
    db = get_db()
    try:
        query_init = select(MtrArea).where(MtrArea.area_id==id)
        area = db.scalars(query_init).first()
        return area,None
    except Exception as err:
        return None,err

def get_area_by_code(code:str):
    db = get_db()
    try:
        query_init = select(MtrArea).where(MtrArea.area_code==code)
        area = db.scalars(query_init).first()
        return area,None
    except Exception as err:
        return None, err

def post_area(req:AreaSchema.MtrAreaRequest,request:Request):
    db = request.state.db
    try:
        db.begin()
        create_area = MtrArea()
        create_area.area_code = req.area_code
        create_area.description = req.description
        create_area.region_id = req.region_id
        db.add(create_area)
        db.commit()
        db.refresh(create_area)
        return create_area,None
    except Exception as err:
        db.rollback()
        return None,err

def update_area(id:int,req:AreaSchema.MtrAreaUpdate):
    db = get_db()
    try:
        query_init = select(MtrArea).where(MtrArea.area_id==id)
        area = db.scalars(query_init).first()
        area.description = req.description
        area.region_id = req.region_id
        db.commit()
        db.refresh(area)
        return area,None
    except Exception as err:
        db.rollback()
        return None, err

def patch_status_area(id:int,request:Request):
    db = request.state.db
    query_activation = select(MtrArea).where(MtrArea.area_id==id)
    activation_status = activation(db,query_activation)
    return activation_status,None