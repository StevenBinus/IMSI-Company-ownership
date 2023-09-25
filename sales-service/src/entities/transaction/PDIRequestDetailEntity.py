from src.configs.database import Base
from sqlalchemy import Column,String,Integer, ForeignKey, DateTime, TIMESTAMP, Float

class TrxPDIRequestDetail(Base):
    __tablename__ = "trx_pdi_request_detail"
    pdi_request_detail_system_number = Column(Integer,primary_key=True,autoincrement=True)
    pdi_request_detail_line_number = Column(Integer,nullable=False)
    pdi_request_system_number = Column(Integer,ForeignKey("trx_pdi_request.pdi_request_system_number"))
    operation_number_id = Column(Integer, nullable = False) #connect to general service
    vehicle_id = Column(Integer,ForeignKey("mtr_vehicle.vehicle_id"))
    estimated_delivery = Column(DateTime, nullable=False)
    pdi_request_detail_line_remark = Column(String (256))
    frt = Column(Float,nullable=False)
    service_date = Column(DateTime, nullable=False)
    service_time = Column(Float,nullable=False)
    pdi_request_detail_line_status_id = Column(Integer, nullable= False)#Connect to general-service
    booking_system_number = Column(Integer, nullable=True)
    work_order_system_number = Column(Integer, nullable=True)
    invoice_payable_system_no = Column(Integer, nullable=True)