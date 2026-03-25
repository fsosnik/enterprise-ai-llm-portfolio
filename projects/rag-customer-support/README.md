# RAG Customer Support Assistant

## Overview
This is a demonstration of a **Retrieval-Augmented Generation (RAG)** pipeline. Given a customer's query, the system retrieves the most relevant pieces of information from a predefined knowledge base and provides them as context to an LLM to generate an accurate, grounded response. 

*Note: This is a conceptual demo. For simplicity, we use `scikit-learn`'s TF-IDF vectorizer to simulate document embeddings and semantic search, keeping the demo lightweight without requiring a dedicated vector database.*

## Stack
- **Python 3.9+**
- **OpenAI API** (LLM generation)
- **Scikit-Learn** (TF-IDF Vectorization & Cosine Similarity for Retrieval)

## How to Run
1. Ensure you have your `OPENAI_API_KEY` set in your environment:
   ```bash
   export OPENAI_API_KEY="your-api-key-here"
   ```
2. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the application:
   ```bash
   python main.py
   ```
