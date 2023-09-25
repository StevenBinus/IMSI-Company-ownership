from fastapi import APIRouter,Depends,HTTPException,status
from src.repositories.common import IncentiveLevelRepo
from src.exceptions.RequestException import ResponseException
from src.payloads.schemas.common import IncentiveLevelSchema
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from src.configs.database import get_db
from src.payloads.responses.GeneralResponse import payload_response

router = APIRouter(tags=["Incentive Level"],prefix="/api/general")

@router.get("/incentive-levels", status_code=200)
async def get_incentive_levels(db:Session=Depends(get_db)):
    incentive_levels = IncentiveLevelRepo.get_incentive_levels_cruds(db,0,100)
    if not incentive_levels:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    return payload_response(ResponseException(200), "Success",incentive_levels)

@router.get("/incentive-level/{incentive_level_id}", status_code=200)
async def get_incentive_level(incentive_level_id, db:Session=Depends(get_db)):
    incentive_level = IncentiveLevelRepo.get_incentive_level_cruds(db, incentive_level_id)
    if not incentive_level:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    return payload_response(ResponseException(200), "Success",incentive_level)

@router.post("/incentive-level", status_code=201)
async def post_incentive_level(payload:IncentiveLevelSchema.MtrIncentiveLevelGetSchema,db:Session=Depends(get_db)):
    try:
        new_incentive_level = IncentiveLevelRepo.post_incentive_level_cruds(db, payload)
        db.add(new_incentive_level)
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))
    db.refresh(new_incentive_level)
    return payload_response(ResponseException(201), "Success",new_incentive_level)

@router.delete("/incentive-level/{incentive_level_id}", status_code=204)
async def delete_incentive_level(incentive_level_id, db:Session=Depends(get_db)):
    erase_incentive_level = IncentiveLevelRepo.delete_incentive_level_cruds(db,incentive_level_id)
    if not erase_incentive_level:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    db.commit()
    return payload_response(ResponseException(204), "Success",erase_incentive_level)

@router.put("/incentive-level/{incentive_level_id}", status_code=202)
async def put_incentive_level(payload:IncentiveLevelSchema.MtrIncentiveLevelGetSchema, incentive_level_id,db:Session=Depends(get_db)):
    update_incentive_level, update_data_new  = IncentiveLevelRepo.put_incentive_level_cruds(db,payload, incentive_level_id)
    if not update_incentive_level:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    db.commit()
    db.refresh(update_data_new)
    return payload_response(ResponseException(202), "Success",update_data_new)

@router.patch("/incentive-level/{incentive_level_id}", status_code=202)
async def patch_incentive_level(incentive_level_id,db:Session=Depends(get_db)):
    active_incentive_level  = IncentiveLevelRepo.patch_incentive_level_cruds(db, incentive_level_id)
    if not active_incentive_level:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    active_incentive_level.is_active = not active_incentive_level.is_active
    db.commit()
    db.refresh(active_incentive_level)
    return payload_response(ResponseException(202), "Success",active_incentive_level.is_active)