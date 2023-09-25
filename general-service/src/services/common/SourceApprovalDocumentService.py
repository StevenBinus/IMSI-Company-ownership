from src.repositories.master import SourceApprovalDocumentRepo
from src.payloads.schemas.master import SourceApprovalDocumentSchema
from fastapi import Request

def get_source_approval_documents_cruds(page:int, limit:int, all_params:dict(), sort_params:dict()):
    get_data, page_results, err = SourceApprovalDocumentRepo.get_source_approval_documents_cruds(page,limit,all_params,sort_params) 
    if err == None:
        return get_data, page_results, None
    else:
        return None, None, err
    
def get_source_approval_document_cruds(id:int):
    result, err = SourceApprovalDocumentRepo.get_source_approval_document_cruds(id)
    if err == None:
        return result, None
    else:
        return result, err
    
    
def post_source_approval_document_cruds(req:SourceApprovalDocumentSchema.MtrSourceApprovalDocumentGetSchema):
    created_data, err = SourceApprovalDocumentRepo.post_source_approval_document_cruds(req)
    if err == None:
        return created_data, None
    else:
        return None, err
    
def patch_source_approval_document_cruds(id:int):
    updated_data, err = SourceApprovalDocumentRepo.patch_source_approval_document_cruds(id)
    if err == None:
        return updated_data, None
    else:
        return None, err
    
def put_source_approval_document(id:int,req:SourceApprovalDocumentSchema.MtrSourceApprovalDocumentGetSchema):
    update_data,err = SourceApprovalDocumentRepo.put_source_approval_document_cruds(id,req)
    if err == None:
        return update_data,None
    else:
        return None,err
    
def delete_source_approval_document(id:int):
    deleted_data,err= SourceApprovalDocumentRepo.delete_source_approval_document_cruds(id)
    if err == None:
        return deleted_data,None
    else:
        return None,err