from fastapi import APIRouter, HTTPException
from controllers.base_controller import BaseController
from models.base_model import BaseModel
from services.base_service_impl import BaseServiceImpl

router = APIRouter()


class BaseControllerImpl(BaseController):
    def __init__(self, model: BaseModel, service: BaseServiceImpl):
        self.model = model
        self.service = service

    @router.get("/")
    def get_all(self):
        return self.service.get_all()

    @router.get("/{id_key}")
    def get_one(self, id_key: int):
        item = self.service.get_one(id_key)
        if item is None:
            raise HTTPException(status_code=404, detail="Item not found")
        return item

    @router.post("/")
    def save(self, entity: BaseModel):
        return self.service.save(entity)

    @router.put("/{id_key}")
    def update(self, id_key: int, entity: BaseModel):
        item = self.service.update(id_key, entity)
        if item is None:
            raise HTTPException(status_code=404, detail="Item not found")
        return item

    @router.delete("/{id_key}")
    def delete(self, id_key: int):
        item = self.service.delete(id_key)
        if item is None:
            raise HTTPException(status_code=404, detail="Item not found")

    @property
    def router(self):
        return router
