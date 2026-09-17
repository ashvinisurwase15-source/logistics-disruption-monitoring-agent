from fastapi import APIRouter

from backend.agents.sourcing_agent import SourcingAgent


router = APIRouter()


@router.get("/sourcing")
def get_alternative_suppliers(material: str = "Lithium"):
    """
    Find alternative suppliers for a given material.
    """

    agent = SourcingAgent()

    return agent.find_alternatives(material)