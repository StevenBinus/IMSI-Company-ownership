from fastapi import APIRouter,Depends,HTTPException,status,Query
from src.payloads.responses.GeneralResponse import payload_response
from src.exceptions.RequestException import ResponseException 
from src.repositories.common import AddressRepo
from src.services.common import AddressService 
from src.payloads.schemas.master import AddressSchema
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from src.configs.database import get_db
from src.payloads.responses.PaginationResponse import pagination_response

router = APIRouter(tags=["Address"],prefix="/api/general")

@router.get("/addresses", status_code=200)
async def get_addresses(page:int, limit:int, is_active:bool|None=None,address_id:int|None=None,address_latitude:str|None=None,address_longitude:str|None=None,
                        address_street_1:str|None=None,address_street_2:str|None=None,address_street_3:str|None=None,address_type:str|None=None,village_id:int|None=None,
                        sort_of:str|None=None, sort_by:str|None=None):
    get_all_params ={
        "is_active":is_active,"address_id":address_id,"address_latitude":address_latitude,"address_longitude":address_longitude,
        "address_street_1":address_street_1,"address_street_2":address_street_2,"address_street_3":address_street_3,"address_type":address_type,"village_id":village_id
    }
    sort_params = {"sort_of":sort_of,"sort_by":sort_by}
    addresses,pages,err = AddressService.get_addresses(page,limit,get_all_params,sort_params)
    if err == None:
        return pagination_response(200,"Success",page,limit,pages["total_rows"],pages["total_pages"],addresses)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))

@router.get("/address/{address_id}", status_code=200)
async def get_address(address_id:int):
    address = AddressService.get_address_by_id(address_id)
    if not address:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    return payload_response(ResponseException(200), "Success", address)

@router.post("/address", status_code=201)
async def post_address(req:AddressSchema.MtrAddressRequest):
    created_data,err = AddressService.post_address(req)
    if err == None:
        return payload_response(201,"Created",created_data)
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))

@router.delete("/address/{address_id}", status_code=204)
async def delete_data(address_id:int):
    delete_address,err = AddressService.delete_address(address_id)
    if err == None:
        return payload_response(204,"Deleted",delete_address)
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))

@router.put("/address/{address_id}", status_code=202)
async def put_data(address_id:int,req:AddressSchema.MtrAddressRequest):
    put_address,err = AddressService.put_address
    if err == None:
        return payload_response(201,"Updated",put_address)
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))

@router.patch("/address/{address_id}", status_code=202)
async def patch_address(address_id:int):
    active_address, err  = AddressService.patch_address(address_id)
    if err == None:
        return payload_response(201,"Updated",active_address)
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))