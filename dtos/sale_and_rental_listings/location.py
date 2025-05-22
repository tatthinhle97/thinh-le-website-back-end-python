from typing import Optional, List
from pydantic import BaseModel


class LocationDTO(BaseModel):
    title: str
    latitude: float
    longitude: float
    propertyType: str
    bedrooms: Optional[float]
    bathrooms: Optional[float]
    livingArea: Optional[float]
    lotArea: Optional[float]
    yearBuilt: Optional[int]
    price: Optional[int]
    status: Optional[str]