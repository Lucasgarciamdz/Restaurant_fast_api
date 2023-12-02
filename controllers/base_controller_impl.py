from typing import Type, List
from fastapi import APIRouter, HTTPException
from controllers.base_controller import BaseController
from schemas.base_schema import BaseSchema
from schemas.nested_schemas import NestedSchema
from services.base_service_impl import BaseServiceImpl


class BaseControllerImpl(BaseController):
    def __init__(self, schema: Type[BaseSchema], service: BaseServiceImpl):
        self.schema = schema
        self.service = service
        self.router = APIRouter()

        @self.router.get("/", response_model=List[self.schema])
        def get_all():
            return self.get_all()

        @self.router.get("/{id_key}", response_model=self.schema)
        def get_one(id_key: int):
            item = self.get_one(id_key)
            if item is None:
                raise HTTPException(status_code=404, detail="Item not found")
            return item

        @self.router.post("/", response_model=NestedSchema)
        def save(schema_in: NestedSchema):
            return self.save(schema_in)

        @self.router.put("/{id_key}", response_model=self.schema)
        def update(id_key: int, schema_in: schema):
            item = self.update(id_key, schema_in)
            if item is None:
                raise HTTPException(status_code=404, detail="Item not found")
            return item

        @self.router.delete("/{id_key}")
        def delete(id_key: int):
            self.delete(id_key)

    def get_all(self):
        return self.service.get_all()

    def get_one(self, id_key: int):
        return self.service.get_one(id_key)

    def save(self, schema: NestedSchema):
        return self.service.save(schema)

    def update(self, id_key: int, schema: BaseSchema):
        return self.service.update(id_key, schema)

    def delete(self, id_key: int):
        self.service.delete(id_key)
