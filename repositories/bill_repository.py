from models.bill import Bill
from repositories.base_repository_impl import BaseRepositoryImpl


class BillRepository(BaseRepositoryImpl):
    def __init__(self):
        super().__init__(Bill)
