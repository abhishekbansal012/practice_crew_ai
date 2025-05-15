from crewai import Crew
from tools import extract_text_from_medium
from tasks import create_summarization_task
from agents import summarizer_agent

def main():
    url = input("Enter Medium article URL: ")
    article_text = extract_text_from_medium(url)

    task = create_summarization_task(article_text)

    crew = Crew(
        agents=[summarizer_agent],
        tasks=[task],
        verbose=True
    )

    result = crew.kickoff()
    print("\n=== Article Summary ===")
    print(result)

if __name__ == "__main__":
    main()
