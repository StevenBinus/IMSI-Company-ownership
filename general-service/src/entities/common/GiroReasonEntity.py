from sqlalchemy import String,Column,Integer, Boolean
from src.configs.database import Base

class MtrGiroReason(Base):
    __tablename__ = 'mtr_giro_reason'
    is_active = Column(Boolean, default=True, nullable=False)
    giro_reason_id = Column(Integer, autoincrement=True, primary_key=True)
    giro_reason_code = Column(String(10), nullable=False, unique=True)
    giro_reason_description = Column(String(50), nullable=False)