from abc import ABC, abstractmethod
from typing import Type, List

from models.base_model import BaseModel
from schemas.base_schema import BaseSchema


class BaseRepository(ABC):
    model: Type[BaseModel]

    @abstractmethod
    def find_all(self) -> List[BaseSchema]:
        pass

    @abstractmethod
    def find_by_id(self, id_key: int) -> BaseSchema:
        pass

    @abstractmethod
    def save(self, model: BaseModel) -> BaseSchema:
        pass

    @abstractmethod
    def update(self, id_key: int, model: BaseModel) -> BaseSchema:
        pass

    @abstractmethod
    def delete(self, id_key: int) -> None:
        pass
