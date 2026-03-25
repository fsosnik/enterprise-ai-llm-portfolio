# Enterprise AI Security & Guardrails

## Overview
This project simulates an **Enterprise AI Security Middleware** layer. Before sending a prompt to an LLM, the system checks for PII (Personally Identifiable Information) and potential Prompt Injection attacks. Once the LLM generates a response, it evaluates the output for toxicity and hallucinations before returning it to the user.

*Note: In a true production environment, you would use frameworks like NVIDIA NeMo Guardrails or Llama Guard. This demo uses rules-based regex and lightweight heuristics to showcase the architectural pattern of an interception layer.*

## Stack
- **Python 3.9+**
- **OpenAI API** (or Claude, Gemini, Local Llama)
- **Re / Regex** (for simplistic PII detection)

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