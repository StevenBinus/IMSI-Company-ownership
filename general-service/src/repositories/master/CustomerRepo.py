from sqlalchemy import select
from sqlalchemy.orm import Session
from typing import List
import datetime, math, requests
from src.entities.master.CustomerEntity import MtrCustomer 
from src.entities.master import CustomerDeliveryAddressEntity, CustomerContactEntity, CustomerBankAccountEntity, CustomerByDealerEntity, CustomerTypeEntity, AddressEntity, CompanyEntity
from src.payloads.schemas.master import CustomerSchema, CustomerDeliveryAddressSchema, CustomerContactSchema, CustomerBankAccountSchema, CustomerByDealerSchema
from src.configs.database import get_db
from src.utils.AddPagination import get_the_pagination_search_list_with_join  

def get_all_customer(db:Session, page:int, limit:int, all_params:dict(), sort_params:dict()):
    try:
        query_set = select(
            MtrCustomer.customer_code, 
            MtrCustomer.customer_name,
            CustomerTypeEntity.MtrCustomerType.customer_type_description,
            AddressEntity.MtrAddress.address_street_1,
            AddressEntity.MtrAddress.address_street_2, 
            AddressEntity.MtrAddress.address_street_3,
            MtrCustomer.id_phone_no,
            MtrCustomer.is_active
            ).join(
                CustomerTypeEntity.MtrCustomerType,
                MtrCustomer.customer_type_id == CustomerTypeEntity.MtrCustomerType.customer_type_id
            ).join(
                AddressEntity.MtrAddress,
                MtrCustomer.id_address_id == AddressEntity.MtrAddress.address_id
            )
        
        join_tables = [MtrCustomer, CustomerTypeEntity.MtrCustomerType, AddressEntity.MtrAddress]
        query_check,counter = get_the_pagination_search_list_with_join(db, query_set, all_params, join_tables)

        if sort_params["sort_by"]==None or sort_params["sort_of"]==None:
            query_check=query_check.order_by(MtrCustomer.customer_code.asc()) 
        else:
            if sort_params("sort_of") == "desc":
                query_check=query_check.order_by(MtrCustomer.customer_code.desc()) 
            else:
                query_check=query_check.order_by(MtrCustomer.customer_code.asc()) 
        
        query_final = query_check.offset(page*limit).limit(limit)
        data = db.execute(query_final).all()
        results = []
        for customer_code, customer_name, customer_type_description, address_street_1, address_street_2, address_street_3, id_phone_no, is_active in data:
            output = {
                "customer_code":customer_code,
                "customer_name":customer_name,
                "customer_type_description":customer_type_description,
                "customer_address": f"{address_street_1} {address_street_2} {address_street_3}",
                "id_phone_no":id_phone_no,
                "is_active":is_active
            }
            results.append(output)
        page_results = {
            "total_rows" : counter,
            "total_pages" : math.ceil(counter/limit)
        }
        return results, page_results, None
    except Exception as err:
        return None, None, err
 
def get_by_id_customer(id: int, db:Session):
    try:
        check_query = select(MtrCustomer).where(MtrCustomer.customer_id==id)
        result = db.scalars(check_query).first()
        if result:
            delivery_address_result, err1 = get_customer_delivery_address(id, db)
            contact_result, err2 = get_customer_contact(id, db)
            bank_account_result, err3 = get_customer_bank_account(id, db)
            by_dealer_result, err4 = get_customer_by_dealer(id, db)
            if err1 or err2 or err3 or err4:
                raise Exception
        return result, delivery_address_result, contact_result, bank_account_result, by_dealer_result, None
    except Exception as err:
        return None, None, None, None, None, err
 
