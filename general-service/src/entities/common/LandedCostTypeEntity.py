from sqlalchemy import String,Column,Integer, Boolean
from src.configs.database import Base

class MtrLandedCostType(Base):
    __tablename__ = 'mtr_landed_cost_type'
    is_active = Column(Boolean, default=True, nullable=False)
    landed_cost_type_id = Column(Integer, autoincrement=True, primary_key=True)
    landed_cost_type_code = Column(String(10), nullable=False, unique=True)
    landed_cost_type_name = Column(String(50), nullable=False)
