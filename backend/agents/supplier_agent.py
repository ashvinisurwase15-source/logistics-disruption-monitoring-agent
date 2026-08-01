from backend.agents.news_agent import NewsAgent
from backend.models.supplier import SupplierImpact


class SupplierAgent:
    def __init__(self):
        self.news_agent = NewsAgent()

    def analyze_supplier_impact(self):
        news = self.news_agent.get_latest_news()

        impacts = []

        for article in news:
            title = article.title.lower()

            supplier = "Unknown"
            material = "Unknown"
            region = "Global"
            impact_level = "Low"
            reason = "No major disruption detected."

            # Supplier Detection
            if "catl" in title:
                supplier = "CATL"
            elif "tesla" in title:
                supplier = "Tesla"
            elif "byd" in title:
                supplier = "BYD"
            elif "lg" in title:
                supplier = "LG Energy Solution"
            elif "panasonic" in title:
                supplier = "Panasonic"

            # Material Detection
            if "lithium" in title:
                material = "Lithium"
            elif "nickel" in title:
                material = "Nickel"
            elif "cobalt" in title:
                material = "Cobalt"
            elif "graphite" in title:
                material = "Graphite"

            # Region Detection
            if "china" in title:
                region = "China"
            elif "india" in title:
                region = "India"
            elif "australia" in title:
                region = "Australia"
            elif "chile" in title:
                region = "Chile"

            # Impact Detection
            if any(word in title for word in ["strike", "shutdown", "ban", "war", "earthquake"]):
                impact_level = "High"
                reason = "Major disruption may impact supplier operations."

            elif any(word in title for word in ["delay", "shortage", "slowdown"]):
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