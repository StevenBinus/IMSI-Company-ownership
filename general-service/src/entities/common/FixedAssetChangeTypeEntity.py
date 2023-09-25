from sqlalchemy import String,Column,Integer, Boolean
from src.configs.database import Base

class MtrFixedAssetChangeType(Base):
    __tablename__ = 'mtr_fixed_asset_change_type'
    is_active = Column(Boolean, default=True, nullable=False)
    fixed_asset_change_type_id = Column(Integer, autoincrement=True, primary_key=True)
    fixed_asset_change_type_code = Column(String(10), nullable=False, unique=True)
    fixed_asset_change_type_description = Column(String(50), nullable=False)