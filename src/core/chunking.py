"""
Responsável por dividir texto em blocos.
Tamanho fixo: Aproximado de 700 tokens, porque mantêm contexto suficiente conforme as API's de LLM.
Overlap: 100 tokens, overlap evita perda de informação entre blocos.
"""

def chunkText(text, size=700, overlap=100):
    words = text.split()
    chunks = []
    step = size - overlap
    
    for i in range(0, len(words), step):
        chunk = words[i:i + size]
        chunks.append(" ".join(chunk))
    
    return chunks
