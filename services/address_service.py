from services.base_service_impl import BaseServiceImpl
from repositories.address_repository import AddressRepository


class AddressService(BaseServiceImpl):

    def __init__(self):
        super().__init__(AddressRepository())
