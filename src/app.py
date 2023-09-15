from fastapi import FastAPI, APIRouter

from src.converter import converter_router

app = FastAPI()

router = APIRouter(
    prefix='/api/v1'
)

router.include_router(converter_router.router)


app.include_router(router)
