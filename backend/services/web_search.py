from backend.models.news import News


def search_news(query: str):
    """
    Temporary dummy news search.
    This will be replaced with a real web search API later.
    """

    return [
        News(
            title="Port Strike Delays EV Battery Shipments",
            source="Reuters",
            url="https://example.com/news1",
            published_date="2026-07-28",
            summary="Port workers strike causes delays in lithium battery transportation."
        ),
        News(
            title="Lithium Prices Increase Worldwide",
            source="Bloomberg",
            url="https://example.com/news2",
            published_date="2026-07-27",
            summary="Global lithium demand continues to rise due to EV production."
        ),
        News(
            title="New Battery Factory Opens in India",
            source="Economic Times",
            url="https://example.com/news3",
            published_date="2026-07-26",
            summary="India expands domestic EV battery manufacturing capacity."
        ),
    ]