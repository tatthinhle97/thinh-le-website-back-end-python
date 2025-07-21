from typing import Optional, List
from pydantic import BaseModel

class LocationSearchDto(BaseModel):
    rentCastApiKey: str
    searchFor: str
    state: str
    city: str
    zipCode: Optional[str] = None
    propertyType: Optional[str] = None
    bedRooms: Optional[str]
    bathRooms: Optional[str]