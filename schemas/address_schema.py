from schemas.base_schema import BaseSchema
from typing import Optional


class AddressSchema(BaseSchema):
    street: str
    number: str
    city: str
    client_id: Optional[int] = None
