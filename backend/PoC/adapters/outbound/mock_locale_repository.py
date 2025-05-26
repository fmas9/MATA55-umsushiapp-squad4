from backend.PoC.domain.entities.locale import Locale
from typing import List
from uuid import UUID
from locale import locale  # sua entidade

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