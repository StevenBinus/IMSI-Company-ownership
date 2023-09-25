from src.configs.database import Base
from sqlalchemy import Column, Integer,String, ForeignKey, DateTime, Float, Boolean
from sqlalchemy.orm import relationship
from datetime import datetime

class TrxProspectHeader(Base):
    __tablename__ = "trx_prospect"
    company_id = Column(Integer,nullable=False,default=0)
    prospect_system_number = Column(Integer,primary_key=True,autoincrement=True,nullable=False)
    prospect_date = Column(DateTime,nullable=False,default=datetime.now())
    prospect_customer_system_number = Column(Integer,ForeignKey("mtr_prospect_customer.prospect_customer_system_number"),nullable=True) # FK to trx_prospect_customer
    customer_id = Column(Integer,nullable=True) #FK to mtr_customer in general-common service
    prospect_document_number = Column(String(25),unique=True,nullable=False) # will be generated after submitting
    prospect_status_id = Column(Integer,ForeignKey("mtr_prospect_status.prospect_status_id"),nullable=True)
    prospect_stage_id = Column(Integer,ForeignKey("mtr_prospect_stage.prospect_stage_id"),nullable=True)
    buying_plan_date = Column(DateTime,nullable=True,default="")
    conduct_test_drive = Column(Boolean,nullable=False,default=False)
    test_drive_date_schedule = Column(DateTime,nullable=True,default="")
    test_drive_date_actual = Column(DateTime,nullable=True,default="")
    competitor_model = Column(String(35),nullable=True,default="")
    fund_type_id = Column(Integer,nullable=False) # FK to mtr_fund_type common-general service
    retail_price_unit = Column(Float,nullable=True,default=0)
    request_discount  = Column(Float,nullable=True,default=0)
    down_payment_budget = Column(Float,nullable=True,default=0)
    sales_repsentative_to = Column(Integer,nullable=False) # FK to user user-service
    prospect_reference = Column(String,nullable=True,default="")
    prospect_note = Column(String,nullable=True,default="")
    stage_date_cc = Column(DateTime,nullable=True,default="") 
    stage_date_ch = Column(DateTime, nullable=True,default="") 
    vehicle_sales_order_system_number = Column(Integer,ForeignKey("trx_vehicle_sales_order.vehicle_sales_order_system_number"),nullable=True)
    prospect_drop_date = Column(DateTime,nullable=True,default="")
    prospect_drop_reason_id = Column(Integer,nullable=False) # FK to mtr_prospect_drop_reason from common-general service
    prospect_drop_remark = Column(String(128),nullable=True,default="")
    #back populates
    prospectheader_prospectstage = relationship("MtrProspectStage",back_populates="prospectstage_prospectheader",foreign_keys=[prospect_stage_id])
    prospectheader_prospectstatus = relationship("MtrProspectStatus",back_populates="prospectstatus_prospectheader",foreign_keys=[prospect_status_id])
    prospectheader_prospectcustomer = relationship("MtrProspectCustomer",back_populates="prospectcustomer_prospectheader",foreign_keys=[prospect_customer_system_number])
    prospectheader_spm = relationship("TrxVehicleSalesOrder",back_populates="spm_prospectheader",foreign_keys=[vehicle_sales_order_system_number])
    prospect_prospectdetail = relationship("TrxProspectDetail",back_populates="prospectdetail_prospect",foreign_keys="TrxProspectDetail.prospect_system_number")
    prospect_followup = relationship("TrxProspectFollowUp",back_populates="followup_prospect",foreign_keys="TrxProspectFollowUp.prospect_system_number")