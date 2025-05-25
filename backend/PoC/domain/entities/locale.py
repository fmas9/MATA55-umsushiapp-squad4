from datetime import datetime
from uuid import UUID
from pydantic import BaseModel
class Regiao(BaseModel):
    id: UUID
    nome: str
    code: str
    country: str
    description: str | None = None
    is_active: bool = True
    created_at: datetime
    updated_at: datetime