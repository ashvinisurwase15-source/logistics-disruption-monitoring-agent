from fastapi import APIRouter

from backend.agents.supplier_agent import SupplierAgent

router = APIRouter()

supplier_agent = SupplierAgent()


@router.get("/supplier", tags=["Supplier Impact"])
def get_supplier_impact():
    """
    Returns supplier impact analysis based on the latest news.
    """
    return supplier_agent.analyze_supplier_impact()