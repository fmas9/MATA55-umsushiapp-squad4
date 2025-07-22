from datetime import datetime
from uuid import UUID
from pydantic import BaseModel

from domain.entities.locale import Locale

class Payer(BaseModel):
    id: UUID
    name: str
    email: str
    password: str
    phone_number: str
    code: str
    locale: Locale
    description: str | None = None
    is_active: bool = True
    created_at: datetime
    updated_at: datetime