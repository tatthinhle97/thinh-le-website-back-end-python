from dtos.page_metadata import PageMetadataDto
from dtos.qdrant.point import PointDto

ORIGIN = 'https://tatthinhle97.vercel.app'

PAGE_METADATA_POINTS = [
    # Specific page
    PointDto(
        id = 0,
        payload = PageMetadataDto(
            url = f"{ORIGIN}",
            title = "Home page",
            path = "/",
            keywords = ["home", "general", "overview"],
            description = "Home page",
        )
    ),
    PointDto(
        id = 1,
        payload = PageMetadataDto(
            url = f"{ORIGIN}/about-me",
            title = "About me page",
            path = "/about-me",
            keywords = ["author", "author of the website", "website's author"],
            description = (
                "Thinh is the author of this website. He is a software developer and currently pursuing a master's "
                "degree in Data Science and Analytics at Stockton University. Outside of work and studies, he enjoys "
                "coding and photography as hobbies."
            ),
        )
    ),
]