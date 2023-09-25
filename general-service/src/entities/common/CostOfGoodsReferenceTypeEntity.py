from sqlalchemy import String,Column,Integer, Boolean
from src.configs.database import Base

class MtrCostOfGoodsReferencesType(Base):
    __tablename__ = 'mtr_cost_of_goods_references_type'
    is_active = Column(Boolean, default=True, nullable=False)
    cost_of_goods_references_type_id = Column(Integer, autoincrement=True, primary_key=True)
    cost_of_goods_references_type_code = Column(String(10), nullable=False, unique=True)
    cost_of_goods_references_type_description = Column(String(50), nullable=False)