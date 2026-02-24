import os
from mistralai import Mistral
from dotenv import load_dotenv

"""
Gerencia criação de embeddings para banco vetorial usando LLM.
"""

load_dotenv()

api_key = os.getenv("MISTRAL_API_KEY")
modelEmbedding = "mistral-embed"

client = Mistral(api_key=api_key)

def embedding(text):
    response = client.embeddings.create(
        model=modelEmbedding,
        inputs=text
    )
    
    return response.data[0].embedding