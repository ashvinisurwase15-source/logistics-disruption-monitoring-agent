from fastapi import APIRouter


router = APIRouter()


@router.get("/sourcing")
def get_alternative_suppliers(material: str = "Lithium"):
    """
    Find alternative suppliers for a given material.
    """

    agent = SourcingAgent()

    return agent.find_alternatives(material)
class SourcingAgent:
    """
    Alternative Sourcing Agent

    Identifies alternative suppliers when a supply chain
    disruption affects the current supply source.
    """

    def find_alternatives(self, material):

        alternatives = {
            "lithium": [
                "Albemarle",
                "SQM",
                "Ganfeng Lithium"
            ],
            "nickel": [
                "Vale",
                "Nornickel",
                "BHP"
            ],
            "cobalt": [
                "Glencore",
                "Umicore",
                "Huayou Cobalt"
            ],
            "graphite": [
                "Syrah Resources",
                "Novonix",
                "Epsilon Advanced Materials"
            ],
            "copper": [
                "Freeport-McMoRan",
                "BHP",
                "Rio Tinto"
            ]
        }

        material_key = material.lower()

        suppliers = alternatives.get(
            material_key,
            [
                "Alternative Supplier A",
                "Alternative Supplier B",
                "Alternative Supplier C"
            ]
        )

        return {
            "material": material,
            "alternative_suppliers": suppliers
        }


if __name__ == "__main__":

    agent = SourcingAgent()

    result = agent.find_alternatives("Lithium")

    print(result)
