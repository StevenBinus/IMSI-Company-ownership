from src.configs.database import Base
from sqlalchemy import Column, Integer,String, ForeignKey, DateTime, Float, Boolean
from sqlalchemy.orm import relationship
from datetime import datetime

class TrxUnitPurchaseOrderBBNCostDetail(Base):
    __tablename__ = "trx_unit_purchase_order_bbn_cost_detail"
    purchase_order_bbn_cost_detail_system_number = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    purchase_order_bbn_detail_system_number = Column(Integer, ForeignKey("trx_unit_purchase_order_bbn_detail.purchase_order_bbn_detail_system_number"), nullable=False)
    cost_type_id = Column(Integer, nullable=False) #Fk dari tabel mtr_cost_type dari general service - common
    cost_amount = Column(Float, nullable=False)
    vat_charged = Column(Boolean, nullable=False)