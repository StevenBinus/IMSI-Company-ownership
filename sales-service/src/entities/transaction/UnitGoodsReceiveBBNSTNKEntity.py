from src.configs.database import Base
from sqlalchemy import Column, Integer,String, ForeignKey, DateTime, Float, Boolean
from sqlalchemy.orm import relationship
from datetime import datetime

class TrxUnitGoodsReceiveBBNSTNK(Base):
    __tablename__ = "trx_unit_goods_receive_bbn_stnk"
    company_id = Column(Integer, nullable=False) #Fk dari mtr_company di general service
    goods_receive_bbn_stnk_system_number = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    goods_receive_bbn_stnk_document_number = Column(String(25), nullable=False, default="")
    goods_receive_bbn_stnk_date = Column(DateTime, nullable=False)
    purchase_order_bbn_detail_system_number = Column(Integer, ForeignKey("trx_unit_purchase_order_bbn_detail.purchase_order_bbn_detail_system_number"), nullable=False)
    police_invoice_number = Column(String(30), nullable=False)
    stnk_number = Column(String(25), nullable=False)
    stnk_expired_date = Column(DateTime, nullable=False)
    stnk_received_date = Column(DateTime, nullable=False)
    stnk_received_by = Column(Integer, nullable=False) #Fk dari mtr_user_details dari user service
    supplier_reference_number = Column(String(25), nullable=True)
    goods_receive_bbn_stnk_remark = Column(String(512), nullable=True)
    stnk_send_document_number = Column(String(25), nullable=True)
    stnk_send_date = Column(DateTime, nullable=True)
    stnk_receiver_name = Column(String(40), nullable=True)
    stnk_receiver_id_number = Column(String(20), nullable=True)

    stnk_po_bbn = relationship("TrxUnitPurchaseOrderBBNDetail", back_populates="po_bbn_stnk", foreign_keys=[purchase_order_bbn_detail_system_number])
    stnk_bpkb = relationship("TrxUnitGoodsReceiveBBNBPKB", back_populates="bpkb_stnk", foreign_keys="TrxUnitGoodsReceiveBBNBPKB.goods_receive_bbn_stnk_system_number")