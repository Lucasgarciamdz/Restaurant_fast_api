from repositories.base_repository_impl import BaseRepositoryImpl
from models.category import Category


class CategoryRepository(BaseRepositoryImpl):
    def __init__(self):
        super().__init__(Category)
