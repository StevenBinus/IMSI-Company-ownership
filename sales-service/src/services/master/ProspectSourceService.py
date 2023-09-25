from src.repositories.master import ProspectSourceRepo
from src.payloads.schemas.master.ProspectSourceSchema import ProspectSourceCreateRequest,ProspectSourceUpdateRequest
from sqlalchemy.orm import Session

async def get_prospect_source_all(db:Session, page: int, limit: int, get_all_params: dict()):
    get_data, page_results, err = await ProspectSourceRepo.get_prospect_source_all(db, page, limit, get_all_params)
    if err == None:
        return get_data, page_results, None
    else:
        return None, None, err

async def get_prospect_source_drop_down(db:Session):
    result, err = await ProspectSourceRepo.get_prospect_source_drop_down(db)
    if err != None:
        result = None
    return result, err

async def get_prospect_source_by_id(db:Session, id: int):
    result, err = await ProspectSourceRepo.get_prospect_source_by_id(db, id)
    if err == None:
        return result, None
    else:
        return None, err


async def post_prospect_source(db:Session, req: ProspectSourceCreateRequest):
    created_data, err = await ProspectSourceRepo.post_prospect_source(db, req)
    if err == None:
        return created_data, None
    else:
        return None, err


async def put_prospect_source(db:Session, id: int, req: ProspectSourceUpdateRequest):
    updated_data, err = await ProspectSourceRepo.put_prospect_source(db, id, req)
    if err == None:
        return updated_data, None
    else:
        return None, err


async def patch_prospect_source(db:Session, id: int):
    patched_data, err = await ProspectSourceRepo.patch_prospect_source(db, id)
    if err == None:
        return patched_data, None
    else:
        return None, err
