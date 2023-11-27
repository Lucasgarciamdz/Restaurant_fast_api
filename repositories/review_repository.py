from repositories.base_repository_impl import BaseRepositoryImpl
from models.review import Review


class ReviewRepository(BaseRepositoryImpl):
    def __init__(self):
        super().__init__(Review)
