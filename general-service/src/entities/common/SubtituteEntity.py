from sqlalchemy import Column,Integer,Boolean,String
from src.configs.database import Base

class MtrSubtitute(Base):
    __tablename__ = 'mtr_substitute'
    is_active = Column(Boolean, default=True, nullable=False)
    subtitute_id = Column(Integer, autoincrement=True, primary_key=True)
    subtitute_code = Column(String(20),nullable=False, unique=True)
    subtitute_description = Column(String(256), nullable=False)