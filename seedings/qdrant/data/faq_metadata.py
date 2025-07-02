from dtos.faq_metadata import FaqMetadataDto
from dtos.qdrant.point import PointDto

FAQ_METADATA_POINTS = [
    # Specific page
    PointDto(
        id='71c38de3-e08d-4920-84a3-5b9e10885582',
        payload=FaqMetadataDto(
            question="Information about the website",
            tags=["information", "website"],
            answer="You are viewing a personal website of a DSSA student at Stockton"
        )
    ),
    PointDto(
        id='de9c77d1-7cc3-4ce2-b213-b8f2e062670b',
        payload=FaqMetadataDto(
            question="Information about the account like create or register for a new account, sign in or sign up",
            tags=["login", "signin", "signup", "account register", "create new account"],
            answer="This function is not implemented yet. You can drink a coffee 🍵 while waiting."
        )
    ),
]