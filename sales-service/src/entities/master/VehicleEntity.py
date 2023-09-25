from sqlalchemy import Column, Boolean, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from src.configs.database import Base


class MtrVehicle(Base):
    __tablename__ = "mtr_vehicle"
    is_active = Column(Boolean, nullable=False, default=False)
    vehicle_id = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    vehicle_chassis_number = Column(String(30), nullable=False, unique=True)
    vehicle_engine_number = Column(String(30), nullable=True, default="")
    vehicle_transmission = Column(String(10), nullable=True, default="")
    vehicle_wheel_drive = Column(String(10), nullable=True, default="")
    vehicle_brand_id = Column(Integer, ForeignKey("mtr_brand.brand_id"))
    vehicle_colour_id = Column(Integer, ForeignKey("mtr_colour.colour_id"))
    vehicle_variant_id = Column(Integer, ForeignKey("mtr_unit_variant.variant_id"))
    # vehicle_model = relationship("MtrUnitModel", back_populates="model_vehicle", foreign_keys="MtrUnitModel.vehicle_id")
    vehicle_tptchassis = relationship(
        "MtrTPTChassis", back_populates="", foreign_keys="MtrTPTChassis.vehicle_id"
    )
