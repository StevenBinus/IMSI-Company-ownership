from sqlalchemy import String,Column,Integer, Boolean
from src.configs.database import Base

class MtrSkillLevelCode(Base):
    __tablename__ = 'mtr_skill_level_code'
    is_active = Column(Boolean, default=True, nullable=False)
    skill_level_code_id = Column(Integer, autoincrement=True, primary_key=True)
    skill_level_code = Column(String(5), nullable=False)