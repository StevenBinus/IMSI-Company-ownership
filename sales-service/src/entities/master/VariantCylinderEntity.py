from sqlalchemy import Column, Boolean, DateTime, Integer, String, ForeignKey, CHAR
from sqlalchemy.orm import relationship
from src.configs.database import Base

class MtrVariantCylinder(Base):
    __tablename__ = "mtr_variant_cylinder"
    is_active = Column(Boolean,nullable=False,default=False)
    variant_cylinder_id = Column(Integer,primary_key=True,autoincrement=True)
    variant_cylinder_code = Column(String(5),unique=True,nullable=False)
    variant_cylinder_name = Column(String(30),nullable=False)
    #backpopulates
    cylinder_unitvariant = relationship("MtrUnitVariant",back_populates="unitvariant_cylinder",foreign_keys="MtrUnitVariant.cylinder_id")
