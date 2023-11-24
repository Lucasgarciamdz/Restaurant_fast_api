from sqlalchemy import Column, Float, DateTime, Enum, Integer, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel
from enum import Enum as PyEnum


class DeliveryMethod(PyEnum):
    DRIVE_THRU = 1
    ON_HAND = 2
    HOME_DELIVERY = 3


class Status(PyEnum):
    PENDING = 1
    IN_PROGRESS = 2
    DELIVERED = 3
    CANCELED = 4


class Order(BaseModel):
    __tablename__ = "orders"

    date = Column(DateTime)
    total = Column(Float)
    delivery_method = Column(Enum(DeliveryMethod))
    status = Column(Enum(Status))

    order_details = relationship("OrderDetail", back_populates="order")

    client_id = Column(Integer, ForeignKey("clients.id"))
    bill_id = Column(Integer, ForeignKey("bills.id"))
