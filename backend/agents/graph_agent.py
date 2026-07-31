from backend.agents.news_agent import NewsAgent
from backend.models.graph import SupplyChainNode, SupplyChainEdge


class GraphAgent:
    def __init__(self):
        self.news_agent = NewsAgent()

    def build_graph(self):
        news = self.news_agent.get_latest_news()

        nodes = []
        edges = []

        # Add central node
        nodes.append(
            SupplyChainNode(
                id="EV_Battery",
                label="EV Battery",
                type="Product"
            )
        )

        for article in news:
            title = article.title

            if "Lithium" in title:
                nodes.append(
                    SupplyChainNode(
                        id="Lithium",
                        label="Lithium",
                        type="Material"
                    )
                )

                edges.append(
                    SupplyChainEdge(
                        source="Lithium",
                        target="EV_Battery",
                        relation="used_in"
                    )
                )

            elif "China" in title:
                nodes.append(
                    SupplyChainNode(
                        id="China",
                        label="China",
                        type="Country"
                    )
                )

                edges.append(
                    SupplyChainEdge(
                        source="China",
                        target="EV_Battery",
                        relation="supplies"
                    )
                )

            else:
                nodes.append(
                    SupplyChainNode(
                        id=title,
                        label=title,
                        type="News"
                    )
                )

                edges.append(
                    SupplyChainEdge(
                        source=title,
                        target="EV_Battery",
                        relation="related_to"
                    )
                )

        return {
            "nodes": nodes,
            "edges": edges
        }