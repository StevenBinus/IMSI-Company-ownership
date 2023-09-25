from fastapi import APIRouter, HTTPException, status, Query, Request
from src.services.common import TaxFormatTypeService
from src.payloads.schemas.common.TaxFormatTypeSchema import MtrTaxFormatTypeGetSchema
from src.payloads.responses.GeneralResponse import payload_response
from src.payloads.responses.PaginationResponse import pagination_response
from src.exceptions.RequestException import ResponseException

router = APIRouter(tags=["Tax Format Type"],prefix="/api/general")

@router.get("/tax-format-types", status_code=200)
async def get_all_tax_format_types(page:int, limit:int, query_of:list[str]=Query(None), query_by:list[str]=Query(None)):
    get_results, pages, err = TaxFormatTypeService.get_all_tax_format_types(page,limit,query_of,query_by)
    if err == None:
        return pagination_response(200,"Success",page,limit,pages["total_pages"],pages["total_rows"],get_results)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))

@router.get("/tax-format-type/{tax_format_type_id}", status_code=200)
async def get_by_id_tax_format_type(tax_format_type_id:int):
    get_result, err = TaxFormatTypeService.get_by_id_tax_format_type(tax_format_type_id)
    if not get_result and err == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    return payload_response(200,"Success",get_result)

@router.post("/tax-format-type",status_code=201)
async def post_tax_format_type(req:MtrTaxFormatTypeGetSchema):
    created_data, err = TaxFormatTypeService.post_tax_format_type(req)
    if err == None:
        return payload_response(201,"Created",created_data)
    else:
        raise HTTPException(status_code= status.HTTP_409_CONFLICT,detail=ResponseException(409))
    
@router.put("/tax-format-type/{tax_format_type_id}",status_code=201)
async def put_tax_format_type(tax_format_type_id:int,req:MtrTaxFormatTypeGetSchema):
    updated_data, err = TaxFormatTypeService.put_tax_format_type(tax_format_type_id,req)
    if err == None:
        return payload_response(201,"Updated",updated_data)
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))
    
@router.delete("/tax-format-type/{tax_format_type_id}",status_code=204)
async def delete_tax_format_type(tax_format_type_id:int):
    erase_data, err = TaxFormatTypeService.delete_tax_format_type(tax_format_type_id)
    if err == None:
        return payload_response(204,"Deleted",erase_data)
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))

@router.patch("/tax-format-type/{tax_format_type_id}",status_code=201)
async def patch_tax_format_type(tax_format_type_id:int):
    updated_data, err = TaxFormatTypeService.patch_tax_format_type(tax_format_type_id)
    if err == None:
        return payload_response(201,"Updated",updated_data)
    else:
        print(str(err))
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))
    