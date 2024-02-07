from pydantic import BaseModel
from typing import Optional


class AdminUpdate(BaseModel):
    firebase_uid: Optional[str]
    name: Optional[str]
    email: Optional[str]
    role: Optional[str]
    last_login: Optional[str]

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "id": "123e4567-e89b-12d3-a456-426614174000",
                "firebase_uid": "abc123",
                "name": "Admin User",
                "email": "admin@example.com",
                "role": "admin",
                "last_login": "2024-02-01T12:00:00Z",
            }
        }