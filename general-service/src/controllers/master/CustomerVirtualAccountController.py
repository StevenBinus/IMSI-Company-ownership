from fastapi import APIRouter, HTTPException, status, Query, Request
from src.services.master import CustomerVirtualAccountService 
from src.payloads.schemas.master.CustomerVirtualAccountSchema import MtrCustomerVirtualAccountSchema 
from src.payloads.responses.GeneralResponse import payload_response
from src.payloads.responses.PaginationResponse import pagination_response
from src.exceptions.RequestException import ResponseException

router = APIRouter(tags=["Customer Virtual Account"],prefix="/api/general")
    
@router.get("/customer-virtual-accounts", status_code=200)
async def get_all_customer_virtual_accounts(page:int,limit:int,
                                            customer_id:int|None=None,
                                            customer_name:str|None=None,
                                            account_bank_company:int|None=None,
                                            approval_status_description:str|None=None,
                                            profit_center_name:str|None=None,
                                            sort_by:str|None=None,
                                            sort_of:str|None=None):
    get_all_params = {
        "customer_id":customer_id,
        "customer_name":customer_name,
        "account_bank_company":account_bank_company,
        "approval_status_description":approval_status_description,
        "profit_center_name":profit_center_name
    }
    sort_fields = {
        "sort_by":sort_by,
        "sort_of": sort_of
    }
    get_result, pages, err = CustomerVirtualAccountService.get_all_customer_virtual_accounts(page,limit,get_all_params,sort_fields)
    if  err == None:
        return pagination_response(200, "Success", page,limit,pages["total_pages"], pages["total_rows"], get_result)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))

@router.get("/customer-virtual-account/{virtual_account_system_number}", status_code=200)
async def get_by_id_customer_virtual_account(virtual_account_system_number:int):
    get_result, err = CustomerVirtualAccountService.get_by_id_customer_virtual_account(virtual_account_system_number)
    if not get_result and err == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    return payload_response(200,"Success",get_result)

@router.post("/post-customer-virtual-account",status_code=status.HTTP_201_CREATED)
async def post_customer_virtual_account(schema:MtrCustomerVirtualAccountSchema):
    created_data, err = CustomerVirtualAccountService.post_customer_virtual_account(schema)
    if err == None:
        return payload_response(201,"Created",created_data)
    else:
        raise HTTPException(status_code= status.HTTP_409_CONFLICT,detail=str(err))
    
@router.delete("/delete-customer-virtual-account/{customer_virtual_account_id}",status_code=204)
async def delete_customer_virtual_account(customer_virtual_account_id:int):
    erase_data, err = CustomerVirtualAccountService.delete_customer_virtual_account(customer_virtual_account_id)
    if err == None:
        return payload_response(204,"Deleted",erase_data)
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))
    