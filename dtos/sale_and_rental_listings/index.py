from typing import List
from pydantic import BaseModel
from dtos.sale_and_rental_listings.coordinate import CoordinateDto
from dtos.sale_and_rental_listings.location import LocationDto

class SaleAndRentalListingsDto(BaseModel):
    locations: List[LocationDto]
    coordinates: List[CoordinateDto]