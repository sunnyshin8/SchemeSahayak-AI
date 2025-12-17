import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

class LLMService:
    def __init__(self):
        msg = "Initializing LLM Service..."
        print(msg)
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            print("WARNING: OPENAI_API_KEY not found.")
            self.client = None
        else:
            self.client = OpenAI(api_key=api_key)

    def chat_about_scheme(self, scheme_text: str, user_question: str):
        if not self.client:
            return "AI Service Unavailable (Missing API Key)."

        try:
            response = self.client.chat.completions.create(
                model="gpt-4o-mini", # or gpt-3.5-turbo
                messages=[
                    {"role": "system", "content": "You are a helpful assistant for the SchemeSahayak platform. Answer the user's question based strictly on the provided scheme details. Be concise and helpful."},
                    {"role": "user", "content": f"Scheme Details:\n{scheme_text}\n\nQuestion: {user_question}"}
                ]
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Error contacting AI: {e}"

llm_service = LLMService()

def get_llm_service():
    return llm_service
