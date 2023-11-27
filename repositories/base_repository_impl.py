import logging
from typing import Type

from sqlalchemy.orm import Session
from repositories.base_repository import BaseRepository
from models.base_model import BaseModel


class InstanceNotFoundError(Exception):
    pass


class BaseRepositoryImpl(BaseRepository):
    def __init__(self, model: Type[BaseModel]):
        self.model = model
        self.logger = logging.getLogger(__name__)

    def _get_instance(self, id_key: int):
        with Session() as session:
            instance = session.query(self.model).get(id_key)
            if instance is None:
                self.logger.error(f"No {self.model.__name__} instance found with id {id_key}")
                raise InstanceNotFoundError(f"No {self.model.__name__} instance found with id {id_key}")
            return instance

    def find_all(self):
        with Session() as session:
            return session.query(self.model).all()

    def find_by_id(self, id_key: int):
        return self._get_instance(id_key)

    def save(self, entity: BaseModel):
        with Session() as session:
            session.add(entity)
            session.commit()
            session.refresh(entity)
            return entity

    def update(self, id_key: int, entity: BaseModel):
        with Session() as session:
            instance = self._get_instance(id_key)
            instance.update(vars(entity))
            session.commit()
            return instance

    def delete(self, id_key: int):
        with Session() as session:
            instance = self._get_instance(id_key)
            session.delete(instance)
            session.commit()
