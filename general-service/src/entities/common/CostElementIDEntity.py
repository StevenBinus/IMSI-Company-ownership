from sqlalchemy import String,Column,Integer, Boolean
from src.configs.database import Base

class MtrCostElementID(Base):
    __tablename__ = 'mtr_cost_element_id'
    is_active = Column(Boolean, default=True, nullable=False)
    cost_element_id = Column(Integer, autoincrement=True, primary_key=True)
    cost_element_variable = Column(String(10), nullable=False, unique=True)
    cost_element_value = Column(String(10), nullable=False, unique=True)
    cost_element_description = Column(String(50), nullable=False)