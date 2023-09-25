from sqlalchemy.orm import Session
from src.repositories.transaction import PreprintedSpmTakeRepo
from src.payloads.schemas.transaction.PreprintedSpmTakeSchema import TrxSpmFormTakeRequestDetail

async def get_spm_takes_search(db:Session,page:int,limit:int,all_params:dict()):
    get_results, page_results, err = await PreprintedSpmTakeRepo.get_spm_takes_search(db,page,limit,all_params)
    if err != None:
        get_results = None
        page_results = None
    return get_results, page_results, err
    
async def get_available_spm_doc_no(db:Session,page:int,limit:int,all_params:dict()):
    get_results, page_results, err = await PreprintedSpmTakeRepo.get_available_spm_doc_no(db,page,limit,all_params)
    if err != None:
        get_results = None
        page_results = None
    return get_results, page_results, err

async def get_all_spm_take_by_id(db:Session,id:int,page:int,limit:int):
    header,detail,pages,err = await PreprintedSpmTakeRepo.get_all_spm_take_by_id(db,id,page,limit)
    if err != None:
        header = None
        detail = None
        pages = None
    return header,detail,pages,err

async def get_available_spm_doc_no_by_id(db:Session,id:int):
    result, err = await PreprintedSpmTakeRepo.get_available_spm_doc_no_by_id(db,id)
    if err != None:
        result = None
    return result, err

async def post_taken_spm(db:Session,req_data:TrxSpmFormTakeRequestDetail):
    get_results, err = await PreprintedSpmTakeRepo.post_taken_spm(db,req_data)
    if err != None:
        get_results = None
    return get_results, err
    
async def update_detail_taken_spm(db:Session,id:int,rev_data:TrxSpmFormTakeRequestDetail):
    update_data,err = await PreprintedSpmTakeRepo.update_detail_taken_spm(db,id,rev_data)
    if err != None:
        update_data = None
    return update_data, err

async def submit_preprinted_spm_taken(db:Session,id:int):
    result, err = await PreprintedSpmTakeRepo.submit_preprinted_spm_taken(db,id)
    if err != None:
        result = None
    return result,err

async def delete_spm_taken_assigned(db:Session,deleted_spm:dict()):
    status_deleted = await PreprintedSpmTakeRepo.delete_spm_taken_assigned(db,deleted_spm)
    return status_deleted