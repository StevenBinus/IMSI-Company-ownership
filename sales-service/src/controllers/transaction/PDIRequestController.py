from fastapi import APIRouter, HTTPException, status, Query, Request
from src.services.transaction import PDIRequestService
from src.payloads.schemas.transaction import PDIRequestSchema
from src.payloads.responses.CommonResponse import payload_response,payload_response_detail
from src.payloads.responses.PaginationResponse import pagination_response
from src.exceptions.RequestException import ResponseException
from datetime import datetime

router = APIRouter(tags=["Transaction : PDI Request"],prefix="/api/sales")


@router.get("/pdi-requests", status_code=200)
async def get_all_pdi_requests(page:int, limit:int, query_of:list[str]=Query(None), query_by:list[str]=Query(None)):
    get_results, pages, err = PDIRequestService.get_all_pdi_requests(page,limit,query_of,query_by)
    if err == None:
        return pagination_response(200,"Success",page,limit,pages["total_pages"],pages["total_rows"],get_results)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=str(err))

#Submit
@router.post("/pdi-request",status_code=status.HTTP_201_CREATED)
async def post_pdi_request(req_data:PDIRequestSchema.TrxPDIRequestAllSchema):
    created_data, err = PDIRequestService.post_pdi_request(req_data)
    if err == None:
        return payload_response(201,"created",created_data)
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(err))

#Add Line
@router.post("/pdi-request-detail",status_code=status.HTTP_201_CREATED)
async def post_pdi_request_detail(req_data:PDIRequestSchema.TrxPDIRequestDetailSchema):
    created_data, err = PDIRequestService.post_pdi_request_detail(req_data)
    if err == None:
        return payload_response(201,"created",created_data)
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(err))
    
#Void    
@router.delete("/pdi-request/{pdi_request_system_number}",status_code=204)
async def delete_pdi_request(pdi_request_system_number:int):
    erase_data, err = PDIRequestService.delete_pdi_request(pdi_request_system_number)
    if err == None:
        return payload_response(204,"Deleted",erase_data)
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))
    
#Get by id
@router.get("/pdi-request/{pdi_request_system_number}", status_code=200)
async def get_by_id_pdi_request(pdi_request_system_number:int):
    get_result, err = PDIRequestService.get_by_id_pdi_request(pdi_request_system_number)
    if not get_result and err == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    return payload_response(200,"Success",get_result)

#Search
@router.get("/pdi-request-search", status_code=status.HTTP_200_OK)
async def get_pdi_request_by_search(
    page:int, 
    limit:int,
    vehicle_model_id:int|None=None,
    vehicle_variant_id:int|None=None,
    vehicle_colour_id:int|None=None,
    vehicle_chassis_number:str|None=None,
    service_dealer_id:int|None=None,
    pdi_request_document_number:str|None=None
    ):
        get_all_params = {"vehicle_model_id":vehicle_model_id,
                    "vehicle_variant_id":vehicle_variant_id,
                    "vehicle_colour_id":vehicle_colour_id,
                    "service_dealer_id":service_dealer_id,
                    "vehicle_chassis_number":vehicle_chassis_number,
                    "service_dealer_id":service_dealer_id,
                    "pdi_request_document_number":pdi_request_document_number
        }

        get_results, pages, err = PDIRequestService.get_by_search_pdi_request(page,limit,get_all_params)
                                                                                                      
        if not get_results or err != None:
            raise HTTPException(status_code=404, detail=str(err))   
        else:
            return pagination_response(200,"success",page,limit,pages["total_pages"],pages["total_rows"],get_results)
        

#Double click grid
@router.get("/pdi-request-full/{id}")
async def get_full_detail_pdi_request_by_id(id:int):
    header,detail,err = PDIRequestService.get_full_detail_pdi_request_by_id(id)
    if not header or err != None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=ResponseException(404)) 
    else:
        

        return payload_response_detail(200,"success",PDIRequestSchema.TrxPDIRequestResponseHeaderDetail(
            brand_id=header.brand_id,
            pdi_request_document_number=header.pdi_request_document_number,
            pdi_request_date=header.pdi_request_date,
            company_id=header.company_id,
            issued_by_id=header.issued_by_id,
            service_dealer_id=header.service_dealer_id,
            service_by_id=header.service_by_id,
            total_frt=header.total_frt,
            pdi_request_remark=header.pdi_request_remark,
            pdirequestlist=detail
        ))
    

#Close order
@router.patch("/pdi-request/{pdi_request_system_number}",status_code=201)
async def patch_pdi_request(pdi_request_system_number:int, pdi_request_detail_line_number:int):
    updated_data, err = PDIRequestService.patch_pdi_request(pdi_request_system_number, pdi_request_detail_line_number)
    if err == None:
        return payload_response(201,"Updated",updated_data)
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=str(err))