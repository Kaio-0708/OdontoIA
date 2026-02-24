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

def chatResponse(prompt, temperature=0.2, max_tokens=700):

    try:
        response = client.chat.complete(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            temperature=temperature,
            max_tokens=max_tokens
        )
        return response.choices[0].message.content

    except Exception as e:
        return f"Erro ao gerar resposta: {str(e)}"
