from docling.document_converter import DocumentConverter
from io import BytesIO

"""
Converter PDF ou TXT.
"""

def analisarPdf(uploadedFile):
    if uploadedFile is None:
        raise ValueError("Não forneceu arquivo")
    
    pdfBytes = uploadedFile.getvalue()
    fileName = uploadedFile.name.lower()
    
    if fileName.endswith(".pdf"):
        converter = DocumentConverter()
        result = converter.convert(BytesIO(pdfBytes))
        text = result.document.export_to_markdown()

    elif fileName.endswith(".txt"):
        text = uploadedFile.getvalue().decode("utf-8")
    
    else:
        raise ValueError("Formato de arquivo não suportado para o contexto!")
    
    return text