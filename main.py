import uvicorn
from fastapi import FastAPI

from config.database import Database
from controllers.address_controller import AddressController
from controllers.bill_controller import BillController
from controllers.category_controller import CategoryController
from controllers.client_controller import ClientController
from controllers.order_controller import OrderController
from controllers.order_detail_controller import OrderDetailController
from controllers.product_controller import ProductController
from controllers.review_controller import ReviewController


def create_fastapi_app():
    fastapi_app = FastAPI()

    client_controller = ClientController()
    fastapi_app.include_router(client_controller.router, prefix="/clients")

    order_controller = OrderController()
    fastapi_app.include_router(order_controller.router, prefix="/orders")

    product_controller = ProductController()
    fastapi_app.include_router(product_controller.router, prefix="/products")

    address_controller = AddressController()
    fastapi_app.include_router(address_controller.router, prefix="/addresses")

    bill_controller = BillController()
    fastapi_app.include_router(bill_controller.router, prefix="/bills")

    order_detail_controller = OrderDetailController()
    fastapi_app.include_router(order_detail_controller.router, prefix="/order_details")

    review_controller = ReviewController()
    fastapi_app.include_router(review_controller.router, prefix="/reviews")

    category_controller = CategoryController()
    fastapi_app.include_router(category_controller.router, prefix="/categories")

    return fastapi_app


def run_app(fastapi_app: FastAPI):
    uvicorn.run(fastapi_app, host="0.0.0.0", port=8000)


if __name__ == "__main__":
    db = Database()
    db.create_tables()
    app = create_fastapi_app()
    run_app(app)
