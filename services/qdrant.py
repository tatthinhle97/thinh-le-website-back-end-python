from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams
import os
from dotenv import load_dotenv
# from services.embedding import encode_texts

load_dotenv()

client = QdrantClient(
    url = os.getenv("QDRANT_URL"),
    api_key = os.getenv("QDRANT_API_KEY"),
)

def create_collection(_collection_name, _size=384, _distance=Distance.COSINE):
    if _collection_name is None:
        print(f"[ERROR] Collection name can't be empty")
        return False

    if client.collection_exists(collection_name=_collection_name):
        print(f"[INFO] Collection {_collection_name} is already created")
        return False

    # https://python-client.qdrant.tech/qdrant_client.async_client_base#qdrant_client.async_client_base.AsyncQdrantBase.create_collection
    try:
        create_collection_result = client.create_collection(
            collection_name=_collection_name,
            # The size and the distance depend on your selected model
            # Below configs were for all-MiniLM-L6-v2 model
            # Model doc: https://sbert.net/docs/sentence_transformer/pretrained_models.html#original-models
            vectors_config=VectorParams(size=_size, distance=_distance)
        )

        print(f"[INFO] Collection {_collection_name} created successfully")
        return create_collection_result
    except Exception as e:
        print(f"[ERROR] Collection {_collection_name} could not be created: {e}")
        return False

def delete_collection(_collection_name):
    if _collection_name is None:
        print(f"[ERROR] Collection name can't be empty")
        return False

    if client.collection_exists(collection_name=_collection_name):
        try:
            client.delete_collection(collection_name=_collection_name)
            print(f"[INFO] Collection {_collection_name} has been deleted")
            return True
        except Exception as e:
            print(f"[ERROR] Collection {_collection_name} could not be deleted: {e}")
            return False
    else:
        print(f"[ERROR] Collection {_collection_name} doesn't exist")

def upsert(_collection_name, _points):
    try:
        if len(_points) == 0:
            return None

        upsert_result = client.upsert(
            collection_name=_collection_name,
            points=_points
        )

        print(f"[INFO] Upsert result: {upsert_result.status}")
        return upsert_result
    except Exception as e:
        print(f"[ERROR] Can't upsert: {e}")
        return None

def search_similar_points_by_query(_collection_name, _query, _limit=5):
    # embedded_vector = encode_texts(_query)
    # similar_points = client.query_points(
    #     collection_name=_collection_name,
    #     query=embedded_vector,
    #     # How many similar sentences you want to return?
    #     limit=_limit)
    #
    # return similar_points
    return []

def find_highest_score(_points):
    if len(_points) == 0:
        return None

    return max(_points,
               key=lambda point: point.score,
               default=None)