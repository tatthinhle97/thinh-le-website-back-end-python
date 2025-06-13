from pydantic import BaseModel


class ChatQueryDTO(BaseModel):
    message: str