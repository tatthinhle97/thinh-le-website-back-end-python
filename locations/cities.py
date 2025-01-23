from fastapi import APIRouter
import os
from utilities.file_reader import read_csv_as_json

router = APIRouter(
    prefix='/cities',
    tags=['cities']
)

@router.get(
    '/',
    summary='Get all cities',
    description='Get all cities by a specific state'
)
async def get_cities():
    file_path = os.path.join(os.getcwd(), 'data', 'cities.csv')
    return read_csv_as_json(file_path)