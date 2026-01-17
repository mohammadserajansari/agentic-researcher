# # # from  config import Config
# # # from crewai.tools import WebsiteSearchTool
# # # from langchain_openai import ChatOpenAI
# # # from config import Config
# # # from crewai_tools import WebsiteSearchTool
# # import os
# # from crewai_tools import WebsiteSearchTool

# # web_search_tools=WebsiteSearchTool()


# # # llm = ChatOpenAI(
# # #     model=Config.MODEL_NAME,
# # #     api_key=Config.OPENAI_API_KEY
# # # )




# # # tool.py
# # import os
# # from dotenv import load_dotenv

# # # 1️⃣ Load .env FIRST
# # load_dotenv()

# # # 2️⃣ HARD ASSERT + FORCE SET (CrewAI tools require this)
# # OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
# # if not OPENAI_API_KEY:
# #     raise RuntimeError("OPENAI_API_KEY not found in environment")

# # # 🔥 Force it into os.environ explicitly
# # os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

# # # 3️⃣ ONLY NOW import CrewAI tools
# # from crewai_tools import WebsiteSearchTool

# # # 4️⃣ Instantiate tool
# # web_search_tools = WebsiteSearchTool()

# from crewai_tools import TavilySearchTool

# web_search_tools = TavilySearchTool()


import os
from dotenv import load_dotenv


load_dotenv()


TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")
if not TAVILY_API_KEY:
    raise RuntimeError("TAVILY_API_KEY not found in environment")

os.environ["TAVILY_API_KEY"] = TAVILY_API_KEY

from crewai_tools import TavilySearchTool


web_search_tools = TavilySearchTool()
