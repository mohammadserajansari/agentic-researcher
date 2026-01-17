import os
import pathlib
from dotenv import load_dotenv
env_path = pathlib.Path(__file__).parent / ".env"
load_dotenv(dotenv_path=env_path)
class Config:
    MODEL_NAME=os.getenv("MODEL_NAME")
    GROQ_TOKEN=os.getenv("GROQ_API_KEY")
    TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

    
