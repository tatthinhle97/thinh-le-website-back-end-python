# from seedings.qdrant.data.faq_metadata import FAQ_METADATA_POINTS
# from seedings.qdrant.data.page_metadata import PAGE_METADATA_POINTS
# from services.qdrant import create_collection, delete_collection, upsert
# from services.embedding import encode_texts
# from qdrant_client.models import PointStruct
#
# # Create a collection name website_metadata if not exists
# COLLECTION_NAME = "website_metadata"
#
# #delete_collection(COLLECTION_NAME)
# create_collection(COLLECTION_NAME)
#
#
# # Create a list of points
# points = []
#
# # Create points related to page metadata
# for page_metadata_point in PAGE_METADATA_POINTS:
#     metadata = page_metadata_point.payload.description
#     metadata_encoded = encode_texts(metadata)
#     points.append(
#         PointStruct(
#             id = page_metadata_point.id,
#             vector = metadata_encoded,
#             # Convert from python class object to dict type
#             payload = page_metadata_point.payload.__dict__
#         )
#     )
#
# # Create points related to faq metadata
# for faq_metadata_point in FAQ_METADATA_POINTS:
#     metadata = (
#         f"Questions: {faq_metadata_point.payload.question}. "
#         f"Answer: {faq_metadata_point.payload.answer}"
#     )
#     metadata_encoded = encode_texts(metadata)
#     points.append(
#         PointStruct(
#             id = faq_metadata_point.id,
#             vector = metadata_encoded,
#             # Convert from python class object to dict type
#             payload = faq_metadata_point.payload.__dict__
#         )
#     )
#
#
# upsert(COLLECTION_NAME, points)
#
