from fastapi import APIRouter,Depends,HTTPException,status
from src.repositories.common import ReferenceTypePurchaseRequestRepo
from src.exceptions.RequestException import ResponseException
from src.payloads.schemas.common import ReferenceTypePurchaseRequestSchema
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from src.configs.database import get_db
from src.payloads.responses.GeneralResponse import payload_response

router = APIRouter(tags=["Reference Type Purchase Request"],prefix="/api/general")

@router.get("/reference-type-purchase-requests", status_code=200)
async def get_reference_type_purchase_requests(db:Session=Depends(get_db)):
    reference_type_purchase_requests = ReferenceTypePurchaseRequestRepo.get_reference_type_purchase_requests_cruds(db,0,100)
    if not reference_type_purchase_requests:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    return payload_response(ResponseException(200), "Success",reference_type_purchase_requests)

@router.get("/reference-type-purchase-request/{reference_type_purchase_request_id}", status_code=200)
async def get_reference_type_purchase_request(reference_type_purchase_request_id, db:Session=Depends(get_db)):
    reference_type_purchase_request = ReferenceTypePurchaseRequestRepo.get_reference_type_purchase_request_cruds(db, reference_type_purchase_request_id)
    if not reference_type_purchase_request:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    return payload_response(ResponseException(200), "Success",reference_type_purchase_request)

@router.post("/reference-type-purchase-request", status_code=201)
async def post_reference_type_purchase_request(payload:ReferenceTypePurchaseRequestSchema.MtrReferenceTypePurchaseRequestGetSchema,db:Session=Depends(get_db)):
    try:
        new_reference_type_purchase_request = ReferenceTypePurchaseRequestRepo.post_reference_type_purchase_request_cruds(db, payload)
        db.add(new_reference_type_purchase_request)
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))
    db.refresh(new_reference_type_purchase_request)
    return payload_response(ResponseException(201), "Success",new_reference_type_purchase_request)

@router.delete("/reference-type-purchase-request/{reference_type_purchase_request_id}", status_code=204)
async def delete_reference_type_purchase_request(reference_type_purchase_request_id, db:Session=Depends(get_db)):
    erase_reference_type_purchase_request = ReferenceTypePurchaseRequestRepo.delete_reference_type_purchase_request_cruds(db,reference_type_purchase_request_id)
    if not erase_reference_type_purchase_request:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    db.commit()
    return payload_response(ResponseException(204), "Success",erase_reference_type_purchase_request)

@router.put("/reference-type-purchase-request/{reference_type_purchase_request_id}", status_code=202)
async def put_reference_type_purchase_request(payload:ReferenceTypePurchaseRequestSchema.MtrReferenceTypePurchaseRequestGetSchema, reference_type_purchase_request_id,db:Session=Depends(get_db)):
    update_reference_type_purchase_request, update_data_new  = ReferenceTypePurchaseRequestRepo.put_reference_type_purchase_request_cruds(db,payload, reference_type_purchase_request_id)
    if not update_reference_type_purchase_request:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    db.commit()
    db.refresh(update_data_new)
    return payload_response(ResponseException(202), "Success",update_data_new)

@router.patch("/reference-type-purchase-request/{reference_type_purchase_request_id}", status_code=202)
async def patch_reference_type_purchase_request(reference_type_purchase_request_id,db:Session=Depends(get_db)):
    active_reference_type_purchase_request  = ReferenceTypePurchaseRequestRepo.patch_reference_type_purchase_request_cruds(db, reference_type_purchase_request_id)
    if not active_reference_type_purchase_request:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    active_reference_type_purchase_request.is_active = not active_reference_type_purchase_request.is_active
    db.commit()
    db.refresh(active_reference_type_purchase_request)
    return payload_response(ResponseException(202), "Success",active_reference_type_purchase_request.is_active)