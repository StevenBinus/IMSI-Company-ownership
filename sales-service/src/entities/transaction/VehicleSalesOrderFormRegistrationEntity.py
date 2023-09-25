from sqlalchemy import Column, String, Integer,DateTime
from sqlalchemy.orm import relationship
from src.configs.database import Base

class TrxVehicleSalesOrderFormRegistration(Base):
    __tablename__ = "trx_vehicle_sales_order_form_registration"
    register_system_number = Column(Integer,nullable=False,primary_key=True)
    register_system_number_old = Column(Integer,nullable=True,default=0)
    company_id = Column(Integer,nullable=False) # foreign key get connected to general service
    register_document_number = Column(String,nullable=False)
    spm_received_by = Column(String,nullable=False) # user_id
    spm_received_date = Column(DateTime,nullable=False)
    spm_number_format = Column(String,nullable=False)
    spm_number_from = Column(Integer,nullable=False)
    total_spm = Column(Integer,nullable=False)
    reference_document_number = Column(String,nullable=False)

    #back populates
    spm_form_reg_detail = relationship("TrxVehicleSalesOrderFormRegistrationDetail",
                                       back_populates="spm_form_reg_header", 
                                       foreign_keys="TrxVehicleSalesOrderFormRegistrationDetail.register_system_number_id")
    
    spmreg_takedetail = relationship("TrxVehicleSalesOrderTakeDetail",back_populates="takedetail_spmreg",
                                     foreign_keys="TrxVehicleSalesOrderTakeDetail.vehicle_sales_order_system_number")
