from sqlalchemy import Column, String, Float
from sqlalchemy.orm import relationship
from models.base_model import BaseModel


class ProductModel(BaseModel):
    __tablename__ = "products"

    name = Column(String, index=True)
    price = Column(Float)
    reviews = relationship("Review", back_populates="product")
