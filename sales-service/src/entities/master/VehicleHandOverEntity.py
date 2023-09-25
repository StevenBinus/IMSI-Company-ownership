from sqlalchemy import Column, Boolean, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from src.configs.database import Base


class MtrVehicleHandOver(Base):
    __tablename__ = "mtr_vehicle_handover" #BPK
    is_active = Column(Boolean,nullable=False,default=True)
    vehicle_handover_id = Column(Integer,nullable=False,primary_key=True,autoincrement=True)
    
    vehicle_id = Column(Integer,ForeignKey("mtr_vehicle.vehicle_id"),nullable=False)
    
    vehicle_handover_customer_code =  Column(String(20),nullable=True)
    vehicle_handover_customer_name = Column(String(100),nullable=True)
    vehicle_handover_document_date = Column(DateTime,nullable=True,default="")
    vehicle_handover_document_number = Column(String(30),nullable=True)
    vehicle_radiotape_code = Column(String(20),nullable=True)
    vehicle_service_booking_number = Column(String(50),nullable=True)
    
    #back populates
    handover_vehicle = relationship("MtrVehicle",back_populates='vehicle_handover',foreign_keys=[vehicle_id])
   
