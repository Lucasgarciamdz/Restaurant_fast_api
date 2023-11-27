from abc import ABC, abstractmethod
from schemas.base_schema import BaseSchema

from services.base_service import BaseService


class BaseController(ABC):
    service: BaseService

    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def get_one(self, id_key: int):
        pass

    @abstractmethod
    def save(self, entity: BaseSchema):
        pass

    @abstractmethod
    def update(self, id_key: int, entity: BaseSchema):
        pass

    @abstractmethod
    def delete(self, id_key: int):
        pass
