from sqlalchemy import Column, Boolean, Integer, String,Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from src.configs.database import Base


class MtrVehicleLastData(Base):
    __tablename__ = "mtr_vehicle_last_data" #LAST_STNK
    is_active = Column(Boolean,nullable=False,default=True)
    vehicle_last_id = Column(Integer,nullable=False,primary_key=True,autoincrement=True)
    vehicle_last_bill_revise_number = Column(Float,nullable=True,default=0)
    
    vehicle_id = Column(Integer,ForeignKey("mtr_vehicle.vehicle_id"),nullable=False)
    
    vehicle_last_stnk_revise_number =  Column(Float,nullable=True,default=0)
    vehicle_last_tax_revise_number = Column(Float,nullable=True,default=0)
    vehicle_last_corr_revise_number = Column(Float,nullable=True,default=0)
    vehicle_last_user_data_revise_number = Column(Float,nullable=True,default=0)
    vehicle_last_faktur_polisi_number = Column(String(30),nullable=True)
    vehicle_last_faktur_polisi_date = Column(DateTime,nullable=True,default="")
    vehicle_last_stnk_number = Column(String(30),nullable=True)
    vehicle_last_stnk_date = Column(DateTime,nullable=True,default="")
    vehicle_last_bpkb_number = Column(String(50),nullable=True)
    vehicle_last_bpkb_date = Column(DateTime,nullable=True,default="")
    vehicle_last_nik_number = Column(String(30),nullable=True)
    vehicle_last_nik_date = Column(DateTime,nullable=True,default="")

    #back populates
    last_vehicle = relationship("MtrVehicle",back_populates='vehicle_last',foreign_keys=[vehicle_id])
   
