from crewai import Task
from agents import summarizer_agent

def create_summarization_task(article_text: str) -> Task:
    return Task(
        description=f"Summarize the following Medium article:\n\n{article_text[:4000]}",
        expected_output="A concise summary (gist) of the article in 5-7 bullet points.",
        agent=summarizer_agent,
    )
