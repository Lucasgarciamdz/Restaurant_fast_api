from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from typing import Type, TypeVar

ModelType = TypeVar("ModelType")

router = APIRouter()

class BaseController:
    model: Type[ModelType]

    @router.get("/")
    def get_all(self, db: Session):
        return db.query(self.model).all()

    @router.get("/{id_key}")
    def get_one(self, db: Session, id_key: int):
        db_item = db.query(self.model).get(id_key)
        if db_item is None:
            raise HTTPException(status_code=404, detail="Item not found")
        return db_item

    @router.post("/")
    def save(self, db: Session, entity: ModelType):
        db.add(entity)
        db.commit()
        db.refresh(entity)
        return entity

    @router.put("/{id_key}")
    def update(self, db: Session, id_key: int, entity: ModelType):
        db_item = db.query(self.model).get(id_key)
        if db_item is None:
            raise HTTPException(status_code=404, detail="Item not found")
        for var, value in vars(entity).items():
            setattr(db_item, var, value) if value else None
        db.commit()
        db.refresh(db_item)
        return db_item

    @router.delete("/{id_key}")
    def delete(self, db: Session, id_key: int):
        db_item = db.query(self.model).get(id_key)
        if db_item is None:
            raise HTTPException(status_code=404, detail="Item not found")
        db.delete(db_item)
        db.commit()