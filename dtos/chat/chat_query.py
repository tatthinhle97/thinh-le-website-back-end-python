from pydantic import BaseModel

class ChatQueryDto(BaseModel):
    collection_name: str
    message: str