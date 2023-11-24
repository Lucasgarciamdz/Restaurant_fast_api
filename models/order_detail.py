from sqlalchemy import Column, Float, INT, ForeignKey
from models.base_model import BaseModel


class OrderDetail(BaseModel):
    __tablename__ = "order_details"

    quantity = Column(INT)
    price = Column(Float)

    order_id = Column(INT, ForeignKey("orders.id"))
    product_id = Column(INT, ForeignKey("products.id"))
