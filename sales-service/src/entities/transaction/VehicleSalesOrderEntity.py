from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from src.configs.database import Base
from datetime import datetime


class TrxVehicleSalesOrder(Base):
    __tablename__ = "trx_vehicle_sales_order"
    vehicle_sales_order_system_number = Column(Integer,primary_key=True,autoincrement=True)
    system_number_old = Column(Integer,nullable=False)
    status_order = Column(String,nullable=False,default="draft")
    sales_representative_code = Column(Integer,nullable=False) #FK from common-general service
    user_employee_id = Column(Integer,nullable=False) #FK from user service
    document_number = Column(String(25),nullable=True)
    stage_date = Column(DateTime,nullable=True,default="")
    terms_of_payment_id = Column(Integer,nullable=False) #FK from common-general service
    dealer_rep_id = Column(Integer,nullable=False) #FK from common-general service
    prospect_source_id = Column(Integer,nullable=False) #FK 
    keyword = Column(String(50),nullable=True,default="")
    order_by_customer_id =  Column(Integer,nullable=False) #FK
    # order_by_id_type = Column(Integer,nullable=False) #FK
    # order_by_id_no = Column(String(30),nullable=True,default="")
    # order_by_prefix = Column(String(15), nullable=True,default="")
    # order_by_name = Column(String(100),nullable=True,default="")
    # order_by_suffix = Column(String(15),nullable=True,default="")
    # order_by_gender_id = Column(Integer,nullable=False) #FK
    # order_by_address_1 = Column(String(100),nullable=True,default="")
    # order_by_address_2 = Column(String(100),nullable=True,default="")
    # order_by_address_3 = Column(String(100),nullable=True,default="")
    # order_by_village_code = Column(Integer,nullable=False) #FK
    # order_by_subdistrict_code = Column(Integer,nullable=False) #FK
    # order_by_municipality_code = Column(Integer,nullable=False)
    # order_by_province_code = Column(Integer,nullable=False)
    # order_by_city_code = Column(Integer,nullable=False)
    # order_by_zip_code = Column(Integer,nullable=False)
    # order_by_phone_no = Column(String,nullable=True)
    # order_by_fax_no = Column(String,nullable=False)
    # order_by_mobile_phone = Column(String,nullable=False)
    # order_by_email_address = Column(String,nullable=False)
    # order_by_tax_invoice_id = Column(String,nullable=False) #FK
    # corporate_business_type_id = Column(Integer,nullable=False) #FK
    # corporate_business_group_id = Column(Integer,nullable=False) #Fk
    # corporate_web_site = Column(String(50),nullable=True,default="")
    # corporate_purchase_order_no = Column(String(50),nullable=True,default="")
    # corporate_purchase_order_date = Column(DateTime,nullable=True,default="")
    # corporate_contact_name = Column(String(40),nullable=True,default="")
    # corporate_contact_gender_id = Column(Integer,nullable=True,default="")
    # corporate_job_title_id = Column(Integer,nullable=True,default="")
    # corporate_mobile_phone = Column(String(30),nullable=True,default="")
    # corporate_email_address = Column(String(128),nullable=True,default="")
    # order_by_tax_invoice_id = Column(Integer,nullable=False) #FK
    # order_by_tax_reg_no = Column(String(30),nullable=True,default="")
    # order_by_tax_reg_date = Column(DateTime,nullable=True,default="")
    # order_by_tax_name = Column(String(100),nullable=True,default="")
    # order_by_tax_address_1 = Column(String(100),nullable=True,default="")
    # order_by_tax_address_2 = Column(String(100),nullable=True,default="")
    # order_by_tax_address_3 = Column(String(100),nullable=True,default="")
    # tax_village_code = Column(Integer,nullable=False) #FK
    # tax_subdistrict_code = Column(Integer,nullable=False) #FK
    # tax_municipality_code = Column(Integer,nullable=False) #FK
    # tax_province_code = Column(Integer,nullable=False) #FK
    # tax_city_code = Column(Integer,nullable=False) #FK
    # tax_zip_code = Column(Integer,nullable=False) #FK
    # pkp_no = Column(String(30),nullable=True,default="")
    # pkp_date = Column(DateTime,nullable=True,default="")
    # stnk_cust_code = Column(String(20),nullable=True,default="")
    # stnk_id_type = Column(String(10),nullable=True,default="")
    # stnk_id_no = Column(String(30),nullable=True,default="")
    # stnk_prefix = Column(String(15),nullable=True,default="")
    # stnk_name = Column(String(100),nullable=True,default="")
    # stnk_suffix = Column(String(15),nullable=True,default="")
    # stnk_gender_id = Column(Integer,nullable=False) #FK
    # stnk_address_1 = Column(String(100),nullable=True,default="")
    # stnk_address_2 = Column(String(100),nullable=True,default="")
    # stnk_address_3 = Column(String(100),nullable=True,default="")
    # stnk_village_code = Column(Integer,nullable=False) #FK
    # stnk_subdistrict_code = Column(Integer,nullable=False) #FK
    # stnk_municipality_code = Column(Integer,nullable=False) #FK
    # stnk_province_code = Column(Integer,nullable=False) #FK
    # stnk_city_code = Column(Integer,nullable=False) #FK
    # stnk_zip_code = Column(Integer,nullable=False) #FK
    # stnk_phone_no = Column(String(30),nullable=True,default="")
    # stnk_fax_no = Column(String(30),nullable=True,default="")
    # stnk_mobile_phone = Column(String(30),nullable=True,default="")
    # stnk_email_address = Column(String(128),nullable=True,default="")
    # correspondent_prefix = Column(String(15),nullable=True,default="")
    # correspondent_name = Column(String(40),nullable=True,default="")
    # correspondent_suffix = Column(String(15),nullable=True,default="")
    # correspondent_gender = Column(Integer,nullable=False) #FK with general-service mtr_gender
    # correspondent_job_title = Column(Integer,nullable=False) #FK with general-service mtr_job_title
    # correspondent_address_1 = Column(String(100),nullable=False,default="")
    # correspondent_address_2 = Column(String(100),nullable=False,default="") 
    # correspondent_address_3 = Column(String(100),nullable=False,default="")
    # correspondent_village_code = Column(Integer,nullable=False) #Fk with general-service mtr_area
    # correspondent_subdistrict_code = Column()
    # correspondent_municipality_code = Column(String())
    # correspondent_province_code = Column(String())
    # correspondent_city_code = Column(String())
    # correspondent_zip_code = Column(String())
    # correspondent_phone_no = Column(String())
    # correspondent_fax_no = Column(String())
    # correspondent_mobile_phone = Column(String())
    # correspondent_email_address = Column(String())
    # prospect_source_id = Column(String())
    # prospect_date = Column(String())
    # note = Column(String())
    # cost_center_id = Column(String())
    # incentive = Column(String())
    # body_type = Column(String())
    # plate_color = Column(String())
    #back populates
    salesordermaster_salesorderaccessories = relationship("TrxVehicleSalesOrderAccessoriesPackage", 
                                                              back_populates="salesorderaccessories_salesordermaster", 
                                                              foreign_keys="TrxVehicleSalesOrderAccessoriesPackage.vehicle_sales_order_system_number")
    salesordermaster_salesorderfreeaccessories = relationship("TrxVehicleSalesOrderFreeAccessories", 
                                                                   back_populates="salesorderfreeaccessories_salesordermaster", 
                                                                   foreign_keys="TrxVehicleSalesOrderFreeAccessories.vehicle_sales_order_system_number")
    salesordermaster_salesorderdetail = relationship("TrxVehicleSalesOrderDetail", 
                                                         back_populates="salesorderdetail_salesordermaster", 
                                                         foreign_keys="TrxVehicleSalesOrderDetail.vehicle_sales_order_system_number")
    spm_prospectheader = relationship("TrxProspectHeader",back_populates="prospectheader_spm",foreign_keys="TrxProspectHeader.vehicle_sales_order_system_number")
