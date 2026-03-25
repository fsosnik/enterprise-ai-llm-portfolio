# Agentic Workflow Automation

## Overview
This project simulates an **Agentic Workflow** using LLM tool calling (function calling). The agent is tasked with analyzing business performance. It autonomously decides to call a mock "fetch_kpis" tool to obtain data from an internal dashboard, then feeds that data back into the LLM context to formulate a business recommendation.

*Note: This is a demo to showcase how LLMs can interact with external APIs to fetch real-time data and take action, simulating an enterprise autonomous agent.*

## Stack
- **Python 3.9+**
- **OpenAI API** (or Claude, Gemini, Local Llama)

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