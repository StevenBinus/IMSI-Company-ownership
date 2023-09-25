from fastapi import APIRouter, HTTPException, status, Query, Request
from src.services.master import DocumentMasterService
from src.payloads.schemas.master import DocumentMasterSchema
from src.payloads.responses.GeneralResponse import payload_response
from src.payloads.responses.PaginationResponse import pagination_response
from src.exceptions.RequestException import ResponseException

router = APIRouter(tags=["Document Master"],prefix="/api/general")

@router.get("/document-master", status_code=status.HTTP_200_OK)
async def get_source_document_search(
    page: int,
    limit: int,
    source_document_type_id: int|None=None,
    brand_id: int|None=None,
    profit_center_id: int|None=None,
    transaction_type_id: int|None=None,
    bank_company_id: int|None=None,
    sort_of:str|None=None,sort_by:str|None=None
):
    get_all_params = {
        "source_document_type_id": source_document_type_id,
        "brand_id": brand_id,
        "profit_center_id": profit_center_id,
        "transaction_type_id": transaction_type_id,
        "bank_company_id": bank_company_id
    }
    sort_params={
        "sort_of":sort_of,"sort_by":sort_by
    }

    get_results, pages, err = DocumentMasterService.get_source_document_search(page, limit, get_all_params,sort_params)
    
    if not get_results or err != None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(err))
    else:
        return pagination_response(200, "success", page, limit, pages["total_pages"], pages["total_rows"], get_results)

@router.post("/document-master",status_code=status.HTTP_201_CREATED)
async def post_source_document(req:DocumentMasterSchema.MtrDocumentRequest):
    created_data, err = DocumentMasterService.post_source_document(req)
    if err == None:
        return payload_response(201,"created",created_data)
    else:
        raise HTTPException(status_code= status.HTTP_409_CONFLICT,detail=str(err))
    
@router.get("/document-master/{id}", status_code=status.HTTP_200_OK)
async def get_source_document_by_id(id:int):
    get_result, err = DocumentMasterService.get_source_document_by_id(id)
    if not get_result or err != None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    return payload_response(200,"success",get_result)

@router.patch("/document-master/{id}",status_code=status.HTTP_201_CREATED)
async def patch_source_document(id:int):
    updated_data, err = DocumentMasterService.patch_source_document(id)
    if err == None:
        return payload_response(201,"updated",updated_data)
    else:
        print(str(err))
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))
    
@router.put("/document-master/{id}",status_code=status.HTTP_201_CREATED)
async def update_source_document(id:int,req:DocumentMasterSchema.MtrDocumentRequest):
    updated_data, err = DocumentMasterService.update_source_document(id, req)
    if err == None:
        return payload_response(201,"updated",updated_data)
    else:
        print(str(err))
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))