from fastapi import APIRouter,Depends,HTTPException,status
from src.repositories.common import GeneralLedgerProcessRepo
from src.exceptions.RequestException import ResponseException
from src.payloads.schemas.common import GeneralLedgerProcessSchema
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from src.configs.database import get_db
from src.payloads.responses.GeneralResponse import payload_response

router = APIRouter(tags=["General Ledger Process"],prefix="/api/general")

@router.get("/general-ledger-processs", status_code=200)
async def get_general_ledger_processs(db:Session=Depends(get_db)):
    general_ledger_processs = GeneralLedgerProcessRepo.get_general_ledger_processs_cruds(db,0,100)
    if not general_ledger_processs:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    return payload_response(ResponseException(200), "Success",general_ledger_processs)

@router.get("/general-ledger-process/{general_ledger_process_id}", status_code=200)
async def get_general_ledger_process(general_ledger_process_id, db:Session=Depends(get_db)):
    general_ledger_process = GeneralLedgerProcessRepo.get_general_ledger_process_cruds(db, general_ledger_process_id)
    if not general_ledger_process:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    return payload_response(ResponseException(200), "Success",general_ledger_process)

@router.post("/general-ledger-process", status_code=201)
async def post_general_ledger_process(payload:GeneralLedgerProcessSchema.MtrGeneralLedgerProcessGetSchema,db:Session=Depends(get_db)):
    try:
        new_general_ledger_process = GeneralLedgerProcessRepo.post_general_ledger_process_cruds(db, payload)
        db.add(new_general_ledger_process)
        db.commit()
    except IntegrityError:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))
    db.refresh(new_general_ledger_process)
    return payload_response(ResponseException(201), "Success",new_general_ledger_process)

@router.delete("/general-ledger-process/{general_ledger_process_id}", status_code=204)
async def delete_general_ledger_process(general_ledger_process_id, db:Session=Depends(get_db)):
    erase_general_ledger_process = GeneralLedgerProcessRepo.delete_general_ledger_process_cruds(db,general_ledger_process_id)
    if not erase_general_ledger_process:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    db.commit()
    return payload_response(ResponseException(204), "Success",erase_general_ledger_process)

@router.put("/general-ledger-process/{general_ledger_process_id}", status_code=202)
async def put_general_ledger_process(payload:GeneralLedgerProcessSchema.MtrGeneralLedgerProcessGetSchema, general_ledger_process_id,db:Session=Depends(get_db)):
    update_general_ledger_process, update_data_new  = GeneralLedgerProcessRepo.put_general_ledger_process_cruds(db,payload, general_ledger_process_id)
    if not update_general_ledger_process:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    db.commit()
    db.refresh(update_data_new)
    return payload_response(ResponseException(202), "Success",update_data_new)

@router.patch("/general-ledger-process/{general_ledger_process_id}", status_code=202)
async def patch_general_ledger_process(general_ledger_process_id,db:Session=Depends(get_db)):
    active_general_ledger_process  = GeneralLedgerProcessRepo.patch_general_ledger_process_cruds(db, general_ledger_process_id)
    if not active_general_ledger_process:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    active_general_ledger_process.is_active = not active_general_ledger_process.is_active
    db.commit()
    db.refresh(active_general_ledger_process)
    return payload_response(ResponseException(202), "Success",active_general_ledger_process.is_active)