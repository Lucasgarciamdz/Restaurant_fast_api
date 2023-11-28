from base_repository_impl import BaseRepositoryImpl
from models.address import AddressModel


class AddressRepository(BaseRepositoryImpl):
    def __init__(self):
        super().__init__(AddressModel)
