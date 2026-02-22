from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    parent_id = Column(Integer, nullable=True)
    level = Column(Integer)


class Manufacturer(Base):
    __tablename__ = "manufacturers"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    official_url = Column(String)


class Series(Base):
    __tablename__ = "series"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    manufacturer_id = Column(Integer, ForeignKey("manufacturers.id"))
    category_id = Column(Integer, ForeignKey("categories.id"))


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    series_id = Column(Integer, ForeignKey("series.id"))

    model_number = Column(String, index=True)
    jan_code = Column(String)
    product_name = Column(String)

    product_page_url = Column(String)
    spec_pdf_url = Column(String)

    image_url = Column(String)
    local_image_path = Column(String)

    distributor_code = Column(String)
    discontinued = Column(Boolean, default=False)

    updated_at = Column(DateTime)
