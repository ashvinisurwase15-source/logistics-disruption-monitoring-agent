from fastapi import APIRouter

from backend.agents.risk_agent import RiskAgent
from backend.agents.recommendation_agent import RecommendationAgent


router = APIRouter()


@router.get("/recommendation")
def get_recommendation():

    # --------------------------------------------------
    # 1. Run Risk Agent
    # --------------------------------------------------

    risk_agent = RiskAgent()

    risks = risk_agent.analyze_risks()


    # --------------------------------------------------
    # 2. Check whether risks were detected
    # --------------------------------------------------

    if not risks:

        return {
            "message": "No risks detected. No recommendation required."
        }


    # --------------------------------------------------
    # 3. Select the highest-risk event
    # --------------------------------------------------

    risk_priority = {
        "high": 3,
        "medium": 2,
        "low": 1
    }

    risk = max(
        risks,
        key=lambda item: risk_priority.get(
            item.severity.lower(),
            0
        )
    )


    # --------------------------------------------------
    # 4. Extract risk information
    # --------------------------------------------------

    disruption_type = risk.category
    risk_level = risk.severity


    # --------------------------------------------------
    # 5. Run Recommendation Agent
    # --------------------------------------------------

    recommendation_agent = RecommendationAgent()

    recommendation = recommendation_agent.generate_recommendation(
        disruption_type=disruption_type,
        risk_level=risk_level
    )


    # --------------------------------------------------
    # 6. Return combined result
    # --------------------------------------------------

    return {
        "risk": risk,
        "recommendation": recommendation
    }