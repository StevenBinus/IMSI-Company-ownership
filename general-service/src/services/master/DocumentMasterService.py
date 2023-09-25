from src.repositories.master import DocumentMasterRepo
from src.payloads.schemas.master import DocumentMasterSchema
from fastapi import Request

def post_source_document(req:DocumentMasterSchema.MtrDocumentRequest):
    created_data, err = DocumentMasterRepo.post_source_document(req)
    if err == None:
        return created_data, None
    else:
        return None, err
    
def get_source_document_search(page:int,limit:int,all_params:dict(),sort_params:dict()):
    get_data, page_results, err = DocumentMasterRepo.get_source_document_search(page,limit,all_params,sort_params)
    if err == None:
        return get_data, page_results, None
    else:
        return get_data, page_results, err
    
def get_source_document_by_id(id:int):
    result, err = DocumentMasterRepo.get_source_document_by_id(id)
    if err == None:
        return result, None
    else:
        return result, err
    
def patch_source_document(id:int):
    updated_data, err = DocumentMasterRepo.patch_source_document(id)
    if err == None:
        return updated_data, None
    else:
        return None, err
    
def update_source_document(id: int, req:DocumentMasterSchema.MtrDocumentRequest):
    updated_data, err = DocumentMasterRepo.update_source_document(id, req)
    if err == None:
        return updated_data, None
    else:
        return None, err
