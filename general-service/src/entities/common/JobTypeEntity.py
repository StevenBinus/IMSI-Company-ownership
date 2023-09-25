from sqlalchemy import String,Column,Integer, Boolean
from src.configs.database import Base

class MtrJobType(Base):
    __tablename__ = 'mtr_job_type'
    is_active = Column(Boolean, default=True, nullable=False)
    job_type_id = Column(Integer, autoincrement=True, primary_key=True)
    job_type_code = Column(String(5), nullable=False, unique=True)
    job_type_name = Column(String(100), nullable=False)