import logging
from contextlib import contextmanager
from typing import Type, List

from config.database import Database
from repositories.base_repository import BaseRepository
from models.base_model import BaseModel


class InstanceNotFoundError(Exception):
    pass


class BaseRepositoryImpl(BaseRepository):
    def __init__(self, model: Type[BaseModel]):
        db = Database()
        self.session = db.get_session()
        self.model = model
        self.logger = logging.getLogger(__name__)

    @contextmanager
    def session_scope(self):
        """Provide a transactional scope around a series of operations."""
        session = self.session()
        try:
            yield session
            session.commit()
        except Exception:
            session.rollback()
            raise
        finally:
            session.close()

    def _get_instance(self, id_key: int):
        with self.session_scope() as session:
            instance = session.query(self.model).get(id_key)
            if instance is None:
                self.logger.error(f"No {self.model.__name__} instance found with id {id_key}")
                raise InstanceNotFoundError(f"No {self.model.__name__} instance found with id {id_key}")
            return instance

    def find_all(self) -> List[BaseModel]:
        with self.session_scope() as session:
            return session.query(self.model).all()

    def find_by_id(self, id_key: int) -> BaseModel:
        return self._get_instance(id_key)

    def save(self, entity: BaseModel) -> BaseModel:
        with self.session_scope() as session:
            session.add(entity)
            session.commit()
            session.refresh(entity)
        return entity

    def update(self, id_key: int, entity: BaseModel) -> BaseModel:
        with self.session_scope() as session:
            instance = self._get_instance(id_key)
            instance.__dict__.update(entity.__dict__)
            session.merge(instance)
            session.commit()
        return instance

    def delete(self, id_key: int) -> None:
        with self.session_scope() as session:
            instance = self._get_instance(id_key)
            session.delete(instance)
            session.commit()
