from fastapi import APIRouter, HTTPException, status, Query, Request
from src.services.common import UnitOfMeasurementItemService
from src.payloads.schemas.common.UnitOfMeasurementItemSchema import MtrUnitOfMeasurementItemGetSchema
from src.payloads.responses.GeneralResponse import payload_response
from src.payloads.responses.PaginationResponse import pagination_response
from src.exceptions.RequestException import ResponseException

from src.payloads.responses.GeneralResponse import payload_response

router = APIRouter(tags=["Unit Of Measurement Item"],prefix="/api/general")

@router.get("/unit-of-measurement-items", status_code=200)
def get_unit_of_measurement_items(page:int, limit:int, query_of:list[str]=Query(None), query_by:list[str]=Query(None)):
    get_results, pages, err = UnitOfMeasurementItemService.get_all_unit_of_measurement_items(page,limit,query_of,query_by)
    if err == None:
        return pagination_response(200,"Success",page,limit,pages["total_pages"],pages["total_rows"],get_results)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    
@router.get("/unit-of-measurement-item/{unit_of_measurement_item_id}", status_code=200)
def get_unit_of_measurement_item(unit_of_measurement_item_id:int):
    get_result, err = UnitOfMeasurementItemService.get_unit_of_measurement_item(unit_of_measurement_item_id)
    if not get_result and err == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    return payload_response(200,"Success",get_result)


@router.post("/unit-of-measurement-item", status_code=201)
def post_unit_of_measurement_item(req:MtrUnitOfMeasurementItemGetSchema):
    created_data, err = UnitOfMeasurementItemService.post_unit_of_measurement_item(req)
    if err == None:
        return payload_response(201,"Created",created_data)
    else:
        raise HTTPException(status_code= status.HTTP_409_CONFLICT,detail=ResponseException(409))

@router.delete("/unit-of-measurement-item/{unit_of_measurement_item_id}", status_code=204)
def delete_unit_of_measurement_item(unit_of_measurement_item_id:int):
    erase_data, err = UnitOfMeasurementItemService.delete_unit_of_measurement_type(unit_of_measurement_item_id)
    if err == None:
        return payload_response(204,"Deleted",erase_data)
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))

@router.put("/unit-of-measurement-item/{unit_of_measurement_item_id}", status_code=201)
def put_unit_of_measurement_item(unit_of_measurement_item_id:int,req:MtrUnitOfMeasurementItemGetSchema):
    created_data, err = UnitOfMeasurementItemService.post_unit_of_measurement_item(req)
    if err == None:
        return payload_response(201,"Created",created_data)
    else:
        raise HTTPException(status_code= status.HTTP_409_CONFLICT,detail=ResponseException(409))

@router.patch("/unit-of-measurement-item/{unit_of_measurement_item_id}", status_code=201)
def patch_unit_of_measurement_item(unit_of_measurement_item_id:int):
    updated_data, err = UnitOfMeasurementItemService.patch_unit_of_measurement_item(unit_of_measurement_item_id)
    if err == None:
        return payload_response(201,"Updated",updated_data)
    else:
        print(str(err))
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))