def get_customer_delivery_address(customer_id:int, db:Session):
    try:    
        query = select(
            CustomerDeliveryAddressEntity.MtrCustomerDeliveryAddress.ship_to_name,
            AddressEntity.MtrAddress.address_street_1,
            AddressEntity.MtrAddress.address_street_2,
            AddressEntity.MtrAddress.address_street_3,
            CustomerDeliveryAddressEntity.MtrCustomerDeliveryAddress.lead_times,
            CustomerDeliveryAddressEntity.MtrCustomerDeliveryAddress.contact_person,
            CustomerDeliveryAddressEntity.MtrCustomerDeliveryAddress.is_active,
            ).join(
                AddressEntity.MtrAddress,
                CustomerDeliveryAddressEntity.MtrCustomerDeliveryAddress.address_id == AddressEntity.MtrAddress.address_id
            ).where(CustomerDeliveryAddressEntity.MtrCustomerDeliveryAddress.customer_id==customer_id)
        
        data = db.execute(query).all()
        results = []
        for ship_to_name, address_street_1, address_street_2, address_street_3, lead_times, contact_person, is_active in data:
            output = {
                "ship_to_name":ship_to_name,
                "customer_address": f"{address_street_1} {address_street_2} {address_street_3}",
                "lead_times":lead_times,
                "contact_person":contact_person,
                "is_active":is_active
            }
            results.append(output)
        
        return results, None
    except Exception as err:
        return None, err
    
def get_customer_contact(customer_id:int, db:Session):
    try:
        query= select(
            CustomerContactEntity.MtrCustomerContact.contact_name,
            CustomerContactEntity.MtrCustomerContact.description,
            CustomerContactEntity.MtrCustomerContact.phone_number,
            CustomerContactEntity.MtrCustomerContact.is_active
            ).where(CustomerContactEntity.MtrCustomerContact.customer_id==customer_id)
        data = db.execute(query).all()
        results = []
        for contact_name, description, phone_number, is_active in data:
            output = {
                "contact_name":contact_name,
                "description":description,
                "phone_number":phone_number,
                "is_active":is_active
            }
            results.append(output)
        return results, None
    except Exception as err:
        return None, err
    
def get_customer_bank_account(customer_id: int, db:Session):
    try:
        query = select(
            CustomerBankAccountEntity.MtrCustomerBankAccount.bank_id,
            CustomerBankAccountEntity.MtrCustomerBankAccount.bank_account_type_id,
            CustomerBankAccountEntity.MtrCustomerBankAccount.currency_id,
            CustomerBankAccountEntity.MtrCustomerBankAccount.bank_account_number,
            CustomerBankAccountEntity.MtrCustomerBankAccount.bank_account_name,
            ).where(CustomerBankAccountEntity.MtrCustomerBankAccount.customer_id==customer_id)
        data = db.execute(query).all()

        results = []
        for bank_id, bank_account_type_id, currency_id, bank_account_number, bank_account_name in data:
            output = {
                "bank_id":bank_id,
                "bank_account_type_id":bank_account_type_id,
                "currency_id":currency_id,
                "bank_account_number":bank_account_number,
                "bank_account_name":bank_account_name
            }
            results.append(output)
        
        for data in results:
            id_bank = data["bank_id"]
            # API currency belum ada
            # id_currency = data["currency_id"]
            bank_url = f"http://10.1.32.26:7000/api/master/bank/{id_bank}" 
            # currency_url = f"http://10.1.32.26:7000/api/master/currency/{id_currency}" 
            try:
                bank_response = requests.get(bank_url)
                bank_data = bank_response.json()
                data["bank_name"] = data.pop("bank_id")
                data["bank_name"] = bank_data["data"]["bank_name"]

                # currency_response = requests.get(currency_url)
                # currency_data = currency_response.json()
                # data["currency_name"] = data.pop("currency_id")
                # data["currency_name"] = bank_data["data"]["currency_name"]
            except Exception as err:
                return None, err

        return results, None
    except Exception as err:
        return None, err

