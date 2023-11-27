from abc import ABC, abstractmethod
from sqlalchemy.orm import Session

from models.base_model import BaseModel
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
    def save(self, entity: BaseModel):
        pass

    @abstractmethod
    def update(self, id_key: int, entity: BaseModel):
        pass

    @abstractmethod
    def delete(self, id_key: int):
        pass
