from crewai import Crew
from task import researcher_task, writer_agent_task
from agent import researcher, writer_agent
from llm import llm
from tool import web_search_tools
Crew=Crew(
    agents=[researcher,writer_agent],
    tasks=[researcher_task,writer_agent_task],
    tools=[web_search_tools],
    verbose=True,
    planning=False
)

Crew.kickoff()