from src.repositories.master import CustomerRepo 
from src.payloads.schemas.master.CustomerSchema import MtrCustomerSchema
from src.payloads.schemas.master.CustomerBankAccountSchema import MtrCustomerBankAccountSchema, MtrCustomerBankAccountUpdateSchema
from src.payloads.schemas.master.CustomerByDealerSchema import MtrCustomerByDealerSchema
from src.payloads.schemas.master.CustomerContactSchema import MtrCustomerContactSchema
from src.payloads.schemas.master.CustomerDeliveryAddressSchema import MtrCustomerDeliveryAddressSchema
from typing import List
from sqlalchemy.orm import Session

def get_all_customer(db: Session, page:int, limit:int,  all_params:dict(), sort_params:dict()):
    get_data, page_results, err = CustomerRepo.get_all_customer(db, page,limit,all_params,sort_params) 
    if err == None:
        return get_data, page_results, None
    else:
        return None, None, err
    
def get_by_id_customer(id:int, db:Session):
    result, result2, result3, result4, result5, err = CustomerRepo.get_by_id_customer(id, db)
    if err == None:
        return result, result2, result3, result4, result5, None
    else:
        return None, None, None, None, None, err

def get_customer_delivery_address_by_id(id:int, db:Session):
    result, err = CustomerRepo.get_customer_delivery_address_by_id(id, db)
    if err == None:
        return result, None
    else:
        return None, err

def get_customer_contact_by_id(id:int, db:Session):
    result, err = CustomerRepo.get_customer_contact_by_id(id, db)
    if err == None:
        return result, None
    else:
        return None, err
    
def get_customer_bank_account_by_id(id:int, db:Session):
    result, err = CustomerRepo.get_customer_bank_account_by_id(id, db)
    if err == None:
        return result, None
    else:
        return None, err
    
def get_customer_by_dealer_by_id(id:int, db:Session):
    result, err = CustomerRepo.get_customer_by_dealer_by_id(id, db)
    if err == None:
        return result, None
    else:
        return None, err
    
def post_customer(req:MtrCustomerSchema, db:Session):
    created_data, err = CustomerRepo.post_customer(req, db)
    if err == None:
        return created_data, None
    else:
        return None, err
    
def post_customer_delivery_address(req: MtrCustomerDeliveryAddressSchema, id:int, db:Session):
    created_data, err = CustomerRepo.post_customer_delivery_address(req,id, db)
    if err == None:
        return created_data, None
    else:
        return None, err
    
def post_customer_contact(req:MtrCustomerContactSchema, id:int, db:Session):
    created_data, err = CustomerRepo.post_customer_contact(req, id, db)
    if err == None:
        return created_data, None
    else:
        return None, err
    
def post_customer_bank_account(req:MtrCustomerBankAccountSchema, id:int, db:Session):
    created_data, err = CustomerRepo.post_customer_bank_account(req, id, db)
    if err == None:
        return created_data, None
    else:
        return None, err
    
def post_customer_by_dealer(req:MtrCustomerByDealerSchema, id:int, db:Session):
    created_data, err = CustomerRepo.post_customer_by_dealer(req, id, db)
    if err == None:
        return created_data, None
    else:
        return None, err

def put_customer(id:int,req:MtrCustomerSchema, db:Session):
    updated_data, err = CustomerRepo.put_customer(id,req, db)
    if err == None:
        return updated_data, None
    else:
        return None, err

def put_customer_delivery_address(id:int, req: MtrCustomerDeliveryAddressSchema, db:Session):
    result, err = CustomerRepo.put_customer_delivery_address(id, req, db)
    if err == None:
        return result,None
    else:
        return None,err

def put_customer_contact(id:int, req: MtrCustomerContactSchema, db:Session):
    result, err = CustomerRepo.put_customer_contact(id, req, db)
    if err == None:
        return result,None
    else:
        return None,err

def put_customer_bank_account(id:int, req: MtrCustomerBankAccountUpdateSchema, db:Session):
    result, err = CustomerRepo.put_customer_bank_account(id, req, db)
    if err == None:
        return result,None
    else:
        return None,err
    
def patch_customer(id:int, db:Session):
    updated_data, err = CustomerRepo.patch_customer(id, db)
    if err == None:
        return updated_data, None
    else:
        return None, err
    
def patch_customer_delivery_address(id:int, db:Session):
    updated_data, err = CustomerRepo.patch_customer_delivery_address(id, db)
    if err == None:
        return updated_data, None
    else:
        return None, err
    
def patch_customer_contact(id:int, db:Session):
    updated_data, err = CustomerRepo.patch_customer_contact(id, db)
    if err == None:
        return updated_data, None
    else:
        return None, err
    
def patch_customer_bank_account(id:int, db:Session):
    updated_data, err = CustomerRepo.patch_customer_bank_account(id, db)
    if err == None:
        return updated_data, None
    else:
        return None, err
    
def patch_customer_by_dealer(id:int, db:Session):
    updated_data, err = CustomerRepo.patch_customer_by_dealer(id, db)
    if err == None:
        return updated_data, None
    else:
        return None, err
    
def get_multiple_customer(id:List[int], db:Session):
    result, err = CustomerRepo.get_multiple_customer(id, db)
    if err == None:
        return result, None
    else:
        return None, err