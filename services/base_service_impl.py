from typing import Type, List

from models.base_model import BaseModel
from schemas.base_schema import BaseSchema
from services.base_service import BaseService
from repositories.base_repository_impl import BaseRepositoryImpl


class BaseServiceImpl(BaseService):

    def __init__(self, repository: BaseRepositoryImpl, model: Type[BaseModel], schema: Type[BaseSchema]):
        self.repository = repository
        self.model = model
        self.schema = schema

    def get_all(self) -> List[BaseSchema]:
        models = self.repository.find_all()
        return [self.to_schema(model) for model in models]

    def get_one(self, id_key: int) -> BaseSchema:
        model = self.repository.find_by_id(id_key)
        return self.to_schema(model)

    def save(self, schema: BaseSchema) -> BaseSchema:
        model = self.to_model(schema)
        saved_model = self.repository.save(model)
        return self.to_schema(saved_model)

    def update(self, id_key: int, schema: BaseSchema) -> BaseSchema:
        model = self.to_model(schema)
        updated_model = self.repository.update(id_key, model)
        return self.to_schema(updated_model)

    def delete(self, id_key: int) -> None:
        self.repository.delete(id_key)

    def to_model(self, schema: BaseSchema) -> BaseModel:
        model_class = type(self.model) if not callable(self.model) else self.model
        model_instance = model_class(**schema.model_dump())
        return model_instance

    def to_schema(self, model: BaseModel) -> BaseSchema:
        return self.schema(**model.__dict__)
