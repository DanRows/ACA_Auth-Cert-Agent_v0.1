from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class DocumentBase(BaseModel):
    title: str
    type: str
    certificate_id: int

class DocumentCreate(DocumentBase):
    content: bytes

class Document(DocumentBase):
    id: int
    file_path: str
    created_at: datetime
    updated_at: datetime
    analysis_status: Optional[str]

    class Config:
        from_attributes = True