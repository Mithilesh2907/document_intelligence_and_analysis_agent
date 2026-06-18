from google import genai
from config.settings import GEMINI_API_KEY

client = genai.Client(
    api_key=GEMINI_API_KEY
)

SYSTEM_PROMPT = """
You are a senior AI engineer.

Explain concepts clearly.
Use practical examples.
Keep answers beginner-friendly.
"""


def ask_gemini(question: str) :
    prompt = f"""
    Question:
    {question}
    """
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    
    return response.text