import os
from pathlib import Path

from dotenv import load_dotenv
from exa_py import Exa

from backend.models.news import News

# Load .env file
BASE_DIR = Path(__file__).resolve().parents[2]
ENV_PATH = BASE_DIR / ".env"

print("ENV PATH:", ENV_PATH)
print("ENV EXISTS:", ENV_PATH.exists())

load_dotenv(ENV_PATH)

api_key = os.getenv("EXA_API_KEY")
print("EXA_API_KEY:", api_key)

if not api_key:
    raise ValueError(
        "EXA_API_KEY not found. Please add it to your .env file."
    )

# Create Exa client
exa = Exa(api_key=api_key)


def search_news(query: str = "EV battery supply chain disruptions"):
    """
    Search the web using Exa.
    """

    response = exa.search_and_contents(
        query=query,
        type="auto",
        num_results=5,
        text=True,
    )

    news_list = []

    for result in response.results:
        news_list.append(
            News(
                title=result.title if result.title else "No Title",
                source="Exa Search",
                url=result.url,
                published_date=None,
                summary=result.text[:300] if result.text else "No summary available."
            )
        )

    return news_list