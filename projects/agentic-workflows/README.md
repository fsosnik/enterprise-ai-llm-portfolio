# Agentic Workflow Automation

## Overview
This project simulates an **Agentic Workflow** using LLM tool calling (function calling). The agent is tasked with analyzing business performance. It autonomously decides to call a mock "fetch_kpis" tool to obtain data from an internal dashboard, then feeds that data back into the LLM context to formulate a business recommendation.

*Note: This is a demo to showcase how LLMs can interact with external APIs to fetch real-time data and take action, simulating an enterprise autonomous agent.*

## Stack
- **Python 3.9+**
- **OpenAI API** (Tool Calling & Generation)

## How to Run
1. Ensure your `OPENAI_API_KEY` is set:
   ```bash
   export OPENAI_API_KEY="your-api-key-here"
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the application:
   ```bash
   python main.py
   ```
