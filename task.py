from crewai import Task
from agent import researcher, writer_agent

researcher_task=Task(
    description="Search the web for the latest AI trends and provide a summarized report.",
    expected_output="A summary of the top 3 trending developments in AI with insights on their impact.",
    agent=researcher
)


writer_agent_task=Task(
    description="Write an engaging blog post about the AI industry based on the research analyst’s summary.",
    expected_output="A well-structured, 4-paragraph blog post in markdown format with simple, engaging content.",
    agent=writer_agent,
    output_file="ai-blog-posts/new_post.md"
)
