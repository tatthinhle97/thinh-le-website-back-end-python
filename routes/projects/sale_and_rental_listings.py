from fastapi import APIRouter
import os
from dtos.sale_and_rental_listings.coordinate import CoordinateDto
from dtos.sale_and_rental_listings.location import LocationDto
from utilities.file_reader import read_json
from dtos.sale_and_rental_listings.index import SaleAndRentalListingsDto
import statistics

router = APIRouter(
    prefix='/projects/sale-and-rental-listings',
    tags=['sale-and-rental-listings']
)

def to_location_dto(_listing):
    return LocationDto(
        title = _listing.get('formattedAddress'),
        latitude = _listing.get('latitude'),
        longitude = _listing.get('longitude'),
        propertyType = _listing.get('propertyType'),
        listingType = _listing.get('listingType'),
        bedrooms = _listing.get('bedrooms'),
        bathrooms = _listing.get('bathrooms'),
        livingArea = _listing.get('squareFootage'),
        lotArea = _listing.get('lotSize'),
        yearBuilt = _listing.get('yearBuilt'),
        price = _listing.get('price'),
        status = _listing.get('status')
    )

def to_coordinate_dto(_listing):
    return CoordinateDto(
        lat = _listing.get('latitude'),
        lng = _listing.get('longitude')
    )

@router.get(
    '/initial-sale-listings',
    summary='Get initial sale listings.',
    description='Sale listings in New Jersey - Atlantic City'
)
async def get_initial_sale_listings():
    file_path = os.path.join(os.getcwd(), 'data', 'nj-sale-listings.json')
    listings = read_json(file_path)
    location_dtos = []
    coordinate_dtos = []

    for listing in listings:
        location_dtos.append(to_location_dto(listing))
        coordinate_dtos.append(to_coordinate_dto(listing))

    result = SaleAndRentalListingsDto(
        locations = location_dtos,
        coordinates = coordinate_dtos,
    )

    return result
