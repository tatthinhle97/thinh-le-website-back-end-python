from typing import Generic, TypeVar, Type
from sqlalchemy import select, Select
from sqlalchemy.orm import Session
from models.locations import BaseModel

# Restrict T to SQLAlchemy models
T = TypeVar("T", bound=BaseModel)

class BaseRepository(Generic[T]):
    def __init__(self, _db_session: Session, _model: Type[T]):
        self.db_session = _db_session
        self.model = _model

    def get_all_as_query(self) -> Select[T]:
        return select(self.model)

    def get_all(self) -> list[T]:
        return self.db_session.scalars(self.get_all_as_query()).all()