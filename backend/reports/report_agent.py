from datetime import datetime

from backend.agents.news_agent import NewsAgent
from backend.agents.risk_agent import RiskAgent
from backend.agents.supplier_agent import SupplierAgent

from backend.models.report import Report


class ReportAgent:
    def __init__(self):
        self.news_agent = NewsAgent()
        self.risk_agent = RiskAgent()
        self.supplier_agent = SupplierAgent()

    def generate_report(self):
        news = self.news_agent.get_latest_news()
        risks = self.risk_agent.analyze_risks()
        suppliers = self.supplier_agent.analyze_supplier_impact()

        high_risk_events = sum(
            1
            for risk in risks
            if risk.severity.lower() == "high"
        )

        impacted_suppliers = list(
            {
                supplier.supplier
                for supplier in suppliers
                if supplier.supplier != "Unknown"
            }
        )

        if high_risk_events > 0:
            summary = (
                "High-risk disruptions detected in the EV battery supply chain."
            )
        else:
            summary = (
                "No major disruptions detected in the EV battery supply chain."
            )

        return Report(
            generated_at=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            total_news=len(news),
            high_risk_events=high_risk_events,
            suppliers_impacted=impacted_suppliers,
            summary=summary,
        )