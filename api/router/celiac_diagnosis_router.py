from fastapi import APIRouter, Depends
from api.models.celiac_patient_model import CeliacPatient
from api.service.celiac_diagnosis_service import CeliacDiagnosisService
router = APIRouter(prefix="/diagnosis",tags=["Celiac Diagnosis"])
service = CeliacDiagnosisService()

@router.post("/logistic-regression")
def predict_celiac_diagnose(data : CeliacPatient = Depends()):
    """
     This endpoint accepts patient information (gender,diabetes,diabetes type,diarrhoea,marsh) and performs a diagnosis for celiac disease using logistic regression.
    It returns the probability of the patient having celiac disease.
    """
    response = service.predict_celiac_diagnosis_logistic_regression(data)
    return response