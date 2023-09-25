from fastapi import Request
from sqlalchemy import select, column
from src.entities.master import JobTitleEntity
from src.payloads.schemas.master import JobTitleSchema
from src.utils.AddPagination import get_the_pagination_search_list
from src.configs.database import get_db
from src.utils.Activation import activation
import math

def get_job_titles_cruds(page:int,limit:int,all_params:dict(),sort_params:dict()):
    db = get_db()
    try:
        query_set=select(JobTitleEntity.MtrJobTitle)
        counter = len(db.scalars(query_set).all())
        query_check = get_the_pagination_search_list(query_set,all_params,sort_params)
            
        if sort_params["sort_by"]==None or sort_params["sort_of"]==None:
                    query_check = query_check.order_by(JobTitleEntity.MtrJobTitle.job_title_id.desc())
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

def get_job_title_cruds(id:int):
    db = get_db()
    try:
        query_set=select(JobTitleEntity.MtrJobTitle).where(JobTitleEntity.MtrJobTitle.job_title_id==id)
        result = db.scalars(query_set).first()
        return result,None
    except Exception as err:
        return None,err
    

def post_job_title_cruds(req:JobTitleSchema.MtrJobTitleGetSchema):
    db=get_db()
    try:
        db.begin()
        new_data=JobTitleEntity.MtrJobTitle()
        new_data.job_title_code=req.job_title_code
        new_data.job_title_name=req.job_title_name
        db.add(new_data)
        db.commit()
        db.refresh(new_data)
        return new_data,None
    except Exception as err:
        db.rollback()
        return None,err

def delete_job_title_cruds(id:int):
    db=get_db()
    try:
        query_set=select(JobTitleEntity.MtrJobTitle).where(JobTitleEntity.MtrJobTitle.job_title_id==id)
        result=db.scalars(query_set).first()
        db.delete(result)
        db.commit()
        return result,None
    except Exception as err:
        db.rollback()
        return None,err
    
def put_job_title_cruds(id:int,req:JobTitleSchema.MtrJobTitleGetSchema):
    db=get_db()
    try:
        query_set = select(JobTitleEntity.MtrJobTitle).where(JobTitleEntity.MtrJobTitle.job_title_id==id)
        result=db.scalars(query_set).first()
        result.job_title_code=req.job_title_code
        result.job_title_name=req.job_title_name
        db.commit()
        db.refresh(result)
        return result,None
    except Exception as err:
        db.rollback()
        return None,err
    

def patch_job_title_cruds(id:int):
    db=get_db()
    query_set=select(JobTitleEntity.MtrJobTitle).where(JobTitleEntity.MtrJobTitle.job_title_id==id)
    result = db.scalars(query_set).first()
    active = result.is_active
    try:
        if active == True:
            result.is_active==False
        if active == False:
            result.is_active==True
        
        db.commit()
        db.refresh(result)
        return result,None
    except Exception as err:
        db.rollback()
        return None,err


