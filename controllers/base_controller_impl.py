from fastapi import APIRouter, HTTPException, Depends
from typing import Type, List
from schemas.base_schema import BaseSchema
from controllers.base_controller import BaseController
from services.base_service_impl import BaseServiceImpl

router = APIRouter()


class BaseControllerImpl(BaseController):
    def __init__(self, schema: Type[BaseSchema], service: BaseServiceImpl):
        self.schema = schema
        self.service = service

    @router.get("/", response_model=List[BaseSchema])
    def get_all(self) -> List[BaseSchema]:
        return self.service.get_all()

    @router.get("/{id_key}", response_model=BaseSchema)
    def get_one(self, id_key: int) -> BaseSchema:
        item = self.service.get_one(id_key)
        if item is None:
            raise HTTPException(status_code=404, detail="Item not found")
        return item

    @router.post("/", response_model=BaseSchema)
    def save(self, schema: BaseSchema = Depends(BaseSchema)) -> BaseSchema:
        return self.service.save(schema)

    @router.put("/{id_key}", response_model=BaseSchema)
    def update(self, id_key: int, schema: BaseSchema = Depends(BaseSchema)) -> BaseSchema:
        item = self.service.update(id_key, schema)
        if item is None:
            raise HTTPException(status_code=404, detail="Item not found")
        return item

    @router.delete("/{id_key}")
    def delete(self, id_key: int) -> None:
        self.service.delete(id_key)

    @property
    def router(self):
        return router
