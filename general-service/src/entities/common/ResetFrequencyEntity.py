from sqlalchemy import Column,Integer,Boolean,String
from src.configs.database import Base
from sqlalchemy.orm import relationship

class MtrResetFrequency(Base):
    __tablename__ = 'mtr_reset_frequency'
    is_active = Column(Boolean, default=True, nullable=False)
    reset_frequency_id = Column(Integer, autoincrement=True, primary_key=True)
    reset_frequency_code = Column(String(20),nullable=False, unique=True)
    reset_frequency_description = Column(String(256), nullable=False)

    #back populates
    reset_frequency_source_document = relationship("MtrDocument", back_populates="source_document_reset_frequency", foreign_keys="MtrDocument.reset_frequency_id")