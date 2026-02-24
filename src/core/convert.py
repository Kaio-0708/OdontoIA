from docling.document_converter import DocumentConverter
from io import BytesIO
import tempfile
from pathlib import Path

"""
Converter PDF ou TXT.
"""

def analisarPdf(uploadedFile):
    if uploadedFile is None:
        raise ValueError("Não forneceu arquivo")
    
    fileName = uploadedFile.name.lower()
    
    if fileName.endswith(".pdf"):
        pdfBytes = uploadedFile.getvalue()
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
            tmp.write(pdfBytes)
            tmp_path = Path(tmp.name)
            
        converter = DocumentConverter()
        result = converter.convert(tmp_path)
        text = result.document.export_to_markdown()

    elif fileName.endswith(".txt"):
        text = uploadedFile.getvalue().decode("utf-8")
    
    else:
        raise ValueError("Formato de arquivo não suportado para o contexto!")
    
    return text