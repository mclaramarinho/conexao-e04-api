from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class FAQUpdate(BaseModel):
    question: Optional[str]
    answer: Optional[str]
    last_edited_by: str = Field(...)
    last_edited_at: str = Field(default_factory=lambda: datetime.now().isoformat())


    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "id": "123e4567-e89b-12d3-a456-426614174000",
                "question": "What is Pydantic?",
                "answer": "Pydantic is a data validation and settings management library for Python.",
                "created_by": "Admin",
                "created_at_timestamp": "2024-01-01T00:00:00Z",
                "last_edited_by": "Admin",
                "last_edited_at": "2024-01-01T00:00:00Z"
            }
        }
