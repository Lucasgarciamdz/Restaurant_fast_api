from models.category import Category
from repositories.base_repository_impl import BaseRepositoryImpl


class CategoryRepository(BaseRepositoryImpl):
    def __init__(self):
        super().__init__(Category)
