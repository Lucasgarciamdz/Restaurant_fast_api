from schemas.base_schema import BaseSchema
from typing import Optional


class AddressBaseSchema(BaseSchema):
    street: str
    number: str
    city: str
    client_id: Optional[int] = None


class AddressCreateSchema(AddressBaseSchema, AddressBaseSchema):
    pass

