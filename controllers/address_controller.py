from base_controller_impl import BaseControllerImpl
from services.address_service import AddressService


class AddressController(BaseControllerImpl):
    model = AddressService

    def __init__(self):
        super().__init__()
        self.router.include_router(self.router, prefix="/address")

    @property
    def router(self):
        return self.router
