from fastapi import APIRouter
import os
from utilities.file_reader import read_json

router = APIRouter(
    prefix='/projects/sale-and-rental-listings',
    tags=['sale-and-rental-listings']
)

@router.get(
    '/initial-sale-listings',
    summary='Get initial sale listings.',
    description='Data was collected in New Jersey - Atlantic City'
)
async def get_initial_sale_listings():
    file_path = os.path.join(os.getcwd(), 'data', 'nj-sale-listings.json')
    return read_json(file_path)