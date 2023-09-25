from fastapi import APIRouter,Depends,HTTPException,status
from src.repositories.common import PriceListCodeRepo
from src.exceptions.RequestException import ResponseException
from src.payloads.schemas.common import PriceListCodeSchema
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from src.configs.database import get_db
from src.payloads.responses.GeneralResponse import payload_response

router = APIRouter(tags=["Price List Code"],prefix="/api/general")

@router.get("/price-list-codes", status_code=200)
async def get_price_list_codes(db:Session=Depends(get_db)):
    price_list_codes = PriceListCodeRepo.get_price_list_codes_cruds(db,0,100)
    if not price_list_codes:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    return payload_response(ResponseException(200), "Success",price_list_codes)

@router.get("/price-list-code/{price_list_code_id}", status_code=200)
async def get_price_list_code(price_list_code_id = None, db:Session=Depends(get_db)):
    price_list_code = PriceListCodeRepo.get_price_list_code_cruds(db, price_list_code_id)
    if not price_list_code:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    return payload_response(ResponseException(200), "Success",price_list_code)

@router.post("/price-list-code", status_code=201)
async def post_price_list_code(payload:PriceListCodeSchema.MtrPriceListCodeGetSchema,db:Session=Depends(get_db)):
    try:
        new_price_list_code = PriceListCodeRepo.post_price_list_code_cruds(db, payload)
        db.add(new_price_list_code)
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))
    db.refresh(new_price_list_code)
    return payload_response(ResponseException(201), "Success",new_price_list_code)

@router.delete("/price-list-code/{price_list_code_id}", status_code=204)
async def delete_price_list_code(price_list_code_id, db:Session=Depends(get_db)):
    erase_price_list_code = PriceListCodeRepo.delete_price_list_code_cruds(db,price_list_code_id)
    if not erase_price_list_code:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    db.commit()
    return payload_response(ResponseException(204), "Success",erase_price_list_code)

@router.put("/price-list-code/{price_list_code_id}", status_code=202)
async def put_price_list_code(payload:PriceListCodeSchema.MtrPriceListCodeGetSchema, price_list_code_id,db:Session=Depends(get_db)):
    update_price_list_code, update_data_new  = PriceListCodeRepo.put_price_list_code_cruds(db,payload, price_list_code_id)
    if not update_price_list_code:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    db.commit()
    db.refresh(update_data_new)
    return payload_response(ResponseException(202), "Success",update_data_new)

@router.patch("/price-list-code/{price_list_code_id}", status_code=202)
async def patch_price_list_code(price_list_code_id,db:Session=Depends(get_db)):
    active_price_list_code  = PriceListCodeRepo.patch_price_list_code_cruds(db, price_list_code_id)
    if not active_price_list_code:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    active_price_list_code.is_active = not active_price_list_code.is_active
    db.commit()
    db.refresh(active_price_list_code)
    return payload_response(ResponseException(202), "Success",active_price_list_code.is_active)