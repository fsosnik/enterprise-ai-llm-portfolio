# LLM Smart Router (Cost & Latency Optimizer)

## Overview
This project demonstrates an **LLM Routing / Fallback Architecture**. Relying on a single foundational model (like GPT-4o) for all tasks is expensive and slow. This demo uses a "Semantic Router" approach: it evaluates the complexity of a user's query and routes it to an inexpensive, fast model (like GPT-3.5-turbo or Gemini Flash) for simple tasks, and only invokes the expensive, powerful model for complex reasoning.

*Note: This showcases FinOps in AI engineering—balancing intelligence, latency, and operational cost.*

## Stack
- **Python 3.9+**
- **OpenAI API**

## How to Run
1. Provide your AI provider credentials:
   ```bash
   export OPENAI_API_KEY="your-openai-key-here"
   # OR
   export ANTHROPIC_API_KEY="your-claude-key-here"
   # OR
   export GEMINI_API_KEY="your-gemini-key-here"
   ```
2. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the application:
   ```bash
   python main.py
   ```