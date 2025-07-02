from pydantic import BaseModel
from constants.types.metadata import MetadataType
from typing import List

class ProjectMetadataDto(BaseModel):
    type: str = MetadataType.PROJECT
    tags: List[str]
    path: str
    title: str
    dateCreated: str
    description: str