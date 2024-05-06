from fastapi import FastAPI
from api.router.celiac_diagnose_router import router as celiac_diagnose_router

app = FastAPI(
    title="Celiac Disease Diagnose API",
    version="0.0.1"
)


app.include_router(
    router= celiac_diagnose_router,
    prefix="/api/v1"
)