from sqlalchemy import String,Column,Integer, Boolean
from src.configs.database import Base

class MtrFeedback(Base):
    __tablename__ = 'mtr_feedback'
    is_active = Column(Boolean, default=True, nullable=False)
    feedback_id = Column(Integer, autoincrement=True, primary_key=True)
    feedback_code = Column(String(10), nullable=False, unique=True)
    feedback_description = Column(String(50), nullable=False)