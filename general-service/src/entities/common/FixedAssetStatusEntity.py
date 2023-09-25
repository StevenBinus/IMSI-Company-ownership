from sqlalchemy import String,Column,Integer, Boolean
from src.configs.database import Base

class MtrFixedAssetStatus(Base):
    __tablename__ = 'mtr_fixed_asset_status'
    is_active = Column(Boolean, default=True, nullable=False)
    fixed_asset_status_id = Column(Integer, autoincrement=True, primary_key=True)
    fixed_asset_status_code = Column(String(10), nullable=False, unique=True)
    fixed_asset_status_description = Column(String(50), nullable=False)