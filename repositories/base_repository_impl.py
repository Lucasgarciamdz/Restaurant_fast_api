import logging
from contextlib import contextmanager
from typing import Type, List

from config.database import Database
from models.base_model import BaseModel
from repositories.base_repository import BaseRepository


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
        session = self.session
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
        model_dict = {c.name: getattr(instance, c.name) for c in instance.__table__.columns}
        return model_dict

    def find_all(self) -> List[dict]:
        with self.session_scope() as session:
            instances = session.query(self.model).all()
            return [{c.name: getattr(instance, c.name) for c in instance.__table__.columns} for instance in instances]

    def find_by_id(self, id_key: int) -> dict:
        return self._get_instance(id_key)

    def save(self, entity: BaseModel) -> dict:
        with self.session_scope() as session:
            session.add(entity)
            session.commit()
            session.refresh(entity)
            model_dict = {c.name: getattr(entity, c.name) for c in entity.__table__.columns}
        return model_dict

    def update(self, id_key: int, entity: BaseModel) -> dict:
        with self.session_scope() as session:
            instance = self._get_instance(id_key)
            instance.__dict__.update(entity.__dict__)
            session.merge(instance)
            session.commit()
            model_dict = {c.name: getattr(instance, c.name) for c in instance.__table__.columns}
        return model_dict

    def delete(self, id_key: int) -> None:
        with self.session_scope() as session:
            instance = self._get_instance(id_key)
            session.delete(instance)
            session.commit()
