from typing import Optional
from pydantic import BaseModel

class LocationHistoryDto(BaseModel):
    date: str
    event: str
    price: float
    daysOnMarket: Optional[int] = None