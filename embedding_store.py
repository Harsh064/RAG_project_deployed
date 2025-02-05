from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

def generate_embeddings(chunks):
    """Generate embeddings for text chunks."""
    model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2') #sentence transformer model
    chunk_embeddings = model.encode(chunks)
    return model, chunk_embeddings

def create_faiss_index(chunk_embeddings):
    """Create and save a FAISS index."""
    dimension = chunk_embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(chunk_embeddings)
    faiss.write_index(index, 'vector_store/vector_store.index')
    return index

def load_faiss_index():
    """Load the FAISS index from disk."""
    return faiss.read_index('vector_store/vector_store.index')

def retrieve_top_k_chunks(query, index, model, chunks, k=3):
    """Retrieve top-k relevant chunks for a query."""
    query_embedding = model.encode([query])
    distances, indices = index.search(query_embedding, k)
    return [chunks[i] for i in indices[0]]

# Run this script to generate embeddings and create the FAISS index
if __name__ == '__main__':
    from data_preparation import load_and_prepare_corpus
    chunks = load_and_prepare_corpus('data/sample.txt')  # Load and preprocess data
    model, chunk_embeddings = generate_embeddings(chunks)  # Generate embeddings
    create_faiss_index(chunk_embeddings)  # Create and save FAISS index
    print("FAISS index created and saved.")