from src.entities.master.CostCenterEntity import MtrCostCenter
from src.payloads.schemas.master import CostCenterSchema
from sqlalchemy.orm import Session
from sqlalchemy import select, column
from src.utils.BoolConvert import strtobool
import math
from src.configs.database import get_db
from src.utils import AddPagination

def get_mtr_cost_centers_cruds(page:int,limit:int,all_params:dict(),sort_params:dict()):
    db = get_db()
    try:
        query_set=select(MtrCostCenter)
        counter = len(db.scalars(query_set).all())
        query_check = AddPagination.get_the_pagination_search_list(query_set,all_params,sort_params)
            
        if sort_params["sort_by"]==None or sort_params["sort_of"]==None:
                    query_check = query_check.order_by(MtrCostCenter.cost_center_id.desc())
        else:
                    if sort_params["sort_by"]=="desc":
                        query_check = query_check.order_by(column(sort_params["sort_by"]).desc())
                    else:
                        query_check = query_check.order_by(column(sort_params["sort_by"]).asc())
        query_final=query_check.offset(page*limit).limit(limit)
                
        result = db.scalars(query_final).all()

        total_rows = counter
        total_pages = int(total_rows/limit)

        page_results = {
                    "total_rows" : total_rows,
                    "total_pages" : total_pages
                }
        return result, page_results, None
    except Exception as err:
         return None,None,err



def get_mtr_cost_center_cruds(id:int):
    db=get_db()
    try:
        query_check=select(MtrCostCenter).where(MtrCostCenter.cost_center_id==id)
        query_set=db.scalars(query_check).first()
        return query_set,None
    except Exception as err:
        return None, err

def post_mtr_cost_center(req:CostCenterSchema.MtrCostCenterPost):
    db = get_db()
    try:
        db.begin()
        new_data = MtrCostCenter()
        new_data.cost_center_code=req.cost_center_code
        new_data.cost_center_name=req.cost_center_name
        db.add(new_data)
        db.commit()
        db.refresh(new_data)
        return new_data,None
    except Exception as err:
        db.rollback()
        return None, err


def update_mtr_cost_center(id:int,req:CostCenterSchema.MtrCostCenterPost):
    db=get_db()
    try:
        query_check=select(MtrCostCenter).where(MtrCostCenter.cost_center_id==id)
        updated_data=db.scalars(query_check).first()
        updated_data.cost_center_code=req.cost_center_code
        updated_data.cost_center_name = req.cost_center_name
        db.commit()
        db.refresh(updated_data)
        return updated_data,None
    except Exception as err:
        return None, err

def del_mtr_cost_center(id:int):
    db= get_db()
    try:
        query_check=select(MtrCostCenter).where(MtrCostCenter.cost_center_id==id)
        query_set=db.scalars(query_check).first()
        db.delete(query_set)
        db.commit()
        return query_set,None
    except Exception as err:
        db.rollback()
        return None, err
    
def patch_mtr_cost_center(id:int):
    db=get_db()
    check_active=select(MtrCostCenter).where(MtrCostCenter.cost_center_id==id)
    current_status=db.scalars(check_active).first()
    active=current_status.is_active
    try:
       if active==True:
           current_status.is_active=False
       else:
           current_status.is_active=True

       db.commit()
       db.refresh(current_status)

       return current_status, None
   
    except Exception as err:
       db.rollback
       return None, err
