from pydantic import BaseModel

# lat & lng is following convention in Google Map API
class CoordinateDTO(BaseModel):
    lat: float
    lng: float