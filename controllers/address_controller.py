from controllers.base_controller_impl import BaseControllerImpl
from schemas.address_schema import AddressSchema
from services.address_service import AddressService


class AddressController(BaseControllerImpl):
    def __init__(self):
        super().__init__(AddressSchema, AddressService())
