from fastapi import APIRouter
import os
from dtos.sale_and_rental_listings.location import LocationDto
from dtos.sale_and_rental_listings.location_history import LocationHistoryDto
from dtos.sale_and_rental_listings.location_search import LocationSearchDto
from utilities.file_reader import read_json
import httpx
import pandas

states_file_path = os.path.join(os.getcwd(), 'data', 'states.csv')

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
        daysOnMarket = _listing.get('daysOnMarket'),
        status = _listing.get('status'),
    )

    hoa = _listing.get('hoa')
    listingOffice = _listing.get('listingOffice')
    listingAgent = _listing.get('listingAgent')
    history = _listing.get('history')

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
    if history:
        location_dto.history = [
        LocationHistoryDto(
            date=_date,
            event=_history["event"],
            price=_history["price"],
            daysOnMarket=_history["daysOnMarket"]
        )
        for _date, _history in history.items()
    ]

    return location_dto

def to_location_dtos(_listings):
    location_dtos = []

    for listing in _listings:
        location_dtos.append(to_location_dto(listing))

    return sorted(location_dtos,
                  key=lambda _listing: _listing.price)

router = APIRouter(
    prefix='/projects/sale-and-rental-listings',
    tags=['sale-and-rental-listings']
)

@router.get(
    '/default-rental-listings',
    summary='Get the default rental listings data.',
    description='Rental listings in New Jersey - Atlantic City'
)
async def get_initial_sale_listings():
    file_path = os.path.join(os.getcwd(), 'data', 'rental-listings.json')
    listings = read_json(file_path)
    return to_location_dtos(listings)


@router.post(
    '/search-listings',
    summary='Search for listings.',
    description='Search for rental or sale listings.'
)
async def get_listings(_locationSearchDto: LocationSearchDto):
    url_prefix = 'https://api.rentcast.io/v1/listings'
    sale_url = f'{url_prefix}/sale'
    rental_url = f'{url_prefix}/rental/long-term'
    url = sale_url if _locationSearchDto.searchFor == 'Sale' else rental_url

    params = {
        'city': _locationSearchDto.city,
        'status': 'Active',
        'limit': 500
    }

    states_df = pandas.read_csv(states_file_path)
    states = states_df[states_df['name'] == _locationSearchDto.state]

    params['state'] = states['code'].iloc[0]

    if _locationSearchDto.zipCode:
        params['zipCode'] = _locationSearchDto.zipCode
    if _locationSearchDto.propertyType:
        params['propertyType'] = _locationSearchDto.propertyType
    if _locationSearchDto.bedRooms:
        params['bedrooms'] = float(_locationSearchDto.bedRooms)
    if _locationSearchDto.bathRooms:
        params['bathrooms'] = float(_locationSearchDto.bathRooms)

    headers = {
        "accept": "application/json",
        "X-Api-Key": _locationSearchDto.rentCastApiKey
    }

    async with httpx.AsyncClient() as client:
        response = await client.get(url, params=params, headers=headers)
        listings = response.json()
        return to_location_dtos(listings)
