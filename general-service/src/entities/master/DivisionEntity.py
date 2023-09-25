from sqlalchemy import String,Column,Integer, Boolean,CHAR
from sqlalchemy.orm import relationship
from src.configs.database import Base

class MtrDivision(Base):
    __tablename__ = "mtr_division"
    is_active = Column(Boolean, default=True, nullable=False)
    division_id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    division_code = Column(CHAR(3), nullable=False)
    division_name = Column(String(35), nullable=False)

    #back populates
    reference_pic_division=relationship("MtrSupplierReferencePic",back_populates = "division_reference_pic",foreign_keys="MtrSupplierReferencePic.pic_division_id")