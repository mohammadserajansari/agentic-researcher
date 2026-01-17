from crewai import Agent
from tool import web_search_tools
from llm import llm
researcher=Agent(
    role="Market Rsearch Analyst",
    goal="Provide me up-to-date market analysis of AI Industry",
    backstory=" An expert Analyst with keen eye for market trend ",
    llm=llm,
    tools=[web_search_tools]
)

writer_agent=Agent(
    role='Content Writer',
    goal='Craft engaging blog posts about the AI industry',
    backstory='A skilled writer with a passion for technology.',
    tools=[],  # No tools needed; writes based on research summary
    llm=llm,
    verbose=True
)

