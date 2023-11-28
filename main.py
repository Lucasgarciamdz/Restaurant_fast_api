from config.database import Database
from controllers.base_controller_impl import router
from fastapi import FastAPI
import uvicorn


def create_fastapi_app():
    # Create FastAPI instance
    fastapi_app = FastAPI()

    # Include your routers
    fastapi_app.include_router(router)
    # Add other routers here

    return fastapi_app


def run_app(fastapi_app: FastAPI):
    uvicorn.run(fastapi_app, host="0.0.0.0", port=8000)


if __name__ == "__main__":
    db = Database()
    db.create_tables()
    app = create_fastapi_app()
    run_app(app)
