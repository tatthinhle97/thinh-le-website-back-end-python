import pandas
from fastapi import APIRouter, HTTPException
import os
from utilities.file_reader import read_csv_as_json

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
async def get_cities_and_states():
    return read_csv_as_json(cities_file_path)

@router.get(
    '/cities-by-state-name',
    summary='Get cities by state name',
    description='Get cities by state name'
)
async def get_cities_by_state_name(state_name: str):
    states_df = pandas.read_csv(states_file_path)
    cities_df = pandas.read_csv(cities_file_path)
    states = states_df[states_df['name'] == state_name]

    if states.empty:
        raise HTTPException(status_code=404, detail="State code not found")

    state_code = states['code'].iloc[0]
    cities = cities_df[cities_df['state'] == state_code]['name']

    return sorted(cities.tolist())