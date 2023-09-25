from fastapi import Request
from sqlalchemy import select, column
from src.payloads.schemas.master import SourceApprovalDocumentSchema
from src.utils.AddPagination import get_the_pagination_search_list
from src.configs.database import get_db
from src.utils.Activation import activation
import math
from src.entities.master import SourceApprovalDocumentEntity

def get_source_approval_documents_cruds(page:int,limit:int,all_params:dict(),sort_params:dict()):
    db = get_db()
    try:
        query_set=select(SourceApprovalDocumentEntity.MtrSourceApprovalDocument)
        counter = len(db.scalars(query_set).all())
        query_check = get_the_pagination_search_list(query_set,all_params,sort_params)
            
        if sort_params["sort_by"]==None or sort_params["sort_of"]==None:
                    query_check = query_check.order_by(SourceApprovalDocumentEntity.MtrSourceApprovalDocument.source_approval_document_id.desc())
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


def get_source_approval_document_cruds(id:int):
    db=get_db()
    try:
        query_check = select(SourceApprovalDocumentEntity.MtrSourceApprovalDocument).where(SourceApprovalDocumentEntity.MtrSourceApprovalDocument.source_approval_document_id==id)
        query_set=db.scalars(query_check).first()
        return query_set,None
    except Exception as err:
        return None,err    

def post_source_approval_document_cruds(req:SourceApprovalDocumentSchema.MtrSourceApprovalDocumentGetSchema):
    db=get_db()
    try:
        db.begin()
        new_data = SourceApprovalDocumentEntity.MtrSourceApprovalDocument()
        new_data.source_approval_document_code=req.source_approval_document_code
        new_data.source_approval_document_name=req.source_approval_document_name
        db.add(new_data)
        db.commit()
        db.refresh(new_data)
        return new_data,None
    except Exception as err:
        db.rollback()
        return None,err

def delete_source_approval_document_cruds(id:int):
    db=get_db()
    try:
        query_set=select(SourceApprovalDocumentEntity.MtrSourceApprovalDocument).where(SourceApprovalDocumentEntity.MtrSourceApprovalDocument.source_approval_document_id==id)
        result = db.scalars(query_set).first()
        db.delete(result)
        db.commit()
        return result,None
    except Exception as err:
        db.rollback()
        return None,err

def put_source_approval_document_cruds(id:int,req:SourceApprovalDocumentSchema.MtrSourceApprovalDocumentGetSchema):
    db=get_db()
    try:
        query_set=select(SourceApprovalDocumentEntity.MtrSourceApprovalDocument).where(SourceApprovalDocumentEntity.MtrSourceApprovalDocument.source_approval_document_id==id)
        update_data=db.scalars(query_set).first()
        update_data.source_approval_document_code=req.source_approval_document_code
        update_data.source_approval_document_name=req.source_approval_document_name
        db.commit()
        db.refresh(update_data)
        return update_data,None
    except Exception as err:
        db.rollback()
        return None,err

def patch_source_approval_document_cruds(id:int):
    db=get_db()
    check_active=select(SourceApprovalDocumentEntity.MtrSourceApprovalDocument).where(SourceApprovalDocumentEntity.MtrSourceApprovalDocument.source_approval_document_id==id)
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