from sqlalchemy import Column, String, Float, Integer, ForeignKey
from sqlalchemy.orm import relationship

from models.base_model import BaseModel


class ProductModel(BaseModel):
    __tablename__ = "products"

    name = Column(String, index=True)
    price = Column(Float)
    category_id = Column(Integer, ForeignKey("categories.id_key"))

    category = relationship('CategoryModel', back_populates='products')
    reviews = relationship("ReviewModel", back_populates="product")
    order_details = relationship("OrderDetailModel", back_populates="product")
