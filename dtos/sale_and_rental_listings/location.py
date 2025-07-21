from typing import Optional, List
from pydantic import BaseModel
from dtos.sale_and_rental_listings.location_history import LocationHistoryDto

class LocationDto(BaseModel):
    fullAddress: Optional[str] = None
    lat: Optional[float] = None
    lng: Optional[float] = None
    propertyType: Optional[str] = None
    listingType: Optional[str] = None
    bedrooms: Optional[float] = None
    bathrooms: Optional[float] = None
    livingArea: Optional[float] = None
    lotArea: Optional[float] = None
    yearBuilt: Optional[int] = None
    price: Optional[float] = None
    hoaFee: Optional[float] = None
    daysOnMarket: Optional[int] = None
    listingOfficeName: Optional[str] = None
    listingOfficePhone: Optional[str] = None
    listingOfficeEmail: Optional[str] = None
    listingAgentName: Optional[str] = None
    listingAgentPhone: Optional[str] = None
    listingAgentEmail: Optional[str] = None
    status: Optional[str] = None
    history: Optional[List[LocationHistoryDto]] = None