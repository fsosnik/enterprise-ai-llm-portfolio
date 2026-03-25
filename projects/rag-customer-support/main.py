import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from openai import OpenAI

# 1. Provide a mock knowledge base (Documents)
KNOWLEDGE_BASE = [
    "Our return policy allows items to be returned within 30 days of purchase with a full refund. Items must be in original packaging.",
    "For technical support with your smart home device, please hold the reset button for 10 seconds to restore factory settings.",
    "Shipping is free for all orders over $50. Standard shipping takes 3-5 business days.",
    "Premium subscription costs $9.99 per month and includes ad-free listening, offline mode, and high-fidelity audio."
]

def chunk_documents(docs, chunk_size=50):
    """
    Simulates a naive text chunker. 
    In reality, we would use LangChain or LlamaIndex recursive splitters.
    """
    chunks = []
    for doc in docs:
        words = doc.split()
        for i in range(0, len(words), chunk_size):
            chunks.append(" ".join(words[i:i+chunk_size]))
    return chunks

def retrieve_relevant_context(query, document_chunks, top_k=1):
    """
    Simulates semantic search using TF-IDF and Cosine Similarity.
    In a real RAG app, this would use text embeddings and a VectorDB (e.g., Pinecone, Chroma).
    """
    vectorizer = TfidfVectorizer()
    # Fit the vectorizer on the documents and the query
    corpus = document_chunks + [query]
    tfidf_matrix = vectorizer.fit_transform(corpus)
    
    # The last row is the query vector
    query_vector = tfidf_matrix[-1]
    doc_vectors = tfidf_matrix[:-1]
    
    # Calculate similarities
    similarities = cosine_similarity(query_vector, doc_vectors).flatten()
    
    # Get top_k indices
    top_indices = similarities.argsort()[-top_k:][::-1]
    return [document_chunks[i] for i in top_indices]

def generate_response(query, context):
    """
    Calls the LLM with the retrieved context and the user query.
    """
    # --- AI Provider Initialization Examples ---
    
    # 1. OpenAI (Default for this demo)
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    
    # 2. Anthropic (Claude) - Requires `pip install anthropic`
    # import anthropic
    # claude_client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

    # 3. Google GenAI (Gemini) - Requires `pip install google-generativeai`
    # import google.generativeai as genai
    # genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
    # gemini_model = genai.GenerativeModel('gemini-1.5-pro')
    
    # ---------------------------------------------
    
    prompt = f"""
    You are a helpful customer support assistant. 
    Answer the user's question ONLY using the provided context below.
    If the context doesn't contain the answer, say "I don't have enough information to answer that."

    Context:
    {context}

    Question:
    {query}
    """
    
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.0
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    print("--- RAG Customer Support Demo ---")
    
    # Process knowledge base
    chunks = chunk_documents(KNOWLEDGE_BASE)
    
    # User query
    user_query = "How long do I have to return a product?"
    print(f"User Query: {user_query}")
    
    # Retrieval Phase
    retrieved_context = retrieve_relevant_context(user_query, chunks, top_k=1)
    context_str = "\n".join(retrieved_context)
    print(f"\n[Retrieved Context]: {context_str}")
    
    # Generation Phase
    api_key = os.getenv("OPENAI_API_KEY") or os.getenv("ANTHROPIC_API_KEY") or os.getenv("GEMINI_API_KEY")
    if not api_key:
        print("\n[!] Error: Provider API Key not set.")
        print("Please set OPENAI_API_KEY, ANTHROPIC_API_KEY, or GEMINI_API_KEY.")
    else:
        # For simplicity, this demo assumes OPENAI_API_KEY is present if running as-is
        answer = generate_response(user_query, context_str)
        print(f"\n[Assistant Response]: {answer}")