def get_customer_by_dealer(customer_id: int, db:Session):
    try:
        query = select(
            CompanyEntity.MtrCompany.company_code,
            CompanyEntity.MtrCompany.company_name,
            CustomerByDealerEntity.MtrCustomerByDealer.is_active
            ).join(
                CompanyEntity.MtrCompany,
                CustomerByDealerEntity.MtrCustomerByDealer.company_id == CompanyEntity.MtrCompany.company_id
            ).where(CustomerByDealerEntity.MtrCustomerByDealer.customer_id==customer_id)
        data = db.execute(query).all()
        
        results = []
        for company_code, company_name, is_active in data:
            output = {
                "company_code":company_code,
                "company_name":company_name,
                "is_active":is_active
            }
            results.append(output)
        return results, None
    except Exception as err:
        return None, err
    
def get_customer_delivery_address_by_id(id:int, db:Session):
    try:    
        query = select(CustomerDeliveryAddressEntity.MtrCustomerDeliveryAddress).where(CustomerDeliveryAddressEntity.MtrCustomerDeliveryAddress.customer_delivery_address_id==id)
        result = db.scalars(query).first()
        return result, None
    except Exception as err:
        return None, err
    
def get_customer_contact_by_id(id:int, db:Session):
    try:
        query= select(CustomerContactEntity.MtrCustomerContact).where(CustomerContactEntity.MtrCustomerContact.customer_contact_id==id)
        result= db.scalars(query).first()
        return result, None
    except Exception as err:
        return None, err
    
def get_customer_bank_account_by_id(id:int, db:Session):
    try:
        query = select(CustomerBankAccountEntity.MtrCustomerBankAccount).where(CustomerBankAccountEntity.MtrCustomerBankAccount.customer_bank_account_id==id)
        result = db.scalars(query).first()
        return result, None
    except Exception as err:
        return None, err
    
def get_customer_by_dealer_by_id(id:int, db:Session):
    try:
        query = select(CustomerByDealerEntity.MtrCustomerByDealer).where(CustomerByDealerEntity.MtrCustomerByDealer.customer_by_dealer_id==id)
        result = db.scalars(query).first()
        return result, None
    except Exception as err:
        return None, err
    
def post_customer(req:CustomerSchema.MtrCustomerSchema, db:Session):
    try:
        db.begin()
        customer_code_generate = generate_customer_code(req.customer_type_id, req.customer_name, db)
        _new_data = MtrCustomer()
        _new_data.customer_code = customer_code_generate
        _new_data.company_id  = req.company_id
        _new_data.dealer_sales_representative  = req.dealer_sales_representative
        _new_data.customer_title_prefix  = req.customer_title_prefix
        _new_data.customer_name  = req.customer_name
        _new_data.customer_title_suffix  = req.customer_title_suffix
        _new_data.customer_type_id  = req.customer_type_id
        _new_data.keyword  = req.keyword
        _new_data.customer_gender_id  = req.customer_gender_id
        _new_data.customer_birthday  = req.customer_birthday
        _new_data.customer_birth_place  = req.customer_birth_place
        _new_data.customer_religion_id  = req.customer_religion_id
        _new_data.customer_marital_status_id  = req.customer_marital_status_id
        _new_data.customer_marriage_date  = req.customer_marriage_date
        _new_data.customer_hobby  = req.customer_hobby
        _new_data.customer_mobile_phone  = req.customer_mobile_phone
        _new_data.customer_mobile_phone2  = req.customer_mobile_phone2
        _new_data.driver_mobile_phone  = req.driver_mobile_phone
        _new_data.customer_email_address  = req.customer_email_address
        _new_data.customer_job_title_id = req.customer_job_title_id
        _new_data.id_type  = req.id_type
        _new_data.id_number  = req.id_number
        _new_data.id_address_id  = req.id_address_id
        _new_data.id_phone_no  = req.id_phone_no
        _new_data.home_address_id  = req.home_address_id
        _new_data.home_phone_no  = req.home_phone_no
        _new_data.home_fax_no  = req.home_fax_no
        _new_data.office_address_id  = req.office_address_id
        _new_data.office_phone_no  = req.office_phone_no
        _new_data.office_fax_no  = req.office_fax_no
        _new_data.reference_name  = req.reference_name
        _new_data.reference_address_id  = req.reference_address_id
        _new_data.reference_phone_number  = req.reference_phone_number
        _new_data.reference_note  = req.reference_note
        _new_data.tax_invoice_type_id  = req.tax_invoice_type_id
        _new_data.tax_registration_number  = req.tax_registration_number
        _new_data.tax_registration_date  = req.tax_registration_date
        _new_data.tax_name  = req.tax_name
        _new_data.tax_address_id  = req.tax_address_id
        _new_data.pkp_number  = req.pkp_number
        _new_data.pkp_type  = req.pkp_type
        _new_data.pkp_date = req.pkp_date
        _new_data.vat_registration_number  = req.vat_registration_number
        _new_data.vat_registration_date  = req.vat_registration_date
        _new_data.vat_name  = req.vat_name
        _new_data.vat_address_id  = req.vat_address_id
        _new_data.vat_pkp_type  = req.vat_pkp_type
        _new_data.vat_pkp_date  = req.vat_pkp_date
        _new_data.vat_pkp_number  = req.vat_pkp_number
        _new_data.vat_tax_office_id  = req.vat_tax_office_id
        _new_data.bill_equal_to  = req.bill_equal_to
        _new_data.correspondence_equal_to  = req.correspondence_equal_to
        _new_data.business_type_id  = req.business_type_id
        _new_data.business_group_id  = req.business_group_id
        _new_data.business_website  = req.business_website
        _new_data.dealer_name_id  = req.dealer_name_id
        _new_data.dealer_contact_date  = req.dealer_contact_date
        _new_data.customer_class_id  = req.customer_class_id
        _new_data.customer_behavior_id  = req.customer_behavior_id
        _new_data.print_state  = req.print_state
        _new_data.collector_id  = req.collector_id
        _new_data.term_of_payment_id  = req.term_of_payment_id
        _new_data.tax_office_id  = req.tax_office_id
        _new_data.vat_transaction_id  = req.vat_transaction_id
        _new_data.customer_price_code  = req.customer_price_code
        db.add(_new_data)
        db.commit()
        db.refresh(_new_data)
        return _new_data, None
    except Exception as err:
        db.rollback()
        return None, err

