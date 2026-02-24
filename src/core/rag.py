from database.vetor_db import search
from core.prompt import prompt
from core.llmService import chatResponse

"""
Pipeline RAG, no qual recupera top-k segmentos do banco vetorial,
monta prompt estruturado e gera resposta via API LLM.
"""

def answerQuestion(collection, question, embedding_function, k=3):
    
    results = search(collection, question, embedding_function, k)
    documents = results["documents"]
    scores = results["distances"]
    
    promptText = prompt(documents, question)
    
    answer = chatResponse(promptText)
    
    return {
        "answer": answer,
        "segments": documents,
        "scores": scores
    }