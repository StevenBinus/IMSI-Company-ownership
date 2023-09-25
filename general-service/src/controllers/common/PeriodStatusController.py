from fastapi import APIRouter,Depends,HTTPException,status
from src.repositories.common import PeriodStatusRepo
from src.exceptions.RequestException import ResponseException
from src.payloads.schemas.common import PeriodStatusSchema
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from src.configs.database import get_db
from src.payloads.responses.GeneralResponse import payload_response

router = APIRouter(tags=["Period Status"],prefix="/api/general")

@router.get("/period-status", status_code=200)
async def get_period_statuss(db:Session=Depends(get_db)):
    period_statuss = PeriodStatusRepo.get_period_statuss_cruds(db,0,100)
    if not period_statuss:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    return payload_response(ResponseException(200), "Success",period_statuss)

@router.get("/period-status/{period_status_id}", status_code=200)
async def get_period_status(period_status_id, db:Session=Depends(get_db)):
    period_status = PeriodStatusRepo.get_period_status_cruds(db, period_status_id)
    if not period_status:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    return payload_response(ResponseException(200), "Success",period_status)

@router.post("/period-status", status_code=201)
async def post_period_status(payload:PeriodStatusSchema.MtrPeriodStatusGetSchema,db:Session=Depends(get_db)):
    try :
        new_period_status = PeriodStatusRepo.post_period_status_cruds(db, payload)
        db.add(new_period_status)
        db.commit()
    except IntegrityError :
        db.rollback()
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))
    db.refresh(new_period_status)
    return payload_response(ResponseException(201), "Success",new_period_status)

@router.delete("/period-status/{period_status_id}", status_code=204)
async def delete_period_status(period_status_id, db:Session=Depends(get_db)):
    erase_period_status = PeriodStatusRepo.delete_period_status_cruds(db,period_status_id)
    if not erase_period_status:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    db.commit()
    return payload_response(ResponseException(204), "Success",erase_period_status)

@router.put("/period-status/{period_status_id}", status_code=202)
async def put_period_status(payload:PeriodStatusSchema.MtrPeriodStatusGetSchema, period_status_id,db:Session=Depends(get_db)):
    update_period_status, updated_data  = PeriodStatusRepo.put_period_status_cruds(db,payload, period_status_id)
    if not update_period_status:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    db.commit()
    db.refresh(updated_data)
    return payload_response(ResponseException(202), "Success",updated_data)

@router.patch("/period-status/{period_status_id}", status_code=202)
async def patch_period_status(period_status_id,db:Session=Depends(get_db)):
    active_period_status  = PeriodStatusRepo.patch_period_status_cruds(db, period_status_id)
    if not active_period_status:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    active_period_status.is_active = not active_period_status.is_active
    db.commit()
    db.refresh(active_period_status)
    return payload_response(ResponseException(202), "Success",active_period_status.is_active)