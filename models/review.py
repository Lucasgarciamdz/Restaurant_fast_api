from sqlalchemy import Column, String, Float, Integer, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel


class Review(BaseModel):
    __tablename__ = "reviews"

    rating = Column(Float)
    comment = Column(String)
    product_id = Column(Integer, ForeignKey("products.id"))

    product = relationship("Product", back_populates="reviews")
