from dtos.page_metadata import PageMetadataDto
from dtos.qdrant.point import PointDto

PAGE_METADATA_POINTS = [
    # Specific page
    PointDto(
        id = '29681354-c0d9-4bc7-ab5b-0a56bf9a4495',
        payload = PageMetadataDto(
            title = "Home page",
            path = "/",
            tags= ["home page"],
            description = "Home page is where you can find a brief introduction to the purpose of this website."
        )
    ),
    PointDto(
        id = 'cd7bfe6a-fab3-4c3f-a1a1-170d8daf0b45',
        payload = PageMetadataDto(
            title = "About me",
            path = "/about-me",
            tags= ["page", "author", "author of the website", "website's author"],
            description= (
                "The about me page has a short introduction about the author of this website, where you can learn more "
                "about his skills, accomplishments, and career goals."
            ),
        )
    ),
    PointDto(
        id = '3c4a0dd3-f11a-4898-91bb-1d8a23447090',
        payload = PageMetadataDto(
            title = "Projects",
            path = "/projects",
            tags= ["page", "projects"],
            description= (
                "The projects page includes projects that are free to use to support the community, as well as small "
                "tool projects to assist the author's programming work."
            ),
        )
    ),
    PointDto(
        id = '7b760c3e-fd03-40b5-9ef2-302aff24c0db',
        payload = PageMetadataDto(
            title = "Sale and rental listings",
            path = "/projects/sale-and-rental-listings",
            tags = ["listings", "house", "building", "apartment", "rent", "sale", "project"],
            description = (
                "This project searches for sale and rental listings across the US, integrating interactive data "
                "visualizations to analyze trends and insights in the housing market."
            )
        )
    ),
    PointDto(
        id = '7c0eec44-b60a-4b1b-b19c-ec610af24f97',
        payload = PageMetadataDto(
            title = "Contact me",
            path = "/contact-me",
            tags= ["page", "contact me"],
            description= (
                "The contact me page is where you can get in touch with the author."
            ),
        )
    )
]