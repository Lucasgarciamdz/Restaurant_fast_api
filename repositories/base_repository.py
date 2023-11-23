from abc import ABC, abstractmethod
from sqlalchemy.orm import Session
from models.base_model import BaseModel


class BaseRepository(ABC):
    model: BaseModel

    @abstractmethod
    def find_all(self, db: Session):
        pass

    @abstractmethod
    def find_by_id(self, db: Session, id_key: int):
        pass

    @abstractmethod
    def save(self, db: Session, entity: BaseModel):
        pass

    @abstractmethod
    def update(self, db: Session, id_key: int, entity: BaseModel):
        pass

    @abstractmethod
    def delete(self, db: Session, id_key: int):
        pass
