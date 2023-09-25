from src.configs.database import Base
from sqlalchemy import Column, Integer,String, ForeignKey, DateTime, Float, Boolean
from sqlalchemy.orm import relationship
from datetime import datetime

class TrxUnitGoodsReceiveBBNBPKB(Base):
    __tablename__ = "trx_unit_goods_receive_bbn_bpkb"
    company_id = Column(Integer, nullable=False) #Fk dari tabel mtr_company dari general service
    goods_receive_bbn_bpkb_system_number = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    goods_receive_bbn_bpkb_document_number = Column(String(25), nullable=False, default="")
    goods_receive_bbn_bpkb_date = Column(DateTime, nullable=False)
    goods_receive_bbn_stnk_system_number = Column(Integer, ForeignKey("trx_unit_goods_receive_bbn_stnk.goods_receive_bbn_stnk_system_number"), nullable=False)
    bpkb_number = Column(String(30), nullable=False)
    bpkb_issue_date = Column(DateTime, nullable=False)
    bpkb_received_date = Column(DateTime, nullable=False)
    bpkb_received_by = Column(Integer, nullable=False) #Fk dari tabel mtr_user_detail dari user_service
    supplier_reference_number = Column(String(25), nullable=True)
    goods_receive_bbn_bpkb_remark = Column(String(512), nullable=True)
    bpkb_send_document_number = Column(String(25), nullable=True)
    bpkb_send_date = Column(DateTime, nullable=True)
    bpkb_receiver_name = Column(String(40), nullable=True)
    bpkb_receiver_id_number = Column(String(20), nullable=True)

    bpkb_stnk = relationship("TrxUnitGoodsReceiveBBNSTNK", back_populates="stnk_bpkb", foreign_keys=[goods_receive_bbn_stnk_system_number])