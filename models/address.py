from sqlalchemy import Column, String, Integer, ForeignKey
from models.base_model import BaseModel


class AddressModel(BaseModel):
    __tablename__ = "addresses"

    street = Column(String, index=True)
    number = Column(String)

    city = Column(String)

    client_id = Column(Integer, ForeignKey("clients.id"))
