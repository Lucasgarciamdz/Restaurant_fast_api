from .base_controller_impl import BaseControllerImpl
from models.product import Product


class ProductController(BaseControllerImpl):
    model = Product

    def __init__(self):
        super().__init__()
        self.router.include_router(self.router, prefix="/product")
