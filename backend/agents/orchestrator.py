from backend.agents.news_agent import NewsAgent
from backend.agents.risk_agent import RiskAgent
from backend.agents.supplier_agent import SupplierAgent
from backend.agents.impact_agent import ImpactAgent
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
        self.impact_agent = ImpactAgent()
        self.recommendation_agent = RecommendationAgent()

    def run(self):

        news = self.news_agent.get_latest_news()

        risks = self.risk_agent.analyze_risks()

        suppliers = self.supplier_agent.analyze_supplier_impact()

        impacts = []
        recommendations = []

        for risk in risks:

            material = "Lithium"

            impact = self.impact_agent.analyze_impact(
                disruption_type=risk.category,
                risk_level=risk.severity,
                material=material
            )

            impacts.append(impact)

            recommendation = self.recommendation_agent.generate_recommendation(
                disruption_type=risk.category,
                risk_level=risk.severity
            )

            recommendations.append(
                {
                    "risk": risk,
                    "impact": impact,
                    "recommendation": recommendation
                }
            )

        return {
            "news_count": len(news),
            "risk_count": len(risks),
            "supplier_count": len(suppliers),
            "impact_count": len(impacts),
            "recommendation_count": len(recommendations),
            "risks": risks,
            "suppliers": suppliers,
            "impacts": impacts,
            "recommendations": recommendations
        }


if __name__ == "__main__":

    orchestrator = SupplyChainOrchestrator()

    result = orchestrator.run()

    print("Multi-Agent Orchestrator Result")
    print("--------------------------------")

    print("News Count:", result["news_count"])
    print("Risk Count:", result["risk_count"])
    print("Supplier Count:", result["supplier_count"])
    print("Impact Count:", result["impact_count"])
    print("Recommendation Count:", result["recommendation_count"])

    print("--------------------------------")

    print("\nBusiness Impact Analysis:")

    for impact in result["impacts"]:
        print(impact)

    print("\nRecommendations:")

    for item in result["recommendations"]:
        print(item)