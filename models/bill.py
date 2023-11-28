from sqlalchemy import Column, String, Float, Date, Enum
from models.base_model import BaseModel
from enum import Enum as PyEnum


class PaymentType(PyEnum):
    CASH = "cash"
    CARD = "card"


class BillModel(BaseModel):
    __tablename__ = "bills"

    bill_number = Column(String, index=True)
    discount = Column(Float)
    date = Column(Date)
    total = Column(Float)
    payment_type = Column(Enum(PaymentType))
