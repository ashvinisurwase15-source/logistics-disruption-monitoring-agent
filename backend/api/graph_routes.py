from fastapi import APIRouter

from backend.agents.graph_agent import GraphAgent

router = APIRouter()

graph_agent = GraphAgent()


@router.get("/graph", tags=["Knowledge Graph"])
def generate_graph():
    """
    Generate and save the Supply Chain Knowledge Graph.
    """
    return graph_agent.generate_graph()