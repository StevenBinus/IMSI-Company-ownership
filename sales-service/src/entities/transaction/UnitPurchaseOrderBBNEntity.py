from src.configs.database import Base
from sqlalchemy import Column, Integer,String, ForeignKey, DateTime, Float, Boolean
from sqlalchemy.orm import relationship
from datetime import datetime

class TrxUnitPurchaseOrderBBN(Base):
    __tablename__ = "trx_unit_purchase_order_bbn"
    company_id = Column(Integer, nullable=False) #Fk dari tabel mtr_company dari general service
    dealer_representative_id = Column(Integer, nullable=True) #Fk dari tabel mtr_dealer_representative dari general service
    profit_center_id = Column(Integer, nullable=False, default=1) #Fk dari tabel mtr_profit_center dari general service
    cost_center_id = Column(Integer, nullable=False) #Fk dari tabel mtr_cost_center dari general service - master
    purchase_order_bbn_system_number = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    purchase_order_bbn_document_number = Column(String(25), nullable=False, default="")
    purchase_order_status_id = Column(Integer, nullable=False, default=1) #Fk dari tabel mtr_approval_status dari general service - common
    purchase_order_date = Column(DateTime, nullable=False)
    purchase_type_id = Column(Integer, nullable=False, default=1) #Fk dari tabel mtr_purchase_type dari general service - common
    purchase_order_remark = Column(String(512), nullable=True)
    brand_id = Column(Integer, ForeignKey("mtr_brand.brand_id"), nullable=False)
    supplier_id = Column(Integer, nullable=False) #Fk dari tabel mtr_supplier dari general service - master
    term_of_payment_id = Column(Integer, nullable=False) #Fk dari tabel mtr_term_of_payment dari general service - master
    bill_code_id = Column(Integer, nullable=False) #Fk dari tabel mtr_bill_code dari general service - common
    currency_id = Column(Integer, nullable=False, default=1) #Fk dari tabel mtr_currenct dari finance service
    order_status_id = Column(Integer, nullable=False, default=1) #Fk dari tabel mtr_order_status dari general service - commmon
    net_amount = Column(Float, nullable=True)
    total_after_vat = Column(Float, nullable=True)
    approval_request_system_number = Column(Integer, nullable=True)#Fk dari tabel trx_approval_request_source
    down_payment_request = Column(Float, nullable=True)