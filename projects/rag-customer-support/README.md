# RAG Customer Support Assistant

## Overview
This is a demonstration of a **Retrieval-Augmented Generation (RAG)** pipeline. Given a customer's query, the system retrieves the most relevant pieces of information from a predefined knowledge base and provides them as context to an LLM to generate an accurate, grounded response. 

*Note: This is a conceptual demo. For simplicity, we use `scikit-learn`'s TF-IDF vectorizer to simulate document embeddings and semantic search, keeping the demo lightweight without requiring a dedicated vector database.*

## Stack
- **Python 3.9+**
- **OpenAI API** (or Claude, Gemini, Local Llama)
- **Scikit-Learn** (TF-IDF Vectorization & Cosine Similarity for Retrieval)

## How to Run

### Option A: Cloud Providers (OpenAI, Claude, Gemini)
Provide your AI provider credentials:
```bash
export OPENAI_API_KEY="your-openai-key-here"
# OR
export ANTHROPIC_API_KEY="your-claude-key-here"
# OR
export GEMINI_API_KEY="your-gemini-key-here"
```

### Option B: Local Inference (Ollama)
For data privacy and zero cost, run a local model:
1. Install [Ollama](https://ollama.com/).
2. Download a model: `ollama run llama3`
3. Uncomment the "Local AI" block inside `main.py`.

### Execution
1. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the application:
   ```bash
   python main.py
   ```