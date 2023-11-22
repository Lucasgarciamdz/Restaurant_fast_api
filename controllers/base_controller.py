from abc import ABC, abstractmethod
from sqlalchemy.orm import Session
from typing import Type, TypeVar

ModelType = TypeVar("ModelType")


class BaseController(ABC):
    model: Type[ModelType]

    @abstractmethod
    def get_all(self, db: Session):
        pass

    @abstractmethod
    def get_one(self, db: Session, id_key: int):
        pass

    @abstractmethod
    def save(self, db: Session, entity: ModelType):
        pass

    @abstractmethod
    def update(self, db: Session, id_key: int, entity: ModelType):
        pass

    @abstractmethod
    def delete(self, db: Session, id_key: int):
        pass
