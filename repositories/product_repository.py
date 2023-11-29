from models.product import ProductModel
from repositories.base_repository_impl import BaseRepositoryImpl


class ProductRepository(BaseRepositoryImpl):
    def __init__(self):
        super().__init__(ProductModel)
