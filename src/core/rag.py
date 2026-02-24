from database.vetor_db import search
from core.prompt import prompt
from core.llmService import chatResponse

def answerQuestion(collection, question, embedding_function, k=3):
    """
    Pipeline RAG corrigido:
    - Recupera top-k segmentos do banco vetorial
    - Monta prompt estruturado
    - Gera resposta via API LLM
    """
    
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