from sqlalchemy import String,Column,Integer, Boolean
from src.configs.database import Base
from sqlalchemy.orm import relationship

class MtrBehaviour(Base):
    __tablename__ = 'mtr_behaviour'
    is_active = Column(Boolean, default=True, nullable=False)
    behaviour_id = Column(Integer, autoincrement=True, primary_key=True)
    behaviour_code = Column(String(2), nullable=False, unique=True)
    behaviour_name = Column(String(256), nullable=False)

    #back populates
    behaviour_reference = relationship("MtrSupplierReferenceEntity",back_populates="behaviour_reference",foreign_keys="MtrSupplierReferenceEntity.supplier_behaviour_id")
