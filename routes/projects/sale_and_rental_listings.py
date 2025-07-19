from fastapi import APIRouter
import os
from dtos.sale_and_rental_listings.location import LocationDto
from utilities.file_reader import read_json

router = APIRouter(
    prefix='/projects/sale-and-rental-listings',
    tags=['sale-and-rental-listings']
)

def to_location_dto(_listing):
    location_dto = LocationDto(
        fullAddress= _listing.get('formattedAddress'),
        lat = _listing.get('latitude'),
        lng = _listing.get('longitude'),
        propertyType = _listing.get('propertyType'),
        listingType = _listing.get('listingType'),
        bedrooms = _listing.get('bedrooms'),
        bathrooms = _listing.get('bathrooms'),
        livingArea = _listing.get('squareFootage'),
        lotArea = _listing.get('lotSize'),
        yearBuilt = _listing.get('yearBuilt'),
        price = _listing.get('price'),
        hoaFee = None,
        daysOnMarket = _listing.get('daysOnMarket'),
        listingOfficeName = None,
        listingOfficePhone = None,
        listingOfficeEmail = None,
        listingAgentName = None,
        listingAgentPhone = None,
        listingAgentEmail = None,
        status = _listing.get('status'),
    )

    hoa = _listing.get('hoa')
    listingOffice = _listing.get('listingOffice')
    listingAgent = _listing.get('listingAgent')

    if hoa:
        location_dto.hoaFee = hoa.get('fee')
    if listingOffice:
        location_dto.listingOfficeName = listingOffice.get('name')
        location_dto.listingOfficePhone = listingOffice.get('phone')
        location_dto.listingOfficeEmail = listingOffice.get('email')
    if listingAgent:
        location_dto.listingAgentName = listingAgent.get('name')
        location_dto.listingAgentPhone = listingAgent.get('phone')
        location_dto.listingAgentEmail = listingAgent.get('email')

    return location_dto

@router.get(
    '/default-rental-listings',
    summary='Get the default rental listings data.',
    description='Rental listings in New Jersey - Atlantic City'
)
async def get_initial_sale_listings():
    file_path = os.path.join(os.getcwd(), 'data', 'nj-rental-listings.json')
    listings = read_json(file_path)
    location_dtos = []

    for listing in listings:
        location_dtos.append(to_location_dto(listing))

    location_dtos_sorted_by_price = sorted(location_dtos,
                                      key=lambda _listing: _listing.price)

    return location_dtos_sorted_by_price
