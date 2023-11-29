from typing import Type, List

from models.base_model import BaseModel
from repositories.base_repository_impl import BaseRepositoryImpl
from schemas.base_schema import BaseSchema
from services.base_service import BaseService


class BaseServiceImpl(BaseService):

    def __init__(self, repository: BaseRepositoryImpl, model: Type[BaseModel], schema: Type[BaseSchema]):
        self.repository = repository
        self.model = model
        self.schema = schema

    def get_all(self) -> List[BaseSchema]:
        model_dicts = self.repository.find_all()
        return [self.schema(**model_dict) for model_dict in model_dicts]

    def get_one(self, id_key: int) -> BaseSchema:
        model_dict = self.repository.find_by_id(id_key)
        return self.schema(**model_dict)

    def save(self, schema: BaseSchema) -> BaseSchema:
        model = self.to_model(schema)
        model_dict = self.repository.save(model)
        return self.schema(**model_dict)

    def update(self, id_key: int, schema: BaseSchema) -> BaseSchema:
        model = self.to_model(schema)
        model_dict = self.repository.update(id_key, model)
        return self.schema(**model_dict)

    def delete(self, id_key: int) -> None:
        self.repository.delete(id_key)

    def to_model(self, schema: BaseSchema) -> BaseModel:
        model_class = type(self.model) if not callable(self.model) else self.model
        model_instance = model_class(**schema.model_dump())
        return model_instance
