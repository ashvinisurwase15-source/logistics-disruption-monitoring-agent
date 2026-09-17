from backend.agents.news_agent import NewsAgent
from backend.agents.risk_agent import RiskAgent
from backend.agents.supplier_agent import SupplierAgent
from backend.agents.recommendation_agent import RecommendationAgent


class SupplyChainOrchestrator:
    """
    Coordinates all AI agents in the
    EV Battery Supply Chain Monitoring system.
    """

    def __init__(self):
        self.news_agent = NewsAgent()
        self.risk_agent = RiskAgent()
        self.supplier_agent = SupplierAgent()
        self.recommendation_agent = RecommendationAgent()

    def run(self):
        """
        Execute the complete multi-agent workflow.
        """

        # ----------------------------------------------
        # 1. News Agent
        # ----------------------------------------------

        news = self.news_agent.get_latest_news()

        # ----------------------------------------------
        # 2. Risk Agent
        # ----------------------------------------------

        risks = self.risk_agent.analyze_risks()

        # ----------------------------------------------
        # 3. Supplier Impact Agent
        # ----------------------------------------------

        suppliers = self.supplier_agent.analyze_supplier_impact()

        # ----------------------------------------------
        # 4. Recommendation Agent
        # ----------------------------------------------

        recommendations = []

        for risk in risks:

            recommendation = self.recommendation_agent.generate_recommendation(
                disruption_type=risk.category,
                risk_level=risk.severity
            )

            recommendations.append(
                {
                    "risk": risk,
                    "recommendation": recommendation
                }
            )

        # ----------------------------------------------
        # 5. Return complete workflow result
        # ----------------------------------------------

        return {
            "news_count": len(news),
            "risk_count": len(risks),
            "supplier_count": len(suppliers),
            "recommendation_count": len(recommendations),
            "risks": risks,
            "suppliers": suppliers,
            "recommendations": recommendations
        }


# --------------------------------------------------
# DIRECT TEST
# --------------------------------------------------

if __name__ == "__main__":

    orchestrator = SupplyChainOrchestrator()

    result = orchestrator.run()

    print("Multi-Agent Orchestrator Result")
    print("--------------------------------")

    print("News Count:", result["news_count"])
    print("Risk Count:", result["risk_count"])
    print("Supplier Count:", result["supplier_count"])
    print("Recommendation Count:", result["recommendation_count"])

    print("--------------------------------")

    print("\nDetected Risks:")

    for risk in result["risks"]:
        print(risk)

    print("\nRecommendations:")

    for item in result["recommendations"]:
        print(item)