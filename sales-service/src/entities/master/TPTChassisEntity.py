from sqlalchemy import Column, Boolean, Integer, String, ForeignKey, CHAR
from sqlalchemy.orm import relationship
from src.configs.database import Base

class MtrTPTChassis(Base):
    __tablename__ = "mtr_tpt_chassis"
    is_active = Column(Boolean,nullable=False,default=True)
    tpt_chassis_id = Column(Integer,nullable=False,primary_key=True,autoincrement=True)
    tpt_id = Column(Integer,ForeignKey("mtr_tpt.tpt_id"),nullable=False)
    vehicle_id = Column(Integer,ForeignKey("mtr_vehicle.vehicle_id"),nullable=False)
    chassis_no_status = Column(CHAR(1),nullable=False)
    #back populates
    tptchassis_tpt = relationship("MtrTPT", back_populates="tpt_tptchassis",foreign_keys=[tpt_id])
    tptchassis_vehicle = relationship("MtrVehicle", back_populates="vehicle_tptchassis", foreign_keys=[vehicle_id])
