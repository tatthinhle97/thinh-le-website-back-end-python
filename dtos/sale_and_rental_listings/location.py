from typing import Optional
from pydantic import BaseModel

class LocationDto(BaseModel):
    title: str
    latitude: float
    longitude: float
    propertyType: str
    listingType: str
    bedrooms: Optional[float]
    bathrooms: Optional[float]
    livingArea: Optional[float]
    lotArea: Optional[float]
    yearBuilt: Optional[int]
    price: Optional[int]
    status: Optional[str]