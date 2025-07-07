from pydantic import BaseModel
from typing import List
from constants.types.metadata import MetadataType

class PageMetadataDto(BaseModel):
    type: str = MetadataType.PAGE
    title: str
    path: str
    tags: List[str]
    description: str