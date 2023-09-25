from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from src.configs.database import Base
from datetime import datetime

class TrxVehicleSalesOrderFreeAccessories(Base):
    __tablename__ = "trx_vehicle_sales_order_free_accessories"
    vehicle_sales_order_free_accessories_system_number = Column(Integer,primary_key=True,autoincrement=True)
    vehicle_sales_order_system_number = Column(Integer,ForeignKey("trx_vehicle_sales_order.vehicle_sales_order_system_number"))
    system_number_old = Column(Integer,nullable=False)
    free_accessories_item_code = Column(String(25),nullable=False)
    free_accessories_quantity = Column(Integer,nullable=False)
    accessories_purchase_price = Column(Integer,nullable=True)
    free_accessories_price = Column(Integer,nullable=True)
    free_accessories_purchase_amount = Column(Integer,nullable=True)

    #back populates    
    salesorderfreeaccessories_salesordermaster = relationship("TrxVehicleSalesOrder", back_populates="salesordermaster_salesorderfreeaccessories", foreign_keys=[vehicle_sales_order_system_number])