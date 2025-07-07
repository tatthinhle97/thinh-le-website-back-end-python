from dtos.faq_metadata import FaqMetadataDto
from dtos.qdrant.point import PointDto

FAQ_METADATA_POINTS = [
    PointDto(
        id='de9c77d1-7cc3-4ce2-b213-b8f2e062670b',
        payload=FaqMetadataDto(
            question="Can I create an account on this website? How do I register or login?",
            tags=["login", "signin", "signup", "account register", "create new account"],
            answer="This function is not implemented yet. You can drink a coffee 🍵 while waiting."
        )
    ),
]