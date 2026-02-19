from .tokenizer import encode, decode

"""
Responsável por dividir texto em blocos.
Tamanho fixo: Aproximado de 700 tokens, porque mantêm contexto suficiente conforme as API's de LLM.
Overlap: 100 tokens, overlap evita perda de informação entre blocos.
"""

def chunkText(text, size=700, overlap=100):
    tokens = encode(text)
    chunks = []
    
    step = size - overlap
    
    for i in range(0, len(tokens), step):
        chunkToken = tokens[i:i + size]
        chunk = decode(chunkToken)
        chunks.append(" ".join(chunk))
        
    return chunks
