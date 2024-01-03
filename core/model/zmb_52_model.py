from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Boolean, DateTime, create_engine, Float
from sqlalchemy.orm import sessionmaker
from database import connection_database

Base = declarative_base()

engine = connection_database.connection()
engine = create_engine(engine)

Session = sessionmaker(bind=engine)
session = Session()


# TODO confirm with Rodrigo if name column last_sales_date is correct
# TODO confirm with Rodrigo if name column part_day is correct cause in the excel file is named as part_age
# TODO confirm with Rodrigo if name column part_age is correct cause in the excel file is named as part_age
class ZMB52(Base):
    __tablename__ = 'ZMB52'
    id = Column(Integer, primary_key=True)
    country = Column(String(2))
    part_suffix = Column(String())
    part_number = Column(String())
    material = Column(String())
    part_description = Column(String())
    base_unit_of_measure = Column(String())
    total_qty_stock = Column(Float(3))
    total_unrestricted_stock = Column(Float(3))
    sales_last_52_weeks = Column(Float(3))
    last_goods_receipt = Column(DateTime)
    last_sales_date = Column(DateTime)
    marketing_code = Column(String())
    product_category = Column(String())
    product_code = Column(String())
    shelf_life_code = Column(Integer())
    material_status = Column(String())
    part_day = Column(Integer())
    part_age = Column(Float(3))
    total_stock_value = Column(Float(2))
    total_consignment_stock = Column(Float(3))
    total_blocked_stoke = Column(Float(3))
    moving_average_price = Column(Float(2))
    net_purchase_price = Column(Float(2))
    last_delivery_date = Column(DateTime)
    last_inventory_date = Column(DateTime)
    total_stock_in_transit = Column(Float(3))
    report_date = Column(DateTime)
    snapshot_date = Column(DateTime)

    def __repr__(self):
        return f"<Account(id={self.id}, country={self.country}, part_suffix={self.part_suffix}, " \
               f"part_number={self.part_number}, material={self.material}, part_description={self.part_description}, " \
               f"base_unit_of_measure={self.base_unit_of_measure}, total_qty_stock={self.total_qty_stock}, " \
               f"total_unrestricted_stock={self.total_unrestricted_stock}, sales_last_52_weeks={self.sales_last_52_weeks}, " \
               f"last_goods_receipt={self.last_goods_receipt}, last_sales_date={self.last_sales_date}, " \
               f"marketing_code={self.marketing_code}, product_category={self.product_category}, " \
               f"product_code={self.product_code}, shelf_life_code={self.shelf_life_code}, " \
               f"material_status={self.material_status}, part_day={self.part_day}, " \
               f"part_age={self.part_age}, total_stock_value={self.total_stock_value}, " \
               f"total_consignment_stock={self.total_consignment_stock}, " \
               f"total_blocked_stoke={self.total_blocked_stoke}, " \
               f"moving_average_price={self.moving_average_price}, " \
               f"net_purchase_price={self.net_purchase_price}, " \
               f"last_delivery_date={self.last_delivery_date}, " \
               f"last_inventory_date={self.last_inventory_date}, " \
               f"total_stock_in_transit={self.total_stock_in_transit}, " \
               f"report_date={self.report_date}, " \
               f"snapshot_date={self.snapshot_date})>"

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


Base.metadata.create_all(engine)
