from abc import ABC, abstractmethod
from typing import Type, List

from sqlalchemy.orm import Session
from models.base_model import BaseModel


class BaseRepository(ABC):
    model: Type[BaseModel]

    @abstractmethod
    def find_all(self) -> List[BaseModel]:
        pass

    @abstractmethod
    def find_by_id(self, id_key: int) -> BaseModel:
        pass

    @abstractmethod
    def save(self, model: BaseModel) -> BaseModel:
        pass

    @abstractmethod
    def update(self, id_key: int, model: BaseModel) -> BaseModel:
        pass

    @abstractmethod
    def delete(self, id_key: int) -> None:
        pass
