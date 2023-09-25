from fastapi import Request
from sqlalchemy import select, column, join, func
from sqlalchemy.orm import load_only, joinedload, subqueryload, Bundle
from src.entities.master import DocumentEntity, ProfitCenterEntity
from src.entities.common import TransactionTypeEntity, DocumentTypeEntity
from src.payloads.schemas.master import DocumentMasterSchema
from datetime import datetime
import calendar
from src.configs.database import get_db
from src.utils.AddPagination import get_the_pagination_search, get_the_pagination_search_with_join

def post_source_document(req:DocumentMasterSchema.MtrDocumentRequest):
    db = get_db()
    try:
        db.begin()
        _new_data = DocumentEntity.MtrDocument()
        # _new_data.is_active = req.is_active
        _new_data.document_type_id = req.document_type_id
        _new_data.brand_id = req.brand_id
        _new_data.profit_center_id = req.profit_center_id
        _new_data.transaction_type_id = req.transaction_type_id
        _new_data.bank_company_id = req.bank_company_id
        _new_data.reset_frequency_id = req.reset_frequency_id
        _new_data.document_name = req.document_name   
        _new_data.document_format = req.document_format
        _new_data.document_reference = req.document_reference
        _new_data.signature_employee_1 = req.signature_employee_1
        _new_data.signature_title_1 = req.signature_title_1
        _new_data.signature_employee_2 = req.signature_employee_2
        _new_data.signature_title_2 = req.signature_title_2
        _new_data.signature_employee_3 = req.signature_employee_3
        _new_data.signature_title_3 = req.signature_title_3
        _new_data.signature_employee_4 = req.signature_employee_4
        _new_data.signature_title_4 = req.signature_employee_4
        _new_data.document_source_doc_prefix = req.document_source_doc_prefix
        _new_data.document_brand_prefix = req.document_brand_prefix
        _new_data.source_document_profit_cost_center_prefix = req.document_profit_cost_center_prefix
        _new_data.document_transaction_type_prefix = req.document_transaction_type_prefix
        _new_data.document_bank_acc_prefix = req.document_bank_acc_prefix
        _new_data.document_auto_number = req.document_auto_number
        db.add(_new_data)
        db.commit()
        db.refresh(_new_data)
        return _new_data, None
    except Exception as err:
        db.rollback()
        return None, err

def get_source_document_search(page:int,limit:int,all_params:dict(),sort_params:dict()):
    db = get_db()
    try:    
        query_set = select(
            DocumentTypeEntity.MtrDocumentType.document_type_code,
            DocumentEntity.MtrDocument.document_name,
            DocumentEntity.MtrDocument.brand_id,
            DocumentEntity.MtrDocument.profit_center_id,
            ProfitCenterEntity.MtrProfitCenter.profit_center_name,
            TransactionTypeEntity.MtrTransactionType.transaction_type_code,
            DocumentEntity.MtrDocument.bank_company_id,
            DocumentEntity.MtrDocument.is_active
        )
        join_tables = [ProfitCenterEntity.MtrProfitCenter,
                       TransactionTypeEntity.MtrTransactionType,
                       DocumentTypeEntity.MtrDocumentType]
        query_check = get_the_pagination_search_with_join(query_set,all_params,DocumentEntity.MtrDocument,join_tables)
        if sort_params["sort_by"]==None or sort_params["sort_of"]==None:
                    query_check = query_check.order_by(DocumentEntity.MtrDocument.document_id.desc())
        else:
                    if sort_params["sort_by"]=="desc":
                        query_check = query_check.order_by(column(sort_params["sort_by"]).desc())
                    else:
                        query_check = query_check.order_by(column(sort_params["sort_by"]).asc())
        query_final = query_check.join(
            ProfitCenterEntity.MtrProfitCenter,
            DocumentEntity.MtrDocument.profit_center_id == ProfitCenterEntity.MtrProfitCenter.profit_center_id
        ).join(
            TransactionTypeEntity.MtrTransactionType,
            DocumentEntity.MtrDocument.transaction_type_id == TransactionTypeEntity.MtrTransactionType.transaction_type_id
        ).join(
            DocumentTypeEntity.MtrDocumentType,
            DocumentEntity.MtrDocument.document_type_id == DocumentTypeEntity.MtrDocumentType.document_type_id
        ).order_by(DocumentEntity.MtrDocument.document_type_id).offset(page*limit).limit(limit)
  
        data = db.execute(query_final).all()

        results=[]
        for source_doc_type_code, source_document_name, brand_id, profit_center_id, profit_center_name, transaction_type_code, bank_company_id, is_active in data:
            go_out = {
                "source_document_type_code": source_doc_type_code,
                "source_document_name": source_document_name,
                "brand_id": brand_id,
                "profit_center_id": profit_center_id,
                "profit_center_name": profit_center_name,
                "transaction_type_code": transaction_type_code,
                "bank_company_id": bank_company_id,
                "is_active": is_active
            }
            results.append(go_out)

        total_rows = len(results)
        total_pages  = int(total_rows/limit)

        page_results = {
            "total_rows" : total_rows,
            "total_pages" : total_pages
        }
        return results,page_results,None
    except Exception as err:
        return None, None, err

def get_source_document_by_id(id:int):
    db = get_db()
    try:
        check_query = select(DocumentEntity.MtrDocument).where(DocumentEntity.MtrDocument.document_id==id)
        result = db.scalars(check_query).first()
        return result, None
    except Exception as err:
        return None, err
    
def patch_source_document(id:int):
    db = get_db()
    try:
        check_active_status = select(DocumentEntity.MtrDocument).where(DocumentEntity.MtrDocument.document_id==id)
        active_status = db.scalars(check_active_status).first()
        current_status = active_status.is_active
    
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
    
def update_source_document(id:int, req:DocumentMasterSchema.MtrDocumentRequest):
    db = get_db()
    check_data = select(DocumentEntity.MtrDocument).where(DocumentEntity.MtrDocument.document_id == id)
    updated_data = db.scalars(check_data).first()
    try:
        updated_data.document_type_id = req.document_type_id
        updated_data.brand_id = req.brand_id
        updated_data.profit_center_id = req.profit_center_id
        updated_data.transaction_type_id = req.transaction_type_id
        updated_data.bank_company_id = req.bank_company_id
        updated_data.reset_frequency_id = req.reset_frequency_id
        updated_data.document_name = req.document_name
        updated_data.document_format = req.document_format
        updated_data.document_reference = req.document_reference
        updated_data.signature_employee_1 = req.signature_employee_1
        updated_data.signature_title_1 = req.signature_title_1
        updated_data.signature_employee_2 = req.signature_employee_2
        updated_data.signature_title_2 = req.signature_title_2
        updated_data.signature_employee_3 = req.signature_employee_3
        updated_data.signature_title_3 = req.signature_title_3
        updated_data.signature_employee_4 = req.signature_employee_4
        updated_data.signature_title_4 = req.signature_title_4
        updated_data.document_source_doc_prefix = req.document_source_doc_prefix
        updated_data.document_brand_prefix = req.document_brand_prefix
        updated_data.source_document_profit_cost_center_prefix = req.document_profit_cost_center_prefix
        updated_data.document_transaction_type_prefix = req.document_transaction_type_prefix
        updated_data.document_bank_acc_prefix = req.document_bank_acc_prefix
        updated_data.document_auto_number = req.document_auto_number
        db.commit()
        db.refresh(updated_data)
        return updated_data, None
    except Exception as err:
        db.rollback()
        return None, err