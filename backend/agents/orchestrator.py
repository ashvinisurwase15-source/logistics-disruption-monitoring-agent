from backend.agents.news_agent import NewsAgent
from backend.agents.risk_agent import RiskAgent


class SupplyChainOrchestrator:
    """
    Coordinates the different AI agents in the
    EV Battery Supply Chain Monitoring system.
    """

    def __init__(self):
        self.news_agent = NewsAgent()
        self.risk_agent = RiskAgent()

    def run(self):
        """
        Execute the initial multi-agent workflow.
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
        # 3. Return combined workflow result
        # ----------------------------------------------

        return {
            "news_count": len(news),
            "risk_count": len(risks),
            "risks": risks
        }


# --------------------------------------------------
# DIRECT TEST
# --------------------------------------------------

if __name__ == "__main__":

    orchestrator = SupplyChainOrchestrator()

    result = orchestrator.run()

    print("Multi-Agent Orchestrator Result")

    print("News Count:", result["news_count"])
    print("Risk Count:", result["risk_count"])
    print("--------------------------------")

    print("\nDetected Risks:")

    for risk in result["risks"]:
        print(risk)