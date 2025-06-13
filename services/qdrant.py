from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams
import os
from dotenv import load_dotenv
from embedding import encode_sentences

load_dotenv()

client = QdrantClient(
    url = os.getenv("QDRANT_URL"),
    api_key = os.getenv("QDRANT_API_KEY"),
)

def create_collection(collection_name):
    if collection_name is None or client.collection_exists(collection_name=collection_name):
        return False

    # https://python-client.qdrant.tech/qdrant_client.async_client_base#qdrant_client.async_client_base.AsyncQdrantBase.create_collection
    client.create_collection(
        collection_name=collection_name,
        # The size and the distance depend on your selected model
        # Below configs were for all-MiniLM-L6-v2 model
        # Model doc: https://sbert.net/docs/sentence_transformer/pretrained_models.html#original-models
        vectors_config=VectorParams(size=384, distance=Distance.COSINE)
    )

def search_similar_sentences(sentence, collection_name, limit=5):
    encoded_sentences = encode_sentences([sentence])
    similar_sentences = client.query_points(
        collection_name=collection_name,
        query=encoded_sentences[0],
        # How many similar sentences you want to return?
        limit=limit)

    return similar_sentences

print(client.get_collections())