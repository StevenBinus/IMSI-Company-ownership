from fastapi import Request
from sqlalchemy import select, column
from src.entities.master import LoggingEntity
from src.payloads.schemas.master import LoggingSchema
from src.utils.AddPagination import get_the_pagination_search_list
from src.configs.database import get_db
from src.utils.Activation import activation
import math

def get_loggings_cruds(page:int,limit:int,all_params:dict(),sort_params:dict()):
    db = get_db()
    try:
        query_set=select(LoggingEntity.MtrLogging)
        counter = len(db.scalars(query_set).all())
        query_check = get_the_pagination_search_list(query_set,all_params,sort_params)
            
        if sort_params["sort_by"]==None or sort_params["sort_of"]==None:
                    query_check = query_check.order_by(LoggingEntity.MtrLogging.logging_id.desc())
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

def get_logging_cruds(id:int):
    db= get_db()
    try:
        query_set=select(LoggingEntity.MtrLogging).where(LoggingEntity.MtrLogging.logging_id==id)
        result=db.scalars(query_set).first()
        return result,None
    except Exception as err:
        return None,err
    

def post_logging_cruds(req:LoggingSchema.MtrLoggingPostSchema):
    db=get_db()
    try:
        db.begin()
        new_data = LoggingEntity.MtrLogging()
        new_data.created_at=req.created_at
        new_data.created_by=req.created_by
        new_data.hitted_apis=req.hitted_apis
        new_data.http_requests=req.http_requests
        new_data.http_respons=req.http_respons
        new_data.data_context=req.data_context
        new_data.triggered_menu=req.triggered_menu
        new_data.ip_address=req.ip_address
        db.add(new_data)
        db.commit()
        db.refresh(new_data)
        return new_data,None
    except Exception as err:
        db.rollback()
        return None,err
        

def delete_logging_cruds(id:int):
    db=get_db()
    try:
        query_check = select(LoggingEntity.MtrLogging).where(LoggingEntity.MtrLogging.logging_id==id)
        result=db.scalar(query_check).first()
        db.delete(result)
        db.commit()
        return result,None
    except Exception as err:
        db.rollback()
        return None,err
    
def put_logging_cruds(id:int,req:LoggingSchema.MtrLoggingPutSchema):
    db=get_db()
    try:
        query_check = select(LoggingEntity.MtrLogging).where(LoggingEntity.MtrLogging.logging_id==id)
        result = db.scalars(query_check).first()
        result.changed_at=req.changed_at
        result.changed_by=req.changed_by
        result.hitted_apis=req.hitted_apis
        result.http_requests=req.http_requests
        result.http_respons=req.http_respons
        result.data_context=req.data_context
        result.triggered_menu=req.triggered_menu
        result.ip_address=req.ip_address
        db.commit()
        db.refresh(result)
        return result,None
    except Exception as err:
        db.rollback()
        return None,err

def patch_logging_cruds(id:int):
    db=get_db()
    check_active=select(LoggingEntity.MtrLogging).where(LoggingEntity.MtrLogging.logging_id==id)
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

