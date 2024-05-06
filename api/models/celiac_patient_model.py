from pydantic import BaseModel
from typing import Optional
from enum import Enum

class GenderEnum(int,Enum):
    MALE = 1
    FEMALE = 0

class DiabetesTypeEnum(int, Enum):
    TYPE_1 = 0
    TYPE_2 = 1
    UNCONFIRMED = 2

class DiarrhoeaEnum(int, Enum):
    FATTY = 0
    INFLAMMATORY = 1
    WATERY = 2

class ShortStatureEnum(int,Enum):
    PSS = 1
    VARIANT = 2
    DSS = 0

class MarshEnum(int,Enum):
    TYPE_0 = 0
    TYPE_1 = 1
    TYPE_2 = 2
    TYPE_3A = 3
    TYPE_3B = 4
    NONE = 5
    TYPE_3C = 6


class CeliacDiseaseTypeEnum(int,Enum):
    POTENTIAL = 3
    ATYPICAL = 0
    LATENT = 1
    SILENT = 4
    TYPICAL = 5
    NONE = 2

class DiagnoseDescriptionEnum(str,Enum):
    CELIAC = "The patient could have celiac disease. Needs more evaluations."
    NON_CELIAC = "The patient may not have celiac disease. Carry out more evaluations to detect the cause of your discomfort."

class ModelEnum(str,Enum):
    LOGISTIC_REGRESSION = 'Logistic Regression'

class CeliacPatient(BaseModel):
    # age : Optional[int]
    gender : Optional[str]
    diabetes : Optional[str]
    diabetes_type : Optional[str]
    diarrhoea : Optional[str]
    # abdominal : Optional[str]
    # short_stature : Optional[str]
    # sticky_stool : Optional[str]
    # weight_loss : Optional[str]
    # ig_a : Optional[float]
    # ig_g : Optional[float]
    # ig_m : Optional[float]
    marsh : Optional[str]
    # cd_type : Optional[str]
    # disease_diagnose : Optional[str]
    
    def get_gender(self) -> GenderEnum:
        return GenderEnum.MALE if self.gender.strip().lower() == "male" else GenderEnum.FEMALE
    def get_diabetes(self) -> bool:
        return self.diabetes.lower() == 'yes'
    def get_diabetes_type(self) -> DiabetesTypeEnum:
        if self.diabetes_type.strip() == 'Type 1':
            return DiabetesTypeEnum.TYPE_1
        elif self.diabetes_type.strip() == 'Type 2':
            return DiabetesTypeEnum.TYPE_2
        else:
            return DiabetesTypeEnum.UNCONFIRMED
    def get_diarrhoea(self) ->DiarrhoeaEnum:
        diarrhoea = self.diarrhoea.strip().lower()
        if diarrhoea == 'inflammatory':
            return DiarrhoeaEnum.INFLAMMATORY
        elif diarrhoea == 'fatty':
            return DiarrhoeaEnum.FATTY
        else:
            return DiarrhoeaEnum.WATERY
    
    def get_marsh(self):
        marsh = self.marsh.strip().lower()
        if marsh == 'marsh type 0':
            return MarshEnum.TYPE_0
        elif marsh == 'marsh type 3a':
            return MarshEnum.TYPE_3A
        elif marsh == 'marsh type 1':
            return MarshEnum.TYPE_1
        elif marsh == 'marsh type 2':
            return MarshEnum.TYPE_2
        elif marsh == 'marsh type 3b':
            return MarshEnum.TYPE_3B
        elif marsh == 'none':
            return MarshEnum.NONE
        elif marsh == 'marsh type 3c':
            return MarshEnum.TYPE_3C
        else:
            raise ValueError("Invalid marsh type string")
        
class ModelResponse(BaseModel):
    ai_model : ModelEnum = ModelEnum.LOGISTIC_REGRESSION
    disease_diagnose : int
    diagnose_description : DiagnoseDescriptionEnum
    accuracy : float


class CeliacPatientEncoded(BaseModel):
    gender : GenderEnum
    diabetes : bool
    diabetes_type : DiabetesTypeEnum
    diarrhoea : DiarrhoeaEnum
    marsh : MarshEnum
    def get_encoded_attributes_list(self):
            return [
                self.gender.value,
                self.diabetes,
                self.diabetes_type.value,
                self.diarrhoea.value,
                self.marsh.value
            ]




