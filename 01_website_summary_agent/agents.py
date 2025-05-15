# agents.py
from crewai import Agent
from langchain.chat_models import ChatOpenAI

llm = ChatOpenAI(
    model_name="gpt-4-turbo",
    temperature=0.7
)

summarizer_agent = Agent(
    role="Medium Article Summarizer",
    goal="Read and summarize Medium articles",
    backstory="An expert in condensing long-form content into short, useful insights.",
    verbose=True,
    llm=llm
)
