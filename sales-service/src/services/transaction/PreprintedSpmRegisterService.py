from src.repositories.transaction import PreprintedSpmRegisterRepo
from src.payloads.schemas.transaction import PreprintedSpmRegisterSchema
from sqlalchemy.orm import Session

async def get_header_preprinted_spm_register_search(db:Session,page:int,limit:int,all_params:dict()):
    get_data, page_results, err = await PreprintedSpmRegisterRepo.get_header_preprinted_spm_register_search(db,page,limit,all_params)
    if err != None:
        get_data = None
        page_results = None
    return get_data, page_results, err
    
async def get_header_preprinted_spm_register_by_id(db:Session,id:int):
    header, detail, err = await PreprintedSpmRegisterRepo.get_header_preprinted_spm_register_by_id(db,id)
    if err != None:
        header = None
        detail = None
    return header,detail, err
    
async def post_preprinted_spm_register(db:Session,req_form:PreprintedSpmRegisterSchema.SpmFormRegisterRequest):
    post_data,err = await PreprintedSpmRegisterRepo.post_preprinted_spm_register(db,req_form)
    if err != None:
        post_data = None
    return post_data, err
    
async def get_detail_preprinted_spm_register(db:Session):
    get_spm_details, err = await PreprintedSpmRegisterRepo.get_detail_preprinted_spm_register(db)
    if err != None:
        get_spm_details = None
    return get_spm_details, err