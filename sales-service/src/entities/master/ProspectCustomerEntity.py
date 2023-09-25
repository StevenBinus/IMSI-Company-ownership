from src.configs.database import Base
from sqlalchemy import Column,String,Integer
from sqlalchemy.orm import relationship

class MtrProspectCustomer(Base):
    __tablename__ = "mtr_prospect_customer"
    company_id = Column(Integer,nullable=False) # FK to mtr_company from common-general service
    prospect_customer_system_number = Column(Integer,primary_key=True,autoincrement=True,nullable=False)
    prospect_code = Column(String(10),unique=True,nullable=False,default="")
    customer_type_id = Column(Integer,nullable=False) # FK to mtr_customer_type from common-general service
    prospect_customer_title_prefix = Column(String(15),nullable=True,default="")
    prospect_customer_name = Column(String(40),nullable=False)
    prospect_customer_title_suffix = Column(String(15),nullable=True,default="")
    business_type_id = Column(Integer,nullable=False) # FK to mtr_business_type from common-general service
    business_group_id = Column(Integer,nullable=False) # FK to mtr_business_group from common-general service
    sales_representative_id = Column(Integer,nullable=False) # FK to user_id from user service
    prospect_address_id = Column(Integer,nullable=False) # FK to mtr_address from general service
    prospect_customer_mobile_phone = Column(String(30),nullable=False)
    prospect_customer_email_address = Column(String(128),nullable=False)
    prospect_customer_website = Column(String(128),nullable=False)
    prospect_customer_phone_number = Column(String(30),nullable=False)
    prospect_customer_fax_number = Column(String(30),nullable=False)
    gender_id = Column(Integer,nullable=False) # FK to mtr_gender from common-general service
    contact_person = Column(String(35),nullable=False)
    job_title_id = Column(Integer,nullable=False) # FK to mtr_job_title from common-general service
    contact_mobile_phone = Column(String(30),nullable=False)
    contact_email_address = Column(String(128), nullable=False) 
    keyword = Column(String(50),nullable=False) 
    #back populates
    prospectcustomer_prospectheader = relationship("TrxProspectHeader",back_populates="prospectheader_prospectcustomer",foreign_keys="TrxProspectHeader.prospect_customer_system_number")