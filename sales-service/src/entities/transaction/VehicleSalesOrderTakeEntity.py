from sqlalchemy import Column,String,Integer,DateTime, ForeignKey
from sqlalchemy.orm import relationship
from src.configs.database import Base

class TrxVehicleSalesOrderTake(Base):
    __tablename__ = "trx_vehicle_sales_order_take"
    taken_system_number = Column(Integer,primary_key=True,autoincrement=True)
    taken_system_number_old = Column(Integer,nullable=False)
    company_id = Column(Integer,nullable=False) #FK to general service company master using API/RabbitMQ
    taken_document_number = Column(String(20),nullable=False)
    brand_id = Column(Integer,ForeignKey("mtr_brand.brand_id"),nullable=False)
    spm_issued_date = Column(DateTime,nullable=False)
    spm_issued_by = Column(Integer,nullable=False) #FK to general service user_details using API/RabbitMQ
    spm_issued_to = Column(Integer,nullable=False) #FK to general service user_details using API/RabbitMQ     
    total_spm_taken = Column(Integer,nullable=False)
    print_counter = Column(Integer, nullable=False, default=0)

    #back populates
    spm_take_brand = relationship("MtrBrand", back_populates="brand_spm_take",foreign_keys=[brand_id])
    takensysnoheader_detail = relationship("TrxVehicleSalesOrderTakeDetail", back_populates="takensysnodetail_header",
                                           foreign_keys="TrxVehicleSalesOrderTakeDetail.taken_system_number")
