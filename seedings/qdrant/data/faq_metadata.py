from dtos.faq_metadata import FaqMetadataDto
from dtos.qdrant.point import PointDto

FAQ_METADATA_POINTS = [
    # Specific page
    PointDto(
        id=2,
        payload=FaqMetadataDto(
            question="Information about the website",
            keywords=["information", "website"],
            answer="You are viewing a personal website of a DSSA student at Stockton"
        )
    ),
    PointDto(
        id=3,
        payload=FaqMetadataDto(
            question="Information about the account like create or register for a new account, sign in or sign up",
            keywords=["login", "signin", "signup", "account register", "create new account"],
            answer="This function is not implemented yet. You can drink a coffee 🍵 while waiting."
        )
    ),
]