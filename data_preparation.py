import re

def chunk_text(text, chunk_size=300):
    """Split text into smaller chunks."""
    words = text.split()
    chunks = [' '.join(words[i:i + chunk_size]) for i in range(0, len(words), chunk_size)]
    return chunks

def load_and_prepare_corpus(file_path):
    """Load and preprocess the corpus."""
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
        chunks = chunk_text(text)
    return chunks

# Run this script to prepare the data
if __name__ == '__main__':
    chunks = load_and_prepare_corpus('data/sample.txt')
    print(f"Prepared {len(chunks)} chunks.")