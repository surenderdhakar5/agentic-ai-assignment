import google.generativeai as genai
from config import GEMINI_API_KEY

if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)
    
    model = genai.GenerativeModel("gemini-2.5-flash")


def detect_intent(question):

    if not GEMINI_API_KEY:
        return None

    prompt = f"""
You are an AI routing assistant.

Classify the user query into ONLY one of these intents:

ORDER_STATUS
PRODUCT_DETAILS
SEARCH_PRODUCT
CHEAPER_ALTERNATIVE
GENERAL_QUERY

Question:
{question}

Return ONLY the intent name.
"""

    try:
        response = model.generate_content(prompt)
        return response.text.strip().upper()

    except Exception as e:
        print("Intent Detection Error:", e)
        return None


def general_chat(question):

    print("=" * 50)
    print("GENERAL_CHAT CALLED")
    print("Question:", question)
    print("=" * 50)

    if not GEMINI_API_KEY:
        print("API KEY NOT FOUND")
        return "LLM not configured."

    try:
        print("Sending request to Gemini...")

        response = model.generate_content(question)

        print("Gemini Response Received")

        return response.text

    except Exception as e:

        print("=" * 50)
        print("GEMINI ERROR")
        print(e)
        print("=" * 50)

        return f"Gemini Error:\n{e}"