from flask import Flask, request, jsonify
from embedding_store import load_faiss_index, retrieve_top_k_chunks
from generation import generate_answer
from database import connect_to_mysql, initialize_chat_history_table, save_chat_message, fetch_chat_history
from sentence_transformers import SentenceTransformer

app = Flask(__name__)

# Load FAISS index and embedding model
index = load_faiss_index()  # Load the FAISS index
model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')  # Load embedding model

# Connect to MySQL and initialize table
db = connect_to_mysql()
initialize_chat_history_table(db)

# Root route for testing
@app.route("/", methods=["GET"])
def home():
    return "Welcome to the RAG (Retrieval-Augmented Generation) Chatbot!"

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    query = data.get('query')
    
    # Retrieve relevant chunks
    retrieved_chunks = retrieve_top_k_chunks(query, index, model, chunks)
    
    # Generate answer
    answer = generate_answer(query, retrieved_chunks)
    
    # Save chat history
    save_chat_message(db, 'user', query)
    save_chat_message(db, 'system', answer)
    
    return jsonify({
        'answer': answer,
        'retrieved_chunks': retrieved_chunks  # Optional for debugging
    })

@app.route('/history', methods=['GET'])
def history():
    history = fetch_chat_history(db)
    return jsonify(history)

# Load and preprocess the corpus
if __name__ == '__main__':
    from data_preparation import load_and_prepare_corpus
    chunks = load_and_prepare_corpus('data/sample.txt')  # Load and preprocess data
    app.run(debug=True)