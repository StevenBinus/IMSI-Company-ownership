from sqlalchemy import Column, Boolean, Integer, String
from sqlalchemy.orm import relationship
from src.configs.database import Base

class MtrVariantUnitType(Base):
    __tablename__ = "mtr_variant_unit_type"
    is_active = Column(Boolean,nullable=False,default=False)
    variant_unit_type_id = Column(Integer,primary_key=True,autoincrement=True)
    variant_unit_type_code = Column(String(5),unique=True,nullable=False)
    variant_unit_type_name = Column(String(30),nullable=False)
    #back populates
    unittype_unitvariant = relationship("MtrUnitVariant",back_populates="unitvariant_unittype",foreign_keys="MtrUnitVariant.unit_type_id")