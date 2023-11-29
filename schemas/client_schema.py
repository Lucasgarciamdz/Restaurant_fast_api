from typing import Optional, List

from schemas.address_schema import AddressSchema
from schemas.base_schema import BaseSchema
from schemas.order_schema import OrderSchema


class ClientSchema(BaseSchema):
    name: Optional[str] = None
    lastname: Optional[str] = None
    email: Optional[str] = None
    telephone: Optional[str] = None
    addresses: List[AddressSchema] = []
    orders: List[OrderSchema] = []
