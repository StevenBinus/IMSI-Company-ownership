from src.repositories.transaction import PDIRequestRepo
from src.payloads.schemas.transaction import PDIRequestSchema
from fastapi import Request



def get_all_pdi_requests(page:int, limit:int, query_of:list[str], query_by:list[str]):
    get_data, page_results, err = PDIRequestRepo.get_all_pdi_requests(page,limit,query_of,query_by) 
    if err == None:
        return get_data, page_results, None
    else:
        return get_data, page_results, err
    
def get_by_id_pdi_request(id:int):
    get_data,err = PDIRequestRepo.get_by_id_pdi_request(id)
    if err == None:
        return get_data, None
    else:
        return get_data, err


def post_pdi_request(req_form:PDIRequestSchema.TrxPDIRequestAllSchema):
    post_data,err = PDIRequestRepo.post_pdi_request(req_form)
    if err == None:
        return post_data, None
    else:
        return post_data, err
    
def delete_pdi_request(id:int):
    erase_data, err = PDIRequestRepo.delete_pdi_request(id)
    if err == None:
        return erase_data, None
    else:
        return None, err
def post_pdi_request_detail(req_form:PDIRequestSchema.TrxPDIRequestDetailSchema):
    post_data,err = PDIRequestRepo.post_pdi_request_detail(req_form)
    if err == None:
        return post_data, None
    else:
        return post_data, err
    

def get_by_search_pdi_request(page:int,limit:int,all_params:dict()):
    get_data, page_results, err = PDIRequestRepo.get_by_search_pdi_request(page,limit,all_params)
    if err == None:
        return get_data, page_results, None
    else:
        return get_data, page_results, err
    


def get_full_detail_pdi_request_by_id(id:int):
    header,detail, err = PDIRequestRepo.get_full_detail_pdi_request_by_id(id)
    if err == None:
        return header,detail, None
    else:
        return None, None, err
    


def patch_pdi_request(pdi_request_system_number: int, pdi_request_detail_line_number: int):
    updated_data, err = PDIRequestRepo.patch_pdi_request(pdi_request_system_number, pdi_request_detail_line_number)
    if err == None:
        return updated_data, None
    else:
        return None, err