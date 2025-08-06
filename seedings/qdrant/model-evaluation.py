from sentence_transformers import SentenceTransformer, util

# Load a pre-trained Sentence Transformer model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Define the texts to compare
user_query = "I want to search for projects on this website."
projects_page = "This page contains all the projects on this website."
home_page = "This page contains general information about the website."

# Encode the sentences into embeddings
embeddings = model.encode([user_query, projects_page, home_page])

# Calculate cosine similarity between pairs of embeddings
user_query_vs_projects_page = util.cos_sim(embeddings[0], embeddings[1])
user_query_vs_home_page = util.cos_sim(embeddings[0], embeddings[2])

print(f"Similarity between user's query and projects page description: {user_query_vs_projects_page.item():.4f}")
print(f"Similarity between user's query and home page description: {user_query_vs_home_page.item():.4f}")