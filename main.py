import uvicorn
from fastapi import FastAPI

from config.database import Database
from controllers.client_controller import ClientController


def create_fastapi_app():
    fastapi_app = FastAPI()

    client_controller = ClientController()
    fastapi_app.include_router(client_controller.router, prefix="/clients")

    return fastapi_app


def run_app(fastapi_app: FastAPI):
    uvicorn.run(fastapi_app, host="0.0.0.0", port=8000)


if __name__ == "__main__":
    db = Database()
    db.create_tables()
    app = create_fastapi_app()
    run_app(app)
