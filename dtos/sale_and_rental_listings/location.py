from typing import Optional, List
from pydantic import BaseModel
from dtos.sale_and_rental_listings.location_history import LocationHistoryDto


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
    hoaFee: Optional[float] = None
    daysOnMarket: Optional[int]
    listingOfficeName: Optional[str] = None
    listingOfficePhone: Optional[str] = None
    listingOfficeEmail: Optional[str] = None
    listingAgentName: Optional[str] = None
    listingAgentPhone: Optional[str] = None
    listingAgentEmail: Optional[str] = None
    status: Optional[str]
    history: List[LocationHistoryDto] = []