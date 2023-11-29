from models.review import ReviewModel
from repositories.base_repository_impl import BaseRepositoryImpl


class ReviewRepository(BaseRepositoryImpl):
    def __init__(self):
        super().__init__(ReviewModel)
