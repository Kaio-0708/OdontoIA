import os
from mistralai import Mistral
from dotenv import load_dotenv

"""
Gerencia chamadas à API com LLM.
"""

load_dotenv()

api_key = os.getenv("MISTRAL_API_KEY")
model = "mistral-medium-latest"

client = Mistral(api_key=api_key)

chatResponse = client.chat.complete(
    model = model,
    messages = [
        {
            "role": "user",
            "content": prompt,
        },
    ]
)