import uuid
from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class Event(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    start_timestamp: str = Field(...)
    end_timestamp: str = Field(...)
    event_name: str = Field(...)
    event_location: str = Field(...)
    description: str = Field(...)
    organizer: Optional[str]
    event_contact_main: Optional[str]
    is_mandatory: str = Field(...)
    created_by: str = Field(...)
    created_at_timestamp: str = Field(default_factory=lambda: datetime.now().isoformat())
    last_edited_by: str = Field(...)
    last_edited_at: str = Field(default_factory=lambda: datetime.now().isoformat())


    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "_id": "066de609-b04a-4b30-b46c-32537c7f1f6e",
                "start_timestamp": "2024-02-05T12:00:00",
                "end_timestamp": "2024-02-05T16:00:00",
                "event_name": "Sample Event",
                "event_location": "Sample Location",
                "description": "This is a sample event description.",
                "organizer": "Sample Organizer",
                "event_contact_main": "contact@example.com",
                "is_mandatory": "Y",
                "created_by": "Admin",
                "created_at_timestamp": "2024-01-01T00:00:00Z",
                "last_edited_by": "Admin",
                "last_edited_at": "2024-01-01T00:00:00Z"
            }
        }