from fastapi import Request
from sqlalchemy import select, desc
import datetime
import math
from src.entities.master import CustomerVirtualAccountEntity, CustomerEntity, ProfitCenterEntity, CompanyEntity
from src.entities.common import ApprovalStatusEntity
from src.payloads.schemas.master import CustomerVirtualAccountSchema 
from src.configs.database import get_db
from src.utils.AddPagination import get_the_pagination_search_list_with_join 

def get_all_customer_virtual_accounts(page:int, limit:int, all_params:dict(), sort_params:dict()):
    db = get_db()
    try:
        query_set = select(
            CustomerVirtualAccountEntity.MtrCustomerVirtualAccount.customer_id,
            CustomerEntity.MtrCustomer.customer_name,
            CustomerVirtualAccountEntity.MtrCustomerVirtualAccount.account_bank_company,
            ApprovalStatusEntity.MtrApprovalStatus.approval_status_description,
            ProfitCenterEntity.MtrProfitCenter.profit_center_name
        ).join(
            CustomerEntity.MtrCustomer,  
            CustomerVirtualAccountEntity.MtrCustomerVirtualAccount.customer_id == CustomerEntity.MtrCustomer.customer_id
        ).join(
            ApprovalStatusEntity.MtrApprovalStatus, 
            CustomerVirtualAccountEntity.MtrCustomerVirtualAccount.approval_dbs == ApprovalStatusEntity.MtrApprovalStatus.approval_status_id
        ).join(
            ProfitCenterEntity.MtrProfitCenter, 
            CustomerVirtualAccountEntity.MtrCustomerVirtualAccount.profit_center_id == ProfitCenterEntity.MtrProfitCenter.profit_center_id
        )

        join_tables = [CustomerVirtualAccountEntity.MtrCustomerVirtualAccount, CustomerEntity.MtrCustomer, ApprovalStatusEntity.MtrApprovalStatus, ProfitCenterEntity.MtrProfitCenter]
        query_check,counter = get_the_pagination_search_list_with_join(db, query_set, all_params, join_tables)
        

        if sort_params["sort_by"]==None or sort_params["sort_of"]==None:
            query_check=query_check.order_by(CustomerVirtualAccountEntity.MtrCustomerVirtualAccount.customer_id.desc()) 
        else:
            if sort_params("sort_of") == "desc":
                query_check=query_check.order_by(CustomerVirtualAccountEntity.MtrCustomerVirtualAccount.customer_id.desc()) 
            else:
                query_check=query_check.order_by(CustomerVirtualAccountEntity.MtrCustomerVirtualAccount.customer_id.asc()) 
        
        query_final = query_check.offset(page*limit).limit(limit)
        data = db.execute(query_final).all()

        results = []
        for customer_id, customer_name, account_bank_company, approval_status_description, profit_center_name in data:
            output = {
                "customer_id":customer_id,
                "customer_name":customer_name,
                "account_bank_company":account_bank_company,
                "approval_status_description":approval_status_description,
                "profit_center_name":profit_center_name
            }
            results.append(output)

        page_results = {
            "total_rows" : counter,
            "total_pages" : math.ceil(counter/limit)
        }
        
        return results, page_results, None
    except Exception as err:
        return None, None, err

def get_by_id_customer_virtual_account(id: int):
    db = get_db()
    try:
        check_query = select(
            CustomerVirtualAccountEntity.MtrCustomerVirtualAccount.customer_id,
            CompanyEntity.MtrCompany.company_name,
            # account_bank_company_code
            CustomerVirtualAccountEntity.MtrCustomerVirtualAccount.customer_virtual_account,
            ApprovalStatusEntity.MtrApprovalStatus.approval_status_description,
            ProfitCenterEntity.MtrProfitCenter.profit_center_name
        ).join(
            CompanyEntity.MtrCompany,
            CustomerVirtualAccountEntity.MtrCustomerVirtualAccount.company_id == CompanyEntity.MtrCompany.company_id 
        ).join(
            ApprovalStatusEntity.MtrApprovalStatus,
            CustomerVirtualAccountEntity.MtrCustomerVirtualAccount.approval_dbs == ApprovalStatusEntity.MtrApprovalStatus.approval_status_id
        ).join(
            ProfitCenterEntity.MtrProfitCenter,
            CustomerVirtualAccountEntity.MtrCustomerVirtualAccount.profit_center_id == ProfitCenterEntity.MtrProfitCenter.profit_center_id
        ).where(CustomerVirtualAccountEntity.MtrCustomerVirtualAccount.virtual_account_system_number_new==id)

        result = db.execute(check_query).first()
        
        output = {
            "customer_id" : result[0],
            "company_name" : result[1],
            "virtual_account" : result[2],
            "approval_status_description" : result[3],
            "profit_center_name" : result[4],
        }

        return output, None
    except Exception as err:
        return None, err
    
def post_customer_virtual_account(req:CustomerVirtualAccountSchema.MtrCustomerVirtualAccountSchema):
    db = get_db()
    result  = get_random_virtual_account()
    try:
        db.begin()
        _new_data = CustomerVirtualAccountEntity.MtrCustomerVirtualAccount()
        _new_data.customer_id = req.customer_id
        _new_data.company_id = req.company_id
        _new_data.account_bank_company = req.account_bank_company
        _new_data.customer_virtual_account = result
        _new_data.profit_center_id = req.profit_center_id
        _new_data.approval_dbs = 1 #seharusnya diisi dengan id mtr_approval_status dengan value wait approve
        db.add(_new_data)
        db.commit()

        db.refresh(_new_data)
        return _new_data, None
    except Exception as err:
        db.rollback()
        return None, err
    
def delete_customer_virtual_account(id:int):
    db = get_db()
    try:
        query_check = select(CustomerVirtualAccountEntity.MtrCustomerVirtualAccount).where(CustomerVirtualAccountEntity.MtrCustomerVirtualAccount.virtual_account_system_number_new==id)
        erase_data = db.scalars(query_check).first()
        db.delete(erase_data)
        db.commit()

        return erase_data, None
    except Exception as err:
        db.rollback()
        return None, err

def get_previous_virtual_account():
    db = get_db()
    try:
        query = select(CustomerVirtualAccountEntity.MtrCustomerVirtualAccount.customer_virtual_account).order_by(desc(CustomerVirtualAccountEntity.MtrCustomerVirtualAccount.customer_virtual_account))
        result = db.scalars(query).first()
        if result == None:
            return "0", "0", None
        else:
            queue = ""
            date = result[-8:-6]

            # get queue number
            for check in result[-6:]:
                if check != '0' or (check == '0' and queue != ''):
                    queue = queue + check 

        return queue, date, None
    except Exception as err:
        return None, None, err
    
def get_random_virtual_account():
    new_queue, date, err_va = get_previous_virtual_account()
    va_map = str(891) # Hardcode yang valuenya diambil dari fields va_map dari entity mtr_bank_company
    today = datetime.datetime.now()
    year = str(today.year)[-2:]
    month = str(today.month).zfill(2)
    curr_date = str(today.day).zfill(2)
 
    if int(curr_date) > int(date):
        queue = 1
    else:
        queue = int(new_queue) + 1
    
    curr_queue = str("%06d")%queue
    result = "9"+va_map+year+month+curr_date+curr_queue
    
    return result



