from sqlalchemy import String,Column,Integer, Boolean
from src.configs.database import Base

class MtrItemGroup(Base):
    __tablename__ = 'mtr_item_group'
    is_active = Column(Boolean, default=True, nullable=False)
    item_group_id = Column(Integer, autoincrement=True, primary_key=True)
    item_group_code = Column(String(5), nullable=False, unique=True)
    item_group_name = Column(String(100), nullable=False)