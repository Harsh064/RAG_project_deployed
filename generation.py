def generate_answer(query, retrieved_chunks):
    """Generate an answer using retrieved chunks."""
    context = ' '.join(retrieved_chunks)
    # Replace this with a proper LLM or rule-based logic
    answer = f"Based on the context: {context[:1000]}... (truncated)"
    return answer