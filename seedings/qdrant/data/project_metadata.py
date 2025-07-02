from dtos.project_metadata import ProjectMetadataDto
from dtos.qdrant.point import PointDto

PROJECT_METADATA_POINTS = [
    # Specific page
    PointDto(
        id = '7b760c3e-fd03-40b5-9ef2-302aff24c0db',
        payload = ProjectMetadataDto(
            title = "Sale and rental listings",
            path = "/projects/sale-and-rental-listings",
            tags = ["listings", "house", "building", "apartment", "rent", "sale"],
            dateCreated = '2024-12-17',
            description = (
                "Search for sale and rental listings across the US, integrating interactive data visualizations to "
                "analyze trends and insights in the housing market."
            )
        )
    ),
]