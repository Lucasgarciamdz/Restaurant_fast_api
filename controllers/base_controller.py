from abc import ABC, abstractmethod
from typing import Type, List

from schemas.base_schema import BaseSchema
from services.base_service import BaseService


class BaseController(ABC):
    service: BaseService
    schema: Type[BaseSchema]

    @abstractmethod
    def get_all(self) -> List[BaseSchema]:
        pass

    @abstractmethod
    def get_one(self, id_key: int) -> BaseSchema:
        pass

    @abstractmethod
    def save(self, schema: BaseSchema) -> BaseSchema:
        pass

    @abstractmethod
    def update(self, id_key: int, schema: BaseSchema) -> BaseSchema:
        pass

    @abstractmethod
    def delete(self, id_key: int) -> None:
        pass
