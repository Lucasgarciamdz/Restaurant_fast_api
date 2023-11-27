from services.base_service import BaseService
from repositories.base_repository_impl import BaseRepositoryImpl


class BaseServiceImpl(BaseService):

    def __init__(self, repository: BaseRepositoryImpl):
        self.repository = repository

    def get_all(self):
        return self.repository.find_all()

    def get_one(self, id_key: int):
        return self.repository.find_by_id(id_key)

    def save(self, entity):
        return self.repository.save(entity)

    def update(self, id_key: int, entity):
        return self.repository.update(id_key, entity)

    def delete(self, id_key: int):
        return self.repository.delete(id_key)
