from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session
from src.configs.database import get_db
from src.services.master import ProspectSourceService
from src.payloads.schemas.master.ProspectSourceSchema import ProspectSourceCreateRequest,ProspectSourceUpdateRequest
from src.payloads.responses.CommonResponse import payload_response
from src.payloads.responses.PaginationResponse import pagination_response
from src.exceptions.RequestException import ResponseException

router = APIRouter(tags=["Master : Prospect Source"], prefix="/api/sales")


@router.get("/prospect-source", status_code=status.HTTP_200_OK)
async def get_prospect_source_all(
    page: int,
    limit: int,
    company_code: str | None = None,
    status_active: bool | None = None,
    db:Session=Depends(get_db)):
    get_all_params = {
        "company_code": company_code,
        "is_active": status_active,
    }
    get_results, pages, err = await ProspectSourceService.get_prospect_source_all(db, page, limit, get_all_params)

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

@router.get("/prospect-source/drop-down")
async def get_prospect_source_drop_down(db:Session=Depends(get_db)):
    results, err = await ProspectSourceService.get_prospect_source_drop_down(db)
    if results == [] or err != None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=str(err))
    return payload_response(200,"Success",results) 

@router.get("/prospect-source/{id}", status_code=status.HTTP_200_OK)
async def get_prospect_source_by_id(id: int, db:Session=Depends(get_db)):
    get_result, err = await ProspectSourceService.get_prospect_source_by_id(db,id)
    if not get_result or err != None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=ResponseException(404)
        )
    return payload_response(200, "success", get_result)


@router.post("/prospect-source", status_code=status.HTTP_201_CREATED)
async def create_prospect_source(req: ProspectSourceCreateRequest, db:Session=Depends(get_db)):
    created_data, err = await ProspectSourceService.post_prospect_source(db,req)
    if err == None:
        return payload_response(201, "created", created_data)
    else:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, detail=ResponseException(409)
        )


@router.put("/prospect-source/{id}", status_code=status.HTTP_200_OK)
async def update_prospect_source(id: int, req: ProspectSourceUpdateRequest, db:Session=Depends(get_db)):
    updated_data, err = await ProspectSourceService.put_prospect_source(db, id, req)
    if err == None:
        return payload_response(200, "updated", updated_data)
    else:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, detail=ResponseException(409)
        )


@router.patch("/prospect-source/{id}", status_code=status.HTTP_200_OK)
async def update_prospect_source_status(id: int, db:Session=Depends(get_db)):
    patched_data, err = await ProspectSourceService.patch_prospect_source(db,id)
    if err == None:
        return payload_response(200, "patched", patched_data)
    else:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, detail=ResponseException(409)
        )