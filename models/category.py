from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel


class Category(BaseModel):
    __tablename__ = "categories"

    name = Column(String, index=True)
    description = Column(String)

    products = relationship("Product", back_populates="category")
