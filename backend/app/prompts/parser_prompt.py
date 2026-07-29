PARSER_PROMPT = """
Given the following natural language complaint from a customer, extract all relevant pharmaceutical complaint data.
If a piece of information is not explicitly mentioned, DO NOT guess or infer it; leave it empty or null.

User Complaint:
{user_prompt}

Return the data in a structured JSON format according to the schema provided.
"""
