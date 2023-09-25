from fastapi import APIRouter, HTTPException, status, Query, Request, Depends
from src.services.master import DivisionService
from src.payloads.schemas.master.DivisionSchema import MtrDivisionRequest, MtrDivisionUpdateRequest
from src.payloads.responses.GeneralResponse import payload_response
from src.payloads.responses.PaginationResponse import pagination_response
from src.exceptions.RequestException import ResponseException
from sqlalchemy.orm import Session
from src.configs.database import get_db

router = APIRouter(tags=["Division"],prefix="/api/general")

@router.get("/division", status_code=status.HTTP_200_OK)
async def get_division_list(page:int, limit:int,
                                is_active:bool|None=None,
                                division_id:int|None=None,
                                division_code:str|None=None,
                                division_name:str|None=None,
                                sort_by:str|None=None,
                                sort_of:str|None=None,
                                db: Session = Depends(get_db)):
    get_all_params={
        "is_active":is_active,"division_id":division_id,"division_code":division_code,"division_name":division_name
    }
    sort_params={"sort_of":sort_of,"sort_by":sort_by}
    default_sort_value=any
    get_results, pages, err = await DivisionService.get_division_list(db,page,limit,get_all_params,sort_params,default_sort_value)
    if err == None:
        return pagination_response(200, "success", page, limit, pages["total_pages"], pages["total_rows"], get_results)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(err))
    
@router.post("/division",status_code=status.HTTP_201_CREATED)
async def post_division(req: MtrDivisionRequest, db:Session=Depends(get_db)):
    created_data, err = await DivisionService.post_division(db,req)
    if err == None:
        return payload_response(201,"created",created_data)
    else:
        raise HTTPException(status_code= status.HTTP_409_CONFLICT,detail=str(err))
    
@router.get("/division/{id}", status_code=status.HTTP_200_OK)
async def get_division_by_id(id:int, db:Session=Depends(get_db)):
    get_result, err = await DivisionService.get_divison_by_id(db,id)
    if not get_result or err != None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    return payload_response(200,"success",get_result)

@router.patch("/division/{id}",status_code=status.HTTP_201_CREATED)
async def patch_division(id:int, db:Session=Depends(get_db)):
    updated_data, err = await DivisionService.patch_division(db,id)
    if err == None:
        return payload_response(201,"updated",updated_data)
    else:
        print(str(err))
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))
    
@router.put("/division/{id}",status_code=status.HTTP_201_CREATED)
async def update_division(id:int,req:MtrDivisionUpdateRequest, db:Session=Depends(get_db)):
    updated_data, err = await DivisionService.update_division(db, id, req)
    if err == None:
        return payload_response(201,"updated",updated_data)
    else:
        print(str(err))
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))