import os
import time
from openai import OpenAI

# Simulating an Enterprise Semantic Router for Cost Optimization (FinOps for AI)

def analyze_complexity(prompt: str) -> str:
    """
    A lightweight heuristic (or a fast local embedding classification) to determine complexity.
    In real systems, this could be a fast naive bayes classifier or semantic embedding match.
    """
    clarification_words = ["analyze", "evaluate", "synthesize", "architect", "why", "compare"]
    word_count = len(prompt.split())
    
    # If it's a long prompt or contains reasoning keywords, route to the heavy model.
    if word_count > 15 or any(w in prompt.lower() for w in clarification_words):
        return "HEAVY"
    return "LIGHT"

def route_and_execute(prompt: str) -> str:
    complexity = analyze_complexity(prompt)
    
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

    # 4. Local AI (e.g., Llama 3) via Ollama
    # client = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")
    
    # ---------------------------------------------
    
    start_time = time.time()
    
    if complexity == "LIGHT":
        print("[Router] Query is simple. Routing to fast, low-cost model (e.g., gpt-3.5-turbo or local Llama 3 8B).")
        target_model = "gpt-3.5-turbo"
    else:
        print("[Router] Query requires deep reasoning. Routing to heavy, capable model (e.g., gpt-4o or Claude 3.5 Sonnet).")
        # In a real setup, this would be gpt-4o or claude-3-5-sonnet
        # Using gpt-3.5-turbo here just so the demo doesn't fail if the user only has basic tier access.
        target_model = "gpt-3.5-turbo"  
        
    response = client.chat.completions.create(
        model=target_model,
        messages=[{"role": "user", "content": prompt}],
    )
    
    latency = time.time() - start_time
    print(f"[Metrics] Model: {target_model} | Latency: {latency:.2f}s | Cost: Optimized Tier")
    
    return response.choices[0].message.content

if __name__ == "__main__":
    print("--- LLM Smart Router (FinOps) Demo ---")
    
    api_key = os.getenv("OPENAI_API_KEY") or os.getenv("ANTHROPIC_API_KEY") or os.getenv("GEMINI_API_KEY")
    if not api_key:
        print("\n[!] Error: Provider API Key not set.")
        print("Please set OPENAI_API_KEY, ANTHROPIC_API_KEY, or GEMINI_API_KEY (or uncomment the local Llama logic in code).")
    else:
        # 1. Simple query -> Routed to cheap model
        q1 = "What is the capital of Argentina?"
        print(f"\nUser: {q1}")
        print(f"Assistant: {route_and_execute(q1)}")
        
        # 2. Complex query -> Routed to heavy model
        q2 = "Analyze the macroeconomic impact of shifting to a carbon-neutral energy grid, and compare the transitional risks with fossil fuel subsidies."
        print(f"\nUser: {q2}")
        print(f"Assistant: {route_and_execute(q2)}")