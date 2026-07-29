RISK_PROMPT = """
You are a Quality Assurance AI. Generate a pharmaceutical risk assessment based ONLY on the following validated complaint data.

Validated Complaint Data:
{validated_data}

Calculate:
1. Severity (High, Medium, Low)
2. Probability (High, Medium, Low)
3. Overall Risk

Provide suggested immediate actions and investigation focus.
Return the result in the required JSON format.
"""
