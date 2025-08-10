# from sentence_transformers import SentenceTransformer
#
# model_name="all-MiniLM-L6-v2"
# local_path="./model_onnx"
#
# """
# Run this once to download and convert the model to ONNX format
# """
# # Load the model
# model = SentenceTransformer(model_name)
#
# # Convert to ONNX and save locally
# model.save(local_path, create_model_card=False)
#
# # Convert to ONNX format
# model.save(local_path, create_model_card=False, safe_serialization=True)
#
# print(f"Model saved to {local_path}")