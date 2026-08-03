from backend.agents.news_agent import NewsAgent
from backend.models.supplier import SupplierImpact
from backend.services.entity_extractor import extract_entities


class SupplierAgent:

    def __init__(self):
        self.news_agent = NewsAgent()

    def analyze_supplier_impact(self):

        news = self.news_agent.get_latest_news()

        impacts = []

        for article in news:

            # Extract supplier, material and region
            supplier, material, region = extract_entities(
                article.title + " " + article.summary
            )

            # Debug prints (remove later if you want)
            print("TITLE:", article.title)
            print("SUMMARY:", article.summary)
            print("EXTRACTED:", supplier, material, region)
            print("=" * 60)

            title = article.title.lower()
            summary = article.summary.lower()

            text = title + " " + summary

            # Default values
            impact_level = "Low"
            reason = "No major disruption detected."

            # High Impact
            if any(word in text for word in [
                "strike",
                "shutdown",
                "earthquake",
                "war",
                "sanction",
                "export ban",
                "fire",
                "explosion",
                "factory closure"
            ]):
                impact_level = "High"
                reason = "Major disruption may impact supplier operations."

            # Medium Impact
            elif any(word in text for word in [
                "delay",
                "shortage",
                "slowdown",
                "congestion",
                "bottleneck",
                "capacity"
            ]):
                impact_level = "Medium"
                reason = "Possible supply chain delays."

            impacts.append(
                SupplierImpact(
                    supplier=supplier,
                    material=material,
                    region=region,
                    impact_level=impact_level,
                    reason=reason
                )
            )

        return impacts