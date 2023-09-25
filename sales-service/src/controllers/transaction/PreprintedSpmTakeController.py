from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session
from src.configs.database import get_db
from src.services.transaction import PreprintedSpmTakeService
from src.payloads.schemas.transaction.PreprintedSpmTakeSchema import TakeResponseHeaderDetail,TrxSpmFormTakeRequestDetail, TrxSpmFormTakeDeleteRequest
from src.payloads.responses.CommonResponse import payload_response
from src.payloads.responses.PaginationResponse import pagination_response_detail
from src.payloads.responses.PaginationResponse import pagination_response
from src.exceptions.RequestException import ResponseException
from datetime import datetime

router = APIRouter(tags=["Transaction : Preprinted SPM Take"],prefix="/api/sales")

@router.get("/preprinted-spm-take", status_code=status.HTTP_200_OK)
async def get_all(page:int,limit:int,
                  taken_document_number:str|None=None,
                  spm_issued_by:int|None=None,
                  spm_issued_date_from:datetime|None=None,
                  spm_issued_date_to:datetime|None=None,
                  spm_issued_to:int|None=None,
                  register_document_number:str|None=None,
                  db:Session=Depends(get_db)):
    get_all_params = {
        "taken_document_number": taken_document_number,
        "spm_issued_by": spm_issued_by,
        "spm_issued_date_from": spm_issued_date_from,
        "spm_issued_date_to": spm_issued_date_to,
        "spm_issued_to": spm_issued_to,
        "vehicle_sales_order_document_number": register_document_number
    }
    get_results, pages, err = await PreprintedSpmTakeService.get_spm_takes_search(db,page,limit,get_all_params)
    if get_results == [] or err != None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=ResponseException(404))    
    return pagination_response(200,"success",page,limit,pages["total_pages"],pages["total_rows"],get_results)

@router.get("/preprinted-spm-take-available", status_code=status.HTTP_200_OK)
async def get_available_spm_doc_no(page:int, limit:int,
                                   spm_from:str|None=None,
                                   spm_to:str|None=None,
                                   db:Session=Depends(get_db)):
    get_all_params = {
        "spm_document_number_from": spm_from,
        "spm_document_number_to": spm_to
    }
    get_results, pages, err = await PreprintedSpmTakeService.get_available_spm_doc_no(db,page,limit,get_all_params)
    if get_results == [] or err != None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(err))    
    return pagination_response(200,"success",page,limit,pages["total_pages"],pages["total_rows"],get_results)
    
@router.get("/preprinted-spm-take/{id}",status_code=status.HTTP_200_OK)
async def get_all_spm_take_by_id(id:int,page:int,limit:int,db:Session=Depends(get_db)):
    header,detail,pages,err = await PreprintedSpmTakeService.get_all_spm_take_by_id(db,id,page,limit)
    if detail == [] or err != None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=ResponseException(404)) 
    return pagination_response_detail(200,"Success",page,limit,pages["total_pages"],pages["total_rows"],TakeResponseHeaderDetail(
        taken_system_number=header.taken_system_number,
        taken_document_number=header.taken_document_number,
        spm_issue_date=header.spm_issued_date,
        spm_issued_by=header.spm_issued_by,
        spm_issued_to=header.spm_issued_to,
        spmtakelist=detail
    ))

@router.get("/preprinted-spm-take-available/{id}",status_code=status.HTTP_200_OK)
async def get_available_spm_doc_no_by_id(id:int,db:Session=Depends(get_db)):
    result,err = await PreprintedSpmTakeService.get_available_spm_doc_no_by_id(db,id)
    if result == [] or err != None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(err))    
    return payload_response(200,"Success",result)
    
@router.post("/preprinted-spm-take",status_code=status.HTTP_201_CREATED)
async def post_taken_spm(req_data:TrxSpmFormTakeRequestDetail,db:Session=Depends(get_db)):
    created_data,err =  await PreprintedSpmTakeService.post_taken_spm(db,req_data)
    if err != None:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(err))
    return payload_response(201,"created",created_data)
    
@router.put("/preprinted-spm-take/{id}",status_code=status.HTTP_200_OK)
async def update_detail_taken_spm(id:int,rev_data:TrxSpmFormTakeRequestDetail,db:Session=Depends(get_db)):
    updated_data, err = await PreprintedSpmTakeService.update_detail_taken_spm(db,id,rev_data)
    if err != None:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=ResponseException(409))
    return payload_response(200,"Updated",updated_data)    

@router.put("/preprinted-spm-take-submit/{id}",status_code=status.HTTP_201_CREATED)
async def submit_spm_taken(id:int,db:Session=Depends(get_db)):
    updated_data,err = await PreprintedSpmTakeService.submit_preprinted_spm_taken(db,id)
    if err != None:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Document number already released")
    return payload_response(200,"Updated",updated_data)   

@router.delete("/preprinted-spm-take",status_code=status.HTTP_200_OK)
async def delete_spm(deleted_spm:TrxSpmFormTakeDeleteRequest,db:Session=Depends(get_db)):
    status_deleted = await PreprintedSpmTakeService.delete_spm_taken_assigned(db,deleted_spm)
    if status_deleted != None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(409))
    return {"message":"data deleted"}