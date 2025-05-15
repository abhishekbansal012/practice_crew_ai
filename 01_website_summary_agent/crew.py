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
    # Extract the actual output string
    summary_text = str(result)  # Or result.output if using CrewAI >= 0.24

    print("\n=== Article Summary ===")
    print(summary_text)

    # Save summary to summary.md
    with open("summary.md", "w", encoding="utf-8") as f:
        f.write("# Medium Article Summary\n\n")
        f.write(summary_text)

if __name__ == "__main__":
    main()
