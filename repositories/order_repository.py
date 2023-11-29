from models.order import Order
from repositories.base_repository_impl import BaseRepositoryImpl


class OrderRepository(BaseRepositoryImpl):
    def __init__(self):
        super().__init__(Order)
