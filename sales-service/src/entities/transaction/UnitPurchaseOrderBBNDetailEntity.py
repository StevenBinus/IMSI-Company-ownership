from src.configs.database import Base
from sqlalchemy import Column, Integer,String, ForeignKey, DateTime, Float, Boolean
from sqlalchemy.orm import relationship
from datetime import datetime

class TrxUnitPurchaseOrderBBNDetail(Base):
    __tablename__ = "trx_unit_purchase_order_bbn_detail"
    purchase_order_bbn_detail_system_number = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    purchase_order_bbn_system_number = Column(Integer, ForeignKey("trx_unit_purchase_order_bbn.purchase_order_bbn_system_number"), nullable=False)
    purchase_order_line_net_amount = Column(Float, nullable=False, default=0)
    vehicle_id = Column(Integer, ForeignKey("mtr_vehicle.vehicle_id"), nullable=False)
    purchase_price = Column(Float, nullable=False, default=0)

    po_bbn_stnk = relationship("TrxUnitGoodsReceiveBBNSTNK", back_populates="stnk_po_bbn", foreign_keys="TrxUnitGoodsReceiveBBNSTNK.purchase_order_bbn_detail_system_number")