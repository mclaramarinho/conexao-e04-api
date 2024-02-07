import uuid
from typing import Optional, List
from pydantic import BaseModel, Field
from datetime import datetime

class Class(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")

    name: str = Field(...)
    days: List[str] = Field(...)
    start_time: List[str] = Field(...)
    end_time: List[str] = Field(...)
    classroom: str = Field(...)
    teacher: str = Field(...)
    exam_1_timestamp: Optional[str]
    exam_2_timestamp: Optional[str]
    re_take_exam_timestamp: Optional[str]
    final_exam_timestamp: Optional[str]
    observations: Optional[str]
    created_by: str = Field(...)
    created_at_timestamp: str = Field(default_factory=lambda: datetime.now().isoformat())
    last_edited_by: str = Field(...)
    last_edited_at: str = Field(default_factory=lambda: datetime.now().isoformat())


    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "id": "123e4567-e89b-12d3-a456-426614174000",
                "name": "Mathematics",
                "days": ["Monday", "Wednesday", "Friday"],
                "start_time": ["08:00 AM", "09:30 AM", "11:00 AM"],
                "end_time": ["09:00 AM", "10:30 AM", "12:00 PM"],
                "classroom": "Room 101",
                "teacher": "John Doe",
                "exam_1_timestamp": "2024-02-10T08:00:00Z",
                "exam_2_timestamp": "2024-03-15T08:00:00Z",
                "re_take_exam_timestamp": "2024-04-20T08:00:00Z",
                "final_exam_timestamp": "2024-05-25T08:00:00Z",
                "observations": "Please bring calculators every class.",
                "created_by": "Admin",
                "created_at_timestamp": "2024-01-01T00:00:00Z",
                "last_edited_by": "Admin",
                "last_edited_at": "2024-01-01T00:00:00Z"
            }
        }