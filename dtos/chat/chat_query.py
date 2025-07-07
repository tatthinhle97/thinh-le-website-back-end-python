from pydantic import BaseModel

class ChatQueryDto(BaseModel):
    message: str