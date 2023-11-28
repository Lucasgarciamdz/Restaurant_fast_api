from sqlalchemy import Column, String, Float, Integer, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel


class ReviewModel(BaseModel):
    __tablename__ = "reviews"

    rating = Column(Float)
    comment = Column(String)
    product_id = Column(Integer, ForeignKey("products.id_key"))

    product = relationship("Product", back_populates="reviews")
