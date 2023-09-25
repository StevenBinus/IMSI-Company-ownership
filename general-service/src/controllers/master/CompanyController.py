from fastapi import APIRouter, HTTPException, status
from src.services.master import CompanyService
from src.payloads.schemas.common.CompanySchema import MtrCompanyRequest
from src.payloads.responses.GeneralResponse import payload_response
from src.payloads.responses.PaginationResponse import pagination_response
from src.exceptions.RequestException import ResponseException

router = APIRouter(tags=["Company"], prefix="/api/general")


@router.get("/company", status_code=status.HTTP_200_OK)
async def get_company_all(
    page: int,
    limit: int,
    company_code: str | None = None,
    company_name: str | None = None,
    status_active: bool | None = None,
    sort_by: str | None = None,
    sort_of: str | None = None,
):
    all_params = {
        "company_code": company_code,
        "company_name": company_name,
        "is_active": status_active,
    }
    sort_fields = {"sort_by": sort_by, "sort_of": sort_of}
    get_results, pages, err = CompanyService.get_company_all(
        page, limit, all_params, sort_fields
    )

    if get_results != [] and err == None:
        return pagination_response(
            200,
            "success",
            page,
            limit,
            pages["total_pages"],
            pages["total_rows"],
            get_results,
        )
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=ResponseException(404)
        )


@router.get("/company/{id}", status_code=status.HTTP_200_OK)
async def get_company_by_id(id: int):
    get_result, err = CompanyService.get_company_by_id(id)

    if not get_result and err == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=ResponseException(404)
        )
    return payload_response(200, "success", get_result)


@router.post("/company", status_code=status.HTTP_201_CREATED)
async def create_company(req: MtrCompanyRequest):
    created_data, err = CompanyService.post_company(req)
    if err == None:
        return payload_response(201, "created", created_data)
    else:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, detail=ResponseException(409)
        )


@router.put("/company/{id}", status_code=status.HTTP_200_OK)
async def update_company(id: int, req: MtrCompanyRequest):
    updated_data, err = CompanyService.put_company(id, req)
    if err == None:
        return payload_response(200, "updated", updated_data)
    else:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, detail=ResponseException(409)
        )


@router.delete("/company/{id}", status_code=status.HTTP_200_OK)
async def delete_company(id: int):
    deleted_data, err = CompanyService.delete_company(id)
    if err == None:
        return payload_response(200, "deleted", deleted_data)
    else:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, detail=ResponseException(409)
        )


@router.patch("/company/{id}", status_code=status.HTTP_200_OK)
async def update_company_status(id: int):
    patched_data, err = CompanyService.patch_company(id)
    if err == None:
        return payload_response(200, "patched", patched_data)
    else:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, detail=ResponseException(409)
        )
