from sqlalchemy import String,Column,Integer, Boolean
from src.configs.database import Base

class MtrDropStatus(Base):
    __tablename__ = 'mtr_drop_status'
    is_active = Column(Boolean, default=True, nullable=False)
    drop_status_id = Column(Integer, autoincrement=True, primary_key=True)
    drop_status_code = Column(String(10), nullable=False, unique=True)
    drop_status_description = Column(String(50), nullable=False)