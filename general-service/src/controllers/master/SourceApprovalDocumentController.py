from fastapi import APIRouter,HTTPException,status,Request
from src.exceptions.RequestException import ResponseException
from src.payloads.schemas.master import SourceApprovalDocumentSchema
from src.payloads.responses.GeneralResponse import payload_response
from src.payloads.responses.PaginationResponse import pagination_response
from src.services.common import SourceApprovalDocumentService

router = APIRouter(tags=["Source Approval Document"],prefix="/api/general")

@router.get("/source-approval-documents", status_code=200)
async def get_source_approval_documents(page:int,limit:int,
                                        is_active:bool|None=None,
                                        source_approval_document_id:str|None=None,
                                        source_approval_document_code:str|None=None,
                                        source_approval_document_name:str|None=None,
                                        sort_of:str|None=None,
                                        sort_by:str|None=None):
    get_all_params={"is_active":is_active, "source_approval_document_id":source_approval_document_id,"source_approval_document_code":source_approval_document_code,"source_approval_document_name":source_approval_document_name}
    sort_params ={"sort_of":sort_of,"sort_by":sort_by}
    get_result,pages,err = SourceApprovalDocumentService.get_source_approval_documents_cruds(page,limit,get_all_params,sort_params)
    if err == None and get_result !=[]:
        return pagination_response(200,"Success",page,limit,pages["total_pages"],pages["total_rows"],get_result)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))


@router.get("/source-approval-document/{source_approval_document_id}", status_code=200)
async def get_source_approval_document(source_approval_documemnt_id:int):
    source_approval_document = SourceApprovalDocumentService.get_source_approval_document_cruds(source_approval_documemnt_id)
    if not source_approval_document:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    return payload_response(ResponseException(200), "Success",source_approval_document)

@router.post("/source-approval-document", status_code=201)
async def post_source_approval_document(req:SourceApprovalDocumentSchema.MtrSourceApprovalDocumentGetSchema):
    new_source_approval_document,err = SourceApprovalDocumentService.post_source_approval_document_cruds(req)
    if err == None:
        return payload_response(201,"Success",new_source_approval_document)
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))

@router.delete("/source-approval-document/{source_approval_document_id}", status_code=204)
async def delete_source_approval_document(source_approval_documemnt_id:int):
    erase_source_approval_document,err = SourceApprovalDocumentService.delete_source_approval_document(source_approval_documemnt_id)
    if err == None:
        return pagination_response(204,"Success",erase_source_approval_document)
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))

@router.put("/source-approval-document/{source_approval_document_id}", status_code=202)
async def put_source_approval_document(source_approval_document_id:int,req:SourceApprovalDocumentSchema.MtrSourceApprovalDocumentGetSchema):
    update_source_approval_document, err = SourceApprovalDocumentService.put_source_approval_document(source_approval_document_id,req)
    if err == None:
        return pagination_response(202,"Success",update_source_approval_document)
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))

@router.patch("/source-approval-document/{source_approval_document_id}", status_code=202)
async def patch_source_approval_document(source_approval_document_id:int):
    active_source_approval_document,err = SourceApprovalDocumentService.patch_source_approval_document_cruds(source_approval_document_id)
    if err == None:
        return pagination_response(202,"Success",active_source_approval_document)
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))