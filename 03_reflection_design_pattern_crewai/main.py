import os
from crewai import Crew
from agents import writer, critic, seo_reviewer, legal_reviewer, ethics_reviewer, meta_reviewer
from tasks import create_tasks
from dotenv import load_dotenv

load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")
if not openai_api_key:
    raise EnvironmentError("OPENAI_API_KEY not set")

# Create the tasks
tasks = create_tasks(
    topic="The benefits of remote work",
    writer=writer,
    critic=critic,
    seo=seo_reviewer,
    legal=legal_reviewer,
    ethics=ethics_reviewer,
    meta=meta_reviewer
)

# Create the crew
crew = Crew(
    agents=[writer, critic, seo_reviewer, legal_reviewer, ethics_reviewer, meta_reviewer],
    tasks=tasks,
    verbose=True
)

# Execute the plan
result = crew.kickoff()
print("\nFinal Output:\n", result)
