from typing import Optional
from pydantic import BaseModel

class LocationDto(BaseModel):
    fullAddress: str
    lat: float
    lng: float
    propertyType: str
    listingType: str
    bedrooms: Optional[float]
    bathrooms: Optional[float]
    livingArea: Optional[float]
    lotArea: Optional[float]
    yearBuilt: Optional[int]
    price: Optional[float]
    hoaFee: Optional[float]
    daysOnMarket: Optional[int]
    listingOfficeName: Optional[str]
    listingOfficePhone: Optional[str]
    listingOfficeEmail: Optional[str]
    listingAgentName: Optional[str]
    listingAgentPhone: Optional[str]
    listingAgentEmail: Optional[str]
    status: Optional[str]