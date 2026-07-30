from backend.agents.news_agent import NewsAgent
from backend.models.risk import RiskAssessment


class RiskAgent:
    """
    Risk Assessment Agent
    """

    def __init__(self):
        self.news_agent = NewsAgent()

    def analyze_risks(self):
        news_list = self.news_agent.get_latest_news()

        risks = []

        for article in news_list:
            text = (article.title + " " + article.summary).lower()

            severity = "Low"
            category = "General"
            region = "Global"
            confidence = 0.60
            reason = "No major disruption detected."

            if any(word in text for word in [
                "strike",
                "shutdown",
                "war",
                "sanction",
                "earthquake",
                "flood"
            ]):
                severity = "High"
                confidence = 0.95
                reason = "Major disruption detected."

            elif any(word in text for word in [
                "delay",
                "shortage",
                "price",
                "inflation",
                "disruption"
            ]):
                severity = "Medium"
                confidence = 0.80
                reason = "Possible supply chain disruption."

            if "port" in text:
                category = "Port Logistics"
            elif "battery" in text:
                category = "Battery Manufacturing"
            elif "lithium" in text:
                category = "Critical Minerals"
            elif "factory" in text:
                category = "Manufacturing"
            elif "shipping" in text:
                category = "Transportation"

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