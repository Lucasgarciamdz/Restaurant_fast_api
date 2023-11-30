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
        return self.repository.find_all()

    def get_one(self, id_key: int) -> BaseSchema:
        return self.repository.find_by_id(id_key)

    def save(self, schema: BaseSchema) -> BaseSchema:
        return self.repository.save(self.to_model(schema))

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
