from repositories.base_repository_impl import BaseRepositoryImpl
from models.bill import Bill


class BillRepository(BaseRepositoryImpl):
    def __init__(self):
        super().__init__(Bill)
