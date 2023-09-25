from sqlalchemy import Column, Boolean, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from src.configs.database import Base


class MtrVehicleRegistrationCertificate(Base):
    __tablename__ = "mtr_vehicle_registration_certificate" #STNK
    is_active = Column(Boolean,nullable=False,default=True)
    vehicle_registration_certificate_id = Column(Integer,nullable=False,primary_key=True,autoincrement=True)
    vehicle_registration_certificate_code = Column(String(20),nullable=True)
    
    vehicle_id = Column(Integer,ForeignKey("mtr_vehicle.vehicle_id"),nullable=False)
    
    vehicle_registration_certificate_tnkb = Column(String(10),nullable=True)
    vehicle_registration_certificate_number  = Column(String(30),nullable=True)
     
    vehicle_registration_certificate_city_id = Column(Integer,nullable=True) # FK to mtr_city from general service
    
    vehicle_registration_certificate_valid_date = Column(DateTime,nullable=True,default="")
    vehicle_registration_certificate_owner_name = Column(String(100),nullable=True)
    
    vehicle_registration_certificate_address_id = Column(Integer,nullable=True) # FK to mtr_address from general service
    
    vehicle_registration_certificate_tnkb_colour = Column(String(20),nullable=True)
    vehicle_bpkb_number = Column(String(50),nullable=True)
    vehicle_bpkb_date = Column(DateTime,nullable=True,default="")

   
    #back populates
    vehicleregistcertif_vehicle = relationship("MtrVehicle",back_populates='vehicle_vehicleregistcertif',foreign_keys=[vehicle_id])
    
    