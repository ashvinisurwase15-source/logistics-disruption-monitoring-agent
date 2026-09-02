from backend.services.web_search import search_news


class NewsAgent:
    """
    News Monitoring Agent
    Responsible for collecting disruption-related news.
    """

    def get_latest_news(
            self,
            query: str = (
                    "EV battery supply chain disruption "
                    "port strike shortage shutdown shipment delay"
            )
    ):
        return search_news(query)