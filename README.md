# RAG Chatbot with Flask, FAISS, and MySQL

This project implements a Retrieval-Augmented Generation (RAG) chatbot using Flask for the API, FAISS for semantic search, and MySQL for storing chat history. The chatbot retrieves relevant text chunks from a corpus, generates answers, and stores the conversation history in a MySQL database.

---

## **1. How to Install and Run the System Locally**

### **Prerequisites**
- Python 3.8 or higher
- MySQL Server
- Git (optional)

### **Steps**

1. **Clone the Repository** (if using Git):
   ```bash
   git clone https://github.com/your-repo/rag-chatbot.git
   cd rag-chatbot
   ```

2. **Set Up a Virtual Environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Prepare the Data:**
   - Place your text corpus in the `data/sample.txt` file.
   - Run the data preparation script:
     ```bash
     python data_preparation.py
     ```

5. **Generate Embeddings:**
   ```bash
   python embedding_store.py
   ```

6. **Run the Flask App:**
   ```bash
   python app.py
   ```
   The Flask app will start at [http://127.0.0.1:5000](http://127.0.0.1:5000).

---

## **2. How to Set Up MySQL and Create the Required Tables**

### **Prerequisites**
- MySQL Server installed and running.

### **Steps**

1. **Log in to MySQL:**
   ```bash
   mysql -u root -p
   ```

2. **Create the Database:**
   ```sql
   CREATE DATABASE chat_history;
   ```

3. **Update MySQL Credentials:**
   Open `database.py` and update the MySQL connection details:
   ```python
   db = mysql.connector.connect(
       host="localhost",
       user="root",  # Replace with your MySQL username
       password="root",  # Replace with your MySQL password
       database="chat_history"
   )
   ```

4. **Initialize the Table:**
   The `chat_history` table will be created automatically when you run the Flask app (`app.py`).

---

## **3. How to Test the `/chat` and `/history` Endpoints**

### **Using Postman**

#### **Test the `/chat` Endpoint:**
- Send a `POST` request to `http://127.0.0.1:5000/chat` with a JSON payload:
  ```json
  {
      "query": "What is RAG?"
  }
  ```


### **Using the Provided Test Script**
Run the test script:
```bash
python tests/test_app.py
```
This script tests both the `/chat` and `/history` endpoints and prints the results to the console.

---

## **4. Project Structure**

```
rag-chatbot/
│
├── app.py                  # Flask API and main application
├── data_preparation.py     # Data preprocessing and chunking
├── embedding_store.py      # Embedding generation and vector store
├── generation.py           # Answer generation logic
├── database.py             # MySQL database connection and operations
├── requirements.txt        # Python dependencies
├── data/                   # Folder containing text corpus
│   └── sample.txt
├── vector_store/           # Folder for storing FAISS index
│   └── vector_store.index
└── tests/                  # Unit tests
    └── test_app.py
```

