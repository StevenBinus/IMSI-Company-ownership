from sqlalchemy import Column, Boolean, DateTime, Integer, String, ForeignKey, CHAR
from sqlalchemy.orm import relationship
from src.configs.database import Base

class MtrVariantFuel(Base):
    __tablename__ = "mtr_variant_fuel"
    is_active = Column(Boolean,nullable=False,default=False)
    variant_fuel_id = Column(Integer,primary_key=True,autoincrement=True)
    variant_fuel_code = Column(String(5),unique=True,nullable=False)
    variant_fuel_name = Column(String(30),nullable=False)
    #back populates
    fuel_unitvariant = relationship("MtrUnitVariant",back_populates="unitvariant_fuel",foreign_keys="MtrUnitVariant.fuel_id")