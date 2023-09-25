from fastapi import APIRouter,Depends,HTTPException,status
from src.repositories.common import LineTypeRepo
from src.exceptions.RequestException import ResponseException
from src.payloads.schemas.common import LineTypeSchema
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from src.configs.database import get_db
from src.payloads.responses.GeneralResponse import payload_response

router = APIRouter(tags=["Line Type"],prefix="/api/general")

@router.get("/line-types", status_code=200)
async def get_line_types(db:Session=Depends(get_db)):
    line_types = LineTypeRepo.get_line_types_cruds(db,0,100)
    if not line_types:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    return payload_response(ResponseException(200), "Success",line_types)

@router.get("/line-type/{line_type_id}", status_code=200)
async def get_line_type(line_type_id, db:Session=Depends(get_db)):
    line_type = LineTypeRepo.get_line_type_cruds(db, line_type_id)
    if not line_type:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    return payload_response(ResponseException(200), "Success",line_type)

@router.post("/line-type", status_code=201)
async def post_line_type(payload:LineTypeSchema.MtrLineTypeGetSchema,db:Session=Depends(get_db)):
    try:
        new_line_type = LineTypeRepo.post_line_type_cruds(db, payload)
        db.add(new_line_type)
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))
    db.refresh(new_line_type)
    return payload_response(ResponseException(201), "Success",new_line_type)

@router.delete("/line-type/{line_type_id}", status_code=204)
async def delete_line_type(line_type_id, db:Session=Depends(get_db)):
    erase_line_type = LineTypeRepo.delete_line_type_cruds(db,line_type_id)
    if not erase_line_type:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    db.commit()
    return payload_response(ResponseException(204), "Success",erase_line_type)

@router.put("/line-type/{line_type_id}", status_code=202)
async def put_line_type(payload:LineTypeSchema.MtrLineTypeGetSchema, line_type_id,db:Session=Depends(get_db)):
    update_line_type, update_data_new  = LineTypeRepo.put_line_type_cruds(db,payload, line_type_id)
    if not update_line_type:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    db.commit()
    db.refresh(update_data_new)
    return payload_response(ResponseException(202), "Success",update_data_new)

@router.patch("/line-type/{line_type_id}", status_code=202)
async def patch_line_type(line_type_id,db:Session=Depends(get_db)):
    active_line_type  = LineTypeRepo.patch_line_type_cruds(db, line_type_id)
    if not active_line_type:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    active_line_type.is_active = not active_line_type.is_active
    db.commit()
    db.refresh(active_line_type)
    return payload_response(ResponseException(202), "Success",active_line_type.is_active)