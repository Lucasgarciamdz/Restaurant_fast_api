from repositories.base_repository_impl import BaseRepositoryImpl
from models.product import Product


class ProductRepository(BaseRepositoryImpl):
    def __init__(self):
        super().__init__(Product)
