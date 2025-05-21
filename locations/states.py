from fastapi import APIRouter
import os
from utilities.file_reader import read_csv_as_json

router = APIRouter(
    prefix='/states',
    tags=['states']
)

@router.get(
    # [Tip] Should not put '/' because front end will receive status 307
    '',
    summary='Get all states',
    description='Get all states'
)
async def get_states():
    file_path = os.path.join(os.getcwd(), 'data', 'states.csv')
    return read_csv_as_json(file_path)