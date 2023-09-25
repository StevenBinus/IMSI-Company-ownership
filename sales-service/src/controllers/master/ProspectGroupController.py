from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session
from src.configs.database import get_db
from src.services.master import ProspectGroupService
from src.payloads.schemas.master.ProspectGroupSchema import ProspectGroupRequest
from src.payloads.responses.CommonResponse import payload_response
from src.payloads.responses.PaginationResponse import pagination_response
from src.exceptions.RequestException import ResponseException

router = APIRouter(tags=["Master : Prospect Group"], prefix="/api/sales")


@router.get("/prospect-group", status_code=status.HTTP_200_OK)
async def get_prospect_group_all(page: int, limit: int, db:Session=Depends(get_db)):
    get_results, pages, err = await ProspectGroupService.get_prospect_group_all(db, page, limit)
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


@router.get("/prospect-group/{id}", status_code=status.HTTP_200_OK)
async def get_prospect_group_by_id(id: int, db:Session=Depends(get_db)):
    get_result, err = await ProspectGroupService.get_prospect_group_by_id(db,id)

    if get_result != [] and err == None:
        return payload_response(200, "success", get_result)
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=ResponseException(404)
        )


@router.post("/prospect-group", status_code=status.HTTP_201_CREATED)
async def create_prospect_group(req: ProspectGroupRequest, db:Session=Depends(get_db)):
    created_data, err = await ProspectGroupService.post_prospect_group(db,req)

    if created_data and err == None:
        return payload_response(201, "success", created_data)
    else:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=ResponseException(400)
        )


@router.put("/prospect-group/{id}", status_code=status.HTTP_200_OK)
async def update_prospect_group(id: int, req: ProspectGroupRequest, db:Session=Depends(get_db)):
    updated_data, err = await ProspectGroupService.update_prospect_group(db,id, req)

    if updated_data and err == None:
        return payload_response(200, "success", updated_data)
    else:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=ResponseException(400)
        )
