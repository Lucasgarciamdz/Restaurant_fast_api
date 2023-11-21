from sqlalchemy import Column, String, Float
from sqlalchemy.orm import relationship
from models.base_model import BaseModel
from sqlalchemy import Column, Integer, ForeignKey


class Review(BaseModel):
    __tablename__ = "reviews"

    rating = Column(Float)
    comment = Column(String)
    product_id = Column(Integer, ForeignKey("products.id"))

    product = relationship("Product", back_populates="reviews")