def post_customer_delivery_address(req: CustomerDeliveryAddressSchema.MtrCustomerDeliveryAddressSchema, cust_id:int, db:Session):
    try:
        query = select(CustomerDeliveryAddressEntity.MtrCustomerDeliveryAddress.ship_to_line_number).where(CustomerDeliveryAddressEntity.MtrCustomerDeliveryAddress.customer_id == cust_id).order_by(CustomerDeliveryAddressEntity.MtrCustomerDeliveryAddress.ship_to_line_number.desc())
        result = db.scalars(query).first()
        if result == None:
            ship_to_line_number = 1
        else:
            ship_to_line_number = result + 1
            
        _new_data = CustomerDeliveryAddressEntity.MtrCustomerDeliveryAddress()
        _new_data.ship_to_line_number  = ship_to_line_number
        _new_data.customer_id  = cust_id
        _new_data.ship_to_name  = req.ship_to_name
        _new_data.address_id  = req.address_id
        _new_data.phone_number  = req.phone_number
        _new_data.fax_number  = req.fax_number
        _new_data.lead_times  = req.lead_times
        _new_data.contact_person  = req.contact_person
        _new_data.job_title_id  = req.job_title_id
        db.add(_new_data)
        db.commit()
        db.refresh(_new_data)
        return _new_data, None
    except Exception as err:
        db.rollback()
        return None, err
    
def post_customer_contact(req:CustomerContactSchema.MtrCustomerContactSchema, customer_id:int, db:Session):
    try:
        query = select(CustomerContactEntity.MtrCustomerContact.contact_line_number).where(CustomerContactEntity.MtrCustomerContact.customer_id == customer_id).order_by(CustomerContactEntity.MtrCustomerContact.contact_line_number.desc())
        result = db.scalars(query).first()
        if result == None:
            ship_to_line_number = 1
        else:
            ship_to_line_number = result + 1

        _new_data = CustomerContactEntity.MtrCustomerContact()
        _new_data.customer_id  = customer_id
        _new_data.contact_line_number  = ship_to_line_number
        _new_data.contact_name  = req.contact_name
        _new_data.description  = req.description
        _new_data.phone_number  = req.phone_number
        db.add(_new_data)
        db.commit()
        db.refresh(_new_data)
        return _new_data, None
    except Exception as err:
        db.rollback()
        return None, err

