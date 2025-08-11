from sentence_transformers import SentenceTransformer

# Use ONNX backend
model = SentenceTransformer("all-MiniLM-L6-v2", backend = "onnx")

def encode_texts(_sentences):
    return model.encode(_sentences)
