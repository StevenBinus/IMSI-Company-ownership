from fastapi import APIRouter,Depends,HTTPException,status
from src.repositories.common import ItemGroupRepo
from src.exceptions.RequestException import ResponseException
from src.payloads.schemas.common import ItemGroupSchema
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from src.configs.database import get_db
from src.payloads.responses.GeneralResponse import payload_response

router = APIRouter(tags=["Item Group"],prefix="/api/general")

@router.get("/item-groups", status_code=200)
async def get_item_groups(db:Session=Depends(get_db)):
    item_groups = ItemGroupRepo.get_item_groups_cruds(db,0,100)
    if not item_groups:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    return payload_response(ResponseException(200), "Success",item_groups)

@router.get("/item-group/{item_group_id}", status_code=200)
async def get_item_group(item_group_id, db:Session=Depends(get_db)):
    item_group = ItemGroupRepo.get_item_group_cruds(db, item_group_id)
    if not item_group:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    return payload_response(ResponseException(200), "Success",item_group)

@router.post("/item-group", status_code=201)
async def post_item_group(payload:ItemGroupSchema.MtrItemGroupGetSchema,db:Session=Depends(get_db)):
    try:
        new_item_group = ItemGroupRepo.post_item_group_cruds(db, payload)
        db.add(new_item_group)
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))
    db.refresh(new_item_group)
    return payload_response(ResponseException(201), "Success",new_item_group)

@router.delete("/item-group/{item_group_id}", status_code=204)
async def delete_item_group(item_group_id, db:Session=Depends(get_db)):
    erase_item_group = ItemGroupRepo.delete_item_group_cruds(db,item_group_id)
    if not erase_item_group:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    db.commit()
    return payload_response(ResponseException(204), "Success",erase_item_group)

@router.put("/item-group/{item_group_id}", status_code=202)
async def put_item_group(payload:ItemGroupSchema.MtrItemGroupGetSchema, item_group_id,db:Session=Depends(get_db)):
    update_item_group, update_data_new  = ItemGroupRepo.put_item_group_cruds(db,payload, item_group_id)
    if not update_item_group:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    db.commit()
    db.refresh(update_data_new)
    return payload_response(ResponseException(202), "Success",update_data_new)

@router.patch("/item-group/{item_group_id}", status_code=202)
async def patch_item_group(item_group_id,db:Session=Depends(get_db)):
    active_item_group  = ItemGroupRepo.patch_item_group_cruds(db, item_group_id)
    if not active_item_group:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    active_item_group.is_active = not active_item_group.is_active
    db.commit()
    db.refresh(active_item_group)
    return payload_response(ResponseException(202), "Success",active_item_group.is_active)