def post_customer_bank_account(req:CustomerBankAccountSchema.MtrCustomerBankAccountSchema, customer_id:int, db:Session):
    try:
        _new_data = CustomerBankAccountEntity.MtrCustomerBankAccount()
        _new_data.customer_id  = customer_id
        _new_data.bank_id  = req.bank_id
        _new_data.bank_account_type_id  = req.bank_account_type_id
        _new_data.bank_account_name  = req.bank_account_name
        _new_data.bank_account_number  = req.bank_account_number
        _new_data.currency_id  = req.currency_id
        
        bank_url = f"http://10.1.32.26:7000/api/master/bank/{req.bank_id}"
        bank_response = requests.get(bank_url)
        bank_data = bank_response.json()
        # currecy_url = f"http://10.1.32.26:7000/api/master/currency/{req.currency_id}"
        # currency_response = requests.get(currency_url)
        # currency_data = currency_response.json()

        if bank_data["status_code"] != 200:#or currency_data["status_code"] != 200
            raise Exception
        db.add(_new_data)
        db.commit()
        db.refresh(_new_data)
        return _new_data, None
    except Exception as err:
        db.rollback()
        return None, err

def post_customer_by_dealer(req:CustomerByDealerSchema.MtrCustomerByDealerSchema, customer_id:int, db:Session):
    try:
        _new_data = CustomerByDealerEntity.MtrCustomerByDealer()
        _new_data.customer_id  = customer_id
        _new_data.company_id  = req.company_id
        db.add(_new_data)
        db.commit()
        db.refresh(_new_data)
        return _new_data, None
    except Exception as err:
        db.rollback()
        return None, err

