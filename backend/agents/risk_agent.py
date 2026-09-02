from backend.agents.news_agent import NewsAgent
from backend.models.risk import RiskAssessment


class RiskAgent:
    """
    Risk Assessment Agent

    Analyzes news articles and classifies supply chain
    disruption severity, category, and confidence.
    """

    def __init__(self):
        self.news_agent = NewsAgent()

    def analyze_risks(self):

        news_list = self.news_agent.get_latest_news()

        risks = []

        for article in news_list:

            text = (
                article.title + " " + (article.summary or "")
            ).lower()

            # Default values
            severity = "Low"
            category = "General"
            region = "Global"
            confidence = 0.60
            reason = "No major disruption detected."

            # --------------------------------------------------
            # HIGH-RISK DISRUPTIONS
            # --------------------------------------------------

            if any(
                word in text
                for word in [
                    "strike",
                    "shutdown",
                    "earthquake",
                    "flood",
                    "fire",
                    "war",
                    "explosion",
                    "blocked",
                    "blockade",
                    "port closure",
                    "factory closure",
                ]
            ):
                severity = "High"
                confidence = 0.95
                reason = "Major supply chain disruption detected."

            # --------------------------------------------------
            # MEDIUM-RISK DISRUPTIONS
            # --------------------------------------------------

            elif any(
                word in text
                for word in [
                    "delay",
                    "shortage",
                    "scarcity",
                    "price increase",
                    "price rise",
                    "inflation",
                    "disruption",
                    "supply gap",
                    "supply constraint",
                    "capacity constraint",
                ]
            ):
                severity = "Medium"
                confidence = 0.80
                reason = "Potential supply chain disruption detected."

            # --------------------------------------------------
            # CATEGORY CLASSIFICATION
            # --------------------------------------------------

            if "strike" in text or "port" in text:
                category = "Port Logistics"

            elif (
                "lithium" in text
                or "nickel" in text
                or "cobalt" in text
                or "graphite" in text
                or "manganese" in text
            ):
                category = "Critical Minerals"

            elif "battery" in text:
                category = "Battery Manufacturing"

            elif "factory" in text or "manufacturing" in text:
                category = "Manufacturing"

            elif (
                "shipping" in text
                or "transportation" in text
                or "shipment" in text
            ):
                category = "Transportation"

            # --------------------------------------------------
            # REGION DETECTION
            # --------------------------------------------------

            countries = [
                "China",
                "India",
                "USA",
                "Canada",
                "Australia",
                "Indonesia",
                "Chile",
                "Brazil",
                "South Korea",
                "Japan",
            ]

            for country in countries:

                if country.lower() in text:
                    region = country
                    break

            # --------------------------------------------------
            # CREATE RISK ASSESSMENT
            # --------------------------------------------------

            risks.append(
                RiskAssessment(
                    title=article.title,
                    severity=severity,
                    category=category,
                    region=region,
                    confidence=confidence,
                    reason=reason,
                )
            )

        return risks


# --------------------------------------------------
# DIRECT TEST
# --------------------------------------------------

if __name__ == "__main__":

    agent = RiskAgent()

    results = agent.analyze_risks()

    for result in results:
        print(result)