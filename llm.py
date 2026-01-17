from crewai import LLM
from config import Config


class GroqLLM:
    def __init__(self):
        if not Config.GROQ_TOKEN:
            raise ValueError("GROQ_TOKEN not set")

        if not Config.MODEL_NAME:
            raise ValueError("MODEL_NAME not set or empty")

        self.llm = LLM(
            model=Config.MODEL_NAME,
            api_key=Config.GROQ_TOKEN,
            base_url="https://api.groq.com/openai/v1",
            temperature=0,
            provider="groq"
        )


llm = GroqLLM().llm
