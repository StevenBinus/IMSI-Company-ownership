from sqlalchemy import String,Column,Integer, Boolean
from src.configs.database import Base

class MtrFreeAccessories(Base):
    __tablename__ = 'mtr_free_accessories'
    is_active = Column(Boolean, default=True, nullable=False)
    free_accessories_id = Column(Integer, autoincrement=True, primary_key=True)
    free_accessories_code = Column(String(10), nullable=False, unique=True)
    free_accessories_description = Column(String(50), nullable=False)