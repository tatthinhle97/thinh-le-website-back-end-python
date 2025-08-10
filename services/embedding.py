# from sentence_transformers import SentenceTransformer
#
# # The PyTorch backend is the default backend for Sentence Transformers. If you
# # don’t specify a device, it will use the strongest available option across
# # “cuda”, “mps”, and “cpu”.
# model = SentenceTransformer("all-MiniLM-L6-v2")
#
# def encode_texts(_sentences):
#     return model.encode(_sentences)