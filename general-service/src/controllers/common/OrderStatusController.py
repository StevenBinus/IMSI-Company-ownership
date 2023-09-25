from fastapi import APIRouter,Depends,HTTPException,status
from src.repositories.common import OrderStatusRepo
from src.exceptions.RequestException import ResponseException
from src.payloads.schemas.common import OrderStatusSchema
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from src.configs.database import get_db
from src.payloads.responses.GeneralResponse import payload_response

router = APIRouter(tags=["Order Status"],prefix="/api/general")

@router.get("/order-status", status_code=200)
async def get_order_statuss(db:Session=Depends(get_db)):
    order_statuss = OrderStatusRepo.get_order_statuss_cruds(db,0,100)
    if not order_statuss:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    return payload_response(ResponseException(200), "Success",order_statuss)

@router.get("/order-status/{order_status_id}", status_code=200)
async def get_order_status(order_status_id, db:Session=Depends(get_db)):
    order_status = OrderStatusRepo.get_order_status_cruds(db, order_status_id)
    if not order_status:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    return payload_response(ResponseException(200), "Success",order_status)

@router.post("/order-status", status_code=201)
async def post_order_status(payload:OrderStatusSchema.MtrOrderStatusGetSchema,db:Session=Depends(get_db)):
    try :
        new_order_status = OrderStatusRepo.post_order_status_cruds(db, payload)
        db.add(new_order_status)
        db.commit()
    except IntegrityError :
        db.rollback()
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))
    db.refresh(new_order_status)
    return payload_response(ResponseException(201), "Success",new_order_status)

@router.delete("/order-status/{order_status_id}", status_code=204)
async def delete_order_status(order_status_id, db:Session=Depends(get_db)):
    erase_order_status = OrderStatusRepo.delete_order_status_cruds(db,order_status_id)
    if not erase_order_status:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    db.commit()
    return payload_response(ResponseException(204), "Success",erase_order_status)

@router.put("/order-status/{order_status_id}", status_code=202)
async def put_order_status(payload:OrderStatusSchema.MtrOrderStatusGetSchema, order_status_id,db:Session=Depends(get_db)):
    update_order_status, updated_data  = OrderStatusRepo.put_order_status_cruds(db,payload, order_status_id)
    if not update_order_status:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    db.commit()
    db.refresh(updated_data)
    return payload_response(ResponseException(202), "Success",updated_data)

@router.patch("/order-status/{order_status_id}", status_code=202)
async def patch_order_status(order_status_id,db:Session=Depends(get_db)):
    active_order_status= OrderStatusRepo.patch_order_status_cruds(db, order_status_id)
    if not active_order_status:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    active_order_status.is_active = not active_order_status.is_active
    db.commit()
    db.refresh(active_order_status)
    return payload_response(ResponseException(202), "Success",active_order_status.is_active)