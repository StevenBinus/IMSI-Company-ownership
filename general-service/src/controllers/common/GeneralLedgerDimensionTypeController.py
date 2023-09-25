from fastapi import APIRouter,Depends,HTTPException,status
from src.repositories.common import GeneralLedgerDimensionTypeRepo
from src.exceptions.RequestException import ResponseException
from src.payloads.schemas.common import GeneralLedgerDimensionTypeSchema
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from src.configs.database import get_db
from src.payloads.responses.GeneralResponse import payload_response

router = APIRouter(tags=["General Ledger Dimension Type"],prefix="/api/general")

@router.get("/general-ledger-dimension-types", status_code=200)
async def get_general_ledger_dimension_types(db:Session=Depends(get_db)):
    general_ledger_dimension_types = GeneralLedgerDimensionTypeRepo.get_general_ledger_dimension_types_cruds(db,0,100)
    if not general_ledger_dimension_types:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    return payload_response(ResponseException(200), "Success",general_ledger_dimension_types)

@router.get("/general-ledger-dimension-type/{general_ledger_dimension_type_id}", status_code=200)
async def get_general_ledger_dimension_type(general_ledger_dimension_type_id, db:Session=Depends(get_db)):
    general_ledger_dimension_type = GeneralLedgerDimensionTypeRepo.get_general_ledger_dimension_type_cruds(db, general_ledger_dimension_type_id)
    if not general_ledger_dimension_type:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    return payload_response(ResponseException(200), "Success",general_ledger_dimension_type)

@router.post("/general-ledger-dimension-type", status_code=201)
async def post_general_ledger_dimension_type(payload:GeneralLedgerDimensionTypeSchema.MtrGeneralLedgerDimensionTypeGetSchema,db:Session=Depends(get_db)):
    try :
        new_general_ledger_dimension_type = GeneralLedgerDimensionTypeRepo.post_general_ledger_dimension_type_cruds(db, payload)
        db.add(new_general_ledger_dimension_type)
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))
    db.refresh(new_general_ledger_dimension_type)
    return payload_response(ResponseException(201), "Success",new_general_ledger_dimension_type)

@router.delete("/general-ledger-dimension-type/{general_ledger_dimension_type_id}", status_code=204)
async def delete_general_ledger_dimension_type(general_ledger_dimension_type_id, db:Session=Depends(get_db)):
    erase_general_ledger_dimension_type = GeneralLedgerDimensionTypeRepo.delete_general_ledger_dimension_type_cruds(db,general_ledger_dimension_type_id)
    if not erase_general_ledger_dimension_type:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    db.commit()
    return payload_response(ResponseException(204), "Success",erase_general_ledger_dimension_type)

@router.put("/general-ledger-dimension-type/{general_ledger_dimension_type_id}", status_code=202)
async def put_general_ledger_dimension_type(payload:GeneralLedgerDimensionTypeSchema.MtrGeneralLedgerDimensionTypeGetSchema, general_ledger_dimension_type_id,db:Session=Depends(get_db)):
    update_general_ledger_dimension_type, update_data_new  = GeneralLedgerDimensionTypeRepo.put_general_ledger_dimension_type_cruds(db,payload, general_ledger_dimension_type_id)
    if not update_general_ledger_dimension_type:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    db.commit()
    db.refresh(update_data_new)
    return payload_response(ResponseException(202), "Success",update_data_new)

@router.patch("/general-ledger-dimension-type/{general_ledger_dimension_type_id}", status_code=202)
async def patch_general_ledger_dimension_type(general_ledger_dimension_type_id,db:Session=Depends(get_db)):
    active_general_ledger_dimension_type  = GeneralLedgerDimensionTypeRepo.patch_general_ledger_dimension_type_cruds(db, general_ledger_dimension_type_id)
    if not active_general_ledger_dimension_type:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    active_general_ledger_dimension_type.is_active = not active_general_ledger_dimension_type.is_active
    db.commit()
    db.refresh(active_general_ledger_dimension_type)
    return payload_response(ResponseException(202), "Success",active_general_ledger_dimension_type.is_active)