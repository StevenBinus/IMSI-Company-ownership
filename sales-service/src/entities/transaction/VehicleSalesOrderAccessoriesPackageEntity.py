from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from src.configs.database import Base

class TrxVehicleSalesOrderAccessoriesPackage(Base):
    __tablename__ = "trx_vehicle_sales_order_accessories_package"
    vehicle_sales_order_accessories_package_system_number = Column(Integer,primary_key=True,autoincrement=True)
    vehicle_sales_order_system_number = Column(Integer,ForeignKey("trx_vehicle_sales_order.vehicle_sales_order_system_number"))
    system_number_old = Column(Integer,nullable=False)
    item_package_code = Column(String(25),nullable=False)
    #back populates    
    salesorderaccessories_salesordermaster = relationship("TrxVehicleSalesOrder", back_populates="salesordermaster_salesorderaccessories", foreign_keys=[vehicle_sales_order_system_number])
