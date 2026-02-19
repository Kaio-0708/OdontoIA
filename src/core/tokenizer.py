from transformers import AutoTokenizer

"""
Responsável por tokenização.
"""

_tokenizer = AutoTokenizer.from_pretrained("mistral-medium-latest")

def encode(text):
    return _tokenizer.encode(text)

def decode(tokens):
    return _tokenizer.decode(tokens)

def countTokens(text):
    return len(encode(text))