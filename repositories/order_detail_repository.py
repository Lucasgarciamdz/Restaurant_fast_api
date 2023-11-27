from repositories.base_repository_impl import BaseRepositoryImpl
from models.order_detail import OrderDetail


class OrderDetailRepository(BaseRepositoryImpl):
    def __init__(self):
        super().__init__(OrderDetail)
