"""
BaseRepository implementation
"""
import logging
from contextlib import contextmanager
from typing import Type, List
from sqlalchemy.orm import Session

from config.database import Database
from models.base_model import BaseModel
from repositories.base_repository import BaseRepository
from schemas.base_schema import BaseSchema


class InstanceNotFoundError(Exception):
    """
    InstanceNotFoundError is raised when a record is not found
    """


class BaseRepositoryImpl(BaseRepository):
    """
    Class BaseRepositoryImpl implements BaseRepository
    """

    def __init__(self, model: Type[BaseModel], schema: Type[BaseSchema]):
        self._model = model
        self._schema = schema
        self.logger = logging.getLogger(__name__)
        self._session = Database().get_session()

    @property
    def session(self) -> Session:
        return self._session

    @property
    def model(self) -> Type[BaseModel]:
        return self._model

    @property
    def schema(self) -> Type[BaseSchema]:
        return self._schema

    @contextmanager
    def session_scope(self):
        """Provide a transactional scope around a series of operations."""
        session = self.session
        try:
            yield session
            session.commit()
        except Exception as e:
            self.logger.error("Session rollback because of error %s", e)
            session.rollback()
            raise
        finally:
            session.close()

    def find(self, id_key: int) -> BaseSchema:
        with self.session_scope() as session:
            model = session.query(self.model).get(id_key)
            if model is None:
                raise InstanceNotFoundError(f"No instance found with id {id_key}")
            return self.schema.model_validate(model)

    def find_all(self) -> List[BaseSchema]:
        with self.session_scope() as session:
            models = session.query(self.model).all()
            schemas = []
            for model in models:
                schemas.append(self.schema.model_validate(model))
            return schemas

    def save(self, model: BaseModel) -> BaseSchema:
        with self.session_scope() as session:
            session.add(model)
            return self.schema.model_validate(model)

    def update(self, id_key: int, model: BaseModel) -> dict:
        with self.session_scope() as session:
            instance = session.query(self.model).get(id_key)
            if instance is None:
                raise InstanceNotFoundError(f"No instance found with id {id_key}")
            instance.update(model.__dict__)
            session.merge(instance)
            session.commit()
        return instance

    def remove(self, id_key: int) -> None:
        with self.session_scope() as session:
            model = session.query(self.model).get(id_key)
            if model is None:
                raise InstanceNotFoundError(f"No instance found with id {id_key}")
            session.delete(model)

    def save_all(self, models: List[BaseModel]) -> List[BaseSchema]:
        with self.session_scope() as session:
            session.add_all(models)
            return [self.schema.model_validate(model) for model in models]
