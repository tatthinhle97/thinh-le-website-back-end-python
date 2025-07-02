from dtos.page_metadata import PageMetadataDto
from dtos.qdrant.point import PointDto

ORIGIN = 'https://tatthinhle97.vercel.app'

PAGE_METADATA_POINTS = [
    # Specific page
    PointDto(
        id = '29681354-c0d9-4bc7-ab5b-0a56bf9a4495',
        payload = PageMetadataDto(
            url = f"{ORIGIN}",
            title = "Home page",
            path = "/",
            tags= ["home", "general", "overview"],
            more_information="you'll get an overview of Thinh's website on the home page.",
        )
    ),
    PointDto(
        id = 'cd7bfe6a-fab3-4c3f-a1a1-170d8daf0b45',
        payload = PageMetadataDto(
            url = f"{ORIGIN}/about-me",
            title = "About me page",
            path = "/about-me",
            tags= ["author", "author of the website", "website's author"],
            # For more information
            more_information= (
                "Thinh is the author of this website. He is a software developer and currently pursuing a master's "
                "degree in Data Science and Analytics at Stockton University. Outside of work and studies, he enjoys "
                "coding and photography as hobbies."
            ),
        )
    ),
    PointDto(
        id = '3c4a0dd3-f11a-4898-91bb-1d8a23447090',
        payload = PageMetadataDto(
            url = f"{ORIGIN}/projects",
            title = "Projects page",
            path = "/projects",
            tags= ["projects"],
            # For more information
            more_information= (
                "these projects demonstrates Thinh's skills to create practical solutions for the community."
            ),
        )
    ),
    PointDto(
        id = '7c0eec44-b60a-4b1b-b19c-ec610af24f97',
        payload = PageMetadataDto(
            url = f"{ORIGIN}/contact-me",
            title = "Contact me page",
            path = "/contact-me",
            tags= ["contact"],
            # Avoid add "For more information if starting with if
            more_information= (
                "If you have a project idea, want to collaborate, or just want to chat, feel free to reach out to me here!"
            ),
        )
    )
]