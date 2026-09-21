class ImpactAgent:
    """
    Business Impact Analysis Agent

    Evaluates the potential business impact of a
    supply chain disruption.
    """

    def analyze_impact(
        self,
        disruption_type,
        risk_level,
        material
    ):
        """
        Analyze business impact based on
        disruption type, risk level, and material.
        """

        risk_level = str(risk_level).lower()
        disruption_type = str(disruption_type)
        material = str(material)

        if risk_level == "high":
            production_impact = "High"
            shortage_risk = "High"
            cost_impact = "High"
            priority = "Critical"

            business_impact = (
                f"High potential impact on EV battery supply "
                f"due to {disruption_type} affecting {material}."
            )

        elif risk_level == "medium":
            production_impact = "Medium"
            shortage_risk = "Medium"
            cost_impact = "Medium"
            priority = "High"

            business_impact = (
                f"Moderate potential impact on EV battery supply "
                f"due to {disruption_type} affecting {material}."
            )

        else:
            production_impact = "Low"
            shortage_risk = "Low"
            cost_impact = "Low"
            priority = "Normal"

            business_impact = (
                f"Limited potential impact from "
                f"{disruption_type} affecting {material}."
            )

        return {
            "disruption_type": disruption_type,
            "material": material,
            "risk_level": risk_level,
            "production_impact": production_impact,
            "shortage_risk": shortage_risk,
            "cost_impact": cost_impact,
            "priority": priority,
            "business_impact": business_impact
        }


if __name__ == "__main__":

    agent = ImpactAgent()

    result = agent.analyze_impact(
        disruption_type="Port Logistics",
        risk_level="high",
        material="Lithium"
    )

    print("Business Impact Analysis")
    print("--------------------------------")

    print("Disruption Type:", result["disruption_type"])
    print("Material:", result["material"])
    print("Risk Level:", result["risk_level"])
    print("Production Impact:", result["production_impact"])
    print("Shortage Risk:", result["shortage_risk"])
    print("Cost Impact:", result["cost_impact"])
    print("Priority:", result["priority"])
    print("Business Impact:", result["business_impact"])