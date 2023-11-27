from base_repository_impl import BaseRepositoryImpl
from models.address import Address


class AdressRepository(BaseRepositoryImpl):
    def __init__(self):
        super().__init__(Address)
