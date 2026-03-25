import os
import json
from pydantic import BaseModel, Field
from openai import OpenAI
from typing import List

# 1. Define the desired structured output schema using Pydantic
class LineItem(BaseModel):
    description: str = Field(description="Description of the item or service")
    amount: float = Field(description="Total cost of the line item")

class InvoiceData(BaseModel):
    invoice_number: str = Field(description="The unique identifier for the invoice")
    vendor_name: str = Field(description="The company issuing the invoice")
    total_amount: float = Field(description="The total amount due")
    items: List[LineItem] = Field(description="List of line items in the invoice")

# 2. Unstructured Document (Simulation of OCR text)
RAW_INVOICE_TEXT = """
Acme Corp Supplies
123 Business Rd, Metropolis
Invoice #: INV-99281
Date: 2023-10-01

To: Wayne Enterprises

Items:
- 10x Heavy Duty Anvils: $1500.00
- 5x Giant Rubber Bands: $250.00
- 1x Rocket Skates: $3200.00

Total Due: $4950.00
Make checks payable to Acme Corp.
"""

def extract_invoice_data(text: str) -> str:
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
    
    # ---------------------------------------------
    
    prompt = f"""
    Extract the invoice information from the following text and format it exactly according to the requested tool schema.
    
    Invoice Text:
    {text}
    """
    
    # Modern approach to structured extraction in OpenAI (Structured Outputs or Tool Calling)
    # Using tools for deterministic extraction schema definition
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        tools=[
            {
                "type": "function",
                "function": {
                    "name": "extract_invoice",
                    "description": "Extract structured data from an invoice.",
                    "parameters": InvoiceData.schema()
                }
            }
        ],
        tool_choice={"type": "function", "function": {"name": "extract_invoice"}}
    )
    
    # Retrieve the JSON string from the tool call arguments
    tool_call = response.choices[0].message.tool_calls[0]
    return tool_call.function.arguments

if __name__ == "__main__":
    print("--- Document Intelligence Extraction Demo ---\n")
    print(f"Raw Input Text:\n{RAW_INVOICE_TEXT}")
    
    api_key = os.getenv("OPENAI_API_KEY") or os.getenv("ANTHROPIC_API_KEY") or os.getenv("GEMINI_API_KEY")
    if not api_key:
        print("\n[!] Error: Provider API Key not set.")
        print("Please set OPENAI_API_KEY, ANTHROPIC_API_KEY, or GEMINI_API_KEY.")
    else:
        # For simplicity, this demo assumes OPENAI_API_KEY is present if running as-is
        json_output = extract_invoice_data(RAW_INVOICE_TEXT)
        print("---------------------------------------------")
        print("Extracted Structured Output (JSON):")
        # Pretty print the JSON
        parsed_json = json.loads(json_output)
        print(json.dumps(parsed_json, indent=2))
        
        # We can now validate this using Pydantic directly
        invoice_obj = InvoiceData(**parsed_json)
        print(f"\n[Validation] Successfully parsed total amount inside Python: ${invoice_obj.total_amount}")