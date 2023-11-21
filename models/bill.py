from sqlalchemy import Column, String, Float
from sqlalchemy.orm import relationship
from models.base_model import BaseModel


class Bill(BaseModel):
    __tablename__ = "bills"

    total = Column(Float)
    products = relationship("Product", back_populates="factura")