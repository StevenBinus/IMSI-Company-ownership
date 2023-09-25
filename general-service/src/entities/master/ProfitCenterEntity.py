from sqlalchemy import Column, String, Integer, Boolean,ForeignKey
from sqlalchemy.orm import relationship
from src.configs.database import Base

class MtrProfitCenter(Base):
    __tablename__ = "mtr_profit_center"
    is_active = Column(Boolean, nullable=False, default=True)
    profit_center_id = Column(Integer, autoincrement=True,primary_key=True)
    profit_center_code = Column(String(5),nullable=False,unique=True)
    profit_center_name = Column(String(100), nullable=False)
    representative = Column(Boolean, nullable=False)
    business_category_id = Column(Integer,ForeignKey("mtr_business_category.business_category_id",ondelete="CASCADE"))
    
    #back populates
    business_category_profit_center = relationship("MtrBusinessCategory",back_populates="profit_center_business_category", foreign_keys=[business_category_id])
    profit_center_source_document = relationship("MtrDocument", back_populates="source_document_profit_center", foreign_keys="MtrDocument.profit_center_id")
    profit_center_source_document_detail = relationship("MtrDocumentDetail", back_populates="source_document_detail_profit_center", foreign_keys="MtrDocumentDetail.profit_center_id")
    profit_center_bfk = relationship("MtrCostProfitMap", back_populates="profit_center_fk", foreign_keys="MtrCostProfitMap.profit_center_id")
    profit_virtual_account = relationship("MtrCustomerVirtualAccount", back_populates="virtual_account_profit", foreign_keys="MtrCustomerVirtualAccount.profit_center_id")
