from sqlalchemy import Column,String,Integer,Boolean
from sqlalchemy.orm import relationship
from src.configs.database import Base
from sqlalchemy.orm import relationship

class MtrCostCenter(Base):
    __tablename__ = "mtr_cost_center"
    is_active = Column(Boolean,nullable=False,default=True)
    cost_center_id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    cost_center_code = Column(String(10),nullable=True)
    cost_center_name = Column(String(100),nullable=True)

    # back populates
    cost_center_bfk = relationship("MtrCostProfitMap", back_populates="cost_center_fk", foreign_keys="MtrCostProfitMap.cost_center_id")
