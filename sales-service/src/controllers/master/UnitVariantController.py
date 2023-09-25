from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session
from src.configs.database import get_db
from src.services.master import UnitVariantService
from src.payloads.schemas.master.UnitVariantSchema import UnitVariantRequest
from src.payloads.responses.CommonResponse import payload_response
from src.payloads.responses.PaginationResponse import pagination_response
from src.exceptions.RequestException import ResponseException

router = APIRouter(tags=["Master : Unit Variant"],prefix="/api/sales")

@router.get("/unit-variant")
async def get_unitvariants(page:int, 
                           limit:int, 
                           variant_code:str|None=None,
                           variant_description:str|None=None,
                           model_code:str|None=None,
                           model_description:str|None=None,
                           is_active:bool|None=None,
                           sort_by:str|None=None,
                           sort_of:str|None=None,
                           db:Session=Depends(get_db)):
    
    all_params = {
        "variant_code":variant_code,
        "variant_description":variant_description,
        "model_code":model_code,
        "model_description":model_description,
        "is_active":is_active,
    }

    sort_params = {
        "sort_by":sort_by,
        "sort_of":sort_of
    }

    results,pages,err = await UnitVariantService.get_unit_variants_list_all(db,page,limit,all_params,sort_params)
    if results == [] or err != None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    return pagination_response(200,"Success",page,limit,pages["total_pages"],pages["total_rows"],results)

@router.get("/unit-variant/drop-down/{model_id}")
async def get_unit_model_drop_down(model_id:int,db:Session=Depends(get_db)):
    results, err = await UnitVariantService.get_unit_variant_drop_down(db,model_id)
    if results == [] or err != None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=str(err))
    return payload_response(200,"Success",results)  

@router.post("/unit-variant")
async def post_unit_variant(req:UnitVariantRequest,db:Session=Depends(get_db)):
    created_data, err = await UnitVariantService.post_unit_variant(db,req)
    if err != None:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))
    return payload_response(200,"created",created_data)

@router.put("/unit-variant/{id}")
async def update_unit_variant(id:int,req:UnitVariantRequest,db:Session=Depends(get_db)):
    updated_data, err = await UnitVariantService.update_unit_variant(db,id,req)
    if err != None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=ResponseException(400))
    return updated_data

@router.patch("/unit-variant/{id}")
async def patch_unit_variant(id:int,db:Session=Depends(get_db)):
    active_status,err = await UnitVariantService.patch_unit_variant(db,id)
    if err != None:
        active_status = None
    return active_status