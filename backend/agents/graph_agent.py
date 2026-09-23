from backend.agents.supplier_agent import SupplierAgent
from backend.agents.risk_agent import RiskAgent
from backend.graph.graph import create_graph


class GraphAgent:
    """
    Knowledge Graph Agent

    Combines supplier information and risk information
    to create a supply chain knowledge graph.
    """

    def __init__(self):
        self.supplier_agent = SupplierAgent()
        self.risk_agent = RiskAgent()

    def generate_graph(self):

        suppliers = (
            self.supplier_agent.analyze_supplier_impact()
        )

        risks = (
            self.risk_agent.analyze_risks()
        )

        graph_path = create_graph(
            suppliers,
            risks
        )

        return {
            "message": "Knowledge Graph Generated Successfully",
            "graph_path": graph_path
        }


if __name__ == "__main__":

    agent = GraphAgent()

    result = agent.generate_graph()

    print(result)