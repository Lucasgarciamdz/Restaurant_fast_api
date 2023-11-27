from repositories.base_repository_impl import BaseRepositoryImpl
from models.client import Client


class ClientRepository(BaseRepositoryImpl):
    def __init__(self):
        super().__init__(Client)
