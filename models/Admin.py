import datetime
from uuid import uuid4
from pydantic import BaseModel, Field


class Admin(BaseModel):
    id: str = Field(default_factory=uuid4, alias="_id")

    firebase_uid: str = Field(...)

    name: str = Field(...)
    email: str = Field(...)
    role: str = Field(...)


    creation_date_timestamp: str = Field(default_factory=lambda: datetime.datetime.now().isoformat())
    last_login: str = Field(default_factory=lambda: datetime.datetime.now().isoformat())

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
                "creation_date_timestamp": "2024-01-01T00:00:00Z"
            }
        }

