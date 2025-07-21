from typing import Optional
from pydantic import BaseModel

class LocationHistoryDto(BaseModel):
    date: Optional[str] = None
    event: Optional[str] = None
    price: Optional[float] = None
    daysOnMarket: Optional[int] = None