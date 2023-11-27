from repositories.base_repository_impl import BaseRepositoryImpl
from models.order import Order


class OrderRepository(BaseRepositoryImpl):
    def __init__(self):
        super().__init__(Order)
