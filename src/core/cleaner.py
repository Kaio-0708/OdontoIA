import re

"""
Limpeza de Markdown ou TXT.
"""

def clearText(text):
    text = text.replace("\r\n", "\n")
    text = re.sub(r"\n{3,}", "\n\n", text)
    text = re.sub(r"[ \t]+$", "", text, flags=re.MULTILINE)
    text = re.sub(r"-\n(?=\w)", "", text)
    
    return text.strip()