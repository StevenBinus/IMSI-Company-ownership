from sqlalchemy import Column, Boolean, DateTime, Integer, String, ForeignKey, CHAR
from sqlalchemy.orm import relationship
from src.configs.database import Base

class MtrVariantTransmission(Base):
    __tablename__ = "mtr_variant_transmission"
    is_active = Column(Boolean,nullable=False,default=False)
    variant_transmission_id = Column(Integer,primary_key=True,autoincrement=True)
    variant_transmission_code = Column(String(5),unique=True,nullable=False)
    variant_transmission_name = Column(String(30),nullable=False)
    #back populates
    transmission_unitvariant = relationship("MtrUnitVariant",back_populates="unitvariant_transmission",foreign_keys="MtrUnitVariant.transmission_id")
