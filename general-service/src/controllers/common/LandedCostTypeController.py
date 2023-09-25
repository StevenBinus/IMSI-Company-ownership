from fastapi import APIRouter,Depends,HTTPException,status
from src.repositories.common import LandedCostTypeRepo
from src.exceptions.RequestException import ResponseException
from src.payloads.schemas.common import LandedCostTypeSchema
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from src.configs.database import get_db
from src.payloads.responses.GeneralResponse import payload_response

router = APIRouter(tags=["Landed Cost Type"],prefix="/api/general")

@router.get("/landed-cost-type", status_code=200)
async def get_landed_cost_types(db:Session=Depends(get_db)):
    landed_cost_types = LandedCostTypeRepo.get_landed_cost_type_cruds(db,0,100)
    if not landed_cost_types:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    return payload_response(ResponseException(200), "Success",landed_cost_types)

@router.get("/landed-cost-type/{landed_cost_type_id}", status_code=200)
async def get_landed_cost_type(landed_cost_type_id, db:Session=Depends(get_db)):
    landed_cost_type = LandedCostTypeRepo.get_landed_cost_type_cruds(db, landed_cost_type_id)
    if not landed_cost_type:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    return payload_response(ResponseException(200), "Success",landed_cost_type)

@router.post("/landed-cost-type", status_code=201)
async def post_landed_cost_type(payload:LandedCostTypeSchema.MtrLandedCostTypeGetSchema,db:Session=Depends(get_db)):
    try :
        new_landed_cost_type = LandedCostTypeRepo.post_landed_cost_type_cruds(db, payload)
        db.add(new_landed_cost_type)
        db.commit()
    except IntegrityError :
        db.rollback()
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))
    db.refresh(new_landed_cost_type)
    return payload_response(ResponseException(201), "Success",new_landed_cost_type)

@router.delete("/landed-cost-type/{landed_cost_type_id}", status_code=204)
async def delete_landed_cost_type(landed_cost_type_id, db:Session=Depends(get_db)):
    erase_landed_cost_type = LandedCostTypeRepo.delete_landed_cost_type(db,landed_cost_type_id)
    if not erase_landed_cost_type:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    db.commit()
    return payload_response(ResponseException(204), "Success",erase_landed_cost_type)

@router.put("/landed-cost-type/{landed_cost_type_id}", status_code=202)
async def put_landed_cost_type(payload:LandedCostTypeSchema.MtrLandedCostTypeGetSchema, landed_cost_type_id,db:Session=Depends(get_db)):
    update_landed_cost_type, updated_data  = LandedCostTypeRepo.put_landed_cost_type_cruds(db,payload, landed_cost_type_id)
    if not update_landed_cost_type:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    db.commit()
    db.refresh(updated_data)
    return payload_response(ResponseException(202), "Success",updated_data)

@router.patch("/landed-cost-type/{landed_cost_type_id}", status_code=202)
async def patch_landed_cost_type(landed_cost_type_id,db:Session=Depends(get_db)):
    active_landed_cost_type  = LandedCostTypeRepo.patch_landed_cost_type_cruds(db, landed_cost_type_id)
    if not active_landed_cost_type:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    active_landed_cost_type.is_active = not active_landed_cost_type.is_active
    db.commit()
    db.refresh(active_landed_cost_type)
    return payload_response(ResponseException(202), "Success",active_landed_cost_type.is_active)