from abc import ABC, abstractmethod
from repositories.base_repository import BaseRepository


class BaseService(ABC):
    repository: BaseRepository

    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def get_one(self, id_key: int):
        pass

    @abstractmethod
    def save(self, entity):
        pass

    @abstractmethod
    def update(self, id_key: int, entity):
        pass

    @abstractmethod
    def delete(self, id_key: int):
        pass
