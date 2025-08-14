from pydantic import BaseModel
from typing import Optional, List

class ContactMeDto(BaseModel):
    firstName: str
    lastName: Optional[str] = ''
    email: str
    phoneNumber: Optional[str] = ''
    message: str