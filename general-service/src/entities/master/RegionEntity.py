from sqlalchemy import Column, String, Integer, Boolean
from sqlalchemy.orm import relationship
from src.configs.database import Base


class MtrRegion(Base):
    __tablename__ = "mtr_region"
    is_active = Column(Boolean, nullable=False, default=True)
    region_id = Column(Integer, primary_key=True)
    region_code = Column(String(10), nullable=True)
    region_name = Column(String(35), nullable=True)
    
    #back populates
    area_region = relationship("MtrArea",back_populates="region_area",foreign_keys="MtrArea.region_id")
