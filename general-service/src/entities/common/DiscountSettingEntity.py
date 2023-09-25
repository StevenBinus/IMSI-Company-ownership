from sqlalchemy import Column,Integer,Boolean,String, Float, ForeignKey, UniqueConstraint
from src.configs.database import Base
from sqlalchemy.orm import relationship

class MtrDiscountSetting(Base):
    __tablename__ = 'mtr_discount_setting'
    is_active = Column(Boolean, default=True, nullable=False)
    discount_setting_id = Column(Integer, autoincrement=True, primary_key=True)
    customer_price_code = Column(String(10), nullable=False, default="")
    item_level_1 = Column(String(10), nullable=True, default=0)
    order_type_id = Column(Integer, ForeignKey("mtr_order_type.order_type_id"), nullable=True, default=0)
    discount_percentage = Column(Float, nullable=True, default=0)

    #back populates
    __table_args__ = (UniqueConstraint('customer_price_code', 'item_level_1', 'order_type_id', name='_unique_field_customer_ship'),)
    order_type_fk = relationship("MtrOrderType", back_populates="order_type_bfk", foreign_keys=[order_type_id])