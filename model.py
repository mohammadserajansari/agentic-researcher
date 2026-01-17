from crewai import LLM
from config import Config
class Model:
    def __init__(self):
        self.llm = LLM(
            model=Config.model_name,
            api_key=Config.model_api,
            base_url="https://api.groq.com/openai/v1",  
            temperature=0,
            provider="groq"  
        )