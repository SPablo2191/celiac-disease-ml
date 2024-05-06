from joblib import load
from api.models.celiac_patient_model import CeliacPatient,CeliacPatientEncoded, ModelResponse,ModelEnum,DiagnoseDescriptionEnum

class CeliacDiagnoseService:
    def __init__(self) -> None:
        try:
            joblib_in = open("api\data\models\celiac_disease_lr_model.joblib","rb")
            self.logistic_regression_model = load(joblib_in)
        except FileNotFoundError:
            print("Model dosn't found.")
        finally:
            joblib_in.close()
    def predict_celiac_diagnose_logistic_regression(self,patient_data : CeliacPatient):
        # encode the data
        patient_attribute_list = CeliacPatientEncoded(
            marsh= patient_data.get_marsh(),
            gender= patient_data.get_gender(),
            diabetes= patient_data.get_diabetes(),
            diabetes_type= patient_data.get_diabetes_type(),
            diarrhoea= patient_data.get_diarrhoea()
        ).get_encoded_attributes_list()
        prediction = self.logistic_regression_model.predict([patient_attribute_list])
        return ModelResponse(
            disease_diagnose=prediction[0],
            diagnose_description =  DiagnoseDescriptionEnum.CELIAC if prediction[0] == 0 else DiagnoseDescriptionEnum.NON_CELIAC,
            ai_model= ModelEnum.LOGISTIC_REGRESSION,
            accuracy= 0
        )