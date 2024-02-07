from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class ImportantContactUpdate(BaseModel):
    name: Optional[str]
    phone_number: Optional[str]
    email: Optional[str]
    when_to_contact: Optional[str]
    last_edited_by: str = Field(...)
    last_edited_at: str = Field(default_factory=lambda: datetime.now().isoformat())

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
             "example": {
                "_id": "066de609-b04a-4b30-b46c-32537c7f1f6e",
                "name": "John Doe",
                "phone_number": "123-456-7890",
                "email": "john.doe@example.com",
                "when_to_contact": "Anytime",
                "created_by": "Admin",
                "created_at_timestamp": "2024-01-01T00:00:00Z",
                "last_edited_by": "Admin",
                "last_edited_at": "2024-01-01T00:00:00Z"
            }
        }