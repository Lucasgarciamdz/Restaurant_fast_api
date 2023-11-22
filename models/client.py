from sqlalchemy import Column, String, Float
from sqlalchemy.orm import relationship
from models.base_model import BaseModel


class Client(BaseModel):
    __tablename__ = "clients"

    name = Column(String, index=True)
    lastname = Column(String, index=True)
    email = Column(String)
    telephone = Column(String)

    addresses = relationship("Address", back_populates="client")
    orders = relationship("Order", back_populates="client")
