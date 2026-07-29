DOCUMENT_PROMPT = """
Extract pharmaceutical complaint information from the following OCR text derived from an uploaded document.
Preserve the document context.

OCR Text:
{ocr_text}

Extract relevant fields and return them in the required JSON format.
"""
