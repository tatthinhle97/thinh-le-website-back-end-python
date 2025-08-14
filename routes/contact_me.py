from fastapi import APIRouter, Request, HTTPException
from dtos.contact_me import ContactMeDto
import requests
import os

router = APIRouter(
    prefix='/contact-me',
    tags=['contactme']
)

@router.post(
    '',
    summary='Send user\'s message to my email',
    description='Receive message from user and send it to my email'
)
async def send_contact_form(contactMeDto: ContactMeDto, request: Request):
    print(request.client.host)
    formatted_message = f"""
    Name: {contactMeDto.firstName} {contactMeDto.lastName}
    Email: {contactMeDto.email}
    Phone number: {contactMeDto.phoneNumber}
    Message: {contactMeDto.message}
    """

    try:
        requests.post(
            "https://api.mailgun.net/v3/sandbox5c1f559d496440debcc0873d23ecfc5a.mailgun.org/messages",
            auth=("api", os.getenv("MAILGUN_API_KEY")),
            data={"from": "Mailgun Sandbox <postmaster@sandbox5c1f559d496440debcc0873d23ecfc5a.mailgun.org>",
                  "to": "Tat Thinh Le <letatthinh.1997@gmail.com>",
                  "subject": "[Psersonal website] Someone sent you a message",
                  "text": formatted_message})
        return True
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
