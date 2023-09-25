from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session
from src.configs.database import get_db
from src.services.transaction import PreprintedSpmRegisterService
from src.payloads.schemas.transaction import PreprintedSpmRegisterSchema
from src.payloads.responses.CommonResponse import payload_response,payload_response_detail
from src.payloads.responses.PaginationResponse import pagination_response
from src.exceptions.RequestException import ResponseException
from datetime import datetime

from src.repositories.transaction import PreprintedSpmRegisterRepo

router = APIRouter(tags=["Transaction : Preprinted SPM Register"],prefix="/api/sales")

@router.get("/preprinted-spm-register-search", status_code=status.HTTP_200_OK)
async def get_header_preprinted_spm_register_search(page:int, 
                                              limit:int,
                                              register_document_number:str|None=None,
                                              spm_received_by:str|None=None,
                                              spm_received_date_from:datetime|None=None,
                                              spm_received_date_to:datetime|None=None,
                                              spm_number_format:str|None=None,
                                              spm_number_from:int|None=None,
                                              total_spm:int|None=None,
                                              db:Session=Depends(get_db)):


    get_all_params = {"register_document_number":register_document_number,
                    "spm_received_by":spm_received_by,
                    "spm_received_date_from":spm_received_date_from,
                    "spm_received_date_to":spm_received_date_to,
                    "spm_number_format":spm_number_format,
                    "spm_number_from":spm_number_from,
                    "total_spm":total_spm}

    
    get_results, pages, err = await PreprintedSpmRegisterRepo.get_header_preprinted_spm_register_search(db,page,limit,get_all_params)
                                                                                                      
    if not get_results or err != None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    else:
        return pagination_response(200,"success",page,limit,pages["total_pages"],pages["total_rows"],get_results)


@router.get("/preprinted-spm-register/{id}", status_code=status.HTTP_200_OK)
async def get_header_preprinted_spm_register_by_id(id:int,db:Session=Depends(get_db)):
    header,detail, err = await PreprintedSpmRegisterService.get_header_preprinted_spm_register_by_id(db,id)
    if not header and not detail and err == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    return payload_response_detail(200,"success",PreprintedSpmRegisterSchema.SpmFormRegisterHeaderDetailResponse(
        company_id=header.company_id,
        register_document_number=header.register_document_number,
        spm_received_date=header.spm_received_date,
        spm_received_by=header.spm_received_by,
        spm_number_format=header.spm_number_format,
        spm_number_from=header.spm_number_from,
        total_spm=header.total_spm,
        list_spm=detail
    ))
    
@router.post("/preprinted-spm-register",status_code=status.HTTP_201_CREATED)
async def post_preprinted_spm_register_preprinted_spm_register(req_data:PreprintedSpmRegisterSchema.SpmFormRegisterRequest,db:Session=Depends(get_db)):
    created_data, err = await PreprintedSpmRegisterService.post_preprinted_spm_register(db,req_data)
    if err != None:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(err))
    return payload_response(201,"created",created_data)
        
    
@router.get("/preprinted-spm-register-detail",status_code=status.HTTP_200_OK)
async def get_detail_preprinted_spm_register(db:Session=Depends(get_db)):
    get_details, err = await PreprintedSpmRegisterService.get_detail_preprinted_spm_register(db)
    if get_details == [] or err != None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=ResponseException(404))
    return payload_response(200,"success",get_details)