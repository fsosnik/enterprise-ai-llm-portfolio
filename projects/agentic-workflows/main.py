import os
import json
from openai import OpenAI

# 1. Define the mock external tool (e.g., fetching data from a database/API)
def fetch_financial_kpis(month: str) -> str:
    """Mock function that returns KPI data for a specific month."""
    mock_db = {
        "January": {"revenue": 45000, "expenses": 32000, "active_users": 1200},
        "February": {"revenue": 41000, "expenses": 35000, "active_users": 1100}
    }
    data = mock_db.get(month, {"error": "No data found for this month."})
    return json.dumps(data)

# 2. Define the tool schema for OpenAI parameter extraction
TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "fetch_financial_kpis",
            "description": "Fetch financial KPIs (Revenue, Expenses, Active Users) for a given month.",
            "parameters": {
                "type": "object",
                "properties": {
                    "month": {
                        "type": "string",
                        "description": "The month to fetch data for, e.g., 'January' or 'February'",
                    }
                },
                "required": ["month"],
            },
        }
    }
]

def run_agent(query: str):
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    
    messages = [{"role": "user", "content": query}]
    print(f"User: {query}")
    
    # Initial call gives the model access to tools
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages,
        tools=TOOLS,
        tool_choice="auto",
    )
    
    message = response.choices[0].message
    
    # Check if the LLM wants to call our tool
    if message.tool_calls:
        tool_call = message.tool_calls[0]
        arguments = json.loads(tool_call.function.arguments)
        print(f"[Agent Logic] LLM decided to call tool '{tool_call.function.name}' with args {arguments}")
        
        # Execute the tool locally
        if tool_call.function.name == "fetch_financial_kpis":
            tool_result = fetch_financial_kpis(arguments.get("month", ""))
            print(f"[Tool Execution] Result: {tool_result}")
            
            # Append interaction to conversation history
            messages.append(message)  
            messages.append({
                "role": "tool",
                "tool_call_id": tool_call.id,
                "name": tool_call.function.name,
                "content": tool_result,
            })
            
            # Second LLM call to generate final response using the tool's data
            final_response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=messages,
            )
            print(f"\\nFinal Agent Output:\\n{final_response.choices[0].message.content}")

if __name__ == "__main__":
    print("--- Agentic Workflow Demo ---")
    if not os.getenv("OPENAI_API_KEY"):
        print("\\n[!] Error: OPENAI_API_KEY environment variable not set.")
    else:
        run_agent("Can you analyze how we performed in February and give me a brief summary?")
