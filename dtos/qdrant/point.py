from pydantic import BaseModel
from typing import Any

class PointDto(BaseModel):
    id: str
    payload: Any