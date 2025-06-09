from backend.PoC.domain.entities.locale import Locale
from typing import List
from uuid import UUID
from locale import locale  # sua entidade
from datetime import datetime, timezone

locales = []
class LocaleMockRepository:
    def __init__(self):
        self._locale: List[locale] = []
        return None
    
    async def get_locale_by_id(self, locale_id: UUID) -> Locale | None:
        for locale in self._locales:
            if locale.id == locale_id:
                return locale
            return None
    async def save_locale(self, locale: locale) -> Locale | None:
        for idx, existing_locale in enumerate(self._locale):
            if existing_locale.id == locale.id:
                self._locale[idx] = locale  # Atualiza
                return
        self._locale.append(locale)  # Adiciona nova região
    async def listar_locale(self) -> List[locale]:
        return self._locale
  
    async def createlocale(locale_data: Locale):
        novo_locale = Locale(
        id= locale_data.id,
        name=locale_data.name,
        code=locale_data.code,
        country=locale_data.country,
        description=locale_data.description,
        is_active=locale_data.is_active,
        created_at=datetime.now(timezone.utc),
        updated_at=datetime.now(timezone.utc),
    )
        await novo_locale(novo_locale)
        return novo_locale