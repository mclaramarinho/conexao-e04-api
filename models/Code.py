import random
import string
from uuid import uuid4, UUID
from pydantic import BaseModel, Field


class Code(BaseModel):
    id: str = Field(default_factory=uuid4, alias="_id")
    code: str = Field(default_factory=lambda:generate_code())
    expired: bool = Field(default_factory=lambda:False)
    role: str = Field(...)
    uid: str = Field(...)
    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "_id": "123e4567-e89b-12d3-a456-426614174000",
                "code": "A1SG34",
                "expired": "true",
                "uid": "firebase_uid"
            }
        }


class OnlyCode(BaseModel):
    code: str = Field(...)

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "code": "A1SG34",
            }
        }


class CodeUpdate(BaseModel):
    id: str = Field(...)



def generate_code() -> str:
    code = ''
    for i in range(6):
        number_or_letter = random.randint(0, 1)
        if number_or_letter == 0:
            next = random.choice(string.ascii_uppercase)
            code += str(next)
        else:
            next = random.randint(0, 9)
            code += str(next)

    return code