from fastapi import FastAPI
from api.router.celiac_diagnosis_router import router as celiac_diagnosis_router

app = FastAPI(
    title="Celiac Disease Diagnosis API",
    version="0.0.1",
    description="An API for diagnosing celiac disease based on patient information."
)


app.include_router(
    router= celiac_diagnosis_router,
    prefix="/api/v1"
)