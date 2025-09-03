from fastapi import APIRouter, Depends
import os
from databases.mysql import get_db_session
from repositories.city import CityRepository

router = APIRouter(
    prefix='/cities',
    tags=['cities']
)

states_file_path = os.path.join(os.getcwd(), 'data', 'states.csv')
cities_file_path = os.path.join(os.getcwd(), 'data', 'cities.csv')

@router.get(
    '',
    summary='Get state-county-city records',
    description='Get all cities with their county and state information'
)
async def get_cities_and_states(db_session = Depends(get_db_session)):
    city_repository = CityRepository(db_session)
    return city_repository.get_all()

@router.get(
    '/cities-by-state-name',
    summary='Get cities by state name',
    description='Get cities by state name'
)
async def get_cities_by_state_name(state_name, db_session = Depends(get_db_session)):
    city_repository = CityRepository(db_session)
    cities = city_repository.get_cities_by_state_name(state_name)
    return cities