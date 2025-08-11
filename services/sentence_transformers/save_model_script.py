from sentence_transformers import SentenceTransformer

model_name = "sentence-transformers/all-MiniLM-L6-v2"
output_directory= "./model_onnx"

"""
Run this once to download and convert the model to ONNX format
"""
# Load the model
model = SentenceTransformer(
    model_name,
    backend="onnx")

model.save_pretrained(output_directory)
print(f"Model saved to {output_directory}")

