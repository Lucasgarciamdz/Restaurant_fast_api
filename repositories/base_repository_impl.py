import logging
from sqlalchemy.orm import Session
from repositories.base_repository import BaseRepository
from models.base_model import BaseModel


class InstanceNotFoundError(Exception):
    pass


class BaseRepositoryImpl(BaseRepository):
    model: BaseModel

    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def find_all(self, db: Session):
        return db.query(self.model).all()

    def find_by_id(self, db: Session, id_key: int):
        instance = db.query(self.model).get(id_key)
        if instance is None:
            self.logger.error(f"No {self.model.__name__} instance found with id {id_key}")
            raise InstanceNotFoundError(f"No {self.model.__name__} instance found with id {id_key}")
        return instance

    def save(self, db: Session, entity: BaseModel):
        db.add(entity)
        db.commit()
        db.refresh(entity)
        return entity

    def update(self, db: Session, id_key: int, entity: BaseModel):
        instance = db.query(self.model).get(id_key)
        if instance is None:
            self.logger.error(f"No {self.model.__name__} instance found with id {id_key}")
            raise InstanceNotFoundError(f"No {self.model.__name__} instance found with id {id_key}")
        instance.update(vars(entity))
        db.commit()
        return instance

    def delete(self, db: Session, id_key: int):
        instance = db.query(self.model).get(id_key)
        if instance is None:
            self.logger.error(f"No {self.model.__name__} instance found with id {id_key}")
            raise InstanceNotFoundError(f"No {self.model.__name__} instance found with id {id_key}")
        db.delete(instance)
        db.commit()
