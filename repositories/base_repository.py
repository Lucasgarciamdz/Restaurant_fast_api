from abc import ABC, abstractmethod
from typing import Type, List

from models.base_model import BaseModel


class BaseRepository(ABC):
    model: Type[BaseModel]

    @abstractmethod
    def find_all(self) -> List[dict]:
        pass

    @abstractmethod
    def find_by_id(self, id_key: int) -> dict:
        pass

    @abstractmethod
    def save(self, model: BaseModel) -> dict:
        pass

    @abstractmethod
    def update(self, id_key: int, model: BaseModel) -> dict:
        pass

    @abstractmethod
    def delete(self, id_key: int) -> None:
        pass
