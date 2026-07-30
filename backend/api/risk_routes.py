from fastapi import APIRouter

from backend.agents.risk_agent import RiskAgent

router = APIRouter()

risk_agent = RiskAgent()


@router.get("/risk")
def get_risk_analysis():
    """
    Returns the risk assessment for the latest supply chain news.
    """
    return risk_agent.analyze_risks()
