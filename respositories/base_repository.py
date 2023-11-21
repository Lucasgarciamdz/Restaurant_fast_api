from sqlalchemy.orm import Session
from models.base_model import BaseModel
from typing import TypeVar, Type, Optional

T = TypeVar("T", bound=BaseModel)


class BaseRepository:
    def __init__(self, model: Type[T], session: Session):
        self.model = model
        self.session = session

    def create(self, obj_in: T) -> T:
        db_obj = self.model(**obj_in.dict())
        self.session.add(db_obj)
        self.session.commit()
        self.session.refresh(db_obj)
        return db_obj

    def find_by_id(self, id_key: int) -> Optional[T]:
        return self.session.query(self.model).filter(self.model.__table__.c.id_key == id_key).first()

    def update(self, id_key: int, obj_in: T) -> T:
        db_obj = self.find_by_id(id_key)
        if db_obj:
            update_data = obj_in.dict(exclude_unset=True)
            for key, value in update_data.items():
                setattr(db_obj, key, value)
            self.session.commit()
            self.session.refresh(db_obj)
        return db_obj

    def delete(self, id_key: int) -> T:
        db_obj = self.find_by_id(id_key)
        self.session.delete(db_obj)
        self.session.commit()
        return db_obj
