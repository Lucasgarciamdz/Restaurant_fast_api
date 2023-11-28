from abc import ABC, abstractmethod
from typing import Type, List

from models.base_model import BaseModel
from repositories.base_repository import BaseRepository
from schemas.base_schema import BaseSchema


class BaseService(ABC):
    repository: Type[BaseRepository]
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

    @abstractmethod
    def to_model(self, schema: BaseSchema) -> BaseModel:
        pass

    @abstractmethod
    def to_schema(self, model: BaseModel) -> BaseSchema:
        pass
