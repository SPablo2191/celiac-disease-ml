from fastapi import APIRouter

router = APIRouter(prefix="/celiac-diagnose",tags=["Celiac Diagnose"])

@router.get("/")
def get_celiac_diagnose():
    return {"message":"you are celiac"}