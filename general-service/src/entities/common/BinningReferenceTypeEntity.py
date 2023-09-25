from sqlalchemy import String,Column,Integer, Boolean
from src.configs.database import Base

class MtrBinningReferenceType(Base):
    __tablename__ = 'mtr_binning_reference_type'
    is_active = Column(Boolean, default=True, nullable=False)
    binning_reference_type_id = Column(Integer, autoincrement=True, primary_key=True)
    binning_reference_type_code = Column(String(10), nullable=False, unique=True)
    binning_reference_type_description = Column(String(50), nullable=False)
