from models.locations import StateModel
from repositories.base import BaseRepository
from sqlalchemy.orm import Session

class StateRepository(BaseRepository[StateModel]):
    def __init__(self, _db_session: Session):
        super().__init__(_db_session, StateModel)