def put_customer(id:int, req:CustomerSchema.MtrCustomerSchema, db:Session):
    try:
        query_check = select(MtrCustomer).where(MtrCustomer.customer_id==id)
        updated_data = db.scalars(query_check).first()
        updated_data.company_id  = req.company_id
        updated_data.dealer_sales_representative  = req.dealer_sales_representative
        updated_data.customer_title_prefix  = req.customer_title_prefix
        updated_data.customer_name  = req.customer_name
        updated_data.customer_title_suffix  = req.customer_title_suffix
        updated_data.customer_type_id  = req.customer_type_id
        updated_data.keyword  = req.keyword
        updated_data.customer_gender_id  = req.customer_gender_id
        updated_data.customer_birthday  = req.customer_birthday
        updated_data.customer_birth_place  = req.customer_birth_place
        updated_data.customer_religion_id  = req.customer_religion_id
        updated_data.customer_marital_status_id  = req.customer_marital_status_id
        updated_data.customer_marriage_date  = req.customer_marriage_date
        updated_data.customer_hobby  = req.customer_hobby
        updated_data.customer_mobile_phone  = req.customer_mobile_phone
        updated_data.customer_mobile_phone2  = req.customer_mobile_phone2
        updated_data.driver_mobile_phone  = req.driver_mobile_phone
        updated_data.customer_email_address  = req.customer_email_address
        updated_data.customer_job_title_id = req.customer_job_title_id
        updated_data.id_type  = req.id_type
        updated_data.id_number  = req.id_number
        updated_data.id_address_id  = req.id_address_id
        updated_data.id_phone_no  = req.id_phone_no
        updated_data.home_address_id  = req.home_address_id
        updated_data.home_phone_no  = req.home_phone_no
        updated_data.home_fax_no  = req.home_fax_no
        updated_data.office_address_id  = req.office_address_id
        updated_data.office_phone_no  = req.office_phone_no
        updated_data.office_fax_no  = req.office_fax_no
        updated_data.reference_name  = req.reference_name
        updated_data.reference_address_id  = req.reference_address_id
        updated_data.reference_phone_number  = req.reference_phone_number
        updated_data.reference_note  = req.reference_note
        updated_data.tax_invoice_type_id  = req.tax_invoice_type_id
        updated_data.tax_registration_number  = req.tax_registration_number
        updated_data.tax_registration_date  = req.tax_registration_date
        updated_data.tax_name  = req.tax_name
        updated_data.tax_address_id  = req.tax_address_id
        updated_data.pkp_number  = req.pkp_number
        updated_data.pkp_type  = req.pkp_type
        updated_data.pkp_date = req.pkp_date
        updated_data.vat_registration_number  = req.vat_registration_number
        updated_data.vat_registration_date  = req.vat_registration_date
        updated_data.vat_name  = req.vat_name
        updated_data.vat_address_id  = req.vat_address_id
        updated_data.vat_pkp_type  = req.vat_pkp_type
        updated_data.vat_pkp_date  = req.vat_pkp_date
        updated_data.vat_pkp_number  = req.vat_pkp_number
        updated_data.vat_tax_office_id  = req.vat_tax_office_id
        updated_data.bill_equal_to  = req.bill_equal_to
        updated_data.correspondence_equal_to  = req.correspondence_equal_to
        updated_data.business_type_id  = req.business_type_id
        updated_data.business_group_id  = req.business_group_id
        updated_data.business_website  = req.business_website
        updated_data.dealer_contact_date  = req.dealer_contact_date
        updated_data.customer_class_id  = req.customer_class_id
        updated_data.customer_behavior_id  = req.customer_behavior_id
        updated_data.print_state  = req.print_state
        updated_data.collector_id  = req.collector_id
        updated_data.term_of_payment_id  = req.term_of_payment_id
        updated_data.tax_office_id  = req.tax_office_id
        updated_data.vat_transaction_id  = req.vat_transaction_id
        updated_data.customer_price_code  = req.customer_price_code
        db.commit()
        db.refresh(updated_data)
        return updated_data, None
    except Exception as err:
        db.rollback()
        return None, err
    
def put_customer_delivery_address(id:int, req:CustomerDeliveryAddressSchema.MtrCustomerDeliveryAddressSchema, db:Session):
    try:
        query = select(CustomerDeliveryAddressEntity.MtrCustomerDeliveryAddress).where(CustomerDeliveryAddressEntity.MtrCustomerDeliveryAddress.customer_delivery_address_id==id)
        update_data = db.scalars(query).first()

        if update_data:
            update_data.ship_to_name  = req.ship_to_name
            update_data.address_id  = req.address_id
            update_data.contact_person  = req.contact_person
            update_data.job_title_id  = req.job_title_id
            db.commit()
            db.refresh(update_data)
        return update_data, None
    except Exception as err:
        db.rollback()
        return None, err
    
def put_customer_contact(id:int, req:CustomerContactSchema.MtrCustomerContactSchema, db:Session):
    query= select(CustomerContactEntity.MtrCustomerContact).where(CustomerContactEntity.MtrCustomerContact.customer_contact_id==id)
    update_data= db.scalars(query).first()
    try:
        if update_data:
            update_data.contact_name  = req.contact_name
            update_data.description  = req.description
            update_data.phone_number  = req.phone_number
            db.commit()
            db.refresh(update_data)
        return update_data, None
    except Exception as err:
        return None, err
    
def put_customer_bank_account(id:int, req: CustomerBankAccountSchema.MtrCustomerBankAccountUpdateSchema, db:Session):
    query = select(CustomerBankAccountEntity.MtrCustomerBankAccount).where(CustomerBankAccountEntity.MtrCustomerBankAccount.customer_bank_account_id==id)
    update_data = db.scalars(query).first()
    try:
        if update_data:
            update_data.bank_account_name  = req.bank_account_name
            update_data.currency_id  = req.currency_id
            db.commit()
            db.refresh(update_data)
        return update_data, None
    except Exception as err:
        return None, err
    
