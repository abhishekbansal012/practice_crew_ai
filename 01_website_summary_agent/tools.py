import requests
from bs4 import BeautifulSoup

def extract_text_from_medium(url: str) -> str:
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        raise Exception(f"Failed to fetch the article: {response.status_code}")

    soup = BeautifulSoup(response.text, "html.parser")
    paragraphs = soup.find_all("p")
    article_text = "\n".join(p.get_text() for p in paragraphs)
    return article_text
