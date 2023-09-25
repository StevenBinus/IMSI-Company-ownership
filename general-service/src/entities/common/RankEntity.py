from sqlalchemy import Column,Integer,Boolean,String
from src.configs.database import Base

class MtrRank(Base):
    __tablename__ = 'mtr_rank'
    is_active = Column(Boolean, default=True, nullable=False)
    rank_id = Column(Integer, autoincrement=True, primary_key=True)
    rank_code = Column(String(20),nullable=False, unique=True)
    rank_description = Column(String(256), nullable=False)