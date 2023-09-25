from sqlalchemy import String,Column,Integer, Boolean
from src.configs.database import Base

class MtrATPMOrderType(Base):
    __tablename__ = 'mtr_atpm_order_type'
    is_active = Column(Boolean, default=True, nullable=False)
    atpm_order_type_id = Column(Integer, autoincrement=True, primary_key=True)
    atpm_order_type_code = Column(String(20), nullable=False, unique=True)
    atpm_order_type_description = Column(String(256), nullable=False)