from typing import List
from pydantic import BaseModel
from dtos.sale_and_rental_listings.coordinate import CoordinateDTO
from dtos.sale_and_rental_listings.location import LocationDTO


class SaleAndRentalListingsDTO(BaseModel):
    locations: List[LocationDTO]
    coordinates: List[CoordinateDTO]