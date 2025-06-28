from pydantic import BaseModel
from typing import List
from constants.types.metadata import MetadataType

class FaqMetadataDto(BaseModel):
    type: str = MetadataType.FAQ
    question: str
    keywords: List[str]
    answer: str