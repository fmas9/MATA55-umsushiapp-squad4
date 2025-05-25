from datetime import datetime
from uuid import UUID
from pydantic import BaseModel
class Locale(BaseModel):
    id: UUID
    name: str
    code: str
    country: str
    description: str | None = None
    is_active: bool = True
    created_at: datetime
    updated_at: datetime