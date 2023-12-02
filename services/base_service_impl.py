from typing import Type, List

from models.base_model import BaseModel
from repositories.address_repository import AddressRepository
from repositories.base_repository_impl import BaseRepositoryImpl
from repositories.bill_repository import BillRepository
from repositories.category_repository import CategoryRepository
from repositories.client_repository import ClientRepository
from repositories.order_detail_repository import OrderDetailRepository
from repositories.order_repository import OrderRepository
from repositories.product_repository import ProductRepository
from repositories.review_repository import ReviewRepository
from schemas.base_schema import BaseSchema
from schemas.nested_schemas import NestedSchema
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

    def save(self, schema: NestedSchema) -> NestedSchema:
        saved_schemas = {}
        for repo_name, sub_schema in schema.schemas.items():
            repository = self.get_repository(repo_name)
            saved_schemas[repo_name] = repository.save(self.to_model(sub_schema))
        return NestedSchema(schemas=saved_schemas)

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

    def get_repository(self, repo_name: str):
        repositories = {
            'client': ClientRepository(),
            'address': AddressRepository(),
            'bill': BillRepository(),
            'category': CategoryRepository(),
            'product': ProductRepository(),
            'order': OrderRepository(),
            'order_detail': OrderDetailRepository(),
            'review': ReviewRepository(),
        }
        return repositories.get(repo_name)
