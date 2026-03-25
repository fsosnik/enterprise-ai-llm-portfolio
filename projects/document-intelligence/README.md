# Document Intelligence (Information Extraction)

## Overview
This project simulates an AI-powered extraction pipeline using LLMs. It takes raw, unstructured text (like an OCR output from an invoice or contract) and uses the LLM to extract key data points directly into a typed JSON schema. 

*Note: This demo leverages the `pydantic` library to define the data structures and uses OpenAI's Function Calling/Structured Output capabilities to enforce the JSON structure. This is a common pattern in enterprise back-office automation.*

## Stack
- **Python 3.9+**
- **OpenAI API** (or Claude, Gemini, Local Llama)
- **Pydantic** (Data validation and schema generation)

## How to Run
1. Provide your AI provider credentials (depending on your preferred model):
   ```bash
   export OPENAI_API_KEY="your-openai-key-here"
   # OR
   export ANTHROPIC_API_KEY="your-claude-key-here"
   # OR
   export GEMINI_API_KEY="your-gemini-key-here"
   # OR use a Local Model (e.g., Llama 3 via Ollama) - see code comments.
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the application:
   ```bash
   python main.py
   ```