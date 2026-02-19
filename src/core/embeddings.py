import os
from mistralai import Mistral
from dotenv import load_dotenv

"""
Gerencia criação de embeddings para banco vetorial usando LLM.
"""

load_dotenv()

api_key = os.getenv("MISTRAL_API_KEY")
model = "mistral-medium-latest"
modelEmbedding = "mistral-embedding-1"

client = Mistral(api_key=api_key)

def embedding(text):
    response = client.embeddings.create(
        model=modelEmbedding,
        input=text
    )
    
    return response.data[0].embedding