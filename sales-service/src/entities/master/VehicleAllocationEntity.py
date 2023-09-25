from sqlalchemy import Column, Boolean, DateTime, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from src.configs.database import Base


class MtrVehicleAllocation(Base):
    __tablename__ = "mtr_vehicle_allocation"
    is_active = Column(Boolean, nullable=False, default=True)
    vehicle_allocation_id = Column(
        Integer, nullable=False, primary_key=True, autoincrement=True
    )
    vehicle_id = Column(Integer, ForeignKey("mtr_vehicle.vehicle_id"), nullable=False)
    vehicle_allocation_number = Column(String(30), nullable=True, default="")
    vehicle_allocation_line_number = Column(String(30), nullable=True, default="")
    vehicle_allocation_date = Column(String(30), nullable=True, default="")
    vehicle_allocation_client = Column(DateTime, nullable=True, default="")
    vehicle_allocation_employee = Column(String(30), nullable=True, default="")
