from src.repositories.common import CompanyRepo
from src.payloads.schemas.common.CompanySchema import MtrCompanyRequest


def get_company_all(page: int, limit: int, all_params: dict(), sort_fields: dict()):
    get_data, page_results, err = CompanyRepo.get_company_all(
        page, limit, all_params, sort_fields
    )
    if err == None:
        return get_data, page_results, None
    else:
        return None, None, err


def get_company_by_id(id: int):
    result, err = CompanyRepo.get_company_by_id(id)
    print("company result: " + str(err))
    if err == None:
        return result, None
    else:
        return result, err


def post_company(req: MtrCompanyRequest):
    created_data, err = CompanyRepo.post_company(req)
    print("post company result: " + str(err))
    if err == None:
        return created_data, None
    else:
        return None, err


def put_company(id: int, req: MtrCompanyRequest):
    updated_data, err = CompanyRepo.put_company(id, req)
    if err == None:
        return updated_data, None
    else:
        return None, err


def delete_company(id: int):
    deleted_data, err = CompanyRepo.delete_company(id)
    if err == None:
        return deleted_data, None
    else:
        return None, err


def patch_company(id: int):
    patched_data, err = CompanyRepo.patch_company(id)
    if err == None:
        return patched_data, None
    else:
        return None, err
