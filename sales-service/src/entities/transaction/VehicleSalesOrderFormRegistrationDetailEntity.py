from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from src.configs.database import Base

class TrxVehicleSalesOrderFormRegistrationDetail(Base):
    __tablename__ = "trx_vehicle_sales_order_form_registration_detail"
    spm_form_registration_detail_id = Column(Integer,nullable=False, primary_key=True)
    register_system_number_id = Column(Integer,ForeignKey("trx_vehicle_sales_order_form_registration.register_system_number"))
    register_document_number = Column(Integer,nullable=False)
    spm_document_number = Column(String,nullable=False)
    last_taken_system_number = Column(Integer,nullable=False)
    last_return_system_number = Column(Integer,nullable=False)
    last_spm_status = Column(String,nullable=False)

    #back populates
    spm_form_reg_header = relationship("TrxVehicleSalesOrderFormRegistration",
                                       back_populates="spm_form_reg_detail", 
                                       foreign_keys=[register_system_number_id])