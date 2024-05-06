from pydantic import BaseModel
from typing import Optional
from enum import Enum

class GenderEnum(int,Enum):
    MALE = 0
    FEMALE = 1

class DiabetesTypeEnum(int, Enum):
    TYPE1 = 0
    TYPE2 = 1
    UNCONFIRMED = 3


class CeliacPatient(BaseModel):
    age : int
    gender : str
    diabetes : str
    diabetes_type : str
    diarrhoea : str
    abdominal : str
    short_stature : str
    sticky_stool : str
    weight_loss : str
    ig_a : float
    ig_g : float
    ig_m : float
    marsh : str
    cd_type : str
    disease_diagnose : Optional[str]

