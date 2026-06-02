from sqlalchemy import Column, Integer, Float,String,DateTime,ForeignKey, create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from database.modals.base_modal import Base

class Customer(Base):
    __tablename__ = 'dim_customers_info'
    customer_id = Column(String)
    customer_sr_key = Column(Integer,primary_key=True)
    customer_name = Column(String)
    customer_email = Column(String)
    customer_phone = Column(String)
    customer_address = Column(String)
    customer_state = Column(String)
    customer_country = Column(String)

class Product(Base):
    __tablename__ = 'dim_products_info'
    product_id = Column(String)
    product_sr_key = Column(Integer, primary_key=True)
    product_name = Column(String)
    product_category = Column(String)

class Order(Base):
    __tablename__ = 'dim_orders_info'
    order_id = Column(String)
    order_sr_key = Column(Integer, primary_key=True)
    order_status = Column(String)
    order_date = Column(DateTime)

class Payment(Base):
    __tablename__ = 'dim_payment_info'
    payment_id = Column(Integer, autoincrement=True)
    payment_sr_key = Column(Integer, primary_key=True)
    payment_method = Column(String)

class Date(Base):
    __tablename__ = 'dim_date'
    date_id = Column(Integer, autoincrement=True)
    date_sr_key = Column(Integer, primary_key=True)
    date = Column(DateTime)
    day = Column(Integer)
    month = Column(Integer)
    year = Column(Integer)

class Shipping(Base):
    __tablename__ = 'dim_shipping_info'
    shipping_id = Column(Integer, autoincrement=True)
    shipping_sr_key = Column(Integer, primary_key=True)
    shipping_address = Column(String)
    shipping_city = Column(String)
    delivery_days = Column(Integer)

class FactSales(Base):
    __tablename__ = 'fact_sales'
    sales_id = Column(Integer,primary_key=True, autoincrement=True)
    customer_sr_key = Column(Integer,ForeignKey('dim_customers_info.customer_sr_key'),nullable=False)
    product_sr_key = Column(Integer,ForeignKey('dim_products_info.product_sr_key'),nullable=False)
    order_sr_key = Column(Integer,ForeignKey('dim_orders_info.order_sr_key'),nullable=False)
    payment_sr_key = Column(Integer,ForeignKey('dim_payment_info.payment_sr_key'),nullable=False)
    date_sr_key = Column(Integer,ForeignKey('dim_date.date_sr_key'),nullable=False)
    shipping_sr_key = Column(Integer,ForeignKey('dim_shipping_info.shipping_sr_key'),nullable=False)
    unit_price = Column(Float)
    quantity = Column(Integer)
    discount = Column(Float)
    total_amount = Column(Float)
