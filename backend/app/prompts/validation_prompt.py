VALIDATION_PROMPT = """
Analyze the following extracted complaint data for logical consistency and completeness.
Check if the following mandatory fields are present and correctly formatted: Product Name, Batch Number, Complaint Description.

Extracted Data:
{complaint_data}

Provide a JSON response indicating whether the complaint is valid, a completeness score (0-100), and list any missing fields or warnings.
"""
