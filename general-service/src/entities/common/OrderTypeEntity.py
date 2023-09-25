from sqlalchemy import String,Column,Integer, Boolean
from src.configs.database import Base
from sqlalchemy.orm import relationship

class MtrOrderType(Base):
    __tablename__ = 'mtr_order_type'
    is_active = Column(Boolean, default=True, nullable=False)
    order_type_id = Column(Integer, autoincrement=True, primary_key=True)
    order_type_code = Column(String(5), nullable=False, unique=True)
    order_type_name = Column(String(100), nullable=False)

    #back populates
    order_type_bfk = relationship("MtrDiscountSetting", back_populates="order_type_fk", foreign_keys="MtrDiscountSetting.order_type_id")