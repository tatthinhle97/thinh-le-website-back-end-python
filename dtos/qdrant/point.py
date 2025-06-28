from pydantic import BaseModel
from typing import Any

class PointDto(BaseModel):
    id: int
    payload: Any