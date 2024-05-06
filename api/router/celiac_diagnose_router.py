from fastapi import APIRouter
from api.models.celiac_patient_model import CeliacPatient
from api.service.celiac_diagnose_service import CeliacDiagnoseService
router = APIRouter(prefix="/celiac-diagnose",tags=["Celiac Diagnose"])
service = CeliacDiagnoseService()

@router.post("/logistic-regression")
def predict_celiac_diagnose(data : CeliacPatient):
    response = service.predict_celiac_diagnose_logistic_regression(data)
    return response