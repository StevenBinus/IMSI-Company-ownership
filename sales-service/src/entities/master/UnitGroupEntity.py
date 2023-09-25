from sqlalchemy import Column, Boolean, Integer, String
from sqlalchemy.orm import relationship
from src.configs.database import Base

class MtrUnitGroup(Base):
    __tablename__ = "mtr_unit_group"
    is_active = Column(Boolean,nullable=False,default=True)
    unit_group_id = Column(Integer,primary_key=True,autoincrement=True)
    unit_group_code = Column(String(100),nullable=False)
    unit_group_name = Column(String(100),nullable=False,default="")
    #back populates
    unitgroup_model = relationship("MtrUnitModel", back_populates="model_unitgroup", foreign_keys="MtrUnitModel.unit_group_id")
