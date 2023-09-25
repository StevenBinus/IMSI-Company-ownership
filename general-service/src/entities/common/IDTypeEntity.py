from sqlalchemy import String,Column,Integer, Boolean
from src.configs.database import Base
from sqlalchemy.orm import relationship

class MtrIDType(Base):
    __tablename__ = 'mtr_id_type'
    is_active = Column(Boolean, default=True, nullable=False)
    id_type_id = Column(Integer, autoincrement=True, primary_key=True)
    id_code = Column(String(10), nullable=False, unique=True)
    id_description = Column(String(50), nullable=False)

    #back populates
    customer_id_type_bfk = relationship("MtrCustomer", back_populates="id_type_fk", foreign_keys="MtrCustomer.id_type")