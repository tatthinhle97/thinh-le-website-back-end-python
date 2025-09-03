from sqlalchemy import select
from models.locations import CityModel, StateModel
from repositories.base import BaseRepository
from sqlalchemy.orm import Session

class CityRepository(BaseRepository[CityModel]):
    def __init__(self, _db_session: Session):
        super().__init__(_db_session, CityModel)

    def get_cities_by_state_name(self, state_name) -> list[str]:
        query = (select(CityModel.city)
                    .distinct()
                    .join(CityModel.state)
                    .where(StateModel.name == state_name))
        return self.db_session.scalars(query).all()