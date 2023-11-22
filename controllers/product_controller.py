from .base_controller import BaseController, router
from models.product import Product  # Assuming Product is a SQLAlchemy model


class ProductController(BaseController):
    model = Product

product_router = router