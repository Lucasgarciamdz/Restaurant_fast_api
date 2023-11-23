from sqlalchemy import Column, String, Float, Date, Enum
from sqlalchemy.orm import relationship
from models.base_model import BaseModel
from sqlalchemy import Column, Integer, ForeignKey
from enum import Enum as PyEnum


class PaymentType(PyEnum):
    CASH = "cash"
    CARD = "card"


class Bill(BaseModel):
    __tablename__ = "bills"

    bill_number = Column(String, index=True)
    discount = Column(Float)
    date = Column(Date)
    total = Column(Float)
    payment_type = Column(Enum(PaymentType))