def patch_customer(id:int, db:Session):
    check_active_status = select(MtrCustomer).where(MtrCustomer.customer_id==id)
    active_status = db.scalars(check_active_status).first()
    current_status = active_status.is_active
    try:
        if current_status == True:
            active_status.is_active = False
        else :
            active_status.is_active = True 
        db.commit()
        db.refresh(active_status)
        return active_status, None
    except Exception as err:
        db.rollback()
        return None, err   
    
def patch_customer_delivery_address(id:int, db:Session):
    check_active_status = select(CustomerDeliveryAddressEntity.MtrCustomerDeliveryAddress).where(CustomerDeliveryAddressEntity.MtrCustomerDeliveryAddress.customer_delivery_address_id==id)
    active_status = db.scalars(check_active_status).first()
    current_status = active_status.is_active
    try:
        if current_status == True:
            active_status.is_active = False
        else :
            active_status.is_active = True 
        db.commit()
        db.refresh(active_status)
        return active_status, None
    except Exception as err:
        db.rollback()
        return None, err   
    
def patch_customer_contact(id:int, db:Session):
    check_active_status = select(CustomerContactEntity.MtrCustomerContact).where(CustomerContactEntity.MtrCustomerContact.customer_contact_id==id)
    active_status = db.scalars(check_active_status).first()
    current_status = active_status.is_active
    try:
        if current_status == True:
            active_status.is_active = False
        else :
            active_status.is_active = True 
        db.commit()
        db.refresh(active_status)
        return active_status, None
    except Exception as err:
        db.rollback()
        return None, err   
    
def patch_customer_bank_account(id:int, db:Session):
    check_active_status = select(CustomerBankAccountEntity.MtrCustomerBankAccount).where(CustomerBankAccountEntity.MtrCustomerBankAccount.customer_bank_account_id==id)
    active_status = db.scalars(check_active_status).first()
    current_status = active_status.is_active
    try:
        if current_status == True:
            active_status.is_active = False
        else :
            active_status.is_active = True 
        db.commit()
        db.refresh(active_status)
        return active_status, None
    except Exception as err:
        db.rollback()
        return None, err   
    
def patch_customer_by_dealer(id:int, db:Session):
    check_active_status = select(CustomerByDealerEntity.MtrCustomerByDealer).where(CustomerByDealerEntity.MtrCustomerByDealer.customer_by_dealer_id==id)
    active_status = db.scalars(check_active_status).first()
    current_status = active_status.is_active
    try:
        if current_status == True:
            active_status.is_active = False
        else :
            active_status.is_active = True 
        db.commit()
        db.refresh(active_status)
        return active_status, None
    except Exception as err:
        db.rollback()
        return None, err   

def generate_customer_code(type_id:int, name:str, db:Session):
    query = select(CustomerTypeEntity.MtrCustomerType.customer_type_description).where(CustomerTypeEntity.MtrCustomerType.customer_type_id == type_id)
    type_result = db.scalars(query).first()

    if type_result == 'individual private':
        type = 'P'
    else:
        type = 'C'

    get_name = name[0].upper()
    today = datetime.datetime.now()
    year = str(today.year)[-2:]
    
    prefix = f"{type}{get_name}{year}"

    query_queue = select(MtrCustomer.customer_code).where(MtrCustomer.customer_code.contains(prefix)).order_by(MtrCustomer.customer_code.desc())
    queue_result = db.scalars(query_queue).first()

    if queue_result == None:
        queue_number = 1
    else:
        queue_number = int(queue_result[-5:]) + 1

    current_number = str("%05d")%queue_number
    result = prefix + current_number
    return result

def get_multiple_customer(id:List[int], db:Session):
    try:

        query_set = select(
            MtrCustomer.customer_id,
            MtrCustomer.customer_name
        ).where(MtrCustomer.customer_id.in_(id))

        result = db.execute(query_set).fetchall()
        customers = []

        for row in result:
            customer = {
                "customer_id": row[0],
                "customer_name": row[1]
            }
            customers.append(customer)
        return customers, None
    except Exception as err:
        return None, err

