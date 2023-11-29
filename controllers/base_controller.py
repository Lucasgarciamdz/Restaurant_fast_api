from abc import ABC, abstractmethod
from typing import Type

from schemas.base_schema import BaseSchema
from services.base_service import BaseService


class BaseController(ABC):
    service: BaseService
    schema: Type[BaseSchema]

    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def get_one(self, id_key: int):
        pass

    @abstractmethod
    def save(self, schema: BaseSchema):
        pass

    @abstractmethod
    def update(self, id_key: int, schema: BaseSchema):
        pass

    @abstractmethod
    def delete(self, id_key: int):
        pass
