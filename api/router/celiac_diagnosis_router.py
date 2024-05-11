from fastapi import APIRouter, Depends
from api.models.celiac_patient_model import CeliacPatient
from api.service.celiac_diagnosis_service import CeliacDiagnosisService
router = APIRouter(prefix="/celiac-diagnose",tags=["Celiac Diagnose"])
service = CeliacDiagnosisService()

@router.post("/logistic-regression")
def predict_celiac_diagnose(data : CeliacPatient = Depends()):
    response = service.predict_celiac_diagnosis_logistic_regression(data)
    return response