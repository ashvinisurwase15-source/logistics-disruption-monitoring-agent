class RecommendationAgent:
    """
    Recommendation / Mitigation Agent

    Generates mitigation actions based on disruption type
    and risk level.
    """

    def generate_recommendation(self, disruption_type, risk_level):

        risk_level = risk_level.lower()
        disruption_type = disruption_type.lower()

        # --------------------------------------------------
        # HIGH RISK
        # --------------------------------------------------

        if risk_level == "high":

            if "port" in disruption_type:
                action = (
                    "Activate alternate ports and transportation routes "
                    "immediately. Prioritize critical battery shipments "
                    "and identify alternate suppliers if required."
                )

            elif "critical minerals" in disruption_type:
                action = (
                    "Activate alternate suppliers for critical battery "
                    "minerals and secure additional material inventory "
                    "to reduce supply shortage risk."
                )

            elif "manufacturing" in disruption_type:
                action = (
                    "Activate backup manufacturing capacity and assess "
                    "alternative battery production facilities immediately."
                )

            elif "transportation" in disruption_type:
                action = (
                    "Reroute shipments through alternative transportation "
                    "routes and prioritize time-critical battery deliveries."
                )

            elif "battery" in disruption_type:
                action = (
                    "Identify alternate battery suppliers and assess "
                    "available production capacity immediately."
                )

            else:
                action = (
                    "Identify alternate suppliers and transportation "
                    "routes immediately and activate the supply chain "
                    "contingency plan."
                )

        # --------------------------------------------------
        # MEDIUM RISK
        # --------------------------------------------------

        elif risk_level == "medium":

            action = (
                "Monitor the disruption closely, evaluate alternate "
                "suppliers and logistics routes, and prepare a contingency "
                "plan before the disruption becomes critical."
            )

        # --------------------------------------------------
        # LOW RISK
        # --------------------------------------------------

        else:

            action = (
                "Continue monitoring the situation and track for any "
                "changes that could increase supply chain risk."
            )

        return {
            "disruption_type": disruption_type,
            "risk_level": risk_level,
            "recommended_action": action
        }


# --------------------------------------------------
# DIRECT TEST
# --------------------------------------------------

if __name__ == "__main__":

    agent = RecommendationAgent()

    result = agent.generate_recommendation(
        disruption_type="Port Logistics",
        risk_level="high"
    )

    print(result)