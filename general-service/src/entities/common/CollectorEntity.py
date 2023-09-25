from sqlalchemy import String,Column,Integer, Boolean
from sqlalchemy.orm import relationship 
from src.configs.database import Base

class MtrCollector(Base):
    __tablename__ = 'mtr_collector'
    is_active = Column(Boolean, default=True, nullable=False)
    collector_id = Column(Integer, autoincrement=True, primary_key=True)
    collector_code = Column(String(10), nullable=False, unique=True)
    collector_description = Column(String(50), nullable=False)

    #back populates
    collector_bfk = relationship("MtrCustomer", back_populates="collector_fk", foreign_keys="MtrCustomer.collector_id")