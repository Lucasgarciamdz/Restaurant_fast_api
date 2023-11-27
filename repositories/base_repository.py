from abc import ABC, abstractmethod
from typing import Type

from sqlalchemy.orm import Session
from models.base_model import BaseModel


class BaseRepository(ABC):
    model: Type[BaseModel]

    @abstractmethod
    def find_all(self):
        pass

    @abstractmethod
    def find_by_id(self, id_key: int):
        pass

    @abstractmethod
    def save(self, entity: BaseModel):
        pass

    @abstractmethod
    def update(self, id_key: int, entity: BaseModel):
        pass

    @abstractmethod
    def delete(self, id_key: int):
        pass
