from fastapi import FastAPI
from api.router.celiac_diagnose_router import router as celiac_diagnose_router

app = FastAPI()


app.include_router(
    router= celiac_diagnose_router,
    prefix="/api/v1"
)