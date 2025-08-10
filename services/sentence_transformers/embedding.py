from sentence_transformers import SentenceTransformer
import os

def load_onnx_model():
    """
    Load the model with ONNX backend for reduced memory usage
    """
    model_path = os.path.join(
        os.getcwd(),
        'services',
        'sentence_transformers',
        'model_onnx')

    if not os.path.exists(model_path):
        raise FileNotFoundError(f"Model directory {model_path} not found. Run save_model_script.py first.")

    # Force ONNX backend usage
    model = SentenceTransformer(
        model_path,
        backend="onnx",  # Use ONNX backend
        device="cpu"     # Force CPU usage for consistency
    )

    return model

def encode_texts(_sentences):
    return load_onnx_model().encode(_sentences)
