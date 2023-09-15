from fastapi import FastAPI, APIRouter


app = FastAPI()

router = APIRouter(
    prefix='/api/v1'
)


app.include_router(router)
