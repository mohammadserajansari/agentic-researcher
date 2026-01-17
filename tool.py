import os
from dotenv import load_dotenv
load_dotenv()

TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")
if not TAVILY_API_KEY:
    raise RuntimeError("TAVILY_API_KEY not found in environment")

os.environ["TAVILY_API_KEY"] = TAVILY_API_KEY

from crewai_tools import TavilySearchTool


web_search_tools = TavilySearchTool()
