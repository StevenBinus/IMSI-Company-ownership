from sqlalchemy import String,Column,Integer, Boolean
from src.configs.database import Base

class MtrFollowUpType(Base):
    __tablename__ = 'mtr_follow_up_type'
    is_active = Column(Boolean, default=True, nullable=False)
    follow_up_type_id = Column(Integer, autoincrement=True, primary_key=True)
    follow_up_type_code = Column(String(10), nullable=False, unique=True)
    follow_up_type_description = Column(String(50), nullable=False)