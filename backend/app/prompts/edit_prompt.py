EDIT_PROMPT = """
You are updating an existing pharmaceutical complaint based on new user instructions.

Existing Complaint State:
{current_state}

User Instruction:
{user_instruction}

Apply ONLY the changes requested in the User Instruction to the Existing Complaint State.
Preserve all other fields exactly as they are.
Return the updated state in the required JSON format.
"""
