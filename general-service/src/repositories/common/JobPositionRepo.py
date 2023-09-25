from fastapi import Request
from sqlalchemy import select, column
from src.entities.master import JobPositionEntity
from src.payloads.schemas.master import JobPositionSchema
from src.utils.AddPagination import get_the_pagination_search_list
from src.configs.database import get_db
from src.utils.Activation import activation
import math

def get_job_positions_cruds(page:int,limit:int,all_params:dict(),sort_params:dict()):
    db = get_db()
    try:
        query_set=select(JobPositionEntity.MtrJobPosition)
        counter = len(db.scalars(query_set).all())
        query_check = get_the_pagination_search_list(query_set,all_params,sort_params)
            
        if sort_params["sort_by"]==None or sort_params["sort_of"]==None:
                    query_check = query_check.order_by(JobPositionEntity.MtrJobPosition.job_position_id.desc())
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
    
def get_job_position_cruds(id:int):
    db=get_db()
    try:
        query_check=select(JobPositionEntity.MtrJobPosition).where(JobPositionEntity.MtrJobPosition.job_position_id==id)
        query_set=db.scalars(query_check).first()
        return query_set,None
    except Exception as err:
        return None, err
    
def post_job_position_cruds(req:JobPositionSchema.MtrJobPositionGetSchema):
    db=get_db()
    try:
        db.begin()
        new_data=JobPositionEntity.MtrJobPosition()
        new_data.job_position_code=req.job_position_code
        new_data.job_position_name=req.job_position_name
        db.add(new_data)
        db.commit()
        db.refresh(new_data)
        return new_data,None
    except Exception as err:
        db.rollback()
        return None,err

def delete_job_position_cruds(id:int):
    db = get_db()
    try:
        db.begin()
        query_check=select(JobPositionEntity.MtrJobPosition).where(JobPositionEntity.MtrJobPosition.job_position_id==id)
        query_set=db.scalars(query_check).first()
        db.delete(query_set)
        db.commit()
        return query_set,None
    except Exception as err:
        db.rollback()
        return None, err

def put_job_position_cruds(id:int,req:JobPositionSchema.MtrJobPositionGetSchema):
    db=get_db()
    try:
        db.begin()
        query_check=select(JobPositionEntity.MtrJobPosition).where(JobPositionEntity.MtrJobPosition.job_position_id==id)
        query_set=db.scalars(query_check).first()

        query_set.job_position_code=req.job_position_code
        query_set.job_position_name=req.job_position_name
        db.commit()
        db.refresh(query_set)
        return query_set,None
    except Exception as err:
        return None, err    

def patch_job_position_cruds(id:int):
    db=get_db()
    check_active=select(JobPositionEntity.MtrJobPosition).where(JobPositionEntity.MtrJobPosition.job_position_id==id)
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