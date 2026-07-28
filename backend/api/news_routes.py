from fastapi import APIRouter
from backend.agents.news_agent import NewsAgent

router = APIRouter()

news_agent = NewsAgent()


@router.get("/news")
def get_news():
    """
    Returns the latest supply chain news.
    """
    return news_agent.get_latest_news()