from backend.agents.supplier_agent import SupplierAgent
from backend.graph.graph import create_graph


class GraphAgent:

    def __init__(self):
        self.supplier_agent = SupplierAgent()

    def generate_graph(self):
        suppliers = self.supplier_agent.analyze_supplier_impact()

        graph_path = create_graph(suppliers)

        return {
            "message": "Knowledge Graph Generated Successfully",
            "graph_path": graph_path
        }