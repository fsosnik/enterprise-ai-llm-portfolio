# Document Intelligence (Information Extraction)

## Overview
This project simulates an AI-powered extraction pipeline using LLMs. It takes raw, unstructured text (like an OCR output from an invoice or contract) and uses the LLM to extract key data points directly into a typed JSON schema. 

*Note: This demo leverages the `pydantic` library to define the data structures and uses OpenAI's Function Calling/Structured Output capabilities to enforce the JSON structure. This is a common pattern in enterprise back-office automation.*

## Stack
- **Python 3.9+**
- **OpenAI API** (or Claude, Gemini, Local Llama)
- **Pydantic** (Data validation and schema generation)

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